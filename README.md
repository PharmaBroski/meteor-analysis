# ✨Meteor Detector

This repository contains scripts designed to analyze .mp4 footage and detect meteors. In the current version of the project, the script does not necessarily look for strictly meteors, but movement in general. Future versions of this project can be expected to feature neural networks which scan the footage not for movement but specifically for meteor movement.

## Screenshots

<img width="400" alt="meteor1" src="https://user-images.githubusercontent.com/27097476/34637687-b861b7de-f278-11e7-8f5e-690601abf417.png">

<img width="400" alt="meteor2" src="https://user-images.githubusercontent.com/27097476/34637688-bc017186-f278-11e7-88b4-cf4723e6dfad.png">

<img width="400" alt="meteor3" src="https://user-images.githubusercontent.com/27097476/34637689-bebe669a-f278-11e7-8025-3a2677e7d03b.png">

## Getting Started

If you'd like to this meteor detector on your local machine, you will need a python environment and OpenCV (which is quite difficult to install depending on which OS you are running).

## Running the tests

If you'd like to run this script on a certain video file:

```
python motion_detector.py --video /(directory of your .mp4 vido file)
```

Or if you'd like to run this script live with your webcam (not supported very well):

```
python motion_detector.py
```
## Python Server (server.py)
This is a python socket server which can easily be connected to using Telnet TCP. I wrote this to have easier access to the meteor-detecting camera. As of now, the server can grab the status of the camera, and turn the motion detector on and off. In the future, I plan on being able to grab images from the camera through the server.

## Server Screenshots

<img width="400" alt="meteor3" src="https://i.imgur.com/gUZgOgb.png">

## Built With

* [OpenCV](http://www.dropwizard.io/1.0.2/docs/) - Computer vision library used
* [imutils](https://github.com/jrosebr1/imutils/issues) - Video analysis library to make otherwise repetitive and difficult tasks easier
*[pyimagesearch](https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/) - Used to generate RSS Feeds

## Authors

* **Hashim Ahmed** - *Initial work* - [PharmaBroski](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/PharmaBroski/meteor-analysis/contributors) who participated in this project.

## Acknowledgments

* Huge thanks to pyimagesearch.com and Mr. Adrian Rosebrock for amazing tutorial blog posts on the topic of motion detection in machine vision.
