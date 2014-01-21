Copyright 2014 Saurav Agarwal, Texas A&M University. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THIS SOFTWARE IS PROVIDED BY Saurav Agarwal ''AS IS'' AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Rafael Muñoz Salinas OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the
authors and should not be interpreted as representing official policies, either expressed
or implied, of Rafael Muñoz Salinas.

 
 
 \mainpage PyArUco: Augmented Reality library


PyArUco is a python port of the ArUco minimal C++ library for detection of Augmented Reality markers based on OpenCv exclusively.
The original C++ version was developed by Rafael Muñoz Salinas. 

It is an educational effort to practise python programming and gain experience in porting code from C++ to python.


\section INTRODUCTION INTRODUCTION

The library relies on the use of coded markers. Each marker has an unique code indicated by the black and white colors in it. The libary detect borders, and analyzes into the rectangular regions which of them are likely to be markers. Then, a decoding is performed and if the code is valid, it is considered that the rectangle is a marker.

The codification included into the marker is a slighly modified version of the Hamming Code. It has a total a 25 bits didived in 5 rows of 5 bits each. So, we have 5 words of 5 bits. Each word, contains only 2 bits of real information, the rest is for  and error detection/correction (error correction is yet to be done). As a conclusion, a marker contains 10 bits of real information wich allows 1024 different markers.


\section BOARDS BOARDS

Aruco allows the possibility to employ board. Boards are markers composed by an array of markers arranged in a known order. The advantages of using boards instead of simple markers are:
 - More robusteness. The misdetection of several markers of the board is not a problem as long as a minimum set of them are detected.
 - More precision. Since there are a larger number of corners, camera pose estimation becomes more precise.


\section APPLICATIONS APPLICATIONS

The library comes with five applications that will help you to learn how to use the library:
 - aruco_create_marker: which creates marker and saves it in a jpg file you can print.
 - aruco_simple : simple test aplication that detects the markers in a image 
 - aruco_test: this is the main application for detection. It reads images either from the camera of from a video and detect markers. Additionally, if you provide the intrinsics of the camera(obtained by OpenCv calibration) and the size of the marker in meters, the library calculates the marker intrinsics so that you can easily create your AR applications.
 - aruco_test_gl: shows how to use the library AR applications using OpenGL for rendering
 - aruco_create_board: application that helps you to create a board
 - aruco_simple_board: simple test aplication that detects a board of markers in a image 
 - aruco_test_board: application that detects boards
 - aruco_test_board_gl: application that detects boards and uses OpenGL to draw

\section LIBRARY LIBRARY DESCRIPTION:

The ArUco library contents are divided in two main directories. The src directory, which contains the library itself. And the utils directory which contains the applications.

The library main classes are: 
   - aruco::CameraParameters: represent the information of the camera that captures the images. Here you must set the calibration info.
   - aruco::Marker: which represent a marker detected in the image
   - aruco::MarkerDetector: that is in charge of deteting the markers in a image Detection is done by simple calling the member funcion ArMarkerDetector::detect(). Additionally, the classes contain members to create the required matrices for rendering using OpenGL. See aruco_test_gl for details
   - aruco::BoardConfiguration: A board is an array of markers in a known order. BoardConfiguracion is the class that defines a board by indicating the id of its markers. In addition, it has informacion about the distance between the markers so that extrinsica camera computations can be done.
   - aruco::Board: This class defines a board detected in a image. The board has the extrinsic camera parameters as public atributes. In addition, it has a method that allows obtain the matrix for getting its position in OpenGL (see aruco_test_board_gl for details).
   - aruco::BoardDetector : This is the class in charge of detecting a board in a image. You must pass to it the set of markers detected by ArMarkerDetector and the BoardConfiguracion of the board you want to detect. This class will do the rest for you, even calculating the camera extrinsics.

 
\section Testing 

For testing the applications, the library provides videos and the corresponding camera parameters of these videos. Into the directories you will find information on how to run the examples.
 
\section Final Notes

 - REQUIREMENTS: OpenCv >= 2.1.0. and OpenGL for (aruco_test_gl and aruco_test_board_gl)
 - CONTACT: Rafael Munoz-Salinas: rmsalinas@uco.es
 - This libary is free software and come with no guaratee!
