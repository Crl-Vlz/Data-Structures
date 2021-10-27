# BST (Binary Search Tree)

## October 4th 2021

---

A binary tree where the nodes are ordered by size of the values.

First we recieve a root node, then depending on the value
if lower is made a left child, else it is made a right child.

This process is recursive, so we know all nodes are ordered by value.

This reduces the search time from O(_n_) to O(_log n_)

**Main Problems:**

- Insertion time is of _log n_

- Requires a full tree

- Eliminating a node value is easy if the node has none or one children nodes.
  The problem comes when the node has two children. To resolve this we have to use a previous function.

### Previous Function

A function of a bst, made for replacing a node that has two children nodes.

### Rotation

When a BST has too many nodes in either direction the search time increases.
To prevent this we should rotate the node. For this we grab:

_Node_ -- _Parent_ -- _Parent of parent_

There are four possible cases for rotation:
-Right-->Right-->Right
-Left-->Left-->Left
-Right-->Left-->Right
-Left-->Right-->Left

In these last two cases it's better to simply rotate the child of the chosen node, and then rotate the node.
