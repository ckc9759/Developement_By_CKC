import pyttsx3
import datetime
from datetime import date
import time
import winsound
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit
import pyautogui

flag = 0

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate',205)
# print(voices)
# print(voices[1].id)

# speak function to speak an audio


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetme():
    '''
    To greet me based on the current time
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("  Good Morning !")
    elif hour >= 12 and hour < 18:
        speak("  Good Afternoon !")
    else:
        speak("  Good Evening !")

    speak("I am Jarvis")
    time.sleep(0.3)
    # speak("Loading records")
    # #beep sound
    # freq=1500
    # duration=1500  #milliseconds
    # winsound.Beep(freq,duration)
    # time.sleep(0.3)
    # speak("We are online and ready !!")
    time.sleep(0.3)
    greet_list = ['Test complete, beginning diagonosis','At your service sir', 'I had indeed been uploaded sir, ready to go', 'We are online and ready sir', 'How may i help you sir !!', 'Checking for updates, initializing sir', 'Importing preferences and calibrating virtual environment',
                  'All clear sir, waiting for your command', 'Sir, There are still terrabytes of calculations needed before start sir. On it !',]
    len_greet = len(greet_list)
    rand_index = random.randint(0, len_greet-1)
    speak(greet_list[rand_index])


def takeCommand():
    '''
    To take microphone inputs from user and returns string output
    '''
    #exception_count=0
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        # speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        say_list=['Say that again please !', "I didn't get you sir",'Can you repeat please',"Pardon me sir, didn't get you","Couldn't find valid results, try again","Try again",
                  "Repeat please",'Sorry !, what did you say',"Didn't understand sir","please try again","Repeat once","I have no records of what you said, sir ! "]
        len_greet = len(say_list)
        rand_index = random.randint(0, len_greet-1)
        print(say_list[rand_index])
        speak(say_list[rand_index])
        #print(exception_count)
        #exception_count=exception_count+1
        # if exception_count==5:
        #     exit()
        return "None"
    return query


def MyIntro(query):
    # about me list
    me_list = ['about me', 'who am i', 'introduce me', 'hum kaun hai', 'ham kaun hain',
               'main kaun hun', 'mere bare mein batao', 'mere bare mein batana']
    if any(word in query for word in me_list):
        speak("You are chaitanya aka ckc 9 7 5 9")
        time.sleep(0.3)
        speak("A 4th year student from Bits Pilani")
        time.sleep(0.3)
        speak("You are the owner of this program")


def JarvisIntro(query):
    # about Jarvis list
    jarvis_list = ['who made you', 'who are you', 'what are you called',
                   'who is jarvis', 'introduce yourself', 'about you', 'tum kaun ho']
    if any(word in query for word in jarvis_list):
        speak("Hello, I am called Jarvis")
        speak("I was created by chaitanya aka ckc 9 7 5 9")
        speak("I am programmed to help you")


def StopJarvis():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Goodbye Sir, Have a nice day !")
        print(f"Goodbye Sir, Have a nice day !")
    elif hour >= 12 and hour < 18:
        speak(f"Goodbye Sir, I hope you have a wonderful day ahead !")
        print(f"Goodbye Sir, I hope you have a wonderful day ahead !")
    else:
        speak(f"Goodbye Sir, I hope you have a great evening !")
        print(f"Goodbye Sir, I hope you have a great evening !")


def Greetings(query):
    if 'hello' in query:
        speak("Hello, how may i help you")

    if 'good morning' in query:
        speak("Good morning sir !!")

    if 'good afternoon' in query:
        speak("Good afternoon sir !!")

    if 'good night' in query:
        speak("Good night sir !!")


def getWikipedia(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results, end="\n\n")
        speak(results)


def funJarvis(query):
    # cuss_list
    cuss_list = ['donkey', 'monkey', 'gadha', 'gadhe', 'pagal', 'bevkuf']
    for words in cuss_list:
        if words in query:
            speak(f"No, I am Jarvis, You are    {words}")
            print(f"No, I am Jarvis, You are {words}")

    # cuss_vowel_list
    cuss_vowel_list = ['idiot']
    for words in cuss_vowel_list:
        if words in query:
            speak(f"No, I am Jarvis, You are an   {words}")
            print(f"No, I am Jarvis, You are an {words}")

def ApplaudJarvis(query):
    # applaud_list
    applaud_list = ['nice', 'good', 'wow', 'great', 'awesome', 'loved it', 'liked it', 'loved', 'liked', 'cool', 'bdhiya', 'mast', 'sexy', 'amazing', 'brilliant',
                    'magical']
    if any(word in query for word in applaud_list) and not 'good night' in query and not 'good morning' in query and not 'good afternoon' in query:
            speak("Thank you sir, anything else you need assistance with ?\n")
            print("Thank you sir, anything else you need assistance with ?\n")

def currTD(query):
    # current time, date.
    time_list = ['what is the time', 'current time',
                 'the time', 'time now', 'present time', 'time']
    if any(word in query for word in time_list) and not 'ctf time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, The time is {strTime}")
        print(f"Sir, The time is {strTime}")

    date_list = ['what is the day', 'current day', 'current date', 'the day','day today'
                 'day now', 'present day', 'present date', 'day', 'date', "today's date"]
    if any(word in query for word in date_list):
        today = date.today()
        strDate = today.strftime('%B %d, %Y')
        speak(f"Sir, The date is {strDate}")
        print(f"Sir, The date is {strDate}")

def youtubeSearch(query):
    if 'youtube search' in query or "search on youtube" in query:
        speak("Okay sir, this is what i found for your search")
        query=query.replace("jarvis","")
        query=query.replace("about","")
        query=query.replace("youtube search","")
        query=query.replace("search on youtube","")
        web="https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)

def googleSearch(query):
    if 'google search' in query or 'search on google' in query:
        speak("Okay sir, this is what i found for your search")
        query=query.replace("jarvis","")
        query=query.replace("about","")
        query=query.replace("google search","")
        query=query.replace("search on google","")
        pywhatkit.search(query)

def music(query):
    speak("Tell me the name of your song !!")
    musicName=takeCommand()
    pywhatkit.playonyt(musicName)
    speak("Starting your song, Enjoy !!")

def whatsapp():
    speak("Tell me the name of person you wish to send messages")
    print("Tell me the name of person you wish to send messages\n")
    name=takeCommand()
    speak("Tell me the message")
    print("Tell me the message\n")
    msg=takeCommand()
    pywhatkit.sendwhatmsg("+91.....",msg)
    # In progress
    # Make a dictionary of favourite contacts with there numbers, use it with fstring to send the message

def screenshot(query):
    if 'screenshot' in query:
        ss=pyautogui.screenshot()
        ss.save("C:\\Users\\Chaitanya K Chauhan\\Dropbox\\My PC (ckc)\\Desktop\\Ckc++\\Screenshots")
        speak("Screenshot saved in Ckc++\Screenshots directory")
        # In progress

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    greetme()
    while flag == 0:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        # if 'jarvis' not in query:
        #     speak("Please try again your query calling me Jarvis")

        # Stop list
        stop_list = ['stop', 'close','terminate', 'nothing', 'rok do', 'ruko', 'band', 'roko',
                     'band kro', 'band', 'bss', 'ruk jao', 'bye', 'tata', 'shut up', 'chup','shut down','shut']
        if any(word in query for word in stop_list):
            StopJarvis()
            flag = 1

        Greetings(query)
        if 'good night' in query:
            flag = 1

        #frivolous
        MyIntro(query) #working
        JarvisIntro(query) #working
        ApplaudJarvis(query) #working
        funJarvis(query) #working
        currTD(query) #working

        # Searches
        youtubeSearch(query)
        getWikipedia(query) #working
        googleSearch(query)

        # Play music
        if "music" in query:
            music()

        # Whatsapp
        #whatsapp()

        # Screenshot
        #screenshot(query)

        #speak("If you want to open a website, please say 'web' first")        
        # open websites using chrome
        chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'

        if 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")
            speak("Opened youtube")
        if 'open google' in query:
            webbrowser.get(chrome_path).open('google.com')
            speak("Opened Google")
        if 'open discord' in query:
            webbrowser.get(chrome_path).open("discord.com")
            speak("Opened discord")
        if 'open ctf time' in query:
            webbrowser.get(chrome_path).open("ctftime.org")
            speak("Opened ctftime")
        if 'open linkedin' in query:
            webbrowser.get(chrome_path).open("linkedin.com")
            speak("Opened linkedin")
        if 'open spotify' in query:
            webbrowser.get(chrome_path).open("spotify.com")
            speak("Opened spotify")
        if 'open github' in query or 'github' in query:
            webbrowser.get(chrome_path).open("github.com")
            speak("Opened github")
        # if flag!=2:
            # speak("Not a recognized command, please try again !!")
            # time.sleep(0.4)

        if 'open code' in query:
            codePath = "C:\\Users\\Chaitanya K Chauhan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Visual code")

        
