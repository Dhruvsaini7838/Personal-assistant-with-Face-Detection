import cv2
import numpy as np
from PIL import Image
import os

path ="Samples"

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("D:\\Face_Detection\\Harcassade file\\haarcascade_frontalface_default.xml")

def Image_and_labels(path):

    imagepaths = [os.path.join(path,f) for f in os.listdir(path)]
    facesamples=[]
    ids=[]
    
    for imagePath in imagepaths:

        gray_img =Image.open(imagePath).convert('L')
        img_arr = np.array(gray_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)

        for (x,y,w,h) in faces:
            facesamples.append(img_arr[y:y+h,x:x+w])
            ids.append(id)

    return facesamples,ids

print("Training Faces ... It will take few secondss... ")

faces,ids = Image_and_labels(path)
recognizer.train(faces, np.array(ids))

recognizer.write ("Trainer/trainer.yml")

print("Model Trainedd.... Now we can rcognize your face")

