import pygame, sys
from pygame.locals import QUIT
from random import choices
from time import sleep

color = dict()
color_name = ["red", "blue", "green", "purple", "cyan", "yellow"]

color["red"] = (255, 000, 000)
color["blue"] = (000, 000, 255)
color["green"] = (000, 255, 000)
color["purple"] = (255, 000, 255)
color["cyan"] = (000, 255, 255)
color["yellow"] = (255, 255, 000)

def main():
    pygame.init()
    print("Enter name of file (DON'T ENTER .in !)")
    A = input()
    file = open("Labyrinth Inputs/" + A + ".in")
    A = file.readlines()
    gridValues = A[0].split()
    sh = int(gridValues[0])
    sv = int(gridValues[1])
    
    width, height = 400, 400

    nH = height//sv
    nW = width//sh

    screen = pygame.display.set_mode((width, height))
    screen.fill( (120, 120, 120) )
    pygame.display.set_caption("Labyrinth")

    gameOn = True

    while gameOn:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        for i in range(sh):
            for j in range(sv):
                pygame.draw.rect(screen, color[choices(color_name)[0]], (nW*i, nH*j, nW, nH))
                #pygame.display.update()
                #sleep(0.5)
        pygame.display.update()
        sleep(1)

main()