from flask import Flask,render_template, make_response,request
from flask_bootstrap import Bootstrap
from policies import statements

import pyaudio
import wave
import time
import sys
import random

sound_effect = ['soundEffects/1.wav', 'soundEffects/2.wav', 'soundEffects/3.wav', 'soundEffects/4.wav', 'soundEffects/5.wav', 'soundEffects/6.wav']

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

# create an instance of the Flask class
app = Flask(__name__)
bootstrap = Bootstrap(app)
# route() decorator binds a function to a URL
@app.route("/set")
def setcookie():
    resp = make_response("setting cookie")
    resp.set_cookie('count','0')
    return resp

@app.route('/')
def home():
    count = int(request.cookies.get('count'))
    # if count >5:
    #     time.sleep(10)
    #     playIt()
    background_color = "rgb("  +  str(255-(count*10))+  "," + str(255-(count*10)) + ","+str(255-(count*10))+");"
    text_color = "rgb("  +  str(count*10)+  "," + str(count*10) + ","+str(count*10)+");"
    return render_template('home.html', statements = statements, count = count, background_color = background_color, text_color = text_color)

@app.route('/policy/<id>')
def policy(id):
    count = int(request.cookies.get('count'))
    for x in statements:
        if x["id"] == id:
            cur_policy = x
    # if count >5:
    #     time.sleep(10)
    #     playIt()
    return render_template('policies.html', pol = cur_policy)


