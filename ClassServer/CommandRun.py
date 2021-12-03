import subprocess, threading


class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self):
        def target():
            print('Thread started')
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()
            print('Thread finished')

        thread = threading.Thread(target=target)
        thread.start()

        if thread.is_alive():
            print('Terminating process')
            thread.join()

