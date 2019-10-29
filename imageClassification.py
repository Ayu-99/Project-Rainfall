import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation,Flatten, Conv2D, MaxPooling2D





DATADIR="/home/ayushi/Pictures/potholes/pothole_image_data"
CATEGORIES=["with", "without"] # 0-with 1-without



training_data=[]
IMG_SIZE = 280


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)  # path to with or without
        class_num=CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                # plt.imshow(img_array, cmap="gray")
                # plt.show()
                # print(img_array.shape)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                # plt.imshow(new_array, cmap='gray')
                # plt.show()
                training_data.append([new_array, class_num])

            except Exception as e:
                pass

create_training_data()
random.shuffle(training_data)

# print(len(training_data))

# for sample in training_data[:10]:
#     print(sample[1])


X=[] #feature set
y=[] #labels

for features, labels in training_data:
    X.append(features)
    y.append(labels)

X=np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

pickle_out=open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out=open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

pickle_in=open("X.pickle", "rb")
X=pickle.load(pickle_in)
# print(X[1])

X =pickle.load(open("X.pickle", "rb"))
y =pickle.load(open("y.pickle", "rb"))

X=X/255.0
model=Sequential()
model.add(Conv2D(64, (3,3), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss="binary_crossentropy",
              optimizer="adam",
              metrics=['accuracy'])

model.fit(X,y, batch_size=32, validation_split=0.1)

