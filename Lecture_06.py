import multiprocessing, time, threading

counter = 0


def first_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
        print('Первый рабочий запустил процесс ', counter)
    print('Первый рабочий изменил значение счётчика, и теперь он равен ', counter)


def second_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
        print('Второй рабочий запустил процесс ', counter)
    print('Второй рабочий изменил значение счётчика, и теперь он равен ', counter)


# thread_1 = threading.Thread(target=first_worker, args=(10,))
# thread_2 = threading.Thread(target=second_worker, args=(5,))
#
# thread_1.start()
# thread_2.start()

if __name__ == '__main__':
    process_1 = multiprocessing.Process(target=first_worker, args=(10,))
    process_2 = multiprocessing.Process(target=second_worker, args=(5,))

    process_1.start()
    process_2.start()
