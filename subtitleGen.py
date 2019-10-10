from pydub import AudioSegment
from pydub.silence import split_on_silence
import subprocess
import os
import wave
import math
import audioop
import speech_recognition as sr
import pysrt
import six

#This will generate subtitles
#It takes in a file source and a filename

def subtitle_gen(source, filename):
	print("filename: ", filename) 
	print("source: ", source)

	#The file must be outputted to a .wav file
	output = "./users/rossheaney/desktop/output.wav"

	#Now we must extract the audio. To do this we will use
	#ffmpeg. Command for this is "ffmpeg -i " + source +" -c:a aac -b:a 128k output.wav"
	rate=16000
    command = ["ffmpeg", "-y", "-i", source,
               "-ac", str(1), "-ar", str(rate),
               "-loglevel", "error", output]

	#This is a subprocess call to use terminal to execute this command




def main():
	


def speechToText():



