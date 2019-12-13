# -*- coding: utf-8 -*-
import filecmp
import os
import shutil
import tempfile
import time


class MacheteTester:

    def __init__(self):
        self.file_directory = os.path.dirname(os.path.abspath(__file__))
        self.sandbox_file_path = os.path.join(
            self.file_directory, "data/sandbox-setup.sh")
        self.correct_output = os.path.join(
            self.file_directory, 'data/correct_output.txt')
        self.machete_sandbox_remote = ""
        self.machete_sandbox = ""
        self.status = None
        self.debug = False

    def __del__(self):
        if self.debug == False:
            os.remove('setup.log')
            os.remove('status.log')

    def createTempDirs(self):
        self.remote_temp_dir = tempfile.TemporaryDirectory()
        self.sandbox_temp_dir = tempfile.TemporaryDirectory()
        self.machete_sandbox_remote = self.remote_temp_dir.name
        self.machete_sandbox = self.sandbox_temp_dir.name

    def setupSandbox(self):
        os.system(
            f'bash {self.sandbox_file_path} {self.machete_sandbox_remote} {self.machete_sandbox} > setup.log 2>&1')

    def checkStatus(self):
        os.chdir(self.machete_sandbox)
        os.system(f'git machete status > {self.file_directory}/status.log')
        time.sleep(1)

    def compareStatus(self):
        os.chdir(self.file_directory)
        if filecmp.cmp(self.correct_output, 'status.log') == True:
            self.status = 'OK'
            return 'OK'
        else:
            self.status = 'Not OK'
            return 'Not OK'


if __name__ == '__main__':
    Tester = MacheteTester()
    Tester.debug = False
    Tester.createTempDirs()
    Tester.setupSandbox()
    Tester.checkStatus()
    # print(Tester.compareStatus())
    if Tester.compareStatus() == 'OK':
        print('''\n
😍 Your machete is sharp a.f and ready to go 🔪🌲
\n''')
    else:
        print('''\n
Im sorry but something is wrong with your machete, check setup.log to see what went wrong\n''')
