import subprocess
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from log import logger


class RestartHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.start_process()

    def start_process(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen([sys.executable, self.script])

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            logger.info(f'File modified: {event.src_path}')
            self.start_process()


if __name__ == "__main__":
    path = '.'  # Путь к директории, которую нужно отслеживать
    script = 'bot.py'  # Замените на имя вашего скрипта

    event_handler = RestartHandler(script)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
