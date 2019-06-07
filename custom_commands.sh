#!/bin/bash

#prints the input
function print_my_input(){
  echo 'Your input: ' $1
}

function new_project(){
  echo 'creating project: ' $1
  cd ~
  cd Desktop/projects
  python3 new_project.py $1
  mkdir $1
  cd $1
  git init
  git remote add origin git@github.com:JohnVicke/$1.git
  touch README.md
  git add .
  git commit -m "initial commit"
  git push origin master
  echo '-----Complete-----'
}