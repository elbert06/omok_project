def who(decide,gameboard_list,winner_row,winner_column):
    if decide == True:
        win = gameboard_list[winner_row]
        winner = win[winner_column]
        current = os.path.dirname(__file__)
        # test = pygame.mixer.Sound(current+"/picture/get.wav"
        # test.play(0)
        # time.sleep(0.75)
        # test.stop()
        if winner == 1:
            print("흑의 승리")
            test = False
        else:
            print("백의 승리")
            test = True
    else:
        return False,test
    return True,test
def test():
    # exec(open("model_black.py", encoding="utf-8" ).read())
    # exec(open("model_white.py", encoding="utf-8" ).read())

    status = False
    file_name = 0
    file_name_2 = 0
    omok_data = ""
    black_position = []
    white_position = []
    m = []
    r = []
    first = True
    turn = True
    fin = False
    # decide는 게임이 끝났는지 확인해주는 bool변수
    decide = False
    #게임보드 생성
    gameboard_list = []
    column = []
    for i in range(1,226):
        if i == 0 : pass 
        elif i % 15 == 0 :
            column.append(0)
            gameboard_list.append(column)
            column = []
        else:
            column.append(0)
    #게임보드 콘솔에 출력
    #파이게임 초기화
    #파이게임의 보여질 배경 및 배경의 좌표 위치 리스트
    #바둑돌의 기본위치로써, 50x + 35가 x,y좌표이다. (1,1)의 바둑돌의 바둑돌 위치는 (35,35)이다
    x = 7
    y = 7
    #시작을 판단하는 함수. False가 흑이 먼저 시작하는것이다
    #1200*800의 디스플레이 크기
    #스크린 생성
    #제목 생성
    #캐릭터 + 배경 추가
    #현재위치 current변수에 저장
    #차례표시 자막
    k = os.listdir("gomocup2020results/Renju")
    g = -1
    for i in k:
        try:
            if(str(i).split("_")[1] == str(g)):
                continue
            else:
                g = int(str(i).split("_")[1])
        except:
            continue
        while True:
            if not os.path.isfile("train2/"+str(file_name_2)+".txt"):
                break
            else:
                file_name_2 += 1
        
        notepad = open("train2/"+str(file_name_2)+".txt","w")
        notepad.write(omok_data)
        notepad.close()
        omok_data = ""
        gameboard_list = []
        column = []
        for m in range(1,226):
            if m == 0 : pass 
            elif m % 15 == 0 :
                column.append(0)
                gameboard_list.append(column)
                column = []
            else:
                column.append(0)
        r = open("gomocup2020results/Renju/"+str(i),"r")
        lines = r.readlines()
        c = len(lines) - 3
        for jl in range(1,c):
            j = lines[jl]
            if turn == True:
                try:
                    x = int(j.split(',')[0])-1
                    y = int(j.split(',')[1])-1
                except:
                    continue
                print(x,y)
                row = gameboard_list[y]
                if row[x] == 0:
                    row[x] = 1
                    gameboard_list[y] = row
                omok_data += str(x)+" "+str(y)+"\n"
                
                black_position.append([50 * x +35,50 * y + 35])
                turn = False
                fin,winner_row,winner_column = key.check(gameboard_list)
                if fin == True and first == True:
                    decide,status = who(fin, gameboard_list, winner_row, winner_column)
                    first = False
                turn = False
                
            else:
                try:
                    peo_x = int(j.split(',')[0])-1
                    peo_y = int(j.split(',')[1])-1
                except:
                    continue    
                print(peo_x,peo_y)              
                row = gameboard_list[peo_y]
                row[peo_x] = -1
                gameboard_list[peo_y] = row
                omok_data += str(peo_x)+" "+str(peo_y)+"\n"
                white_position.append([50 * peo_x +35,50 * peo_y + 35])     
                fin,winner_row,winner_column = key.check(gameboard_list)
                if fin == True and first == True:
                    decide,status = who(fin, gameboard_list, winner_row, winner_column)
                    first = False
                turn = True
            if(decide == True):
                decide = False
                break
                

import os
import key
from ai import *
from random import *
while True:
    try:
        test()
    except:
        test()
