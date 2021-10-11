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
            global goal
            goal = fstNode.index

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
            val = start-1
            values.append(val)
        if nodeU and nodeU.state and not nodeU.searched:
            nodeU.searched = True
            self.addNode(nodeU, root)
            val = start-limit
            values.append(val)
        if nodeR and nodeR.state and not nodeR.searched:
            nodeR.searched = True
            self.addNode(nodeR, root)
            val = start+1
            values.append(val)
        if nodeD and nodeD.state and not nodeD.searched:
            nodeD.searched = True
            self.addNode(nodeD, root)
            val = start+limit
            values.append(val)
            
        for child in root.children:
            if values:
                self.goThroughGrid(values[0], limit, limitY, map, child)
                values.popleft()

    def amplitudeSearch(self, node):

        values = deque()

        found = False


        if node.value == 'B':
            found = True
            global goal
            goal = node.index

        for child in node.children:
            values.append(child)

        print(node.children)

        return values, found



    def searchBranch(self, node):

        path = []
        global Map
        
        while node != self.root:
            path.append(node.index)
            node = Map[node.parent]

        path.append(node.index)

        return path
        
    def printTree(self, root = None):

        if not root:
            root = self.root

        while True:
            print(root)
            print(root.children)
            if root.children:
                root = root.children[0]
            else:
                break

        print("Later Yo")

def main():

    Path = []

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


    labTree.goThroughGrid(start, sh, sv, Map, Map[value])

    startVals.append(labTree.root)

    foundB = False

    startY = 0
    while start >= sh:
        start -= sh
        startY += 1

    while startVals and not foundB:
        
        value = startVals[0]

        vals, foundB = labTree.amplitudeSearch(value)

        for val in vals:
            startVals.append(val)

        coord = value.index

        y = 0
        while coord >= sh:
            coord -= sh
            y += 1
        pygame.draw.rect(screen, color["purple"], (nW*coord, nH*y, nW, nH))
        pygame.draw.rect(screen, color["red"], (nW*start, nH*startY, nW, nH))
        pygame.display.update()

        sleep(0.1)
        startVals.popleft()

    global goal

    if goal != -1:
        Path = labTree.searchBranch(Map[goal])
        print(Path)
        y = 0
        while goal >= sh:
            goal -= sh
            y += 1
        pygame.draw.rect(screen, color["blue"], (nW*goal, nH*y, nW, nH))
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

        if Path:
            for cell in reversed(Path):
                y = 0
                while cell >= sh:
                    cell -= sh
                    y += 1
                pygame.draw.rect(screen, color["yellow"], (nW*cell, nH*y, nW, nH))
                sleep(0.2)
                pygame.display.update()

        pygame.display.update()

main()