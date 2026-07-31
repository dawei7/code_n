## Description

You are given an integer `n` and an undirected tree whose nodes are numbered from `0` through `n - 1`. The `n - 1` pairs in `edges` describe its undirected edges.

An equally long array `group` assigns a group label to every node. Nodes `u` and `v` belong to the same group exactly when `group[u] == group[v]`.

The **interaction cost** of two nodes is the number of edges on their unique connecting path in the tree. Return the sum of this cost over every unordered pair of distinct nodes that belongs to the same group.
