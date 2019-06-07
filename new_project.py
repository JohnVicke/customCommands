import sys
from github import Github
from variables import *
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

g = Github(username, password)
init(strip=not sys.stdout.isatty())

if __name__ == '__main__':
  print("----- CURRENT REPOS ON GITHUB -----")
  for repo in g.get_user().get_repos():
    print(repo.name)

  user = g.get_user()
  repo = user.create_repo(sys.argv[1])
  
  print("----- UPDATED LIST OF  REPOS  -----")

  for repo in g.get_user().get_repos():
    print('*', sys.argv[1]) if repo.name == sys.argv[1] else print(repo.name)

  print("-----------------------------------")
  cprint(figlet_format(':)', font='starwars'), 'yellow', 'on_red', attrs=['bold'])    
