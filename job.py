from time import sleep


class Job:
    def __init__(self, start_at="", max_working_time=-1, tries=0, dependencies=[]):
        sleep(2)
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



