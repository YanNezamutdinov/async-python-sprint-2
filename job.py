def coroutine(f):
    def wrap(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen
    return wrap

class Job:
    def __init__(self, name=None, start_at="", max_working_time=-1, tries=0, dependencies=[]):
        self.name = name
        self.start_at = start_at
        self.max_working_time = max_working_time
        self.tries = tries
        self.dependencies = dependencies

    def __call__(self, *args, **kwargs):
        print(self.name)


    def run(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass


# class DeferredJob(Job):
#
#     def run(self):



