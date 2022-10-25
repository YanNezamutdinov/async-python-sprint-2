# def coroutine(f):
#     def wrap(*args, **kwargs):
#         gen = f(*args, **kwargs)
#         gen.send(None)
#         return gen
#     return wrap
import threading
import time
from datetime import datetime


class Job:

    @staticmethod
    def run(key=None, func=None, start_at=None, max_working_time=-1, tries=0, dependencies=[]):
        if start_at:
            print("Start Job")
            time_obj = datetime.combine(datetime.today().date(), datetime.strptime(start_at, '%H:%M').time())
            delayed = int((time_obj - datetime.today()).total_seconds())
            if delayed > 0:
                timer = threading.Timer(delayed, func)
                timer.start()
                timer.join()
        print("Fin Job")
        return key

    def pause(self):
        pass

    def stop(self):
        pass


# class DeferredJob(Job):
#
#     def run(self):



