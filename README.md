# Face-Detection-Using-Open-CV
This is a simple demonstration of face detection using the OpenCV library in python (in a few lines of code). Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.. We will be using the face classifier. 


We need to download the trained classifier XML file (haarcascade_frontalface_default.xml), which is available in OpenCv’s GitHub repository. It should be saved to the working location/directory/path.

The detection works only on grayscale images. So it is important to convert the color image to grayscale. 

"detectMultiScale" function (line 10) is used to detect the faces. It takes 3 arguments — the input image, scaleFactor and minNeighbours. scaleFactor specifies how much the image size is reduced with each scale. minNeighbours specifies how many neighbors each candidate rectangle should have to retain it.


Similarly, we can detect faces in videos. As videos are basically made up of frames, which are still images.

The only difference here is that we use an infinite loop to loop through each frame in the video. We use cap.read() to read each frame. The first value returned is a flag that indicates if the frame was read correctly or not. We don’t need it. The second value returned is the still frame on which we will be performing the detection.

<img align = centre height = 500 width = 500   src = https://github.com/sarthakkmishraa/Face-Detection-Using-Open-CV/blob/master/Output.PNG>
