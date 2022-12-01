import asyncio
import sys
import argparse
import aiohttp



parser = argparse.ArgumentParser()
parser.add_argument('workers', type=int, help='Первым аргументом должно быть число воркеров')
parser.add_argument('file', type=str, help="Вторым аргументом должен быть файл с url'ами")
args = parser.parse_args()


class Fetcher:

    def __init__(self, numb_of_workers, name_of_file):
        self.numb_of_workers = numb_of_workers
        self.file = name_of_file
        self.corr_dict = {i: 0 for i in range(1, self.numb_of_workers + 1)}
        self.inv_url_counter = 0
        self.timeout_counter = 0

    async def fetch(self, number_of_corr, session, queue, timeout=5):
        while True:
            url = await queue.get()
            try:
                async with session.get(url, timeout=timeout) as resp:
                    assert resp.status == 200
                    await resp.read()
                    self.corr_dict[number_of_corr] += 1
            except asyncio.TimeoutError:
                self.timeout_counter += 1
                print('Timeout!')
            except aiohttp.InvalidURL:
                self.inv_url_counter += 1
                print('Invalid url!')
            finally:
                queue.task_done()

    async def process(self):
        que = asyncio.Queue()
        with open(self.file, 'r') as f:
            for line in f:
                await que.put(line.replace('\n', ''))

            async with aiohttp.ClientSession() as session:
                workers = [
                    asyncio.create_task(self.fetch(i, session, que))
                    for i in range(1, self.numb_of_workers + 1)
                ]
                await que.join()

                for worker in workers:
                    worker.cancel()


fetcher = Fetcher(args.workers, args.file)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(fetcher.process())
loop.close()
print(sys.argv)
