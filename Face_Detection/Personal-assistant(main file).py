from distutils import command
from modulefinder import IMPORT_NAME
from urllib import request
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import sys
import os
from os import name, startfile, system
from pydoc import cli 
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
from geopy.geocoders import Nominatim 
from geopy.distance import great_circle 
import geocoder
import requests
import cv2
import numpy as np
from PIL import Image
import pyautogui as p 



engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
#print("HELLOO")
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dict_apps={"Command prompt":"cmd","paint":"paint","chrome":"chrome","excel":"excel","word":"winword","whatsapp":"whatsApp","notepad":"notepad"}    

def Wishme():
    hour=int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    if hour>=0 and hour<12:
        speak(f"Good Morning  sir , wake up jaaan its {strTime}")
        print(f"Good Morning  sir ,  its {strTime}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon  sir  , wake up  its already  {strTime}")
        print(f"Good Afternoon  sir  , wake up   its already  {strTime}")

    elif hour>=18 and hour<24:
        speak(f"good evening  sir , its {strTime} ")
        print(f" Good evening  sir, its  {strTime}")

    
    speak("  Please tell me how may i help you")    
    print("Please tell me how may i help you")        

def takeCommand():
    # It takes microphone input from the user 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']

    return city, state,country

def open_app(query):
    speak("Launching sir ")
    #if ".com" in query or ".co.in" or ".org" in query:
     #   query=query.replace("open","")
     #   query=query.replace("jarvis","")
      #  query=query.replace("launch","")
       # query = query.replace(" ","")
       # webbrowser.open(f"https://www.{query}")
    apps=list(dict_apps.keys())
    for app in apps:
        if app in query:
            os.system(f"start  {dict_apps[app]}")

def close_app(query):
    speak("Closing sir")
    apps=list(dict_apps.keys())
    for app in apps:
        if app in query:
            os.system(f"taskkill /f /im {dict_apps[app]}.exe")
    

