## Description

An undirected connected tree has nodes labeled 1 through `n`, with node 1 as its root. For every node labeled `v > 1`, its parent is labeled $\lfloor v/2\rfloor$. Initially, every node stores the value 0.

For each label in `queries`, flip the value of that node and every node in its rooted subtree: 0 becomes 1 and 1 becomes 0. Process the queries in order, then return how many nodes finally store 1.
