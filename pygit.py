#!/usr/local/bin/python3

import sys 
from github import Github

g = Github(sys.argv[1])

repo = g.get_repo(sys.argv[2])

for pull in repo.get_pulls():
    print (pull)





