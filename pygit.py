#!/usr/local/bin/python3

import sys 
from github import Github

#g = Github("1dd4d253131209b93194524c51643d53fc150067")
g = Github(sys.argv[1])


repo = g.get_repo(sys.argv[2])

for pull in repo.get_pulls():
    print (pull)





