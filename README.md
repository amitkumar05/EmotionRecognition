# EmotionRecognition

There are two approaches for Emotion Recognition –
a)	Hand crafted feature extraction
b)	Using Deep Neural Network



Hand crafted feature extraction followed by SVM classification –

Face detection and cropping – Under landmark_detection->face_detection.py . Using dlib
Landmark_extraction  - Under landmark_detection->face_detection.py . Using dlib
Face Registration – Done using the PHDTool
Feature Extraction – Can use any feature like hog,lbp . File is missing .
Classification – Using SVM . 



Deep Neural network approach –

We tried to mock the approach used in the link below by using the pre-trained model -

https://gist.github.com/GilLevi/54aee1b8b0397721aa4b

Rest files can be found in the folder named deepnet
