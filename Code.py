import speech_recognition as sr
import smtplib
from gtts import gTTS
import pyglet
import os, time

dict={'attherate':'@','underscore':'_','dot':'.','comma':',','hyphen':'-'}
recognizer=sr.Recognizer()
fromaddr = 'senderemail@gmail.com'
password= '**********'
username=fromaddr

#to input recievers email address
with sr.Microphone() as source:
    print('Clearing background noise..')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    RecAdd = gTTS(text='Enter Recievers Address', lang='en')
    filename=("clip.mp3")
    RecAdd.save(filename)
    music = pyglet.media.load(filename, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(filename)
    print('Enter recievers address')
    toaddrs=recognizer.listen(source)
    print("Receiver's  email recorded")
try:
    print('Printing Recievers mail address..')
    text2=recognizer.recognize_google(toaddrs,language='en-US')
    text2 = text2.lower()
    text2=text2.replace(" ","")
    print("Receiver's mail is:{}".format(text2))

except Exception as ex:
    print(ex)    

#to replace words with special characters    
for key, value in dict.items():
    text2 = text2.replace(key, value) 
    toaddrs=text2

#to input email content
with sr.Microphone() as source:
    print('Clearing background noise..')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    tts = gTTS(text="Speak your message", lang='en')
    ttsname=("clip.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    print("Speak your message...")
    recordedaudio=recognizer.listen(source)
    print('Message recorded!')
try:
    print('Printing the message..')
    text=recognizer.recognize_google(recordedaudio,language='en-US')

    print('Your message:{}'.format(text))

except Exception as ex:
    print(ex)

#to output email content    
message = gTTS(text='Your Message is', lang='en')
filename=("clip.mp3")
message.save(filename)
music = pyglet.media.load(filename, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(filename)

message = gTTS(text=text, lang='en')
filename=("clip.mp3")
message.save(filename)
music = pyglet.media.load(filename, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(filename)

#to ask for confirmation
message = gTTS(text='Do you want to send this message?', lang='en')
filename=("clip.mp3")
message.save(filename)
music = pyglet.media.load(filename, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(filename)


print("Do you want to send this message?")
with sr.Microphone() as source:
    print('Clearing background noise..')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for confirmation")
    recordedaudio=recognizer.listen(source)
    print('Response Recorded!')
try:
    print('Printing the response..') 
    response=recognizer.recognize_google(recordedaudio,language='en-US')

    print('Your Response:{}'.format(response))
except Exception as ex:
    print(ex)
    

#to send the email
server = smtplib.SMTP('smtp.gmail.com', 587) #to create smtp object
server.ehlo()
server.starttls()
server.login(username, password)  

if(response=='yes'or response=='YES'):
    server.sendmail(fromaddr, toaddrs, text)  
    server.quit()
    tts = gTTS(text="Message Sent", lang='en')
    ttsname=("name.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print('Message Sent')
    
else:
    tts = gTTS(text="Message Not Sent", lang='en')
    ttsname=("name.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print('Message Not Sent')  
    
