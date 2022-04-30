import os
import speech_recognition as sr






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
        return "none"
    return query

while True:
    Wake_Up=takeCommand().lower()
    if "wake" or "get up"  in Wake_Up:
        os.startfile("D:\\Face_Detection\\PA.py")

    else:
        print("Nothing.....")    

