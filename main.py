import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser
import os

openai.api_key=api_data

completion=openai.Completion()

def Reply(question):
    prompt=f'Bays: {question}\n Jarvis: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Bay'], max_tokens=200)
    answer=response.choices[0].text.strip()
    return answer

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello How Are You? ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Mendengarkan....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Mengenali.....")
        query=r.recognize_google(audio, language='en-in')
        print("Bays Said: {} \n".format(query))
    except Exception as e:
        print("Say That Again....")
        return "None"
    return query


if __name__ == '__main__':
    while True:
        query=takeCommand().lower()
        ans=Reply(query)
        print(ans)
        speak(ans)
        if 'Youtube' in query:
            webbrowser.open("www.youtube.com")
        if 'Google' in query:
            webbrowser.open("www.google.com")
        if 'bye' in query:
            break