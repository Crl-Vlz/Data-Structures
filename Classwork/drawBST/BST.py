from time import sleep
from node import Node
from dataclasses import dataclass

from pygame import Surface, display

@dataclass
class BST:
    
    SCREEN_WIDTH: int
    SCREEN_HEIGHT: int

    nodeScreen: Surface = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    root: Node = None
    length: int = 0
    top: int = 0
    size: int = 64

    def getSurface(self) -> Surface:
        return self.nodeScreen

    def updateSize(self):
        nNodes = self.inorder()
        self.length = nNodes = len(nNodes)
        self.top = self.height()
        self.size = self.SCREEN_WIDTH // nNodes

    def height(self, node: Node = None) -> int:
        flagLeft = 0
        flagRight = 0
        if node.left: flagLeft = self.height(node.left)
        if node.right: flagRight = self.height(node.right)
        if flagLeft > flagRight: return flagLeft
        else: return flagRight 

    def depth(self, key: int) -> int:
        node = self.searchNode(key)
        i = 0
        if node:
            while node.father:
                i += 1
                node = node.father
        return i

    def addNode(self, newNode: Node, parentNode: Node = None) -> None:
        if not parentNode:
            if self.root: parentNode = self.root
            else: self.root = newNode; return
        if newNode.key < parentNode.key:
            if not parentNode.left:
                parentNode.left = newNode
                newNode.father = parentNode
                self.updateSize()
                height = self.depth(newNode.key)
                length = self.inorder()
                width = 0
                for i in range(len(length)):
                    if length[i] == newNode.key:
                        width = i
                        break
                newNode.drawSelf(self.size, self.size//3, (self.size * width, self.size * height), True)
                self.nodeScreen.blit(newNode.getSurface(), (self.size * width, self.size * height),)
                display.update()
                sleep(0.5)
                newNode.drawSelf(self.size, self.size//3, (self.size * width, self.size * height), True)
                display.update()
                self.nodeScreen.blit(newNode.getSurface(), (self.size * width, self.size * height),)
            else: self.addNode(newNode, parentNode.left)
        elif newNode.key > parentNode.key:
            if not parentNode.right:
                parentNode.right = newNode
                newNode.father = parentNode
                self.updateSize()
                height = self.depth(newNode.key)
                length = self.inorder()
                width = 0
                for i in range(len(length)):
                    if length[i] == newNode.key:
                        width = i
                        break
                newNode.drawSelf(self.size, self.size//3, (self.size * width, self.size * height), True)
                self.nodeScreen.blit(newNode.getSurface(), (self.size * width, self.size * height))
                display.update()
                sleep(0.5)
                newNode.drawSelf(self.size, self.size//3, (self.size * width, self.size * height), True)
                display.update()
                self.nodeScreen.blit(newNode.getSurface(), (self.size * width, self.size * height))
            else: self.addNode(newNode, parentNode.right)

    def searchNode(self, key: int, parentNode = None) -> Node:
        if not parentNode and self.root: parentNode = self.root
        else: return None
        returnable = None
        if key == parentNode.key: return parentNode
        elif key > parentNode.key: returnable =  self.searchNode(key, parentNode.right)
        elif key < parentNode.key: returnable =  self.searchNode(key, parentNode.left)
        return returnable

    def rightmost(self, node: Node) -> Node:
        while node.right: node = node.right
        return node

    def previous(self, node: Node) -> Node:
        if node.left: return self.rightmost(node.left)
        else:
            if not node.father: return None
            parent = node.father
            while node.left == node:
                node = node.parent
                parent = node.parent
                if not parent: return None
            return parent

    def leftmost(self, node: Node) -> Node:
        while node.left: node = node.left
        return node

    def interchange(self, nodeA: Node, nodeB: Node) -> None:
        nodeA.key, nodeB.key =  nodeB.key, nodeA.key
        nodeA.value, nodeB.value = nodeB.value, nodeA.value

    def delete(self, node: int) -> None:
        if type(node) == int: node = self.searchNode(node)
        if not node: return

        if not node.left and not node.right:
            parent = node.father
            if parent:
                if parent.left == node: parent.left = None
                else: parent.right = None
            node = None

        elif not node.left or not node.right:
            if node.left: child = node.left
            else: child = node.right
            parent = node.parent
            if parent:
                if parent.left == node: parent.left = child
                else: parent.right = child
            child.father = parent
            node = None

        else:
            leftmostNode = self.leftmost(self, node)
            if leftmostNode:
                self.interchange(leftmostNode, node)
                self.delete(leftmostNode)
        self.updateSize()

    def relink(self, father: Node, child: Node, isLeft: bool) -> None:
        if isLeft: father.left = child
        else: father.right = child
        if child: child.father = father

    def rotate(self, node: Node) -> None:
        nodeY = node.father
        nodeZ = nodeY.father
        self.relink(nodeZ, node, nodeY == nodeZ.left)
        if node == nodeY.left:
            self.relink(nodeY, node.right, True)
            self.relink(node, nodeY, False)
        if node == nodeY.right:
            self.relink(nodeY, node.left, False)
            self.relink(node, nodeY, True)

    def doubleRotate(self, node: Node) -> None:
        if type(node) == int: node = self.searchNode(node)
        nodeY = node.father
        nodeZ = nodeY.father

        height = self.depth(node.key)
        length = self.inorder()
        width = 0
        for i in range(len(length)):
            if length[i] == node.key:
                width = i
                break

        node.drawSelf(self.size, self.size//3, (self.size * width, self.top * height), True)

        heightY = self.depth(nodeY.key)
        widthY = 0
        for i in range(len(length)):
            if length[i] == nodeY.key:
                widthY = i
                break

        nodeY.drawSelf(self.size, self.size//3, (self.size * widthY, self.top * heightY), True)

        heightZ = self.depth(nodeZ.key)
        widthZ = 0
        for i in range(len(length)):
            if length[i] == nodeZ.key:
                widthZ = i
                break

        nodeZ.drawSelf(self.size, self.size//3, (self.size * widthZ, self.top * heightZ), True)

        self.nodeScreen.blit(node.getSurface(), (self.size * width, self.top * height),)
        self.nodeScreen.blit(nodeY.getSurface(), (self.size * width, self.top * height),)
        self.nodeScreen.blit(nodeZ.getSurface(), (self.size * width, self.top * height),)
        display.update()
        sleep(0.5)
        
        if (node == nodeY.right) == (nodeY == nodeZ.right): self.rotate(nodeY)
        else:
            self.rotate(node)
            self.rotate(node)

        self.updateSize()

        height = self.depth(node.key)
        length = self.inorder()
        width = 0
        for i in range(len(length)):
            if length[i] == node.key:
                width = i
                break

        heightY = self.depth(nodeY.key)
        widthY = 0
        for i in range(len(length)):
            if length[i] == nodeY.key:
                widthY = i
                break

        heightZ = self.depth(nodeZ.key)
        widthZ = 0
        for i in range(len(length)):
            if length[i] == nodeZ.key:
                widthZ = i
                break

        node.drawSelf(self.size, self.size//3, (self.size * width, self.top * height), False)
        nodeY.drawSelf(self.size, self.size//3, (self.size * widthY, self.top * heightY), False)
        nodeZ.drawSelf(self.size, self.size//3, (self.size * widthZ, self.top * heightZ), False)
        self.nodeScreen.blit(node.getSurface(), (self.size * width, self.top * height),)
        self.nodeScreen.blit(nodeY.getSurface(), (self.size * width, self.top * height),)
        self.nodeScreen.blit(nodeZ.getSurface(), (self.size * width, self.top * height),)
        display.update()
        sleep(0.5)

        self.nodeScreen.blit(node.getSurface(), node.coords)

    def preorder(self, node: Node = None) -> list:
        if not node and self.root: node = self.root
        keys = [node.key]
        if node.left: keys += self.inorder(node.left)
        if node.right: keys += self.inorder(node.right)
        return keys

    def inorder(self, node: Node = None) -> list:
        if not node and self.root: node = self.root
        if node.left: keys = self.inorder(node.left)
        keys += [node.key]
        if node.right: keys += self.inorder(node.right)
        return keys

    def postorder(self, node: Node = None) -> list:
        if not node and self.root: node = self.root
        if node.left: keys = self.postorder(node.left)
        if node.right: keys += self.postorder(node.right)
        keys += [node.key]
        return keys


