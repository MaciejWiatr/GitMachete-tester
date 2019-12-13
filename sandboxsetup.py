import os
import tempfile
import random
import string


class SandboxSetup():

    def __init__(self):
        self.temp1 = tempfile.TemporaryDirectory()
        self.temp2 = tempfile.TemporaryDirectory()
        self.file_dir = os.path.dirname(os.path.abspath(__file__))
        self.remote_path = self.temp1.name
        self.sandbox_path = self.temp2.name

    def newRepo(self, *args):
        dir = args[0]
        os.chdir(dir)
        if len(args) > 1:
            opt = args[1]
            os.system(f'git init {opt}')
        else:
            os.system('git init')
        return self

    def newBranch(self, branch_name):
        os.system(f'git checkout -b {branch_name}')
        return self

    # rstrip

    def commit(self, *args):
        # branch = os.popen('git symbolic-ref --short HEAD').read().strip()
        random_name = "".join(random.choices(string.ascii_letters, k=10))
        f = f'{random_name}.txt'
        # f = f'{branch}-{args[0]}.txt'
        os.system(f'touch {f}')
        os.system(f'git add {f}')
        os.system(f'git commit -m "{"".join(args)}"')
        return self

    def push(self):
        branch = os.popen('git symbolic-ref --short HEAD').read()
        os.system(f'git push -u origin {branch}')
        return self

    def setupSandbox(self):
        self.newRepo(self.remote_path, '--bare')
        self.newRepo(self.sandbox_path)
        os.system(f'git remote add origin {self.remote_path}')
        self.newBranch('root')\
            .commit('root')\
            .newBranch('develop')\
            .commit('develop commit')\
            .newBranch('allow-ownership-link')\
            .commit('Allow ownership links')\
            .push()\
            .newBranch('build-chain')\
            .commit('Build arbitrarily long chains')
        os.system('git checkout allow-ownership-link')
        self.commit('1st round of fixes')
        os.system('git checkout develop')
        self.commit('Other develop commit')\
            .push()\
            .newBranch('call-ws')\
            .commit('Call web service')\
            .commit('1st round of fixes')\
            .push()\
            .newBranch('drop-constraint')\
            .commit('Drop unneeded SQL constraints')
        os.system('git checkout call-ws')
        self.commit('2nd round of fixes')
        os.system('git checkout root')
        self.newBranch('master')\
            .commit('Master commit')\
            .push()\
            .newBranch('hotfix/add-trigger')\
            .commit('HOTFIX Add the trigger')\
            .push()
        os.system('git commit --amend -m "HOTFIX Add the trigger (amended)"')
        machete_string = """
develop
    allow-ownership-link PR #123
        build-chain PR #124
    call-ws
master
    hotfix/add-trigger
"""
        with open('.git/machete', "w+") as file:
            file.writelines(machete_string)
        os.system('git branch -d root')
        machete_status_process = os.popen(f'git machete status')
        machete_status = machete_status_process.read()
        machete_status_process.close()
        return machete_status


if __name__ == '__main__':
    Setup = SandboxSetup()
    Setup.setupSandbox()
