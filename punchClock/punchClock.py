# please run "pip install gitpython"
# run this only from root folder
# make sure git user is configured

from datetime import datetime
import os
from git import Repo
import sys
import argparse

parser = argparse.ArgumentParser(description=''' Punch clock for R and D projects. ''')
parser.add_argument('name', help='Your name')
parser.add_argument('mode', help='"in" (for starting counter) or "out" (to push end commit)')
args = parser.parse_args()

name = args.name
mode = args.mode

now = datetime.now()
myfolder = os.path.abspath(os.getcwd())
print(myfolder)
current_time = now.strftime("%H:%M:%S")
current_day = datetime.today().strftime('%Y-%m-%d')

# Caminho para o arquivo de log onde os registros serão salvos
log_file = os.path.join(myfolder, +name+'.txt')

# Verifica quantas linhas já existem no arquivo de log
if os.path.exists(log_file):
    with open(log_file, 'r') as f:
        lines = f.readlines()
        tam_lines = len(lines)
else:
    tam_lines = 0

# Incrementa o contador para o próximo registro
next_number = tam_lines + 1

if mode == 'out':
    task = input("Enter what you've done: ")
    text = current_time+" >> "+task+"\n"
    msg = "Ck_"+next_number+" - Punch created for "+name+" at "+current_day+" - "+current_time
else:
    text = current_day+" : "+current_time+" - "
    msg = "Ck_"+next_number+" - In registred for "+name+" at "+current_day+" - "+current_time

f = open('./punchClock/'+name+'.txt','a+')
f.write(text)
f.close()
print(msg)

PATH_OF_GIT_REPO = myfolder+'/.git'  # make sure .git folder is properly configured
repo = Repo(PATH_OF_GIT_REPO)
repo.git.add('./punchClock/'+name+'.txt')
repo.index.commit(msg)
origin = repo.remote(name='origin')
origin.push()
