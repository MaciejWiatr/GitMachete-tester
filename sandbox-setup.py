import os
import tempfile
import random
import string
file_dir = os.path.dirname(os.path.abspath(__file__))
remote_path = os.path.join(file_dir, 'remote/')
sandbox_path = os.path.join(file_dir, 'sandbox/')


def newRepo(*args):
    dir = args[0]
    os.chdir(dir)
    if len(args) > 1:
        opt = args[1]
        os.system(f'git init {opt}')
    else:
        os.system('git init')


def newBranch(branch_name):
    os.system(f'git checkout -b {branch_name}')

#rstrip

def commit(*args):
    branch = os.popen('git symbolic-ref --short HEAD').read().strip()
    random_name = "".join(random.choices(string.ascii_letters,k=10))
    f = f'{random_name}.txt'
    print(f)
    os.system(f'touch {f}')
    os.system(f'git add {f}')
    os.system(f'git commit -m "{"".join(args)}"')


def push():
    branch = os.popen('git symbolic-ref --short HEAD').read()
    os.system(f'git push -u origin {branch}')


newRepo(remote_path, '--bare')
newRepo(sandbox_path)
os.system(f'git remote add origin {remote_path}')
newBranch('root')
commit('root')
newBranch('develop')
commit('develop commit')
newBranch('allow-ownership-link')
commit('Allow ownership links')
push()
newBranch('build-chain')
commit('Build arbitrarily long chains')
os.system('git checkout allow-ownership-link')
commit('1st round of fixes')
os.system('git checkout develop')
commit('Other develop commit')
push()
newBranch('call-ws')
commit('Call web service')
commit('1st round of fixes')
push()
newBranch('drop-constraint')
commit('Drop unneeded SQL constraints')
os.system('git checkout call-ws')
commit('2nd round of fixes')
os.system('git checkout root')
newBranch('master')
commit('Master commit')
push()
newBranch('hotfix/add-trigger')
commit('HOTFIX Add the trigger')
push()
os.system('git commit --amend -m "HOTFIX Add the trigger (amended)"')
machete_string="""
develop
    allow-ownership-link PR #123
        build-chain PR #124
    call-ws
master
    hotfix/add-trigger
"""
with open('.git/machete',"w+") as file:
    file.writelines(machete_string)
os.system('git branch -d root')
os.system('git machete status')