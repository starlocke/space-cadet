# Space Cadet

Space Cadet's Log. Earthdate 2017-07-20.

I have completed the "intro to space robotics" challenge, taking the route of
controlling an "actuator", in this case, the built-in LED of an Arduino Nano.

## Environment of the Day

- Python 2.7.x
- macOS
- Port 5000 is available

## Hardware of the Day

- Arduino Nano + USB Cable
- Macbook Pro

## Plug and Play

Optionally, prepare a virtual environment and activate it.

Assuming your environment already has Python:

```
pip install -r requirements.txt
```

The Arduino Nano must now be plugged into the USB port.

Launch the Flask web server:

```
./run.sh
```

... and then:

- Browse to http://127.0.0.1:5000/
- Use the "range" (slide) controls to tweak the duration of "off" and "on".

## Inspecting the Code

### led-on-led-off.py

This is the Flask-powered "web service".

### templates/index.html

This is the rudimentary web UI.

### nano/nano.ino

This is the rudimentary "Arduino IDE" sketch.
