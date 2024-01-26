import asyncio, time, aiohttp, aiofiles

async def url_input():
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

async def download(url, st):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            index = url[::-1].find('/')
            file_name = url[-index:]
            if response.status == 200:
                f = await aiofiles.open(f'./{file_name}', mode='wb')
                await f.write(await response.read())
                await f.close()
                print('Успех. Изображение скачено:', file_name, f'Время загрузки: {time.time()-st:2f}')
            else:
                print('Неудача. Изображение на сайте не обнаружено')

async def main():
    task = []
    start_time = time.time()
    if url_list:
        for url in url_list:
            task.append(asyncio.create_task(download(url, start_time)))
        await asyncio.gather(*task)
    print(f'Время выполнения: {time.time()-start_time:2f}')

if __name__ == '__main__':
    url_list = asyncio.run(url_input())
    asyncio.run(main())