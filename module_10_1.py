import time
import threading


def write_words(word_count, file_name):
    try:
        with open(file_name, 'a', encoding='utf-8') as f:
            for i in range(word_count):
                f.write(f"Какое-то слово № {i+1}\n")
                #sleep(1)
            print(f'Завершилась запись в файл {f}')
    except FileExistsError:
        print(f'Файл {file_name} не существует.')


start_def_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_def_time = time.time()

start_thread_time = time.time()

threads = []
args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt'),
]


for arg in args:
    t = threading.Thread(target=write_words, args=arg)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_thread_time = time.time()

print(end_def_time - start_def_time)
print(end_thread_time - start_thread_time)