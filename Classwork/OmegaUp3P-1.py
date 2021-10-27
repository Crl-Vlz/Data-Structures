from dataclasses import dataclass

@dataclass
class node:
    pass

@dataclass
class node:
    value: int
    left = node
    right = node

class tree:
    def __init__(self, root):
        self.root = root
    def addNode(self, node, parent = None):
        if not parent:
            parent = self.root
        parValue = parent.value
        evaluate = node.value
        if evaluate < parValue:
            if not parent.left:
                parent.left = node