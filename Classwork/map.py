from typing import List
import pygame, sys
from pygame.locals import QUIT
from random import choices
from time import sleep

from dataclasses import dataclass

from collections import deque

color = dict()
color_name = ["red", "blue", "green", "purple", "cyan", "yellow"]

Map = []

color["red"] = (255, 000, 000)
color["blue"] = (000, 000, 255)
color["green"] = (000, 255, 000)
color["purple"] = (255, 000, 255)
color["cyan"] = (000, 255, 255)
color["yellow"] = (255, 255, 000)

Path = []

#Paths checked
startVals = deque()
found = False

goal = -1

@dataclass
class node:
    value: str
    children: list()
    index: int = 0
    state: int = 1
    parent: int = 0
    searched: bool = False

    def __repr__(self):
        return "The value is " + self.value

class tree:
    def __init__(self, root):
        self.root = root
    def addNode(self, node, parent):
        node.parent = parent.index
        parent.children.append(node)

    #Travels through the grid
    def goThroughGrid(self, start, limit, limitY, map, root = None):
        #Add nodes
        fstNode = map[start]
        fstNode.searched = True
        fstNode.index = start

        if fstNode.value == 'B':
            global found
            found = True
            global goal
            goal = fstNode.index

        #print(fstNode)

        Path.append(start)

        if not root:
            root = self.root

        #Variables for nodes
        nodeL = None 
        nodeU = None 
        nodeD = None 
        nodeR = None

        values = deque()

        #Adds node based on value
        if (start % limit) != 0:
            nodeL = map[start-1]
        if start >= limit:
            nodeU = map[start-limit]
        if (start % limit) < (limit - 1):
            nodeR = map[start+1]
        if (start // limit) + 1 < limitY:
            nodeD = map[start + limit]

        if nodeL and nodeL.state and not nodeL.searched:
            nodeL.searched = True
            self.addNode(nodeL, root)
            values.append(start-1)
        if nodeU and nodeU.state and not nodeU.searched:
            self.addNode(nodeU, root)
            values.append(start-limit)
        if nodeR and nodeR.state and not nodeR.searched:
            self.addNode(nodeR, root)
            values.append(start+1)
        if nodeD and nodeD.state and not nodeD.searched:
            self.addNode(nodeD, root)
            values.append(start+limit)

#        cont = 0
#        for child in root.children:
#            #print(child)
#            self.goThroughGrid(startVals[cont], limit, limitY, map, child)
#            cont += 1

        return values

#    def searchBranch(self, node = None):
#
#        if not node:
#            node = self.root
#
#        found = False
#
#        path = []
#
#        if node.value == 'B':
#            found = True
#
#        for child in node.children:
#            p1, f1 = self.searchBranch(child)
#            if f1:
#                found = f1
#                path += p1
#
#        if found:
#            path.append(node.index)
#
#        return path, found



    def searchBranch(self, node):

        path = []
        global Map
        
        while node != self.root:
            print(node)
            path.append(node.index)
            node = Map[node.parent]

        path.append(node.index)

        return path
        

def main():
    pygame.init()
    print("Hello")
    print("Enter name of file (DON'T ENTER .in !)")
    A = input()
    start = 0
    file = open("Labyrinth Inputs/" + A + ".in")
    A = file.readlines()
    gridValues = A[0].split()

    #Adds values for the grid and grid cells
    sh = int(gridValues[0])
    sv = int(gridValues[1])

    width, height = 400, 400

    nH = height//sv
    nW = width//sh

    #Fills the creen with a gray/grey color/colour
    screen = pygame.display.set_mode((width, height))
    screen.fill( (120, 120, 120) )
    pygame.display.set_caption("Labyrinth")

    #Creates a hashmap of the labyrinth
    for i in range(1, len(A)):
        line = A[i]
        line = line.rstrip("\n")
        for j in range(len(line)):
            value = (i -1) * sh + j
            if line[j] == 'A':
                start = (i - 1) * sh + j
                #print("the start value is " + str(start))
                Map.append(node(str(line[j]), [], value))
                pygame.draw.rect(screen, color["red"], (nW*j, nH*(i-1), nW, nH))
            elif line[j] == '0':
                Map.append(node(str(line[j]), [], value, 0))
                pygame.draw.rect(screen, color["cyan"], (nW*j, nH*(i-1), nW, nH))
            else:
                Map.append(node(str(line[j]), [], value))
                if line[j] == 'B':
                    pygame.draw.rect(screen, color["blue"], (nW*j, nH*(i-1), nW, nH))
                else:
                    pygame.draw.rect(screen, color["green"], (nW*j, nH*(i-1), nW, nH))
    
    labTree = tree(Map[start])

    startVals.append(start)

    while startVals and not found:
        value = startVals[0]
        val = labTree.goThroughGrid(value, sh, sv, Map, Map[value])
        for v in val:
            startVals.append(v)
        #print(cell)
        y = 0
        while value >= sh:
            value -= sh
            y += 1
        pygame.draw.rect(screen, color["purple"], (nW*value, nH*y, nW, nH))
        pygame.display.update()
        sleep(0.1)
        startVals.popleft()

    if goal != -1:
        Path = labTree.searchBranch(Map[goal])
        print(Path)
    else:
        print("No path available")

    gameOn = True

    while gameOn:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        sleep(2)

        for cell in reversed(Path):
            #print(cell)
            y = 0
            while cell >= sh:
                cell -= sh
                y += 1
            pygame.draw.rect(screen, color["yellow"], (nW*cell, nH*y, nW, nH))
            sleep(0.2)
            pygame.display.update()

        pygame.display.update()
        #sleep(60)

main()