from queue import Queue
import time, threading


def getter(queue):
    while True:
        time.sleep(3)
        item = queue.get()
        print(threading.current_thread(), 'Взят элемент', item)


q = Queue(maxsize=10)
thread_1 = threading.Thread(target=getter, args=(q,), daemon=True)
thread_1.start()

for i in range(10):
    time.sleep(2)
    q.put(i)
    print(threading.current_thread(), 'положил элемент', i)

print('Конец программы')
