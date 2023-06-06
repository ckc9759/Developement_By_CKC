import pyttsx3
import datetime
import time
import winsound
import speech_recognition as sr
import wikipedia
import webbrowser
import os


flag=0

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices)
#print(voices[1].id)

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
        speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")

    speak("I am Jarvis")
    time.sleep(0.3)
    # speak("Loading records")
    # #beep sound
    # freq=1500
    # duration=1500  #milliseconds
    # winsound.Beep(freq,duration)
    #time.sleep(0.3)
    #speak("We are online and ready !!")
    time.sleep(0.3)
    speak("How may i help you sir !!")


def takeCommand():
    '''
    To take microphone inputs from user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        #speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        speak("Say that again please....\n")
        flag=2
        return "None"
    return query


if __name__ == "__main__":
    greetme()
    while flag==0:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        # if 'jarvis' not in query:
        #     speak("Please try again your query calling me Jarvis")
        
        if 'hello' in query:
            speak("Hello, how may i help you")
        
        # cuss_list
        cuss_list=['donkey','monkey','gadha','gadhe','pagal','bevkuf']
        for words in cuss_list:
            if words in query:
                speak(f"No, I am Jarvis, You are    {words}")
                print(f"No, I am Jarvis, You are {words}")

        # cuss_vowel_list
        cuss_vowel_list=['idiot']
        for words in cuss_vowel_list:
            if words in query:
                speak(f"No, I am Jarvis, You are an   {words}")
                print(f"No, I am Jarvis, You are an {words}")

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results,end="\n\n")
            speak(results)

        # Stop list
        stop_list=['stop','terminate','nothing','rok do','roko','band kro','band','bss','ruk jao','bye','tata','shut up','chup']
        if any(word in query for word in stop_list):
            speak("Goodbye Sir, Have a nice day !")
            print("Goodbye Sir, Have a nice day !")
            flag=1

        # about me list
        me_list=['about me','who am i','introduce me','hum kaun hai','ham kaun hain','main kaun hun','mere bare mein batao','mere bare mein batana']    
        if any(word in query for word in me_list):
            speak("You are chaitanya aka ckc 9 7 5 9")
            time.sleep(0.3)
            speak("A 4th year student from Bits Pilani")
            time.sleep(0.3)
            speak("You are the owner of this program")

        # about Jarvis list
        jarvis_list=['who made you','who are you','what are you called','who is jarvis','introduce yourself','about you','tum kaun ho']
        if any(word in query for word in jarvis_list):
            speak("Hello, I am called Jarvis")
            speak("I was created by chaitanya aka ckc 9 7 5 9")
            speak("I am programmed to help you")

        # current time, date.
        time_list=['what is the time','current time','the time','time now','present time']
        if any(word in query for word in time_list):
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is{strTime}")

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
            webbrowser.get(chrome_path).open("ctftime.com")
            speak("Opened ctftime")
        if 'open linkedin' in query:
            webbrowser.get(chrome_path).open("linkedin.com")
            speak("Opened linkedin")
        if 'open spotify' in query:
            webbrowser.get(chrome_path).open("spotify.com")
            speak("Opened spotify")
        if 'open github' in query:
            webbrowser.get(chrome_path).open("github.com")
            speak("Opened github")
        # if flag!=2:
            # speak("Not a recognized command, please try again !!")
            # time.sleep(0.4)

        if 'open code' in query:
            codePath="C:\\Users\\Chaitanya K Chauhan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Visual code")
