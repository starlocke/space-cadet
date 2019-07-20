from flask import Flask
from flask import render_template
import random
import serial

app = Flask(__name__)
ser = serial.Serial('/dev/tty.usbserial-A1083GYE', 9600)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set/-<int:val>')
def set_on(val):
    return str(serial_send(-(val)))

@app.route('/set/<int:val>')
def set_off(val):
    return str(serial_send(val))

def serial_send(val):
    if 0 < val and val < 5:
        val = 5
    elif -5 < val and val < 0:
        val = -5
    elif val == 0:
        return 'No-op.'
    try:
        with serial.Serial('/dev/tty.usbserial-A1083GYE', 9600) as ser:
            ser.write(bytes(str(val) + "\n"))
            ser.close()
            return val;
    except:
        return 'Sorry.'
