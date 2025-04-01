import threading
import time
import random


class City_library:
    def __init__(self):
        self.reader_count = threading.Semaphore(value=3)

    def meet_reader(self, reader):
        print(f"\n Спрашиваем читателя {reader}")
        self.reader_count.acquire()

        print(f"Ищем книгу для читателя {reader}")
        time.sleep(random.randint(4, 10))

        print(f"Завершение работы с читателем {reader}")
        self.reader_count.release()

    def readers(self, count):
        for reader in range(1, count + 1):
            reader_thread = threading.Thread(target=self.meet_reader, args=[reader])
            reader_thread.start()


if __name__ == "__main__":
    read = City_library()

    count = 6
    read.readers(count)
