## Description

Convert a binary search tree into a sorted circular doubly linked list **in place**.

Interpret each node's `left` pointer as the list's predecessor link and its `right` pointer as the successor link.
Circularity means that the smallest node's predecessor is the largest node and the largest node's successor is the
smallest node.

After the transformation, every existing node must use those pointer meanings. Return the smallest node in the
resulting list.

The source's introductory figure uses this five-node binary search tree for its first example:

| Node | Original left child | Original right child |
|---:|---:|---:|
| 4 | 2 | 5 |
| 2 | 1 | 3 |
| 5 | none | none |
| 1 | none | none |
| 3 | none | none |
