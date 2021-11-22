import os
import cv2 as cv
import numpy as np

people = ['Chan', 'joey', 'monica', 'Phoebe','rachel']

# p = []
# for i in os.listdir(r'D:\opencv\faces'):
#     p.append(i)

# print(p)

# other method
DIR = r'D:\opencv\faces'
haar_cascade = cv.CascadeClassifier('haar_face.xml')
features = []
labels = []

def  create_train():
    for person in people: 
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            # we are going to read in that image from this path
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] 
                # crop out the face in the image
                features.append(faces_roi)
                labels.append(label)
                # label variable is the index of this list. 
                # label is given a numerical value is to reduce strain to computer by mapping bw string and numerical label
                # mapping we are goin to do is index of the list

create_train()
print('training done--------')
print(f'length of the features list = {len(features)}')
print (f'length of the labels = {len(labels)}')

features = np.array(features, dtype = 'object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer on the features list and labels list 
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')


np.save('features.npy', features)
np.save('labels.npy', labels)

# we can save this trained model so that we dont need to repeat thus