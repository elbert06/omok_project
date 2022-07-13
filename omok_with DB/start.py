import pygame
import os
import omok
import enter
def start():
    pygame.init()
    screen_wid = 1200
    screen_hei = 800
    gamefont = pygame.font.SysFont("malgungothic", 30)
    screen = pygame.display.set_mode((screen_wid,screen_hei))
    current = os.path.dirname(__file__)
    character = []
    character_pos = []
    back2 = pygame.image.load(current+"/picture/back2.png")
    character.append(back2)
    character_pos.append([0,0])
    back_left = pygame.image.load(current+"/picture/back_left.png")
    character.append(back_left)
    character_pos.append([0,0])
    back_right = pygame.image.load(current+"/picture/back_right.png")
    character.append(back_right)
    character_pos.append([(screen_wid / 2),0])
    bytwo = gamefont.render("in one device", True, (0,0,0))
    character.append(bytwo)
    character_pos.append([(screen_wid / 14 * 4),(screen_hei / 2)])
    bytwo = gamefont.render("in match", True, (0,0,0))
    character.append(bytwo)
    character_pos.append([(screen_wid / 14*8),(screen_hei / 2)])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                dec = event.pos
                if dec[0] < (screen_wid/2):
                    omok.omok()
                    return
                elif dec[0] > (screen_wid/2):
                    enter.wait()
                    return
        for s in range(0,len(character)):
            screen.blit(character[s],character_pos[s])
        pygame.display.update()
    pygame.quit()