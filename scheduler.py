import json
import threading
import uuid
from concurrent.futures._base import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from queue import Queue

from job import Job


def coroutine(f):
    def wrap(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen
    return wrap


class Scheduler:
    def __init__(self, pool_size: 10):
        self.pool_size = pool_size
        self.tasks = list()
        self.q = Queue()

    def schedule(self, **kargs):
        with open('myfile.json', mode='r') as f:
            data = json.load(f)
        data[str(uuid.uuid4())] = [kargs]
        with open('myfile.json', 'w') as f:
            json.dump(data, fp=f, ensure_ascii=False, indent=4)

        with open('myfile.json') as f:
            data = json.load(f)
        print(data)

        try:
            self.run().send(True)
        except StopIteration:
            pass


    @coroutine
    def run(self):
        try:
            while True:
                data_chunk = (yield)
                if data_chunk:
                    with ThreadPoolExecutor(max_workers=self.pool_size) as pool:
                        # return pool.submit(Job, **self.tasks.pop()).result()
                        futures = []
                        # for kargs in self.tasks:
                        futures.append(pool.submit(Job, ))
                        for future in as_completed(futures):
                            print(future.result())
        except GeneratorExit:
            pass

    def restart(self):
        pass

    def stop(self):
        pass
