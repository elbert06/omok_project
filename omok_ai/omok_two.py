import pygame
import os
import key
import ai
def omok():
    status = False
    file_name = 0
    file_name_2 = 0
    omok_data = ""
    black_position = []
    white_position = []
    m = []
    r = []
    first = True
    turn = False
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
    pygame.init()
    print("Game_element loading...")
    #파이게임의 보여질 배경 및 배경의 좌표 위치 리스트
    character = []
    character_pos = []
    #바둑돌의 기본위치로써, 50x + 35가 x,y좌표이다. (1,1)의 바둑돌의 바둑돌 위치는 (35,35)이다
    x = 7
    y = 7
    #시작을 판단하는 함수. False가 흑이 먼저 시작하는것이다
    #1200*800의 디스플레이 크기
    screen_wid = 1200
    screen_hei = 800
    #스크린 생성
    screen = pygame.display.set_mode((screen_wid,screen_hei))
    #제목 생성
    pygame.display.set_caption("omok")
    #캐릭터 + 배경 추가
    #현재위치 current변수에 저장
    current = os.path.dirname(__file__)
    #백그라운드 생성
    back2 = pygame.image.load(current+"/picture/back2.png")
    character.append(back2)
    character_pos.append([0,0])
    #바둑판 로드
    back = pygame.image.load(current+"/picture/game_board2.png")
    character.append(back)
    character_pos.append([0,0])
    #바둑알 in 바둑판 로드
    black = pygame.image.load(current+"/picture/black.png")
    character.append(black)
    character_pos.append([(screen_wid / 4 * 3),(screen_hei / 3 * 2)])
    # 흰색
    white = pygame.image.load(current+"/picture/white.png")
    character.append(white)
    character_pos.append([(screen_wid / 4 * 3),(screen_hei / 3 * 1)])
    #바둑알 in 배경 로드
    black_sign = pygame.image.load(current+"/picture/last_sign1.png")
    book_x = 50 * 7 + 35
    book_y = 50 * 7 + 35
    white_in = pygame.image.load(current+"/picture/white2.png")
    black_in = pygame.image.load(current+"/picture/black2.png")
    #폰트 지정
    gamefont = pygame.font.SysFont("malgungothic", 30)
    winning = gamefont.render("", True, (0,0,0))
    #차례표시 자막
    running = True
    while running:
        if turn == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if fin == True:
                        running = False
                        from PIL import ImageGrab
                        import time
                        now = time.localtime()
                        img=ImageGrab.grab()
                        saveas="{}{}".format("result",'.png')
                        img.save(saveas)
                    x,y = key.mousetap(event.pos)
                    if x < 15 and y < 15:
                        posibletostep = key.check2(gameboard_list, x, y)
                        if posibletostep == True:
                            current = os.path.dirname(__file__)
                        
                            row = gameboard_list[y]
                            if row[x] == 0:
                                row[x] = -1

                                gameboard_list[y] = row
                            omok_data += str(x)+" "+str(y)+"\n"
                            black_position.append([50 * x +35,50 * y + 35])
                            turn = False
                            m = []
                            fin,winner_row,winner_column = key.check(gameboard_list)
                            turn = False
                            if fin == True and first == True:
                                winning,decide,status = key.who(fin, gameboard_list, winner_row, winner_column, winning)
                                first = False
                elif event.type == pygame.MOUSEMOTION:
                    x,y = key.mousetap(event.pos)
                    if x < 15 and y < 15:
                        book_x = 50 * x +35
                        book_y = 50 * y + 35
            
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
            winning = gamefont.render("loading...", True, (0,0,0))
            screen.blit(winning, ((screen_wid /4*3),(screen_hei / 2)))
            pygame.display.update()
            peo_x,peo_y = ai.analyze_black(gameboard_list,black_position,white_position)                       
            row = gameboard_list[peo_y]
            row[peo_x] = 1
            gameboard_list[peo_y] = row
            omok_data += str(peo_x)+" "+str(peo_y)+"\n"
            m = []
            white_position.append([50 * peo_x +35,50 * peo_y + 35])            
            fin,winner_row,winner_column = key.check(gameboard_list)
            turn = True
            winning = gamefont.render("", True, (0,0,0))
        for sr in range(0,len(character)):
            screen.blit(character[sr],character_pos[sr])
        for sk in range(0,len(black_position)):
            screen.blit(black_in,(black_position[sk][0],black_position[sk][1]))
        for sk in range(0,len(white_position)):
            screen.blit(white_in,(white_position[sk][0],white_position[sk][1]))
        screen.blit(winning, ((screen_wid /4*3),(screen_hei / 2)))
        screen.blit(black_sign, (book_x,book_y))
        pygame.display.update()
        # if(fin == True):
        #     if(status == True):
        #         while True:
        #             if not os.path.isfile("train/"+str(file_name)+".txt"):
        #                 break
        #             else:
        #                 file_name += 1
        #         notepad = open("train/"+str(file_name)+".txt","w")
        #         notepad.write(omok_data)
        #         notepad.close()
        #         # running = False
        #     if(status == False):
        #         while True:
        #             if not os.path.isfile("train2/"+str(file_name_2)+".txt"):
        #                 break
        #             else:
        #                 file_name_2 += 1
        #         notepad = open("train2/"+str(file_name_2)+".txt","w")
        #         notepad.write(omok_data)
        #         notepad.close()
                # running = False
    pygame.quit()
