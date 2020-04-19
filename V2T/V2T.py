from twilio.rest import Client
from pygame import mixer
import os
import speech_recognition as sr
from gtts import gTTS
import urllib3


def sendMessage(response):
    account_sid = 'Y-O-U-R      T-W-I-L-I-O      I-D'
    auth_token = 'T-W-I-L-I-O       T-O-K-E-N'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=response,
        to=' ' #YOUR WhatsApp number eg(whatsapp:+91789XXXXXXX)
    )

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

mixer.init()
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("\n\n\n\n\n\n\t\t\t\t\t\t\t\t\tSay something!")
    audio = r.listen(source, phrase_time_limit=5)

try:
    
    response = r.recognize_google(audio)
    print(response)
    sendMessage(response)

except sr.UnknownValueError:
    print("Sorry , i am not able to understand your voice")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
