import subprocess
import psutil
from time import sleep
from loguru import logger


class Show():

    def __init__(self):
        self.child_pid = None

    def save_img(self, content, file):
        with open(file, 'wb') as f:
            f.write(content)
            logger.debug(f'save_img: {file}')

    def show_img(self, file_name):
        shell_process = subprocess.Popen([file_name], shell=True)
        parent = psutil.Process(shell_process.pid)
        for _ in range(999):
            children = parent.children(recursive=True)
            if children:
                break
            sleep(0.1)
        self.child_pid = children[0].pid

    def close_img(self):
        subprocess.check_output(f"Taskkill /PID {self.child_pid} /F")
