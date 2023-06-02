import os
import logging
import threading
from time import sleep
from watchdog.events import FileSystemEventHandler
from os.path import join
import shutil

dest_dir_sfx = r"E:\Download\Effects"
dest_dir_music = r"E:\Download\Muzyka"
dest_dir_video = r"E:\Download\Video"
dest_dir_image = r"E:\Download\Obrazy"
dest_dir_documents = r"E:\Download\Dokumenty"
dest_dir_arch_comp = r"E:\Download\Arch"

audio_extensions = (".mp3", ".wav", ".flac")
video_extensions = (".mp4", ".mkv", ".avi")
image_extensions = (".jpg", ".jpeg", ".png", ".gif")
document_extensions = (".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf")
arch_comp_extensions = (".zip", ".rar", ".7z")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class FileMover(FileSystemEventHandler):
    def __init__(self, observer, timeout_semaphore, source_dir):
        super().__init__()
        self.observer = observer
        self.timeout_semaphore = timeout_semaphore
        self.file_moved = False
        self.timer = None
        self.source_dir = source_dir

    def on_modified(self, event):
        with os.scandir(self.source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)

    def check_audio_files(self, entry, name):
        for audio_ext in audio_extensions:
            if name.endswith(audio_ext) or name.endswith(audio_ext.upper()):
                if entry.stat().st_size < 2_500_000 or "SFX" in name:
                    dest = dest_dir_sfx
                else:
                    dest = dest_dir_music
                self.move_file(dest, entry, name)
                logging.info(f"Moving document file: {name}")
                self.file_moved = True

    def check_video_files(self, entry, name):
        for video_ext in video_extensions:
            if name.endswith(video_ext) or name.endswith(video_ext.upper()):
                self.move_file(dest_dir_video, entry, name)
                logging.info(f"Moving document file: {name}")
                self.file_moved = True

    def check_image_files(self, entry, name):
        for image_ext in image_extensions:
            if name.endswith(image_ext) or name.endswith(image_ext.upper()):
                self.move_file(dest_dir_image, entry, name)
                logging.info(f"Moving document file: {name}")
                self.file_moved = True

    def check_document_files(self, entry, name):
        for document_ext in document_extensions:
            if name.endswith(document_ext) or name.endswith(document_ext.upper()):
                self.move_file(dest_dir_documents, entry, name)
                logging.info(f"Moving document file: {name}")
                self.file_moved = True

    def move_file(self, dest_dir, entry, name):
        dest = join(dest_dir, name)
        try:
            shutil.move(entry.path, dest)
        except PermissionError:
            logging.info(f"Permission denied for file: {name}. Waiting for the file download to complete...")

        if self.file_moved:
            self.observer.stop()

    def start_timer(self):
        self.timer = threading.Timer(10, self.check_activity_timeout)
        self.timer.start()

    def check_activity_timeout(self):
        if not self.file_moved:
            logging.info("Timeout reached. Exiting program.")
            self.observer.stop()
