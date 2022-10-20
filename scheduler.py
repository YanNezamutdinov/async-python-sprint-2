import json
import uuid
from concurrent.futures._base import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

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
        with open('myfile.json', 'r') as f:
            try:
                data = json.load(f)
            except:
                data = dict()
        data[str(uuid.uuid4())] = kwargs

        with open('myfile.json', 'w') as f:
            json.dump(data, f)

    @coroutine
    def run(self):
        try:
            while True:
                with open("myfile.json", 'r') as f:
                    data = json.load(f)
                with ThreadPoolExecutor(max_workers=self.pool_size * 2) as pool:
                    future_to_url = {pool.submit(Job, name=key, **val): val for key, val in data.items()}
                    # futures = []
                    # futures.append(pool.submit(Job, ))
                    for future in as_completed(future_to_url):
                        print(future.result())
                    #     print(future.)
        except GeneratorExit:
            pass

    # def restart(self):
    #     pass
    #
    # def stop(self):
    #     pass
