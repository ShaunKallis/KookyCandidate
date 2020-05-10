"""PyAudio Example: Play a wave file (callback version)"""

import pyaudio
import wave
import time
import sys
import random

# if len(sys.argv) < 2:
#     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
#     sys.exit(-1)

sound_effect = ['soundEffects/1.wav', 'soundEffects/2.wav', 'soundEffects/3.wav', 'soundEffects/4.wav', 'soundEffects/5.wav', 'soundEffects/6.wav']

# scare = random.randrange(50)

# if(counter<50):
# 	scare = counter
def playIt():

	wf = wave.open(random.choice(sound_effect), 'rb')
	
	p = pyaudio.PyAudio()
	
	def callback(in_data, frame_count, time_info, status):
	    data = wf.readframes(frame_count)
	    return (data, pyaudio.paContinue)
	
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		            channels=wf.getnchannels(),
		            rate=wf.getframerate(),
		            output=True,
		            stream_callback=callback)
		
	stream.start_stream()

	time.sleep(3)
		
	stream.stop_stream()
	stream.close()
	wf.close()
		
	p.terminate()

# first sound effect will display at the fifth clicks
# the rest per 10 clicks will display a sound effect

if(counter == 5):
	playIt()
if(counter == 15):
	playIt()
if(counter == 25):
	playIt()
if(counter == 35):
	playIt()
if(counter == 45):
	playIt()