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

    def schedule(self, **kwargs):
        # with open('myfile.txt', 'a') as f:
        #     line = f'{uuid.uuid4()}: {kargs}'
        #     f.write(line)
        #     f.write('\n')
        for key in kwargs:
            print(key)

        with open('myfile.json', 'r') as f:
            try:
                data = json.load(f)
            except:
                data = list()
        data.append({str(uuid.uuid4()): dict(kwargs)})

        with open('myfile.json', 'w') as f:
            json.dump(data, f)


        # data = {line.strip() for line in open("myfile.txt", 'r')}


    @coroutine
    def run(self):
        try:
            while True:
                for line in open("myfile.json", 'r'):
                    print(line.get('start_at'))
                # data = {dict(line) for line in open("myfile.json", 'r')}
                with ThreadPoolExecutor(max_workers=self.pool_size) as pool:
                    # for item in data:
                    #     print(item.get('start_at'))
                    # futures = []
                    # futures.append(pool.submit(Job, ))
                    # for future in as_completed(futures):
                    #     print(future.result())
                    pass
        except GeneratorExit:
            pass

    # def restart(self):
    #     pass
    #
    # def stop(self):
    #     pass
