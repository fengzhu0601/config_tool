@echo off
python script/gen.py template/ xml/ codegen/ pbgen/

xcopy codegen\golang\game\* ..\src\ /e /y /Q

pause
