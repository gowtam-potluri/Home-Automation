#!/usr/bin/python3
from flask
import Flask, request, send_from_directory
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
17
gpio.output(12, gpio.HIGH)
gpio.output(12, gpio.LOW)
app = Flask(__name__)
global lampstate
lampstate = False
@app.route('/lamp/<state>', methods = ['GET'])
def result(state = None):
 global lampstate
if state == "on":
 print("Lamp Turned On")
lampstate = True
gpio.output(12, gpio.HIGH)
elif state == "off":
 print("Lamp Turned Off")
lampstate = False
gpio.output(12, gpio.LOW)
elif state == "get":
 print(lampstate)
else :
 lampstate = not lampstate
if lampstate:
 gpio.output(12, gpio.HIGH)
else :
 gpio.output(12, gpio.LOW)
return str(lampstate)
@app.route('/<path:path>')
def send_js(path):

 return send_from_directory('web', path)
if __name__ == "__main__":
 
hosts.
 app.run(debug = False, use_reloader = True, host = '0.0.0.0', port = 80)
