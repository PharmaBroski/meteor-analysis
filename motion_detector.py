## Motion detection & Tracking using Python and OpenCV
#python motion_detector.py --video videos/
# python motion_detector.py --video test-files/rendered.mp4
# Dependencies/Packages

import argparse
import datetime
import imutils
import time
import cv2


framesize = 900;
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="/test-files") #path to video file? I included full path including file. Unsure if this is correct
# Min area is a region in pixels for a region of image to be considered motion
ap.add_argument("-a", "--min-area", type=int, default=framesize/40, help="minimum area size")
args = vars(ap.parse_args())

# if the video argument is None, then we are reading from webcam
# NOTE: This part of the code is unnecessary and should be deleted
if args.get("video", None) is None:
	camera = cv2.VideoCapture(0)
	time.sleep(0.25)

# otherwise, we are reading from a video file
else:
	camera = cv2.VideoCapture(args["video"])

# initialize the first frame in the video stream
firstFrame = None

# loop over the frames of the video
while True:
	# grab the current frame and initialize the occupied/unoccupied
	# text
	(grabbed, frame) = camera.read()
	text = "Not Detected"

	# if the frame could not be grabbed, then we have reached the end
	# of the video
	if not grabbed:
		break

	# resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=framesize)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (7, 7), 0)

	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue

# compute the absolute difference between the current frame and
	# first frame
	frameDelta = cv2.absdiff(firstFrame, gray)

	t=time.time()



	# if text == "Not Detected":
		# firstFrame = gray



	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	thresh2 = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_TOZERO)[1]
	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
	# thresh = cv2.dilate(thresh, None, iterations=2)
	(_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < args["min_area"]:
			continue

		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Detected"

	# draw the text and timestamp on the frame
	cv2.putText(frame, "Motion: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

	# draw fram total
	frameNumber = camera.get(cv2.CAP_PROP_POS_FRAMES)
	if frameNumber%50 == 0:
		savedFrame = frameNumber
		# if(text == "Not Detected"):
		firstFrame = gray
		print("Grayed the frame")


	cv2.putText(frame, "Frame Count: {}".format(frameNumber), (240, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	# show the frame and record if the user presses a key
	cv2.imshow("Feed", frame)
	# cv2.imshow("Thresh", thresh)
	# cv2.imshow("Thresh2", thresh2)
	# cv2.imshow("Frame Delta", frameDelta)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key is pressed, break from the loop
	if key == ord("q"):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
