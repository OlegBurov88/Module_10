from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            line = line.rstrip('\n')
            if not line:
                break
            else:
                all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start_time = datetime.now()
    for nane in filenames:
        read_info(nane)
    end_time = datetime.now()
    print(f' {end_time - start_time} (линейный)')

    start_time = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = datetime.now()
    print(f' {end_time - start_time} (многопроцессный)')
