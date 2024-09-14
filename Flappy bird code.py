import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption('Flappy Bird')
icon = pygame.image.load('gallery/images/flap 3.png')
pygame.display.set_icon(icon)

class bird:
    def __init__(self):
        self.f1 =  pygame.image.load('gallery/images/flap 1.png').convert_alpha()
        self.f2 =  pygame.image.load('gallery/images/flap 2.png').convert_alpha()
        self.f3 =  pygame.image.load('gallery/images/flap 3.png').convert_alpha()
        
        self.time_time = 0
        self.angle = 100
        self.r_speed = 1
        
        self.accelerat = 2
        self.bird_x = 300

        self.flap = 0
        self.timer = 0
        self.flap_speed = 7

    def blit(self,what,cond):

        self.flaps = [
            pygame.transform.rotate(self.f1,self.angle),
            pygame.transform.rotate(self.f2,self.angle),
            pygame.transform.rotate(self.f3,self.angle)
        ]

        self.flap_up = True
        self.timer += 1
        self.time = [0,1,2,1,0]

        if self.timer >= self.flap_speed:
            self.timer = 0
            self.time_time += 1
            self.flap = self.time[self.time_time]
            if self.time_time == 4:
                self.time_time = 0
        
        self.accelerat += what
        self.bird_x += self.accelerat   
        self.bird_rect = self.flaps[self.flap].get_rect(topleft=(300,self.bird_x))
        self.bird_mask = pygame.mask.from_surface(self.flaps[self.flap])
        if cond:
            self.bird_rect.y = 300
            self.accelerat = 0
            self.bird_x = 300
            
        screen.blit(self.flaps[self.flap],self.bird_rect)

    def rotate(self):
        self.r_speed += 0.05

        self.angle -= self.r_speed
        if self.angle <= -90:
            self.angle = -90

    def jump(self):
        self.accelerat = self.accelerat-self.accelerat -15
        self.r_speed = 0
        self.angle = 20

class resume:
    def __init__(self):
        self.but_list = [
            pygame.image.load('gallery/images/resume but.png'),
            pygame.image.load('gallery/images/resume but ap.png')
        ]
        
        self.which_one = 0
        posi = pygame.mouse.get_pos()
        self.res_but_rect = self.but_list[self.which_one].get_rect(topleft = (300,500))

        
        screen.blit(self.but_list[self.which_one],self.res_but_rect)
        if self.res_but_rect.collidepoint(posi):
            self.which_one = 1
        else:
            self.which_one = 0




#score
font = pygame.font.SysFont('comic sans',60)
score = 0
score_con = False
def draw_scrore(text):
    sc = font.render(str(text),True,(255,255,255))
    screen.blit(sc,(700,10))
        
bg_x = 0
#pillars
pil_x = 500
pil_y = 300
pillars = pygame.image.load('gallery/images/pillars.png')

pillar_rect_1 = pillars.get_rect(midleft = (pil_x,pil_y))
pillar_rect_2 = pillars.get_rect(midleft = (pil_x+600,pil_y))
pillar_rect_3 = pillars.get_rect(midleft = (pil_x+1200,pil_y))
pillar_rect_4 = pillars.get_rect(midleft = (pil_x+1800,pil_y))

pillar_mask_1 = pygame.mask.from_surface(pillars)

bg = pygame.image.load('gallery/images/flappy b.g.png')
plr = bird()

start = False
ac = 0
init_con = True
out =False
menu_but_num= 0
menu_but_con = False
#menu
title_s = 10
title_y = -400
st_bt_x = -300
st_pos = 0
first_time = True
def tell_score(score):
    last_score = font.render("Your Score was "+str(score),True,(255,255,255))
    screen.blit(last_score,(1000,300))

def draw_any_text(txt,x,y):
    text = pygame.font.SysFont('comic sans',25).render(str(txt),True,(255,255,255))
    screen.blit(text,(x,y))

inst_con = False
inst_open = '/\ '

restart = True
menu = True
game = True
run = True

