from typing import List
import pygame, sys
from pygame.locals import QUIT
from random import choices
from time import sleep

from dataclasses import dataclass

color = dict()
color_name = ["red", "blue", "green", "purple", "cyan", "yellow"]

Map = []

color["red"] = (255, 000, 000)
color["blue"] = (000, 000, 255)
color["green"] = (000, 255, 000)
color["purple"] = (255, 000, 255)
color["cyan"] = (000, 255, 255)
color["yellow"] = (255, 255, 000)

@dataclass
class node:
    value: str
    state: int = 1
    goal: bool = False
    searched: bool = False
    children: List(str) = [None] * 4

class tree:
    def __init__(self, root):
        self.root = root
    def addNode(self, node, parent):
        parent.children.append(node)
    def goThroughGrid(self, start, limit, limitY, map, root = None):
        
        value = ""
        found = False

        if not root:
            root = self.root
        searchVals = []
        
        if start % limit != 0:
            searchVals.append(start-1)
        if start % limit != (limit -1):
            searchVals.append(start+1)
        if start > limit:
            searchVals.append(start-limit)
        if start//limit+1 < limitY:
            searchVals.append(start+limit)
        
        for i in range(len(searchVals)):
            map[searchVals[i]].searched = True
            if not map[searchVals[i]].searched:
                self.addNode(map[searchVals[i]], root)
                self.goThroughGrid(searchVals[i], limit, limitY, map, root.children[i])

        return value, found
        

def main():
    pygame.init()
    print("Enter name of file (DON'T ENTER .in !)")
    A = input()
    start = 0
    file = open("Labyrinth Inputs/" + A + ".in")
    A = file.readlines()
    gridValues = A[0].split()

    #Creates a hashmap of the labyrinth
    for i in range(1, len(A)):
        line = A[i].rstrip("\n")
        for j in range(len(line)):
            if line[j] == 'B':
                start = (i - 1) + j
                Map.append(node(str(line[j])))
            elif line[j] == '0':
                Map.append(node(str(line[j]), 0))
            elif line[j] == 'A':
                Map.append(node(str(line[j]), 1, True))
            else:
                Map.append(node(str(line[j])))
            


    labTree = tree(Map[start])



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
        pygame.display.update()
        sleep(1)

main()