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

    def schedule(self, task):
        self.tasks.append(task)
        print(self.tasks)
        self.run().send(task)

    @coroutine
    def run(self):
        try:
            while True:
                data_chunk = (yield)
                self.tasks.remove(data_chunk)
                data_chunk()
        except GeneratorExit:
            pass

    def restart(self):
        pass

    def stop(self):
        pass
