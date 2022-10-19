from threading import Thread


class Job:
    def __init__(self, start_at="", max_working_time=-1, tries=0, dependencies=[]):
        print(start_at)

    def run(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass


# class DeferredJob(Job):
#
#     def run(self):



