import json
import threading
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
        open('myfile.json', 'x')
        self.condition = threading.Condition()

    def schedule(self, func, **kwargs):
        with open('myfile.json', 'r') as f:
            try:
                data = json.load(f)
            except Exception:
                data = dict()
        kwargs.update(func=func.__name__)
        if kwargs.get("dependencies"):
            dep = [dependence_func.__name__ for dependence_func in kwargs.get("dependencies")]
            kwargs.update(dependencies=dep)
        data[str(uuid.uuid4())] = kwargs

        with open('myfile.json', 'w') as f:
            json.dump(data, f)

    @coroutine
    def run(self):
        try:
            while True:
                with open("myfile.json", 'r') as f:
                    data = json.load(f)
                with ThreadPoolExecutor(max_workers=self.pool_size) as pool:
                    future_to_url = {pool.submit(Job.run, key=key, cond=self.condition, **val) for key, val in data.items()}
                    for future in as_completed(future_to_url):
                        with open('myfile.json', 'r') as f:
                            data = json.load(f)
                            del data[future.result()]
                        with open('myfile.json', 'w') as f:
                            json.dump(data, f)
        except GeneratorExit:
            pass
