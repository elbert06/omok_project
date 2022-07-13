import pygame
import os
import key
import time
import timeit
import data
import start
def omok(db_name,real_turn):
    m = []
    r = []
    first = True
    fin = False
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
    n = 0
    #차례표시 자막
    running = True
    while running:
        if fin == True:
            pass
        elif n % 2 ==0 :
            turn = False
            winning = gamefont.render("black turn", True, (0,0,0))
        else:
            turn = True
            winning = gamefont.render("white turn", True, (0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                data.drop(db_name)
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fin == True: running = False
                if real_turn == turn:
                    x,y = key.mousetap(event.pos)
                    if x < 15 and y < 15:
                        stattt = key.check2(gameboard_list, x, y)
                        if stattt == True:
                            current = os.path.dirname(__file__)
                            test = pygame.mixer.Sound(current+"/picture/step.wav")
                            test.play(0)
                            time.sleep(test.get_length())
                            test.stop()
                            data.DB_insert2([1,x,y], db_name)
            elif event.type == pygame.MOUSEMOTION:
                if real_turn == turn:
                    x,y = key.mousetap(event.pos)
                    if x < 15 and y < 15:
                        book_x = 50 * x +35
                        book_y = 50 * y + 35
        m = data.find_wait2(db_name)
        n = len(m)
        for sr in range(0,len(character)):
            screen.blit(character[sr],character_pos[sr])
        for sh in range(0,len(m)):
            s = m[sh]
            if sh % 2 == 0:
                screen.blit(black_in,(s.get("X")*50+35,s.get("Y")*50+35))
                gameboard_list,status = key.step2(gameboard_list, s.get("X"), s.get("Y"), True)
            else:
                screen.blit(white_in,(s.get("X")*50+35,s.get("Y")*50+35))
                gameboard_list,status = key.step2(gameboard_list, s.get("X"), s.get("Y"), False)
        fin,winner_row,winner_column = key.check(gameboard_list)
        if real_turn == turn:
            screen.blit(black_sign,(book_x,book_y))
        if fin == True and first == True:
            winning,decide = key.who(fin, gameboard_list, winner_row, winner_column, winning)
            first = False
        screen.blit(winning, ((screen_wid / 4 * 3),(screen_hei / 2)))
        pygame.display.update()
    pygame.quit()