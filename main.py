import os
import wave
import pydub
import random
import pyaudio
import speech_recognition
from time import sleep as wait

from __init__ import *


if __name__ == '__main__':

    while True:        
        task = input("Hear[H]/Record[R]: ").lower()

        if task == 'h':
            cls()
            hear()

        elif task == 'r':
            cls()
            student_name = input("Student name: ").lower()
            record(student_name)