### Initiate Virtual Enviroment
python -m virtualenv kivy_venv
``kivy_venv\Scripts\activate`` (windows)
``source kivy_venv/bin/activate`` (linux)

# raspberry:
``
sudo apt-get install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev pkg-config libgl1-mesa-dev libgles2-mesa-dev python-setuptools libgstreamer1.0-dev git-core gstreamer1.0-plugins-{bad,base,good,ugly} gstreamer1.0-{omx,alsa} python-dev libmtdev-dev xclip xsel
``
and
``
sudo apt-get install -y  ffmpeg libavcodec-dev libavdevice-dev libavfilter-dev libavformat-dev libavutil-dev libswscale-dev libswresample-dev libpostproc-dev libsdl2-dev libsdl2-2.0-0 libsdl2-mixer-2.0-0 libsdl2-mixer-dev python3-dev
``
# list mouse devices
less /proc/bus/input/devices | grep mo
udevadm info --export-db | grep tou

set mouse=event0

# install GPM 
sudo apt install gpm
gpm -m /dev/input/mice -t help

# Config touch
egalax = hidinput,/dev/input/event0,rotation=0,invert_y=1,invert_x=1
mtdev_%(name)s = probesysfs,provider=mtdev
hid_%(name)s = probesysfs,provider=hidinput

https://stackoverflow.com/questions/49894375/how-to-use-touchscreen-on-startup-with-kivy