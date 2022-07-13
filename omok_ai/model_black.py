import numpy as np
from keras.utils import np_utils
from keras.layers import Dense,Conv2D,Reshape
from keras import Sequential
from keras.layers import Flatten 
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
hallo = tf.constant('why?' )
print(hallo)
def game_init():
    return [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
x = []
y = []
file_name = 0
omok_data = ""
turn = True
for file_name in range(1,4501):
    # y_test = game_init()
    if(file_name % 10 == 0):
        print(str(file_name))
    x_test = game_init()
    x.append(x_test)
    x_test[7][7] = 1
    y.append(x_test)
    x_test = game_init()
    try:
      notepad = open("train2/"+str(file_name)+".txt","r")
    except:
      continue
    turn = True
    line = notepad.readlines()
    for k in range(0,len(line)-1):
        i = line[k]
        x_zapo,y_zapo = i.replace("\n","").split(" ")
        x_zapo = int(x_zapo)
        y_zapo = int(y_zapo)
        if(turn == True):
            x_test[y_zapo][x_zapo] = 1
            turn =False
        else:
            x_test[y_zapo][x_zapo] = -1
            turn =True  
        x.append(x_test)
        i = line[k+1]
        x_zapo,y_zapo = i.replace("\n","").split(" ")
        x_zapo = int(x_zapo)
        y_zapo = int(y_zapo)
        y_test = x_test
        if(turn == True):
            y_test[y_zapo][x_zapo] = 1
        else:
            y_test[y_zapo][x_zapo] = -1
        y.append(y_test)             
    notepad.close()
    file_name += 1
print(len(x),len(y))
# print(xt.shape,yt.shape)
# yt = np_utils.to_categorical(yt, 225)
# Y_train = np_utils.to_categorical(yt, 10)
model = Sequential()
model.add(Conv2D(64, kernel_size=7, padding='same', activation='relu',input_shape=(15,15,1)))
model.add(Conv2D(128, kernel_size=7,  padding='same', activation='relu'))
model.add(Conv2D(256, kernel_size=7,  padding='same', activation='relu'))
model.add(Conv2D(128, kernel_size=7,  padding='same', activation='relu'))
model.add(Conv2D(64, kernel_size=7, padding='same', activation='relu'))

model.add(Flatten())
model.add(Dense(225,activation = 'softmax'))
model.add(Reshape((15,15)))

model.compile(optimizer='adam',loss='mse')
# print("TEst")
xt = np.array(x)
yt = np.array(y)
model.fit(xt,yt,epochs=1,verbose=1)
print(model.output_shape)
model.save("omok_black.h5")