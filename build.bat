@echo off
echo Limpando builds antigos...
rmdir /s /q build
rmdir /s /q dist
del main.spec

echo Gerando novo executavel...
pyinstaller --onefile --name BackupTool --noconsole --icon=icone.ico --add-data "config.json;." main.py

echo Finalizado!
pause