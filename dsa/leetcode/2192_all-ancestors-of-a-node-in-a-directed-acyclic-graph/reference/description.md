## Description

You are given a positive integer `n` representing the number of nodes of a **Directed Acyclic Graph** (DAG). The nodes are numbered from `0` to `n - 1` (**inclusive**).

You are also given a 2D integer array `edges`, where `edges[i] = [from_i, to_i]` denotes that there is a **unidirectional** edge from `from_i` to `to_i` in the graph.

Return *a list* `answer`*, where *`answer[i]`* is the **list of ancestors** of the* `i^th` *node, sorted in **ascending order***.

A node `u` is an **ancestor** of another node `v` if `u` can reach `v` via a set of edges.
