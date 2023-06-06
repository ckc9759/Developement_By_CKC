
import pyttsx3
'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print('DAVID: ' + voices[0].id)
print('HAZEL: ' + voices[1].id)
'''

'''
import pyttsx3
import getpass
import os
USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath("C:\Users\Chaitanya K Chauhan\Dropbox\My PC (ckc)\Desktop\Developement\Jarvis\test.py"))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)
'''

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()
