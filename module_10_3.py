import threading, time
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            up = randint(50, 500)
            self.balance += up
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {up}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            dow = randint(50, 500)
            print(f'Запрос на {dow}')
            if dow <= self.balance:
                self.balance -= dow
                print(f'Снятие: {dow}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
