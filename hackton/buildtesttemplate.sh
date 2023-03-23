#! /bin/bash
cd C:/Users/swuser/PycharmProjects/
git clone https://github.com/sergeysmirnoff/GeneratedProject.git ./GeneratedProject1
cd GeneratedProject1
py -m venv .venv
source .venv/Scripts/activate
py -m pip install -r ./requirements.txt

