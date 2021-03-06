import pygame
import os
import time
import random
import data
import string
def move(x_pos,y_pos,move_direction,x,y):
    if move_direction == 1:
        if x - 1 > -1:
            x -= 1
            x_pos -= 50
    elif move_direction == 2:
        if x + 1 < 15:
            x += 1
            x_pos += 50
    elif move_direction == 3:
        if y - 1 > -1:
            y -= 1
            y_pos -= 50
    elif move_direction == 4:
        if y + 1 < 15:
            y += 1
            y_pos += 50
    return x_pos,y_pos,x,y
def print_game(gameboard_listard_list):
    for i in range(0,len(gameboard_listard_list)):
        m = gameboard_listard_list[i]
        for s in range(0,len(m)):
            print(m[s],end=" ")
        print()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def makeboard():
    n = []
    m = []
    for i in range(1,226):
        if i == 0 : pass 
        elif i % 15 == 0 :
            m.append('a')
            n.append(m)
            m = []
        else:
            m.append('a')
    return n
def check(gameboard_list):
    m = []
    ss = 0
    for i in range(len(gameboard_list)):
        for s in gameboard_list[i]:
            m.append(s)
    for h in range(0,len(m)):
        if int((h + 4) / 15) == ss and h+4 < 225:
            if m[h] == m[h+1] and m[h+2] == m[h+3] and m[h+4] == m[h+1] and m[h+1] == m[h+2] and m[h] != 'a':
                return True,int(h / 15),h % 15
        elif (h+4) % 15 == 0 and h+4 < 225:
            if m[h] == m[h+1] and m[h+2] == m[h+3] and m[h+4] == m[h+1] and m[h+1] == m[h+2] and m[h] != 'a':
                return True,int(h / 15),h % 15
        elif h % 15 == 0:
            ss += 1
    for h in range(0,len(m)):
        if h + 60 < len(m):
            if m[h] == m[h+15] and m[h+30] == m[h+45] and m[h+60] == m[h] and m[h+15] == m[h+30] and m[h] != 'a':
                return True,int(h / 15),h % 15
        if h + 64 < len(m):
            if m[h] == m[h+16] and m[h+32] == m[h+48] and m[h+64] == m[h] and m[h+16] == m[h+32] and m[h] != 'a':
                return True,int(h / 15),h % 15
        if h + 56 < len(m):
            if m[h] == m[h+14] and m[h+28] == m[h+42] and m[h+56] == m[h] and m[h+14] == m[h+28] and m[h] != 'a':
                return True,int(h / 15),h % 15
    return False,0,0
def mousetap(mouse_pos):
    main_x = mouse_pos[0]
    main_y = mouse_pos[1]
    main_x -= 35
    main_y -= 35
    floa_x = main_x / 50
    floa_y = main_y / 50
    floa_x += 0.3
    floa_y += 0.3
    int_x = int(floa_x)
    int_y = int(floa_y)
    return int_x,int_y
def step(gameboard_list,black_main,white_main,x,y,decide):
    gamefont = pygame.font.SysFont("malgungothic", 30)
    row = gameboard_list[y]
    if row[x] == 'a':
        current = os.path.dirname(__file__)
        pygame.mixer.init()
        test = pygame.mixer.Sound(current+"/picture/step.wav")
        test.play(0)
        time.sleep(test.get_length())
        test.stop()
        if decide == False:
            black_main.append([(50*x+35),(50*y+35)])
            decide = True
            row[x] = 'o'
            winning = gamefont.render("black turn", True, (0,0,0))
        elif decide == True:    
            white_main.append([(50*x+35),(50*y+35)])
            decide = False
            row[x] = 'x'
            winning = gamefont.render("white turn", True, (0,0,0))
        gameboard_list[y] = row
        print_game(gameboard_list)
    elif decide == False:
        winning = gamefont.render("black turn", True, (0,0,0))
    elif decide == True:
        winning = gamefont.render("white turn", True, (0,0,0))
    return gameboard_list,black_main,white_main,decide,winning   
def div(num):
    gamefont = pygame.font.SysFont("malgungothic", 30)
    real = 3599 - num
    time_min = str(int(real / 60))
    time_sec = str(int(real % 60))
    time = gamefont.render((time_min+"???"+time_sec+"???"), True, (0,0,0))
    return time
def who(decide,gameboard_list,winner_row,winner_column,winning):
    gamefont = pygame.font.SysFont("malgungothic", 30)
    if decide == True:
        win = gameboard_list[winner_row]
        winner = win[winner_column]
        current = os.path.dirname(__file__)
        test = pygame.mixer.Sound(current+"/picture/get.wav")
        test.play(0)
        time.sleep(0.75)
        test.stop()
        if winner == 'o':
            print("?????? ??????")
            winning = gamefont.render("black win", True, (0,0,0))
        else:
            print("?????? ??????")
            winning = gamefont.render("white win", True, (0,0,0))
    else:
        return winning,decide
    return winning,decide
def numberset():
    status = True
    while status == True:
        m = []
        PINNUM = str(random.randint(1,9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))
        USERID = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
        m.append(USERID)
        m.append(PINNUM)
        status = ishere(USERID,PINNUM)
    data.DB_insert(m)
    return USERID,PINNUM
def ishere(userid,PINNUM):
    if userid == '' or PINNUM == '':
        return False,None
    isthere = data.find_wait()
    for isin in isthere:
        if isin.get("PINNUM") == int(PINNUM) and userid != isin.get("USERID"):
            return True,PINNUM
    return False,None
def ishere2(userid,PINNUM):
    if userid == '' or PINNUM == '':
        return False,None
    isthere = data.find_wait()
    for isin in isthere:
        if isin.get("PINNUM") == int(PINNUM) and userid != isin.get("USERID"):
            return True,isin.get("USERID")
    return False,None
def getcenter(things,x,y):
    things_pos = things.get_rect()
    things_pos.centerx = x
    things_pos.centery = y
    return things_pos
def step2(gameboard_list,x,y,turn):
    row = gameboard_list[y]
    if row[x] == 'a':
            if turn == True:
                row[x] = 'o'
            elif turn == False:
                row[x] = 'x'
            gameboard_list[y] = row
            print_game(gameboard_list)
            return gameboard_list,True
    return gameboard_list,False
def check2(gameboard_list,x,y):
    row = gameboard_list[y]
    if row[x] == 'a':
            return True
    return False