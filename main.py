from funcshions import crud_file, get_weather, crud_dir
from scheduler import Scheduler

if __name__ == '__main__':
    scheduler = Scheduler(pool_size=3)
    scheduler.schedule(crud_dir, dependencies=[crud_file, get_weather])
    scheduler.schedule(crud_file)
    scheduler.schedule(get_weather)

    scheduler.run()
