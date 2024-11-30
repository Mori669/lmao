import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power, enemy=100):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = enemy

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemy > 0:
            self.enemy -= self.power
            days += 1
            print(f'{self.name} сражается {days} день(дня)..., осталось {self.enemy}')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все рыцари победили врагов!")