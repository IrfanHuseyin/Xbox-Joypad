import pygame
import math

pygame.init()

display = pygame.display.set_mode((600, 400))

pygame.display.set_caption("XBOX Controller GUI By IF")

sprite_sheet = pygame.image.load("controller.png").convert_alpha()

joysticks = [pygame.joystick.Joystick(x) for x in range (pygame.joystick.get_count())]

if len(joysticks) == 0:
    print("Error: No controller connected!")
    exit()

# Colours
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GREY = [50, 50, 50]

pygame.display.update()

open = True
while open:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
       
        display.fill((WHITE))

        # Triggers
        # LEFT
        pygame.draw.circle(display, (math.floor((joysticks[0].get_axis(4)+1)*128), 0, 0), (175, 75+10*joysticks[0].get_axis(4)), 40)
        # RIGHT
        pygame.draw.circle(display, (math.floor((joysticks[0].get_axis(5)+1)*128), 0, 0), (423, 75+10*joysticks[0].get_axis(5)), 40)

        display.blit(sprite_sheet, (0, 20))

        # BUMPERS
        # LB
        if joysticks[0].get_button(4):
            pygame.draw.circle(display, (WHITE), (145, 74), 5)
        else:
            pygame.draw.circle(display, (BLACK), (145, 74), 5)
        if joysticks[0].get_button(4):
            pygame.draw.circle(display, (WHITE), (173, 65), 5)
        else:
            pygame.draw.circle(display, (BLACK), (173, 65), 5)
        if joysticks[0].get_button(4):
            pygame.draw.circle(display, (WHITE), (200, 60), 5)
        else:
            pygame.draw.circle(display, (BLACK), (200, 60), 5)
        # RB
        if joysticks[0].get_button(5):
            pygame.draw.circle(display, (WHITE), (400, 60), 5)
        else:
            pygame.draw.circle(display, (BLACK), (400, 60), 5)
        if joysticks[0].get_button(5):
            pygame.draw.circle(display, (WHITE), (427, 65), 5)
        else:
            pygame.draw.circle(display, (BLACK), (427, 65), 5)
        if joysticks[0].get_button(5):
            pygame.draw.circle(display, (WHITE), (453, 74), 5)
        else:
            pygame.draw.circle(display, (BLACK), (453, 74), 5)

        # Back And Start Buttons
        if joysticks[0].get_button(6):
            pygame.draw.circle(display, (WHITE), (264, 148), 14)
        else:
            pygame.draw.circle(display, (BLACK), (264, 148), 14)
        
        if joysticks[0].get_button(7):
            pygame.draw.circle(display, (WHITE), (335, 148), 14)
        else:
            pygame.draw.circle(display, (BLACK), (335, 148), 14)
                             
        # Button Colours 
        # Red
        if joysticks[0].get_button(1):
            pygame.draw.circle(display, (RED), (459, 148), 20)
        else:
            pygame.draw.circle(display, (64, 0, 0), (459, 148), 20)
        # Green
        if joysticks[0].get_button(0):
            pygame.draw.circle(display, (GREEN), (425, 181), 20)
        else:
            pygame.draw.circle(display, (0, 64, 0), (425, 181), 20)
        # Blue
        if joysticks[0].get_button(2):
            pygame.draw.circle(display, (BLUE), (391, 148), 20)
        else:
            pygame.draw.circle(display, (0, 0, 64), (391, 148), 20)
        # Yellow
        if joysticks[0].get_button(3):
            pygame.draw.circle(display, (YELLOW), (425, 115), 20)
        else:
            pygame.draw.circle(display, (100, 100, 0), (425, 115), 20)

        # Analog Sticks With Button Press
        if joysticks[0].get_button(8):
            pygame.draw.circle(display, (GREY), (174+15*joysticks[0].get_axis(0), 148+15*joysticks[0].get_axis(1)), 30)
        else:
            pygame.draw.circle(display, (BLACK), (174+15*joysticks[0].get_axis(0), 148+15*joysticks[0].get_axis(1)), 30)

        if joysticks[0].get_button(9):
            pygame.draw.circle(display, (GREY), (363+15*joysticks[0].get_axis(2), 223+15*joysticks[0].get_axis(3)), 30)
        else:
            pygame.draw.circle(display, (BLACK), (363+15*joysticks[0].get_axis(2), 223+15*joysticks[0].get_axis(3)), 30)

        # D-PAD KEYS
        # UP
        if joysticks[0].get_hat(0) [1] == 1:
            pygame.draw.rect(display, (WHITE), (230, 196, 21, 25), 11, 3)
        else:
            pygame.draw.rect(display, (GREY), (230, 196, 21, 25), 11, 3)
        # DOWN 
        if joysticks[0].get_hat(0) [1] == -1:
            pygame.draw.rect(display, (WHITE), (230, 238, 21, 25), 11, 3)
        else:
            pygame.draw.rect(display, (GREY), (230, 238, 21, 25), 11, 3)
        # LEFT
        if joysticks[0].get_hat(0) [0] == -1:
            pygame.draw.rect(display, (WHITE), (207, 219, 25, 21), 11, 3)
        else:
            pygame.draw.rect(display, (GREY), (207, 219, 25, 21), 11, 3)
        # RIGHT
        if joysticks[0].get_hat(0) [0] == 1:
            pygame.draw.rect(display, (WHITE), (249, 219, 25, 21), 11, 3)
        else:
            pygame.draw.rect(display, (GREY), (249, 219, 25, 21), 11, 3)
        # CENTER STATIC SQUARE
        pygame.draw.rect(display, (GREY), (230, 219, 21, 21), 11)

        pygame.display.update()

pygame.quit()