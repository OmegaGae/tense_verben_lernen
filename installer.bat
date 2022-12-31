@echo on 
echo Start installing all needed packages and executable for VerbenLernen APP
py -m pip install -r requirements.txt
pyi-makespec --paths=./scripts --paths=./lib --paths=./lib/edit --paths=./lib/img --paths=./lib/windows --paths=./lib/img/positive_smiley.png --paths=./lib/img/sad_smiley.jpg --paths=./lib/img/sad_smiley_2.png --paths=./lib/img/smiley_with_thumb_up.png --paths=./lib/img/smiley_with_tear.jpg --paths=./lib/edit/starke_unregelmeassie.txt --noconsole VerbenLernen.py
pyinstaller VerbenLernen.spec
robocopy .\lib .\dist\VerbenLernen\lib
robocopy .\lib\edit .\dist\VerbenLernen\lib\edit
robocopy .\lib\img .\dist\VerbenLernen\lib\img
robocopy .\lib\windows .\dist\VerbenLernen\lib\windows
robocopy .\scripts .\dist\VerbenLernen\scripts
echo END OF INSTALLATION THE .EXE GAME CAN BE FOUND IN \dist\VerbenLernen\VerbenLernen.exe (type: Application)
TIMEOUT 10