while game:
    key =pygame.key.get_pressed()
    while menu:


        #running the game
        
        screen.fill((0,255,0))
        bg_x = 0
        pil_x = 500
        pil_y = 300
        bird_y = 300
        start = False
        ac = 0
        init_con = True
        pillar_rect_1.midleft = (pil_x,pil_y)
        pillar_rect_1.x = pil_x 
        pillar_rect_2.x = pil_x + 600
        pillar_rect_3.x = pil_x + 1200
        pillar_rect_4.x = pil_x + 1800
        ac = 0
        bg_x += 1
        plr.accelerat = 0
        plr.angle = 0
        out =False
        game = True
        run = True
        #running the game\



        # menu G.U.I
        start_but = [
            pygame.image.load('gallery/images/start flapy.png'),
            pygame.image.load('gallery/images/start flapy a_h.png'),
            pygame.image.load('gallery/images/start flapy a_p.png')
        ]

        start_but_rect = start_but[st_pos].get_rect(topleft= (st_bt_x,500))

        title = pygame.image.load('gallery/images/title flapy.png')
        menu = pygame.image.load('gallery/images/menu.png')
        

        screen.blit(menu,(0,0))
        screen.blit(title,(370,title_y))
        screen.blit(start_but[st_pos],start_but_rect)
        # instruction

        pos= pygame.mouse.get_pos()
        
        
        inst_rect = pygame.Rect((10,16,180,25))
        
        
        if inst_con:
            inst_open = '\/ '
            draw_any_text("Keys :-",10,35)
            draw_any_text("-You can also press 'r' to start.",13,60)
            draw_any_text("-Press 'p' to pause or resume.",13,85)
            draw_any_text("-Press 'Space bar' to fly.",13,110)
            draw_any_text("-Press 'q' to quit",13,135)
            draw_any_text("-This game is designed to be ",13,160)
            draw_any_text(" played at fulscreen, its the best.",13,185)
            
        else:
            inst_open = '/\ '

                

        draw_any_text(str(inst_open)+'Instructions',10,10)

        if not first_time:
            tell_score(score)

        if not st_bt_x >= 30:
            st_bt_x +=9
        
        if title_y >= 10:
            title_y = 10
        else:
            title_y += title_s
            title_s -= 0.04
        
        if start_but_rect.collidepoint(pos):
            st_pos = 1
            if pygame.mouse.get_pressed()[0]:
                st_pos = 2
                menu = False
            else:
                st_pos = 1
        else:
            st_pos = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    menu = False
                if event.key == pygame.K_q:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if inst_rect.collidepoint(pos):
                        if not inst_con:
                            inst_con = True
                        else:
                            inst_con = False
        pygame.display.update()

        run = True
        menu_but_con = False
    score = 0
    inst_con = False
    while run:
        screen.fill((255,0,0))
        restart = True
        pos = pygame.mouse.get_pos()
        # background
        screen.blit(bg, (bg_x, -80))
        if not out:
            bg_x -= 1
        if bg_x <= 1536-2605:
            bg_x = 0
        #for menu
        menu = True
        title_s = 10
        title_y = -400
        st_bt_x = -300
        first_time = False
        # pillars 3 blitting
        if not out:
            pillar_rect_1.x -= 5
            pillar_rect_2.x -= 5
            pillar_rect_3.x -= 5
            pillar_rect_4.x -= 5

        if pillar_rect_1.x <= -200:
            pillar_rect_1.x = 2100
            pillar_rect_1.y = random.randint(-600, -250) - 300

        if pillar_rect_2.x <= -200:
            pillar_rect_2.x = 2100
            pillar_rect_2.y = random.randint(-600, -250) - 300

        if pillar_rect_3.x <= -200:
            pillar_rect_3.x = 2100
            pillar_rect_3.y = random.randint(-600, -250) - 300

        if pillar_rect_4.x <= -200:
            pillar_rect_4.x = 2100
            pillar_rect_4.y = random.randint(-600, -250) - 300

        screen.blit(pillars, pillar_rect_1)
        screen.blit(pillars, pillar_rect_2)
        screen.blit(pillars, pillar_rect_3)
        screen.blit(pillars, pillar_rect_4)



        #player collision
        plr.blit(ac,init_con)
        
        
        if plr.bird_mask.overlap(pillar_mask_1,(pillar_rect_1.x - plr.bird_rect.x,pillar_rect_1.y - plr.bird_rect.y)):
            if not out:
                pygame.mixer.Sound('gallery/audio/gallery_audio_die.wav').play()
            
            out = True
        

        if plr.bird_mask.overlap(pillar_mask_1,(pillar_rect_2.x - plr.bird_rect.x,pillar_rect_2.y - plr.bird_rect.y)):
            if not out:
                pygame.mixer.Sound('gallery/audio/gallery_audio_die.wav').play()
            
            out = True

        if plr.bird_mask.overlap(pillar_mask_1,(pillar_rect_3.x - plr.bird_rect.x,pillar_rect_3.y - plr.bird_rect.y)):
            if not out:
                pygame.mixer.Sound('gallery/audio/gallery_audio_die.wav').play()
            
            out = True
        
        if plr.bird_mask.overlap(pillar_mask_1,(pillar_rect_4.x - plr.bird_rect.x,pillar_rect_4.y - plr.bird_rect.y)):
            if not out:
                pygame.mixer.Sound('gallery/audio/gallery_audio_die.wav').play()
            
            out = True
        
        menu_but = [
            pygame.image.load('gallery/images/menu but.png'),
            pygame.image.load('gallery/images/menu but ap.png')
        ]
        
        #star mechanics
        if not start:
            plr.bird_rect.y = bird_y
            pillar_rect_1.x += 5 
            pillar_rect_2.x += 5 
            pillar_rect_3.x += 5 
            pillar_rect_4.x += 5 
            ac = 0
            bg_x += 1
            plr.accelerat = 0
            plr.angle = 0
            menu_but_rect = menu_but[menu_but_num].get_rect(topleft=(800,500))
            if menu_but_con:
                screen.blit(menu_but[menu_but_num],menu_but_rect)
            if menu_but_rect.collidepoint(pos):
                menu_but_num = 1
                if pygame.mouse.get_pressed()[0]:
                    run = False
            else:
                menu_but_num = 0
            if menu_but_con:
                res_but = resume()
                if res_but.res_but_rect.collidepoint(pos):
                    res_but.which_one = 1
                    if pygame.mouse.get_pressed()[0]:
                     start = True
                else:
                    res_but.which_one = 0
            
                


            
        
            
        else:
            plr.rotate()
            ac = 1.0
            init_con = False

            
        # scrores 
        if plr.bird_rect.colliderect(pillar_rect_1):
            if not score_con:
                score += 1
                pygame.mixer.Sound('gallery/audio/gallery_audio_point.wav').play()
            score_con= True
        elif plr.bird_rect.colliderect(pillar_rect_2):
            if not score_con:
                score += 1
                pygame.mixer.Sound('gallery/audio/gallery_audio_point.wav').play()
            score_con= True
        elif plr.bird_rect.colliderect(pillar_rect_3):
            if not score_con:
                score += 1
                pygame.mixer.Sound('gallery/audio/gallery_audio_point.wav').play()
            score_con= True
        elif plr.bird_rect.colliderect(pillar_rect_4):
            if not score_con:
                score += 1
                pygame.mixer.Sound('gallery/audio/gallery_audio_point.wav').play()
            score_con= True
        else:
            score_con = False
        draw_scrore("score : "+str(score))

        #restart
        if out:
            if plr.bird_rect.y >= 2000:
                run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not out:
                        plr.jump()
                        menu_but_con = True
                        pygame.mixer.Sound('gallery/audio/gallery_audio_wing.wav').play()
                        start = True
                        init_con = False
                if event.key == pygame.K_p:
                    if start ==False:
                        start = True
                    else:
                        start = False
                        s = pygame.display.Info()
                        
            
        
        pygame.display.update()
        clock.tick(60)
        if key[pygame.K_r]:
            run =False
        if key[pygame.K_q]:
            pygame.quit()
    

pygame.quit()
