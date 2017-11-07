# Time-lapse photography
This project aims to allow a DSLR camera without native time-lapse movie support, to take pictures programmatically.


## Update (10/10/2017)
Originally, the project tried to use a servo controller to physically depress the shutter button as a way to control the 
camera.
The code for this strategy exists in servo_control.py, but work going forward now focuses on controlling the camera
using existing command line packages (gphoto2).

# Installation
This project makes a few assumptions that you'll need to meet if you'd like to run this project yourself.
Check the list of hardware at the bottom of this README to make sure you have the required hardware.
This project runs using a first generation Canon 7D digital SLR camera, but other camera models will work if they can be
controlled with gphoto2. You can find a list of compatible cameras [here](http://gphoto.sourceforge.net/doc/remote/).

This project assumes you have a Raspberry Pi that you can connect to as the default user ```pi```.
If you're new to using a Raspberry Pi, you may want to check out the 
[offical setup guide](https://www.raspberrypi.org/documentation/setup/README.md).

Once you're connected to the Raspberry Pi, clone the repository by using the following commands:
```
cd ~
git clone https://github.com/cts-admin/timelapse-dslr.git
```
Change into the new directory you just cloned:
```
cd timelapse-dslr
```


### servo-control (obsolete)
This project used to control a micro servo (sg90) to press a remote shutter release button. 
This enables programmatic time-lapse photography with a DSLR camera. The code for this method still exists in 
servo_control.py but is no longer actively developed.

Hardware Used:

* [USB 2.0 Cable - A-Male to Mini-B](http://amzn.to/2yYhant)
* [Raspberry Pi 2](http://amzn.to/2wiIVpx) (newer version available; [Raspberry Pi 3](http://amzn.to/2w3hO2p))
* [Canon 7D](http://amzn.to/2vfPpZj) (now discontinued; latest equivalent: [7D Mark II](http://amzn.to/2hluSwK))

Used in obsolete version of the project:
* [SG90 Micro Servo](http://amzn.to/2w3q3vs)
* [Remote Shutter Release](http://amzn.to/2w3OPMa)

 
![Servo pushing remote shutter release button](remote_shutter_servo.jpg)

