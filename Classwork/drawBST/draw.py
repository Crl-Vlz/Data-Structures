from typing import TextIO
import pygame
from time import sleep
from BST import BST
from node import Node

tree = BST(1000, 500)

def insert(key: int, value: str, surface: pygame.Surface) -> None:
    tree.addNode(Node(key, value))
    surface.blit(tree.getSurface, (0, 0))

def delete(key: int, surface: pygame.Surface) -> None:
    tree.delete(key)
    surface.blit(tree.getSurface(), (0,0))

def search(key: int, surface: pygame.Surface) -> None:
    tree.searchNode(key)
    surface.blit(tree.getSurface(), (0,0))

def rotate(key: int, surface: pygame.Surface) -> None:
    tree.rotate(key)
    surface.blit(tree.getSurface(), (0,0))

def convertInstruction(instruction:str) -> int:
    instruction = instruction.upper()
    if instruction == "INSERTAR": return 1
    elif instruction == "BUSCAR": return 2
    elif instruction == "ELIMINAR": return 3
    elif instruction == "ROTAR": return 4

def readFile() -> list:
    f = input()
    file = open(f+ ".in")
    lines = file.readlines()

    instructions = []

    for line in lines:
        line.rstrip()
        line = line.split
        line[0], line[1] = convertInstruction(line[0]), int(line[1])
        instructions.append(line)

    return instructions

def menu(instruction: int, key: int, value: str, surface: pygame.Surface) -> None:
    if instruction == 1: insert(key, value, surface)
    elif instruction == 2: search(key, surface)
    elif instruction == 3: delete(key, surface)
    elif instruction == 4: rotate(key, surface)

def main():
    instructions = readFile()
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    for instruction in instructions:
        menu(instruction[0], instruction[1], str(instruction[2]), screen)
    pygame.quit()

