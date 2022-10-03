import os
import wave
import pydub
import random
import pyaudio
import speech_recognition
from time import sleep as wait


def hear():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone(0) as source:
        print('Listening...', end='')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print('Processing...')
        query = recognizer.recognize_google(audio, language='en-in')
        
        if query == ('exit' or 'abort'): print('Aborting...'); exit()
        else: print(f'you said: {query}\n')

    except Exception as E:
        print(E)
    
    # return audio