import multiprocessing, random, time, array

my_array = array.array('i',[])
processes = []
summary = 0

def append_array(arr, count):
    for _ in range(count):
        arr.append(random.randint(1, 100))

def make_sum(num):
    global summary
    summary += num

def threading_start():
    start_time = time.time()
    # for _ in range(count):
    #     process = multiprocessing.Process(target=append_array, args=[my_array])
    #     processes.append(process)
    #     process.start()
    # print(f'Время заполнения массива: {time.time()-start_time:2f}')
    for elem in my_array:
         process = multiprocessing.Process(target=make_sum, args=[elem])
         processes.append(process)
         process.start()
    print(f'Время подсчёта суммы: {time.time()-start_time:2f}')
    print(f'Время выполнения программы: {time.time()-start_time:2f}\nСумма: {summary}')
    for process in processes:
        process.join()

if __name__ == '__main__':
    append_array(my_array, 10)
    threading_start()
