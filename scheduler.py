# def coroutine(f):
#     def wrap(*args, **kwargs):
#         gen = f(*args, **kwargs)
#         gen.send(None)
#         return gen
#     return wrap
from concurrent.futures.thread import ThreadPoolExecutor


class Scheduler:
    def __init__(self, pool_size: 10):
        self.pool_size = pool_size
        self.tasks = list()

    def schedule(self, task):
        self.tasks.append(task)

    # @coroutine
    def run(self):
        with ThreadPoolExecutor(max_workers=self.pool_size) as pool:
            futures = {pool.submit(task() for task in self.tasks}
            for future in as_completed(futures):
                try:
                    item = dict()
                    item['city_name'] = futures[future]
                    item['forecasts'] = future.result()['forecasts']
                    result.append(item)
                except Exception as exc:
                    print(f'{futures[future]} сгенерировано исключение: {exc}')  # Бобавить логтрование

    def restart(self):
        pass

    def stop(self):
        pass
