import numpy 
import cv2 as cv

'''
This class represents an Aruco Marker. It is a matrix of the 4 corners of the marker.
'''

class Marker:

	def __init__(self, corners = numpy.float32((4,2)), markerID = 1):

		self.id = markerID

		self.corners = corners

		self.ssize = markerID

		self.Rvec = numpy.zeros((3,1))

		self.Tvec = numpy.zeros((3,1))

		self.candidateIdx = -1

		self.candidateContour = []


	def isValid(self):

		 if(self.id == -1 or self.corners.shape!=(4,2)):
		 	return False

		 return True

	def draw(self, img, color=(255,0,0), lineWidth=2, writeID = True):

		if (self.isValid() == False):

			print 'The marker is invalid'
			return

		# draw lines joining the four corners
		cv.line(img,(self.corners[0][0],self.corners[0][1]),(self.corners[1][0],self.corners[1][1]),color,lineWidth)
		cv.line(img,(self.corners[1][0],self.corners[1][1]),(self.corners[2][0],self.corners[2][1]),color,lineWidth)
		cv.line(img,(self.corners[2][0],self.corners[2][1]),(self.corners[3][0],self.corners[3][1]),color,lineWidth)
		cv.line(img,(self.corners[3][0],self.corners[3][1]),(self.corners[0][0],self.corners[0][1]),color,lineWidth)

		cv.rectangle(img,(int(self.corners[0][0]-2),int(self.corners[0][1]-2)),(int(self.corners[0][0]+2),int(self.corners[0][1]+2)),(0,255,255),1)
		cv.rectangle(img,(int(self.corners[1][0]-2),int(self.corners[1][1]-2)),(int(self.corners[1][0]+2),int(self.corners[1][1]+2)),(255,0,255),1)
		cv.rectangle(img,(int(self.corners[2][0]-2),int(self.corners[2][1]-2)),(int(self.corners[2][0]+2),int(self.corners[2][1]+2)),(255,255,0),1)

		if(writeID):

			centerx = 0
			centery = 0

			for i in range(0,4):

				centerx += self.corners[i][0]/4
				centery += self.corners[i][1]/4
			
			width = abs(self.corners[1][0]-self.corners[0][0])/2

			cv.putText(img,str(self.id),(int(centerx-width/2),int(centery)),cv.FONT_HERSHEY_SIMPLEX, 1, 255)

		return img


	def calculateExtrinsics(self, markerSize=0,cameraParameters = [],setYPerpendicular=True):

		assert markerSize > 0

		assert cameraParameters.isValid()

		halfSize = markerSize/2

		objPoints = numpy.float32([[-halfSize, -halfSize,0],
								  [-halfSize, halfSize, 0],
								  [halfSize, halfSize,  0],
								  [halfSize, -halfSize, 0]])

		flag, self.Rvec, self.Tvec = cv.solvePnP(objPoints, self.corners, cameraParameters.cameraMatrix, cameraParameters.distortionCoeffs)


'''
	#def getCenter():

	#def getArea():

'''