def whatsapp(name,message):
    startfile("C:\\Users\\DHRUV SAINI\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(16)
    click(x=391, y=127)
    sleep(3)
    write(name)
    sleep(1)
    click(x=238, y=308)
    sleep(1)
    click(x=1031, y=977)
    sleep(1)
    write(message)
    press("enter")

def whatsapp_call(name):
    startfile("C:\\Users\\DHRUV SAINI\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(14)
    click(x=401, y=129)
    sleep(2)
    write(name)
    sleep(2)
    click(x=238, y=308)
    sleep(2)
    click(x=1712, y=62)
    press("enter")

def Notepad():
    speak("Tell me the query sir!! ")
    speak("i am ready to write  sir ")
    writes = takeCommand()

    time =(datetime.datetime.now().strftime("%H:%M:%S"))
    filename= str(time).replace(":","-") + ".note.txt"

    with open(filename,"w") as file:
        file.write(writes)
    path_1 ="D:\Face_Detection\\" + str(filename)
    path_2 ="D:\\Face_Detection\\Database\\Notepad_Data\\" + str(filename)
    os.rename(path_1,path_2)
    os.startfile(path_2)

#def YOutubeAuto():

            





#if __name__=="__main__":
def TaskExecution():
    
    speak("verification succesful sir")
    speak("welcome back Dhruv Saini")
    print("Thanks for cooperating with the face recoginition process")
    speak("Thanks for cooperating with the face recoginition process")
    p.press('q')
    cam.release()
    cv2.destroyAllWindows()

    Wishme()
    


    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia... ")
            query = query.replace("wikipedia","")
            query = query.replace("search for","")
            results= wikipedia.summary(query,sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    
        

        elif 'open google' in query:
            speak("Sir, What should i search on google")
            tm = takeCommand().lower()
            webbrowser.open(f"{tm}")
            

        elif 'the time' in query:
            strTime1 = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"SIr ,THe TIme is  {strTime1}") 

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'date' in query:
            speak("No  Sorry for that    as    i am having  headache")

        elif "are you single" in query:
            speak("No  i am having relationship with wifi")    


        
        elif "launch" in query:
            speak("Sir, tell me the name of the website !!")
            web=takeCommand()
            web='https://www.'+web+'.com'
            webbrowser.open(web)

        elif "shut up" in query:
            speak("Thanks for using me sir, have a good day") 
            speak("Good night sir , take care")
            break

        elif "send whatsapp message" in query:
            speak("please tell me name of the person sir:")
            name=takeCommand()
            print(f"Name of the person: {name} ")
            speak("Tell me the message sir:")
            message=takeCommand()
            print(message)
           
            whatsapp(name,message)

        elif "call" in query:
            speak("please tell me the name of the person:")
            name=takeCommand()
            speak(f"Calling  {name} ")
            whatsapp_call(name)  
            

        elif "open" in query:
            open_app(query)
            
        elif "close" in query:
            close_app(query)
            
        elif "increase" in query:
            p.press('volumeup')
            speak("increased sir")

        elif "decrease" in query:
            p.press('volumedown') 
            speak("decreased sir")

        elif "mute" in query:
            p.press("volumemute")
            speak("muted sir")           

               


        elif "online class" in query:
            speak("which class you want to attend sir:")
            print("which class you want to attend sir:")
            online_class_attend=takeCommand()
            if "science" in online_class_attend:
                from LINK import science
                Link = science()
                webbrowser.open(Link)
                sleep(10)
                click(x=630, y=787)
                sleep(1)
                click(x=720, y=792)
                sleep(2)
                click(x=1364, y=565)
                speak("Link joined sir")
                
            elif "maths" in online_class_attend:
                from LINK import maths 
                Link = maths()
                webbrowser.open(Link)
                sleep(10)
                click(x=630, y=787)
                sleep(1)
                click(x=720, y=792)
                sleep(2)
                click(x=1364, y=565)
                speak("Link joined sir")
                
        elif "write" in query:
            Notepad()

        elif "where i am" in query or "current location" in query or "where am i" in query:
            my_location()
            try:
                city, state, country = my_location()
                print(f" Sir your city is {city}")
                print(f" Sir your state is {state}")
                print(f" Sir your country is {country}")
                speak(f"You are currently in {city} city which is in {state} state and country {country}")
            except Exception as e:
                speak("Sorry sir, I coundn't fetch your current location. Please try again")  
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'pause' in query:
            p.press("spacebar")

        elif 'resume' in query:
            p.press("space")
        elif 'full screen' in query:
            p.press("f")
        elif "skip" in query:
            p.press("l")
        elif "back" in query:
            p.press("j")
        elif "next" in query:
            p.press("nexttrack")
        elif "previous" in query:
            with p.hold('shift'):
                p.press("p")

        elif "remember" in query:
            speak("what do you want me to remember sir ")
            remembermsg=takeCommand()
            remembermsg = remembermsg.replace("jarvis","")
            remembermsg = remembermsg.replace("remember","")
            remember = open("data.txt","w")
            remember.write(remembermsg)
            remember.close()
            speak("Ok sir i have saved it in my database ")
        elif "do youq" in query:
            remember = open("data.txt","r")
            speak(f"You tell me that  {remember}")



recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("D:\\Face_Detection\\Trainer\\trainer.yml")
cascadepath ="Harcassade file\haarcascade_frontalface_default.xml"
facecascade = cv2.CascadeClassifier(cascadepath)

font = cv2.FONT_HERSHEY_SIMPLEX

id = 10

names =["","DHRUV SAINI"]

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(3,640)
cam.set(4,600)


minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img =cam.read()
    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiScale(
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW),int(minH)) 
        )
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h) , (0,255,0), 2)
        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])

        if (accuracy <100):
            id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            cv2.putText(img, str(id), (x+5,y-5), font,1,(255,255,255),2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font,1,(255,255,0),1)
            
            
            TaskExecution()

        else:
            id = "unknown"
            accuracy = " {0}%".format(round(100 - accuracy))
            cv2.putText(img, str(id), (x+5,y-5), font,1,(255,255,255),2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font,1,(255,255,0),1)
            
            speak("sorry you are not registered to access me ")
            speak("try again later")
            p.press('q')
            
        cv2.putText(img, str(id), (x+5,y-5), font,1,(255,255,255),2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font,1,(255,255,0),1)

    cv2.imshow('camera',img)
    if cv2.waitKey(2) % 0xff ==ord('q'):
        break


    #if k==27:
      #  break
print("Thanks for using this program ")
cam.release()
cv2.destroyAllWindows()    


                    