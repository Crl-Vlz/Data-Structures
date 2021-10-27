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
