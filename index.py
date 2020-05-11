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
    # function that uses pyaudio plays audio when called

	wf = wave.open(random.choice(sound_effect), 'rb')
	
	p = pyaudio.PyAudio()
	time.sleep(5)

	def callback(in_data, frame_count, time_info, status):
	    data = wf.readframes(frame_count)
	    return (data, pyaudio.paContinue)

    # opens audio clip 
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		            channels=wf.getnchannels(),
		            rate=wf.getframerate(),
		            output=True,
		            stream_callback=callback)
		
	stream.start_stream()

    # time for which the audio plays
	time.sleep(4)
		
	stream.stop_stream()
	stream.close()
	wf.close()
		
	p.terminate()

# create an instance of the Flask class
app = Flask(__name__)
bootstrap = Bootstrap(app)

# set route
@app.route("/set")
def setcookie():
    resp = make_response("setting cookie")
    resp.set_cookie('count','0')
    return resp

# home route
@app.route('/')
def home():
    count = int(request.cookies.get('count'))
    if count >10:
        playIt()

    background_color = "rgb("  +  str(235-(count*20))+  "," + str(235-(count*20)) + ","+str(255-(count*20))+");"
    text_color = "rgb("  +  str(count*30)+  "," + str(count*20) + ","+str(count*20)+");"
    if count < 3:
        jumbo_color = "rgba(150,150,150,.7);"
    elif 3<=count<5:
        jumbo_color = "rgba(187,10,30,.1);"
    elif 5<=count<10:
        jumbo_color = "rgba(187,10,30,.3);"
    elif 10<=count<15:
        jumbo_color = "rgba(187,10,30,.5);"
    else:
        jumbo_color = "rgb(187,10,30);"
    return render_template('home.html', statements = statements, count = count, background_color = background_color, text_color = text_color, jumbo_color=jumbo_color)

# policy route
@app.route('/policy/<id>')
def policy(id):
    """navigates to to policy wih the id passed"""
    count = int(request.cookies.get('count'))
    for x in statements:
        if x["id"] == id:
            cur_policy = x
    if count >10:
        playIt()
    return render_template('policies.html', pol = cur_policy, count=count)


