from dataclasses import dataclass
from pygame import Rect, Surface
from pygame import draw

import pygame.font

colors = dict()

colors["activeCircle"] = "#ADF67C"
colors["passiveCircle"] = "#A0F5F6"
colors["activeLine"] = "#F5A0C1"
colors["passiveLine"] = "#9F8BF5"


@dataclass
class Node:
    pass

@dataclass
class Node:
    
    key: int
    value: str
    father: Node = None
    left: Node = None
    right: Node = None
    height: int = 0
    coords: tuple = (0,0)
    drawing: Surface = None
    lineToFather: Rect = None
    
    def leftHeight(self):
        return self.left.height if self.left else 0

    def rightHeight(self):
        return self.right.height if self.right else 0

    def drawSelf(self, size: int, pt: int, coords: tuple, active: bool = True) -> None:
        
        pos = list(coords)
        pos[0], pos[1] = pos[0] + (size//2), pos[1] + (size//2)
        coords = tuple(pos)
        self.coords = coords
        screen = Surface((size, size))
        screen.fill((255, 255, 255, 0))
        if active:
            draw.circle(screen, colors["activeCircle"], (size, size), size)
            if self.father:
                self.lineToFather = draw.line(screen, colors["activeLine"], self.coords, self.father.coords)
        else:
            draw.circle(screen, colors["passiveCircle"], (size, size), size)
            if self.father:
                self.lineToFather = draw.line(screen, colors["passiveLine"], self.coords, self.father.coords)
        pygame.font.init()
        font = pygame.font.SysFont(None, pt)
        textImg = font.render(self.value, False, (000, 000, 000))
        Surface.blit(screen, textImg, (size, size))
        pygame.font.quit()
        self.drawing = screen

    def getSurface(self) -> Surface:
        return self.drawing