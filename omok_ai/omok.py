import pygame
import os
import key
import time
def omok():
    status = False
    file_name = 0
    file_name_2 = 0
    omok_data = ""
    # decide는 게임이 끝났는지 확인해주는 bool변수
    decide = False
    #게임보드 생성
    gameboard_list = key.makeboard()
    #게임보드 콘솔에 출력
    key.print_game(gameboard_list)
    #파이게임 초기화
    pygame.init()
    pygame.mixer.init()
    #파이게임의 보여질 배경 및 배경의 좌표 위치 리스트
    character = []
    character_pos = []
    #바둑돌의 기본위치로써, 50x + 35가 x,y좌표이다. (1,1)의 바둑돌의 바둑돌 위치는 (35,35)이다
    x = 7
    y = 7
    #시작을 판단하는 함수. False가 흑이 먼저 시작하는것이다
    turn = False
    #흑,백의 총 시간을 체크하는 변수(초단위)
    black_second,white_second = 0,0
    #한 턴동안 올라가는 시간을 체크하기 위한 변수
    turn_last = 0
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
    white_sign = pygame.image.load(current+"/picture/last_sign2.png")
    book_x = 50 * 7 + 35
    book_y = 50 * 7 + 35
    black_pos,white_pos = [],[]
    white_in = pygame.image.load(current+"/picture/white2.png")
    black_in = pygame.image.load(current+"/picture/black2.png")
    #폰트 지정
    gamefont = pygame.font.SysFont("malgungothic", 30)
    #차례표시 자막
    winning = gamefont.render("black turn", True, (0,0,0))
    #x,y = 50x + 35
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    book_x,book_y,x,y = key.move(book_x, book_y, 1, x, y)
                elif event.key == pygame.K_RIGHT:
                    book_x,book_y,x,y = key.move(book_x, book_y, 2, x, y)
                elif event.key == pygame.K_UP:
                    book_x,book_y,x,y = key.move(book_x, book_y, 3, x, y)
                elif event.key == pygame.K_DOWN:
                    book_x,book_y,x,y = key.move(book_x, book_y, 4, x, y)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if decide == True:
                        running = False
                    omok_data += str(x)+" "+str(y)+"\n"
                    gameboard_list,black_pos,white_pos,turn,winning = key.step(gameboard_list, black_pos, white_pos, x, y,turn)
                    turn_last = 0
                    decide,winner_row,winner_column = key.check(gameboard_list)
                    winning,decide,status = key.who(decide,gameboard_list,winner_row,winner_column,winning)
                    print(status)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if decide == True:
                    running = False
                elif event.button == 1:
                    x,y = key.mousetap(event.pos)
                    omok_data += str(x)+" "+str(y)+"\n"
                    gameboard_list,black_pos,white_pos,turn,winning = key.step(gameboard_list, black_pos, white_pos, x, y,turn)
                    turn_last = 0
                    decide,winner_row,winner_column = key.check(gameboard_list)
                    winning,decide,status = key.who(decide,gameboard_list,winner_row,winner_column,winning)
                    
            elif event.type == pygame.MOUSEMOTION:
                x,y = key.mousetap(event.pos)
                if x < 15 and y < 15:
                    book_x = 50 * x + 35
                    book_y = 50 * y + 35
        white_time = key.div(white_second)
        black_time = key.div(black_second)
        for s in range(0,len(character)):
            screen.blit(character[s],character_pos[s])
        for w,r in black_pos:
            screen.blit(black_in, (w,r))
        for w,r in white_pos:
            screen.blit(white_in, (w,r))
        if turn == False:
            screen.blit(black_sign,(book_x,book_y))
        elif turn == True:
            screen.blit(white_sign,(book_x,book_y))
        screen.blit(winning, ((screen_wid / 4 * 3),(screen_hei / 2)))
        screen.blit(black_time, ((screen_wid / 8 * 7),(screen_hei / 3 * 2)))
        screen.blit(white_time, ((screen_wid / 8 * 7),(screen_hei / 3 * 1)))
        if(decide == True):
            if(status == True):
                while True:
                    if not os.path.isfile("train/"+str(file_name)+".txt"):
                        break
                    else:
                        file_name += 1
                notepad = open("train/"+str(file_name)+".txt","w")
                notepad.write(omok_data)
                notepad.close()
                running = False
            if(status == False):
                while True:
                    if not os.path.isfile("train2/"+str(file_name_2)+".txt"):
                        break
                    else:
                        file_name_2 += 1
                notepad = open("train2/"+str(file_name_2)+".txt","w")
                notepad.write(omok_data)
                notepad.close()
                running = False        
        pygame.display.update()
    pygame.quit()