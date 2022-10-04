import os
import wave
import pydub
import random
import pyaudio
import speech_recognition
from time import sleep as wait


def cls():
    os.system('cls')


def hear():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone(0) as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print('Processing audio...')
        query = recognizer.recognize_google(audio, language='en-in')

        if query == ('exit' or 'abort'): print('Aborting...'); exit()
        else: print(f'you said: {query}\n')

    except Exception as E:
        print(E)


def record(file_name: str):
    print('When it says speak, speak for 10 sec.')
    FRAMES_PER_BUFFER = 3200
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    
    print('Speak...')
    
    recoorder = pyaudio.PyAudio()
    
    stream = recoorder.open(
        format=FORMAT,
        frames_per_buffer=FRAMES_PER_BUFFER,
        channels=CHANNELS,
        rate=RATE,
        input=True
    )


    time_in_sec = 10
    frames = []
    
    try:
        for i in range(0, int(RATE/FRAMES_PER_BUFFER * time_in_sec)):
            data = stream.read(FRAMES_PER_BUFFER)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        recoorder.terminate()

        with wave.open(f'Database/Audios/{file_name}.wav', 'wb') as audio_file:
            audio_file.setnchannels(CHANNELS)
            audio_file.setsampwidth(recoorder.get_sample_size(FORMAT))
            audio_file.setframerate(RATE)
            audio_file.writeframes(b"".join(frames))

        print('STATUS: Audio saved')

    except Exception as E: print(f'STATUS: Unable to save the audio\nError: {E}\n\n')
