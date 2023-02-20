import OPC_analysis as OPC
from nifty_50_Real_Time_price import get_current_N50
from OI_visulization import OPC_OI_data_visulize
import pyttsx3
import datetime
import speech_recognition as sr
import os

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = datetime.datetime.now().day
    month = datetime.datetime.now().strftime("%B")
    year = datetime.datetime.now().year
    speak(f"the current date is {day} {month} {year}")
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("SHADOW at your service sir, please tell me how may I help you.")
    print("SHADOW at your service sir, please tell me how may I help you.")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm SHADOW created by Mr. Parth ")
            print("I'm SHADOW created by Mr. Parth ")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "option chain" and "grow" in query:
            print(OPC.show_OPC_GROWW())
            speak("sir the data is on your screen")
        
        elif "option chain" and "icici direct" in query:
            print(OPC.show_OPC_ICICD())
            speak("sir the data is on your screen")

        elif "Nifty" and "price" in query:
            data = get_current_N50()
            speak(f"nifty fifty trade at {data[0]} with hike of {data[1]} which is {data[2]} percent higher then yesterday's closing")
            print(f'''NIFTY 50\n{data[0]}\n{data[1]} ({data[2]}%) ''')
            speak("you can see data on your screen")

        elif "PCR" and "ratio" in query:
            data = OPC.get_pcr()
            speak(f"PCR ratio is {data}")
            print("PCR ratio : ",data)
            speak("you can see data on your screen")
            
        elif "open interest" and "graph" in query:
            OPC_OI_data_visulize()

        elif 'exit' in query or 'stop' in query:
            hour = datetime.datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()


# ibm watson api
# rasa 
# aws serverless bot framework
