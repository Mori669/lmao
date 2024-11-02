import os
import time

directory = r'C:\Users\mori66_9\PycharmProjectsES\pythonProject1\tasks 2\module_7'

for root, dirs, files in os.walk(directory):
    for file_name in files:
        file_path = os.path.join(root, file_name)

        last_modified_time = os.path.getmtime(file_path)
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modified_time))

        file_size = os.path.getsize(file_path)

        parent_directory = os.path.dirname(file_path)

        print(f"Файл: {file_name}")
        print(f"Полный путь: {file_path}")
        print(f"Последнее изменение: {formatted_time}")
        print(f"Размер файла: {file_size} байт")
        print(f"Родительская директория: {parent_directory}")
        print("-" * 40)
