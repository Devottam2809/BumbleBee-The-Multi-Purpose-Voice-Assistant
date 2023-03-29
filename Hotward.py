#main file for our project
#Hotward Detection
#base to further program

import os
import struct
import pyaudio
import pvporcupine
from pydub import AudioSegment 
from pydub.playback import play


porcupine=None
paud=None
audio_stream=None
 
def start():
    audio=AudioSegment.from_wav("whatsappaudio.wav")
    play(audio)

try:
    porcupine=pvporcupine.create(keywords=["bumblebee"]) 
    paud=pyaudio.PyAudio()
    audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
    while True:
        keyword=audio_stream.read(porcupine.frame_length)
        keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
        keyword_index=porcupine.process(keyword)
        if keyword_index>=0:
            print("hotword detected")
            start()
            #from voiceassistant import*
            
            
finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if paud is not None:
        paud.terminate()

'''
{'computer', 'grasshopper', 'americano', 'grapefruit', 'pico clock', 'picovoice',
 ,, 'bumblebee', 'blueberry'}
'''