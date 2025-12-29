@echo off

python.exe -m pip install --upgrade pip
pip install colorama

py wlintro.py
:loop
py game.py
pause
goto loop