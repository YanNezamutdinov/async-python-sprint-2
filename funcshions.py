import os
import shutil
from concurrent.futures._base import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from method import YandexWeatherAPI, CITIES


def crud_dir():
    for _i in range(5):
        if not os.path.isdir(f"folder_{_i}"):
            os.makedirs(f"folder_{_i}/chdir1/chdir2/chdir3")
        shutil.rmtree(f"folder_{_i}")
    print("crud_dir finish!")


def crud_file():
    with open("test_file.txt", "w") as file:
        file.writelines([f"line number {_i}\n" for _i in range(1000)])
    print("crud_file finish!")


def get_weather():
    with ThreadPoolExecutor() as pool:
        futures = {pool.submit(YandexWeatherAPI().get_forecasting, city_name=city): city for city in CITIES}
        for future in as_completed(futures):
            try:
                print(future.result())
            except Exception as exc:
                print(f'{futures[future]} сгенерировано исключение: {exc}')


dct_func = {
        crud_dir.__name__: crud_dir,
        crud_file.__name__: crud_file,
        get_weather.__name__: get_weather
    }
