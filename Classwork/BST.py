from dataclasses import dataclass

@dataclass
class node:
    pass

@dataclass
class node:
    key: int
    value: int
    left: node = None
    right: node = None

class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class btree:
    def __init__(self, root = None):
        self.root = root
    def addNode(self, node, root = None):
        if not root:
            root = self.root
            if not root:
                root = node
        else:
            if node < root.value:
                if root.left:
                    self.addNode(self, node, root.left)
                elif not root.left:
                    root.left = node
            elif node > root.value:
                if root.right:
                    self.addNode(self, node, root.right)
                elif not root.right:
                    root.right = node

tree = btree

list = [40, 20, 60, 50, 80, 10]

j = 0

for i in list:
    Node = node(j, i)
    j += 1
    tree.addNode(Node)

print(tree)
