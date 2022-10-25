from scheduler import Scheduler

def test_func_one():
    pass

def test_func_two():
    pass

if __name__ == '__main__':
    open('myfile.json', 'w').close()
    scheduler = Scheduler(pool_size=3)
    scheduler.schedule(test_func_one, start_at="19:50", dependencies=[])
    scheduler.schedule(test_func_two, start_at="19:51")
    scheduler.schedule(test_func_one, start_at="19:52")
    scheduler.schedule(test_func_one, start_at="19:50", dependencies=[])
    scheduler.schedule(test_func_two, start_at="19:51")
    scheduler.schedule(test_func_one, start_at="19:52")
    scheduler.schedule(test_func_one, start_at="19:50", dependencies=[])
    scheduler.schedule(test_func_two, start_at="19:51")
    scheduler.schedule(test_func_one, start_at="19:52")
    scheduler.schedule(test_func_one, start_at="19:50", dependencies=[])
    scheduler.schedule(test_func_two, start_at="19:51")
    scheduler.schedule(test_func_one, start_at="19:52")
    # scheduler.schedule(start_at="12:00")
    # scheduler.schedule(start_at="12:00")
    # scheduler.schedule(start_at="12:00")
    # scheduler.schedule(start_at="12:00")
    # scheduler.schedule(start_at="12:00")
    # scheduler.schedule(start_at="12:00")
    # scheduler.schedule(start_at="12:00")
    # scheduler.schedule(start_at="12:00")
    # scheduler.schedule(start_at="12:00")
    # scheduler.schedule(start_at="12:00")
    # scheduler.schedule(start_at="12:00")
    # scheduler.schedule(start_at="12:00")
    scheduler.run()
