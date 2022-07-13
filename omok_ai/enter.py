import random
import pygame
import key
import os
import omok_two
def wait():
    status = False
    conti = False
    check_text = ''
    current = os.path.dirname(__file__)
    gamefont = pygame.font.SysFont("malgungothic", 30)
    myid,myroompassword = key.numberset()
    pygame.init()
    screen_wid = 1200
    screen_hei = 800
    screen = pygame.display.set_mode((screen_wid,screen_hei))
    first_tell = gamefont.render("""put down the other pin number your boss's pin is """+str(myroompassword), True, (0,0,0))
    first_tell_pos = key.getcenter(first_tell,(screen_wid / 2),(screen_hei / 8 * 1))
    first_input = gamefont.render(check_text, True, (0,0,0))
    first_input_pos = key.getcenter(first_input, (screen_wid / 2), (screen_hei / 8 * 2))
    second_tell = gamefont.render("", True, (0,0,0))
    second_tell_pos = key.getcenter(second_tell, (screen_wid / 2), (screen_hei / 8 * 3))
    third_tell = gamefont.render("", True, (0,0,0))
    third_tell_pos = key.getcenter(third_tell, (screen_wid / 2), (screen_hei / 8 * 4))
    back2 = pygame.image.load(current+"/picture/back2.png")
    running = True
    while running:
        first_input = gamefont.render(check_text, True, (0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                data.drop(str(myid))
                data.DB_delete(myid)
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    check_text = check_text[0:len(check_text) - 1]
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if conti == True:
                        if n == True:
                            data.CRE(str(myid))
                            data.DB_delete(myid)
                            data.DB_insert([myid,bosspassword])
                            omok_two.omok(str(myid),False)
                        if n == False:
                            omok_two.omok(str(othersid),True)
                            return
                    status,bosspassword = key.ishere(myid,check_text)
                    if status == True:
                        second_tell = gamefont.render("your boss's id is "+str(bosspassword)+" press enter if it is correct", True, (0,0,0))
                        conti = True
                        n = True
                    else:
                        status,othersid = key.ishere2(myid,myroompassword)
                        if status == True:
                            second_tell = gamefont.render("Someone joined to you press enter if it is want", True, (0,0,0))
                            conti = True
                            n = False
                        else:
                            second_tell = gamefont.render("there is no boss", True, (0,0,0))
                    second_tell_pos = key.getcenter(second_tell, (screen_wid / 2), (screen_hei / 8 * 3))
                else:
                    check_text += event.unicode
        screen.blit(back2, (0,0))
        screen.blit(first_tell, (first_tell_pos))
        screen.blit(first_input, (first_input_pos))
        screen.blit(second_tell, (second_tell_pos))
        screen.blit(third_tell, (third_tell_pos))
        pygame.display.update()
    pygame.quit()