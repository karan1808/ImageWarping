#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 23:26:18 2019

@author: abhishekkaranath
"""

import numpy as np
import cv2
import math
from threading import Thread
import datetime
#from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils #contains the classes mentioned below

#class FPS:
#	def __init__(self):
#		# store the start time, end time, and total number of frames
#		# that were examined between the start and end intervals
#		self._start = None
#		self._end = None
#		self._numFrames = 0
# 
#	def start(self):
#		# start the timer
#		self._start = datetime.datetime.now()
#		return self
# 
#	def stop(self):
#		# stop the timer
#		self._end = datetime.datetime.now()
# 
#	def update(self):
#		# increment the total number of frames examined during the
#		# start and end intervals
#		self._numFrames += 1
# 
#	def elapsed(self):
#		# return the total number of seconds between the start and
#		# end interval
#		return (self._end - self._start).total_seconds()
# 
#	def fps(self):
#		# compute the (approximate) frames per second
#		return self._numFrames / self.elapsed()
    
 
#class WebcamVideoStream:
#	def __init__(self, src=0):
#		# initialize the video camera stream and read the first frame
#		# from the stream
#		self.stream = cv2.VideoCapture(src)
#		(self.grabbed, self.frame) = self.stream.read()
# 
#		# initialize the variable used to indicate if the thread should
#		# be stopped
#		self.stopped = False
#	def start(self):
#		# start the thread to read frames from the video stream
#		Thread(target=self.update, args=()).start()
#		return self
# 
#	def update(self):
#		# keep looping infinitely until the thread is stopped
#		while True:
#			# if the thread indicator variable is set, stop the thread
#			if self.stopped:
#				return
# 
#			# otherwise, read the next frame from the stream
#			(self.grabbed, self.frame) = self.stream.read()
# 
#	def read(self):
#		# return the frame most recently read
#		return self.frame
# 
#	def stop(self):
#		# indicate that the thread should be stopped
#		self.stopped = True
        
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())


# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from webcam...")
vs = WebcamVideoStream(src=0).start() # this stream is used to continuously read frames from webcam. 
fps = FPS().start()
 
# loop over some frames...this time using the threaded stream
#while fps._numFrames < args["num_frames"]:
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    
    rows, cols, columns = frame.shape
    img_output = np.zeros(frame.shape, dtype=frame.dtype)
    
# below loop warps the current frame by superimposing a sinusoidal function
    for i in range(rows):
        for j in range(cols):
            offset_x = int(20.0 * math.sin(2 * 3.14 * i / 150))
            offset_y = int(20.0 * math.cos(2 * 3.14 * j / 150))
            if i+offset_y < rows and j+offset_x < cols:
                img_output[i,j] = frame[(i+offset_y)%rows,(j+offset_x)%cols]
            else:
                img_output[i,j] = 0
 
	# check to see if the frame should be displayed to our screen
	#if args["display"] > 0:
    img_output1 = imutils.resize(img_output, width=1000)
    cv2.imshow("Frame", img_output1)
    key = cv2.waitKey(1) & 0xFF
 
	# update the FPS counter
    fps.update()
 
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()