import threading
import random
import time


class Bank:
    def __init__(self, lock, balance=0):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        with self.lock:
            for i in range(100):
                dep = random.randint(50, 100)
                self.balance += dep
                print(f'Пополнение: {dep}. Баланс: {self.balance}')
                time.sleep(0.001)

    def take(self):
        with self.lock:
            for i in range(100):
                dep = random.randint(50, 100)
                print(f'Запрос на {dep}.')
                if self.balance >= dep:
                    self.balance -= dep
                    print(f'Снятие: {dep}. Баланс: {self.balance}')
                    time.sleep(0.001)
                else:
                    print(f'Запрос отклонён, недостаточно средств.')
                    break


lock = threading.Lock()

bk = Bank(lock)

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')