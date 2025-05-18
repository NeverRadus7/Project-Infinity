@echo off

python.exe -m pip install --upgrade pip
pip install colorama
pip install rich

py wlintro.py
:loop
py game.py
goto loop