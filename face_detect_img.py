
import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('test.jpg')
#convert 
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.6, 18)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    print(img.shape)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)
# Display the output
cv2.imshow('output', img)
cv2.waitKey(0)
