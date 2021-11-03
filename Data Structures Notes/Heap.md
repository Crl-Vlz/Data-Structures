# Heaps

## 20211103

---

### Definition

A tree where the parents are more importante than the children. When you pop the first node (Most important node),
you interchange the node for the last node. BUt now we don't have the most important node, so we need to bubble it.

### Bubble

Compare priority value with the priority values of the children. The higher value and the original node must be
interchanged. This function is recursive.

### Complexity

Complexity = O(log n)

### Float

When we add elemts to a tree we are adding the node to an available space. But, if the priority is higher we must
float the node to an upper position.

We compare value with father, if father is of lower priority we interchange nodes.

### Comlexity

Complexity = O(log n)

Converting a list to a heap we have a complexity of O( n log n)

Converting a heap to a list takes O( n log n)

A heap is already implemented in python:

```Python
import heapq

ls = [10, 8, 6, 4, 1, 21, 15, 2]

heapq.heapify(ls)
```
