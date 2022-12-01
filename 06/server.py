import argparse
import json
import re
from collections import Counter
import socket
import threading
import queue
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--workers', type=int)
parser.add_argument('-k', '--k', type=int)
args = parser.parse_args()

WORKERS = args.workers
MOST_COMMON_NUMBER = args.k

HOST = "127.0.0.1"
PORT = 60584


class Server:
    _workers = WORKERS
    _mcn = MOST_COMMON_NUMBER
    lock = threading.Lock()

    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.que = queue.Queue()
        self.socket = None
        self.recv_urls_number = 0
        self.__handled_urls = 0

    def connect(self):
        master_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        master_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        master_s.bind((self.__host, self.__port))
        master_s.listen()
        self.socket = master_s
        conn, addr = master_s.accept()
        return conn, addr

    def listen_and_send_to_workers(self, conn):
        while True:
            data = conn.recv(1024)
            data_list = data.decode('utf-8').split('\n')

            if 'END' in data_list:
                data_list.remove('END')
                for data in data_list:
                    self.recv_urls_number += 1
                    self.que.put(data)
                return
            data_list.remove('')
            for data in data_list:
                self.recv_urls_number += 1
                self.que.put(data)
        return True

    def handle_url(self, conn):
        while self.__handled_urls != self.recv_urls_number:
            try:

                url = self.que.get(timeout=2)
                if url is None:
                    break
            except queue.Empty:
                continue
            resp = self.request_and_count_words(url, self._mcn)
            conn.sendall(resp.encode('utf-8'))
            with self.lock:
                self.__handled_urls += 1
                print(f"{self.__handled_urls} is handled at the moment")

        return True

    def close_connection(self, conn):
        conn.close()
        self.socket.close()

    def request_and_count_words(self, url, number):
        try:
            text = BeautifulSoup(requests.get(url).text, features='html.parser').text
            cleared_text = re.findall(r'[а-яёА-ЯЁa-zA-Z]+', text)
            most_common_cnt = Counter(cleared_text)
            return json.dumps(dict(most_common_cnt.most_common(number)), ensure_ascii=False)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            return json.dumps({'invalid_link': 'invalid_link'})

    def process(self):
        conn = self.connect()[0]
        workers = [threading.Thread(target=self.handle_url, args=(conn,)) for _ in range(self._workers)]
        master = threading.Thread(target=self.listen_and_send_to_workers, args=(conn,))
        master.start()
        for worker in workers:
            worker.start()
        for worker in workers:
            worker.join()
        master.join()
        self.close_connection(conn)


server = Server(HOST, PORT)
server.process()
