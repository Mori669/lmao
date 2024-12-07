import multiprocessing
import time
from datetime import timedelta


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


filenames = [f'./file {i}.txt' for i in range(1, 5)]


def linear_execution():
    start_time = time.monotonic()
    for filename in filenames:
        read_info(filename)
    end_time = time.monotonic()
    print(f"Линейный вызов: {timedelta(seconds=end_time - start_time)}")


def parallel_execution():
    start_time = time.monotonic()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.monotonic()
    print(f"Многопроцессный вызов: {timedelta(seconds=end_time - start_time)}")


if __name__ == "__main__":
    linear_execution()
    parallel_execution()
