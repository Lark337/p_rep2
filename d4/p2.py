import requests
import multiprocessing
from pathlib import Path
import time
import sys


def load_img(url):
    img_data = requests.get(url).content
    name = url.split("/")[-1]
    dir1 = "img2"
    p = Path(__file__).parent.resolve() / dir1
    Path(p).mkdir(exist_ok=True)
    if ".jpg" not in name:
        name += ".jpg"
    with open(str(p) + "/" + name, 'wb') as handler:
        handler.write(img_data)



url_list = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Felis_silvestris_silvestris.jpg/275px-Felis_silvestris_silvestris.jpg",
    "https://www.tourdom.ru/upload/iblock/e33/e335dc672050dc1267f32d8ef4f074b4.jpg",
    "https://img.freepik.com/free-photo/cute-cat-relaxing-in-studio_23-2150692730.jpg"]

processes = []
if __name__ == '__main__':
    if len(sys.argv) > 1:
        url_list = sys.argv.copy()
        url_list.pop(0)

    start_time = time.time()
    for url in url_list:
        process = multiprocessing.Process(target=load_img, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"На выполнение затрачено: {time.time() - start_time} с")