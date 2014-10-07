import numpy 
import math
import cv2 as cv
from marker import Marker

    
'''
Detects markers in the input image.
'''
class MarkerDetector:

	def __init__(self):

		#self.doErosion = False

		#self.enableCylinderWarp = False

		#self.threshMethod = cv.ADPT_THRES

		self.threshParam1 = 7

		self.threshParam2 = 7

		self.minSize = 0.04

		self.maxSize = 0.5

		self.speed = 0

		self.markerWarpSize = 56

		self.candidates = []

		self.pydrdown_level = 0

		self.gray = []

		self.thres = []

		self.thres2 = []

		self.reduced = []


	def detect(self, inputImg, cameraParameters=[], markerSize=-1, setYPerpendicular=True):

		#if(inputImg.type() == cv.CV_8UC3):
		
		#self.gray = cv.cvtColor(inputImg, cv.COLOR_BGR2GRAY)
		#else:
		self.gray = inputImg

		detectedMarkers = []

		imgToBeThresholded = self.gray

		ThresParam1 = self.threshParam1

		ThresParam2 = self.threshParam2

		if(self.pydrdown_level != 0 ):

			self.reduced = gray

			for i in range(0,self.pydrdown_level):

				self.reduced = cv.pyrDown(self.reduced)

			red_den = 2**self.pydrdown_level

			imgToBeThresholded = self.reduced

			ThresParam1 = ThresParam1 / red_den

			ThresParam2 = ThresParam2 / red_den

		self.thres = self.threshold(imgToBeThresholded, ThresParam1, ThresParam2)

		# By default, erosion is disabled in C++ version, so we don't implement it

		markerCandidates = self.detectRectangles(self.thres)

		return self.thres




	'''
	In the originall C++ library, there are 3 thresholding methods to choose from, However only
	adaptive/canny is provided here because it performs the best.
	'''
	def threshold(self, gray, param1, param2):

		if param1 == -1:
			param1 = self.ThresParam1

		if param2 == -1:
			param2 = self.ThresParam2

		if param1 < 3:
			param1 = 3

		elif param1%2 != 1:
			param1 = param1+1

		#thresholdedImage = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,param1,param2)
		thresholdedImage = cv.Canny(gray,10,220)

		return thresholdedImage

		
	
	def detectRectangles(self, thresImg):

		markerCandidates = []

		minSize = self.minSize*max(thresImg.shape)*4
		maxSize = self.maxSize*max(thresImg.shape)*4

		self.thres2 = thresImg

		contours2, hierarchy2 = cv.findContours(self.thres2, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

		counterIndx = 0

		for contour in contours2:

			if(minSize < contour.shape[0] and contour.shape[0] < maxSize):

				approxCurve = cv.approxPolyDP(contour, contour.shape[0]*0.05, True)

				approxCurve = numpy.vstack(approxCurve)

				if approxCurve.shape[0] == 4:

					if cv.isContourConvex(approxCurve):

						minDist = 1e10

						for j in range(0,4):

							d = math.sqrt( (approxCurve[j][0]-approxCurve[(j+1)%4][0])**2 + (approxCurve[j][1]-approxCurve[(j+1)%4][1])**2 )

							if d < minDist:
								minDist = d

						if minDist > 10:

							m = Marker(approxCurve)
							m.candidateIdx = counterIndx
							markerCandidates.append(m)
			counterIndx += 1

		#arrange in anti-clockiwise
		swapped = []
		for i in range(0,len(markerCandidates)):

			dx1 = markerCandidates[i].corners[1][0] - markerCandidates[i].corners[0][0]
			dy1 = markerCandidates[i].corners[1][1] - markerCandidates[i].corners[0][1]
			dx2 = markerCandidates[i].corners[2][0] - markerCandidates[i].corners[0][0]
			dy2 = markerCandidates[i].corners[2][1] - markerCandidates[i].corners[0][1]

			o = ( dx1*dy2 )- ( dy1*dx2 )

			if(o < 0.0):

				markerCandidates[i].corners[1], markerCandidates[i].corners[3] = markerCandidates[i].corners[3], markerCandidates[i].corners[1]			
				swapped.append(True)
			else:
				swapped.append(False)

		#remove those elements whose corners are too close to each other

		return markerCandidates

	#def refineCandidateLines():

