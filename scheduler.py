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
        manager = self.run()
        manager.send(task)

    @coroutine
    def run(self):
        while True:
            try:
                task = (yield)
                task()
            except GeneratorExit:
                raise

    def restart(self):
        pass

    def stop(self):
        pass
