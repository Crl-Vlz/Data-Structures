# AVL Trees

---

A tree is balanced if the following statement is true:

| height(Left) - height(Right) | <= 1

Using this definition being balanced does not mean that the node has all its possible children.

To configure this code we must follow the next steps:

- Insert a node.
- Check height diffirences from inserted nodes.
- Check diffs of parent of each node evaluated.
- If a diff of higher value than 1, rotate the granchild node and start again.

Eliminating nodes can also disbalance the tree. For this we have the following logic

- Eliminate the node
- Crawl through the nodes
- If diff found restructure the granchild

```Python
class NodeAVL(Node):
    def __init__(self, key, value):
        super().__init__(key, value)
        self.height = 0 #Updated with search

    def height_left(self):
        return self.left.height if self.left else 0

    def height_right(self):
        return self.right.height if self.right else 0

class BST:

    ...

    def recalculate_height(self, p):
        p.height =  max(p.height_left(), p.height_right()) + 1

    def is_balanced(self, p):
        return abs(p.height_left()-p.height_right()) <= 1

    def insert(self, key, value):
        p = super().insert(key, value)
        self.rebalance(p)

    def top_child(self, p):
        if p.height_left() > p.height_right():
            return p.left
        else:
            return p.right

    def top_grandchild(self, p):
        child = self.top_child(p)
        child = self.top_child(child)
        return child

    def rebalance(self, p):
        while p != self.root:
            last_height = p.height
            if not self.is_balanced(p):
                self.restructure(self.top_grandchild(p))
                if p.left: self.recalculate_height(p.left)
                if p.right: self.recalculate_height(p.right)
            self.recalculate_height(p)
            if p.height == last_height:
                p = self.root
            else:
                p = p.father

```
