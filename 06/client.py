import argparse
import socket
import queue
import threading

parser = argparse.ArgumentParser()
parser.add_argument('threads', type=int, help='Первым аргументом должно быть число потоков')
parser.add_argument('File', type=str, help="Вторым аргументом должен быть файл с url'ами")
args = parser.parse_args()

THREADS = args.threads
FILE_NAME = args.File
HOST = "127.0.0.1"
PORT = 60584


class Client:
    _threads = THREADS

    def __init__(self, host, port, url_file):
        self.__host = host
        self.__port = port
        self.__url_file = url_file
        self.connected = False
        self.socket = None
        self.que = queue.Queue()

    def filling_queue(self):
        with open(self.__url_file, 'r') as file:
            for line in file:
                self.que.put(line)
        self.que.put('END')
        return self.que

    def create_connection(self):
        if not self.connected:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.__host, self.__port))
            self.socket = s
            self.connected = True
            return True
        return False

    def close_connection(self):
        if self.connected:
            self.socket.close()
            return True
        return False

    def send_data_and_get_answer_with_one_thread(self):
        while not self.que.empty():
            url = self.que.get()
            self.socket.send(url.encode('utf-8'))
            data = self.socket.recv(1024).decode('utf-8')
            print(data)

    def send_data_and_get_answer_with_multithreading(self):
        threads = [threading.Thread(target=self.send_data_and_get_answer_with_one_thread,
                                    args=())
                   for _ in range(self._threads)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.close_connection()

    def run(self):
        self.create_connection()
        self.filling_queue()
        self.send_data_and_get_answer_with_multithreading()


client = Client(HOST, PORT, FILE_NAME)
client.run()
