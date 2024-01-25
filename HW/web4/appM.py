import multiprocessing, time, requests, shutil


processes = []

def url_input():
    urls = []
    try:
        count = int(input('Сколько ссылок ввести?\n>: '))
    except ValueError:
        print('Необходимо количество строк')
        return
    for i in range(count):
        url = input(f'{i+1} ссылка\n>: ')
        if '.jpg' in url or '.png' in url or '.webp' in url:
            urls.append(url)
        else:
            print('В ссылке не содержится изображение')
    return urls

def download(url, st):
    response = requests.get(url, stream=True)
    index = url[::-1].find('/')
    file_name = url[-index:]
    if response.status_code == 200:
        with open(f'./{file_name}','wb') as f:
            shutil.copyfileobj(response.raw, f)
        print('Успех. Изображение скачено:', file_name, f'Время загрузки: {time.time()-st:2f}')
    else:
        print('Неудача. Изображение на сайте не обнаружено')


if __name__ == '__main__':
    url_list = url_input()
    start_time = time.time()

    if url_list:
        for url in url_list:
            multiprocess = multiprocessing.Process(target=download, args=[url, start_time])
            processes.append(multiprocess)
            multiprocess.start()

    for multiprocess in processes:
        multiprocess.join()

    print(f'Время выполнения: {time.time()-start_time:2f}')