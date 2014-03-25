'''
A camera parameter class that contains the camera matrix, distortion parameters.
It describes the properties of the camera.
'''
import numpy

class CameraParameters:

	def __init__(self, cameraMatrix=numpy.zeros((1,1)), distortionCoeffs=numpy.zeros((1,1)), size=(-1,-1)):

		self.cameraMatrix = cameraMatrix

		self.distortionCoeffs = distortionCoeffs

		self.size = size # the size tuple is (width,height)

	def setParams(self, cameraMatrix, distortionCoeffs, size):

		self.cameraMatrix = cameraMatrix

		self.distortionCoeffs = distortionCoeffs

		self.size = size

	def setCameraMatrix(self,cameraMatrix):

		self.cameraMatrix = cameraMatrix

	def setDistortionCoefficients(self, distortionCoeffs):

		self.distortionCoeffs = distortionCoeffs


	def setSize(self,size):

		self.size = size

	# Check if the camera parameter instance is valid or not
	def isValid(self):

		if(self.cameraMatrix.shape != (3,3) or self.distortionCoeffs.shape[0] < 4 or self.distortionCoeffs.shape[0] > 7 or self.size == (-1,-1) ):
			return False

		return True



