import speech_recognition as sr
import smtplib
from gtts import gTTS
import pyglet
import os, time

recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise..')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    tts = gTTS(text="Speak your message", lang='en')
    ttsname=("name.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    print("waiting for your message...")
    recordedaudio=recognizer.listen(source)
    print('Done recording..!')
try:
    print('Printing the message..')
    text=recognizer.recognize_google(recordedaudio,language='en-US')

    print('Your message:{}'.format(text))

except Exception as ex:
    print(ex)

fromaddr = 'enter senders email here'
toaddrs = 'enter recievers email here' 
username= 'enter username here'
password= '**********'
server = smtplib.SMTP('smtp.gmail.com', 587) #to create smtp object
server.ehlo()
server.starttls()
server.login(username, password)  
server.sendmail(fromaddr, toaddrs, text)  
server.quit()

tts = gTTS(text="Message Sent", lang='en')
ttsname=("name.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)
