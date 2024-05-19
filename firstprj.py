import pygame
from Character import Thanh

pygame.init()

#game window
Screen_witdh = 1000
Screen_height = 650

screen = pygame.display.set_mode((Screen_witdh, Screen_height))
pygame.display.set_caption("Block fighting game")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#add color 
Red = (255, 0, 0)
Green = (0, 255, 0)
White = (255,255,255)

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

#background image
bg_img = pygame.image.load("image/Background.jpg").convert_alpha()
def background():
    screen.blit(bg_img, (0, 0))
    scaled_bg = pygame.transform.scale(bg_img, (Screen_witdh, Screen_height))

#text
def draw_text(text, font, text_col, x, y):
  font = pygame.font.Font('freesansbold.ttf', 32)
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#health bar
def draw_health_bar(health, x ,y):
    ratio = health/100
    pygame.draw.rect(screen, White, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, Red, (x, y, 400, 30))
    pygame.draw.rect(screen, Green, (x, y, 400*ratio, 30))

#create instances of fighter
Fighter1 = Thanh(200, 310)
Fighter2 = Thanh(700, 310)
        
#game loop
running = True
while running:

    clock.tick(FPS)
    
    background()
    draw_health_bar(Fighter1.health, 20, 30)
    draw_health_bar(Fighter2.health, 580, 30)
    draw_text("P1: " + str(score[0]), 0, Red, 20, 70)
    draw_text("P2: " + str(score[1]), 0, Red, 580, 70)

      #update countdown
    if intro_count <= 0:
        #move fighters
        Fighter1.move(Screen_witdh, Screen_height, screen, Fighter2, round_over)
        Fighter2.move1(Screen_witdh, Screen_height, screen, Fighter1, round_over)
    else:
        #display count timer
        draw_text(str(intro_count), 0, Red, Screen_witdh / 2, Screen_height / 3)
        #update count timer
    if (pygame.time.get_ticks() - last_count_update) >= 1000:
        intro_count -= 1
        last_count_update = pygame.time.get_ticks()

    #update
    Fighter1.update()
    Fighter2.update()
    #draw fighter
    Fighter1.draw(screen)
    Fighter2.draw1(screen)

     #check for player defeat
    if round_over == False:
        if Fighter1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif Fighter2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        #display victory image
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            Fighter1 = Thanh(200, 310)
            Fighter2 = Thanh(700, 310)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()