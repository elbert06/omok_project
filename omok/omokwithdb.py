import pygame
import os
import key
def omok():    
    bye = 0
    pygame.init()
    ar = key.toar()
    key.send(ar)
    show = []
    show_data = []
    x = 7
    y = 7
    sun = 1
    #기본적인 설정 내용
    screen_wid = 1200
    screen_hei = 800
    screen = pygame.display.set_mode((screen_wid,screen_hei))
    pygame.display.set_caption("omok")
    #캐릭터 + 배경 추가
    current = os.path.dirname(__file__)
    back2 = pygame.image.load(current+"/picture/back2.png")
    show.append(back2)
    show_data.append([0,0])
    back = pygame.image.load(current+"/picture/game_board2.png")
    show.append(back)
    show_data.append([0,0])
    black = pygame.image.load(current+"/picture/black.png")
    black_data = []
    black_data.append(screen_wid / 4 * 3)
    black_data.append(screen_hei / 3 * 2)
    show.append(black)
    show_data.append(black_data)
    white = pygame.image.load(current+"/picture/white.png")
    white_data = []
    white_data.append(screen_wid / 4 * 3)
    white_data.append(screen_hei / 3 * 1)
    show.append(white)
    show_data.append(white_data)
    check = pygame.image.load(current+"/picture/last_sign1.png")
    check_x = 50 * 7 + 35
    check_y = 50 * 7 + 35
    black_main,white_main = [],[]
    white_in = pygame.image.load(current+"/picture/white2.png")
    black_in = pygame.image.load(current+"/picture/black2.png")
    #x,y = 50x + 35
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    show_data,x,check_x = key.right(show_data,x,check_x)
                if event.key == pygame.K_LEFT:
                    show_data,x,check_x = key.left(show_data,x,check_x)
                if event.key == pygame.K_UP:
                    show_data,y,check_y = key.up(show_data,y,check_y)
                if event.key == pygame.K_DOWN:
                    show_data,y,check_y = key.down(show_data,y,check_y)
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if sun == 1:
                        eh = ar[y]
                        if eh[x] == 'a':
                            black_main.append([(50*x+35),(50*y+35)])
                            sun = 2
                            eh[x] = 'o'
                            ar[y] = eh
                            key.send(ar)
                            x,y = key.judge(ar)
                            eh = ar[y]
                            if eh[x] == 'a':
                                white_main.append([(50*x+35),(50*y+35)])
                                sun = 1
                                eh[x] = 'x'
                                ar[y] = eh
                                key.send(ar)
                    bye,fm,fmch = key.check(ar)
                    if bye == 1:
                        win = ar[fm]
                        winner = win[fmch]
                        if winner == 'o':
                            print("흑의 승리")
                        else:
                            print("백의 승리")
                        running = False
        for s in range(0,len(show)):
            screen.blit(show[s],show_data[s])
        for w,r in black_main:
            screen.blit(black_in, (w,r))
        for w,r in white_main:
            screen.blit(white_in, (w,r))
        if sun == 1:
            screen.blit(check,(check_x,check_y))
        pygame.display.update()
    pygame.quit()
    