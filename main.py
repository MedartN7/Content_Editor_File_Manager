import os
import logging
from watchdog.observers import Observer
import threading
from time import sleep
from filemover import FileMover

source_dir = r"C:\Users\User\Desktop"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    observer = Observer()
    timeout_semaphore = threading.Semaphore(value=0)
    file_mover = FileMover(observer, timeout_semaphore, source_dir)
    observer.schedule(file_mover, source_dir, recursive=True)

    try:
        observer.start()
        logging.info('Looking for files to move...')
        file_mover.start_timer()
        observer.join()
    except KeyboardInterrupt:
        observer.stop()

    if file_mover.timer is not None:
        file_mover.timer.cancel()
