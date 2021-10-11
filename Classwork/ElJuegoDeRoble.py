from dataclasses import dataclass

@dataclass
class node:
    pass

@dataclass
class node:
    value: int
    left: node = None
    right: node = None
    searched: bool = False

    def __repr__(self):
        return str(self.value)

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
            else:
                self.addNode(node, parent.left)
        else:
            if not parent.right:
                parent.right = node
            else:
                self.addNode(node, parent.right)
    def __repr__(self):
       return str(self.root.value)
    
    def search(self, root=None):

        if not root:
            root = self.root

        results = []
        
        NodeLeft = root.left
        NodeRight = root.right

        if NodeLeft:
            results += self.search(NodeLeft)

        if NodeRight:
            results += self.search(NodeRight)

        results = [root] + results

        return results


n = int(input())
nodos = input().split(" ")
flag = n - 1
listaNodos = tree(node(int(nodos[-1])))

nodos = nodos[0:flag]

for nodeValue in reversed(nodos):
	listaNodos.addNode(node(int(nodeValue)))

result = listaNodos.search()

final = ""

for char in result:
    final += str(char.value) + " "

print(final)