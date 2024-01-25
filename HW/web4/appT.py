import threading, time, requests, shutil


threads = []

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

url_list = url_input()
start_time = time.time()

def download(url):
    response = requests.get(url, stream=True)
    index = url[::-1].find('/')
    file_name = url[-index:]
    if response.status_code == 200:
        with open(f'./{file_name}','wb') as f:
            shutil.copyfileobj(response.raw, f)
        print('Успех. Изображение скачено:', file_name, f'Время загрузки: {time.time()-start_time:2f}')
    else:
        print('Неудача. Изображение на сайте не обнаружено')

if url_list:
    for url in url_list:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()

print(f'Время выполнения: {time.time()-start_time:2f}')