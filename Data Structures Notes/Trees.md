# Trees

## September 13th 2021

---

### Definition

Data structure with heirarchy

- Data stored in nodes
- There is only one node with no parents (Root node)
- Each node con have 0 or more nodes
  - If a node has children it will be known as an internal node.
  - If a node does not have children, it will be known as a leaf.
- Node *x* is an ancestor of node *y* if *x* is ancestor of parent of *y*, or *x = y*

> To understand recursion first you must understand recursion ~ Profesor Miguel Alcaraz

- Node *y* is descendant of *x* if *x* is ancestor of *y*

---

### What is a sub-tree

**The sub-tree *T* is a tree with root on *n***

**In that way** sub-tree *T* is *n* and all of its descendants.

- An aryst is relationship between the nodes *x* and *y* when *x* and *y* are parent and child.
- A path is a series of consecutive arysts where two consecutive nodes share a same node.
In that sense the first aryst starts in *x* and the last aryst stops at *y*.

There **always** exists a path between two nodes.

## Binary Trees

A special type of tree were each node can only have two children nodes.

In that way, considering the root level as level 0, the nde has a storage capacity of 2<sup>n</sup>:

|Level|Nodes|Total|
|---|---|---|
|0|1|1|
|1|2|3|
|2|4|7|
|n|2<sup>n</sup>|2<sup>n+1</sup>-1|

### Definitions

**Path length**: Quantity of arysts that are made between two nodes.
