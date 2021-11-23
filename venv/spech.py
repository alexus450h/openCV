import speech_recognition as sr
import pyttsx3
import os
def saying(command):
    engine=pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()
voc={'greetings':['Hello','Hi','Good morning'],
         'yelling':['Shut up','Zip it']
         }
def word_typ():
    global text
    r=sr.Recognizer()
    text='SMTH wrong'
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2=r.listen(source2)
            text=r.recognize_google(audio2)
            text=text.lower()
            saying(text)
            return text
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")
    return text
fl=True
print('>>>>')
while fl:

    word_typ()
    if text=='hello':
        fl=False
    elif text=='open':
        print('Opening program')
print('Finished')