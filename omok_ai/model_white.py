import numpy as np
from keras.utils import np_utils
from keras.layers import Dense,Conv2D
from keras import Sequential
from keras.layers import Flatten,Reshape 
import tensorflow as tf
import os
def rotate_up_down(arr):
    temp = [[0] * 15 for _ in range(15)]
 
    # 1. 반복문
    for i in range(15):
        for j in range(15):
            temp[i][j] = arr[i][15-1-j]
    
    # 2. 문자열 슬라이싱
    for i in range(15):
        arr[i] = arr[i][::-1]
    return arr
def rotate_left_right(arr):
    temp = [[0] * 15 for _ in range(15)]
 
    # 1. 반복문
    for i in range(15):
        temp[i] = arr[15-1-i]
    
    # 2. 문자열 슬라이싱
    arr = arr[::-1]
    return arr
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
hallo = tf.constant('why?' )
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
y = []
x = []
file_name = 0
omok_data = ""
turn = True
while os.path.isfile("drive/MyDrive/train/"+str(file_name)+".txt"):
# for file_name in range(0,800):
    # y_test = game_init()
    if(file_name % 10 == 0):
        print(str(file_name))
    
    x_test = game_init()
    x.append(x_test)
    x_test[7][7] = -1
    y.append(x_test)
    x_test = game_init()
    try:
      notepad = open("drive/MyDrive/train/"+str(file_name)+".txt","r")
    except:
      continue
    turn = False
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
        x.append(rotate_90(x_test))
        x.append(rotate_90(rotate_90(x_test)))
        x.append(rotate_90(rotate_90(rotate_90(x_test))))
        x.append(rotate_left_right(x_test))
        x.append(rotate_90(rotate_left_right(x_test)))
        x.append(rotate_90(rotate_90(rotate_left_right(x_test))))
        x.append(rotate_90(rotate_90(rotate_90(rotate_left_right(x_test)))))
        x.append(rotate_up_down(x_test))
        x.append(rotate_90(rotate_up_down(x_test)))
        x.append(rotate_90(rotate_90(rotate_up_down(x_test))))
        x.append(rotate_90(rotate_90(rotate_90(rotate_up_down(x_test)))))
        x.append(rotate_left_right(rotate_up_down(x_test)))
        x.append(rotate_90(rotate_left_right(rotate_up_down(x_test))))
        x.append(rotate_90(rotate_90(rotate_left_right(rotate_up_down(x_test)))))
        x.append(rotate_90(rotate_90(rotate_90(rotate_left_right(rotate_up_down(x_test))))))
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
        y.append(rotate_90(y_test))
        y.append(rotate_90(rotate_90(y_test)))
        y.append(rotate_90(rotate_90(rotate_90(y_test))))
        y.append(rotate_left_right(y_test))
        y.append(rotate_90(rotate_left_right(y_test)))
        y.append(rotate_90(rotate_90(rotate_left_right(y_test))))
        y.append(rotate_90(rotate_90(rotate_90(rotate_left_right(y_test)))))
        y.append(rotate_up_down(y_test))
        y.append(rotate_90(rotate_up_down(y_test)))
        y.append(rotate_90(rotate_90(rotate_up_down(y_test))))
        y.append(rotate_90(rotate_90(rotate_90(rotate_up_down(y_test)))))
        y.append(rotate_left_right(rotate_up_down(y_test)))
        y.append(rotate_90(rotate_left_right(rotate_up_down(y_test))))
        y.append(rotate_90(rotate_90(rotate_left_right(rotate_up_down(y_test)))))
        y.append(rotate_90(rotate_90(rotate_90(rotate_left_right(rotate_up_down(y_test))))))
    notepad.close()
    file_name += 1
print(len(x),len(y))
# print(xt.shape,yt.shape)
# yt = np_utils.to_categorical(yt, 225)
# Y_train = np_utils.to_categorical(yt, 10)
model = Sequential()
model.add(Conv2D(64, kernel_size=5, padding='same', activation='linear',input_shape=(15,15,1)))
model.add(Conv2D(128, kernel_size=5,  padding='same', activation='linear'))
model.add(Conv2D(256, kernel_size=5,  padding='same', activation='relu'))
model.add(Conv2D(128, kernel_size=5,  padding='same', activation='relu'))
model.add(Conv2D(64, kernel_size=5, padding='same', activation='relu'))

model.add(Flatten())
model.add(Dense(225,activation = 'linear'))
model.add(Reshape((15,15)))

model.compile(optimizer='adam',loss='mse')
# print("TEst")
xt = np.array(x)
yt = np.array(y)
model.fit(xt,yt,epochs=5,verbose=1)
print(model.output_shape)
model.save("omok_white.h5")