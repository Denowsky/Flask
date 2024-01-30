import threading, random, time, array

my_array = array.array('i',[])
threads = []
summary = 0


def append_array(arr):
    arr.append(random.randint(1, 100))

def make_sum(num):
    global summary
    summary += num

def threading_start(count):
    start_time = time.time()
    for _ in range(count):
        thread = threading.Thread(target=append_array, args=[my_array])
        threads.append(thread)
        thread.start()
    print(f'Время заполнения массива: {time.time()-start_time:2f}')
    reset_time = time.time()
    for elem in my_array:
         thread = threading.Thread(target=make_sum, args=[elem])
         threads.append(thread)
         thread.start()
    print(f'Время подсчёта суммы: {time.time()-reset_time:2f}')
    print(f'Время выполнения программы: {time.time()-start_time:2f}\nСумма: {summary}')
    for thread in threads:
        thread.join()

threading_start(1000000)
