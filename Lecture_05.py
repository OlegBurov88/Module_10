from threading import Thread, Event
from time import sleep


def first_worker():
    print('Первый рабочий приступил к своей задаче')
    event.wait()
    print('Первый рабочий продолжил выполнять задачу')
    sleep(5)
    print('Первый рабочий закончил выполнять задачу')
    event.clear()


def second_worker():
    print('Второй рабочий приступил к своей задаче')
    sleep(10)
    print('Второй рабочий закончил выполнять задачу')
    event.set()


event = Event()

thread_1 = Thread(target=first_worker)
thread_2 = Thread(target=second_worker)

thread_1.start()
thread_2.start()
