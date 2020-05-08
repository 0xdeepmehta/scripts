#!/usr/bin/python3
from github import Github
import pickle
import sys

with open("/home/vivekascoder/scripts/credentials.cred", "rb") as file:
    data = pickle.load(file)
    username, password = data['username'], data['password']

git = Github(username, password)
user = git.get_user()
repo = user.get_repo('urls')
content = repo.get_contents("index.html")

html_file = open("/home/vivekascoder/scripts/index.html", "a+")

if len(sys.argv) ==3:
    temp = f"\n<li><a href='{sys.argv[1]}'>{sys.argv[2]}</a></li>"
else:
    print("[+] You need to provide two argument, master...")
    sys.exit(0)

html_file.write(temp)
html_file.close()
file = open("/home/vivekascoder/scripts/index.html", "r")
data = file.read()
# print(data)
file.close()

try:
    repo.update_file("index.html", temp, data, content.sha, 'master')
    # print(data)
    print("[+] 🔥 You're data is updated ...")
except:
    print("[+] There are some problem while updating github file, master ...")
    sys.exit(0)
