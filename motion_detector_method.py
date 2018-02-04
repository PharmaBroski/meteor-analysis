def runDetector():
	## Motion detection & Tracking using Python and OpenCV
	#python motion_detector.py --video videos/
	# python motion_detector.py --video test-files/rendered.mp4
	# python motion_detector.py --video ../hiddengithub/test-files/rendered.mp4
	# Dependencies/Packages

	import numpy as np #screenshots
	import pyautogui #screenshots
	import argparse	#terminal commands
	import datetime #timestamp
	import imutils #video funcitons
	import time #time
	import cv2



	framesize = 900
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-v", "--video", help="/test-files") #path to video file? I included full path including file. Unsure if this is correct
	# Min area is a region in pixels for a region of image to be considered motion
	ap.add_argument("-a", "--min-area", type=int, default=framesize/400, help="minimum area size")
	args = vars(ap.parse_args())

	# if the video argument is None, then we are reading from webcam
	# NOTE: This part of the code is unnecessary and should be deleted
	if args.get("video", None) is None:
		camera = cv2.VideoCapture(0)
		time.sleep(0.25)

	# otherwise, we are reading from a video file
	else:
		camera = cv2.VideoCapture(args["video"])



	# loop over the frames of the video
	while True:
		(grabbed, frame) = camera.read()
		cv2.imshow("Feed", frame)
		# if the frame could not be grabbed, then we have reached the end
		# of the video
		if not grabbed:
			break


	# cleanup the camera and close any open windows
	camera.release()
	cv2.destroyAllWindows()
