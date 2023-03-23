#! /bin/bash
cd C:/Users/swuser/PycharmProjects/
git clone https://github.com/sergeysmirnoff/TemplateProject.git ./TemplateProject9
cd TemplateProject9
py -m venv .venv
source .venv/Scripts/activate
py -m pip install -r ./requirements.txt

