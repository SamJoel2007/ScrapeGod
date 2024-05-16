@echo off
set "username=%USERNAME%"
set path="C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
copy config.bat %path%