import numpy

import cv2 as cv

import math

from cameraparameters import CameraParameters

from marker import Marker

from markerdetector import MarkerDetector

##############################
'''
Global Variables
'''
#image capturer
CAMERA_CAPTURE = cv.VideoCapture(0)

#camera matrix
CAMERA_MATRIX = numpy.float64([[6.1906137008775738e+02, 0., 3.2360640534848199e+02], 
								[0.,6.1704791658058059e+02, 2.3643770933395314e+02],
							    [0., 0., 1.] ])

#camera distortion coeffs
DISTORTION_COEFFS = numpy.float64([[-1.9079042931059744e-02], 
								[7.0512921579698037e-03], 
								[4.6213426507682913e-03], 
								[6.2298548406807463e-03], 
								[-4.0376985556252837e-01]])

#camera size
CAM_SIZE = (640,480)

#camera parameter object
MY_CAMERA = CameraParameters(CAMERA_MATRIX, DISTORTION_COEFFS, CAM_SIZE)

# marker size in meters
MARKER_SIZE = 0.171
##############################

# Displays view from the camera with index = "camIndx"
def displayCameraView(camIndx):

	counter = 0

	cap = CAMERA_CAPTURE
	
	while(True):
		
		ret, frame = cap.read()

		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		corners = numpy.zeros((2,2),dtype=numpy.int_)

		corners[0][0] = counter/10
		corners[0][1] = counter/10
		corners[1][0] = abs(100*math.sin(counter/100))
		corners[1][1] = abs(100*math.cos(counter/100))
 
		cv.line(gray,(corners[0][0], corners[0][1]),(corners[1][0],corners[1][1]),(255,0,0),5)

		if frame != None:
			cv.imshow('frame', gray)

		if cv.waitKey(1) & 0xFF == ord('q'):
			break

		counter+=1

	cap.release()
	cv.destroyAllWindows()

# Test the camera parameter class
def testCameraParameters():

	cam = CameraParameters()

	assert cam.isValid() == False

	mat = numpy.zeros((3,3))
	dist = numpy.zeros((1,4))
	size = (101,101)

	cam.setParams(mat,dist,size)

	assert cam.isValid() == True

	print 'Pass, cameraparameters passed basic validation'

# Test the marker class
def testMarker():

	cap = CAMERA_CAPTURE

	while(True):
		
		ret, frame = cap.read()

		corners = numpy.float32([[100,100],
								[200,100],
								[200,200],
								[100,200]])

		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		mm = Marker(corners)

		print "Test 1: Drawing the marker"
		gray = mm.draw(gray)

		print "Test 2: Calculate Extrinsics"
		mm.calculateExtrinsics(MARKER_SIZE, MY_CAMERA)

		print "RVec : " , mm.Rvec, "\n"
		print "Tvec : " , mm.Tvec, "\n"

		if gray != None:
			cv.imshow('frame', gray)

		if cv.waitKey(1) & 0xFF == ord('q'):
			break

	print "Marker passed validation"
	cap.release()
	cv.destroyAllWindows()


# test the marker detector
def testMarkerDetector():

	cap = CAMERA_CAPTURE

	while(True):
		
		ret, frame = cap.read()

		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		detector = MarkerDetector()
		
		thres = detector.detect(gray)

		if thres != None:
			cv.imshow('frame', thres)

		if cv.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv.destroyAllWindows()

if __name__ == '__main__':

	print '--This is a test program to practise opencv in python--'
	
	#print CAMERA_MATRIX, DISTORTION_COEFFS, CAM_SIZE
	#print MY_CAMERA.isValid()
	
	#testCameraParameters()
	#displayCameraView(0)
	#testMarker()
	testMarkerDetector()








