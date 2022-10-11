from time import sleep

from job import print_job
from scheduler import Scheduler

if __name__ == '__main__':
    scheduler = Scheduler(pool_size=3)
    scheduler.schedule(print_job)
    sleep(1)
    scheduler.schedule(print_job)
    sleep(2)
    scheduler.schedule(print_job)
    sleep(3)
    scheduler.schedule(print_job)
    scheduler.schedule(print_job)
    scheduler.schedule(print_job)
