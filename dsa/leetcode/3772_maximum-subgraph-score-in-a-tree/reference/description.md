## Description

You are given an undirected tree with $n$ nodes numbered from $0$ through $n-1$. Its `n - 1` edges are listed in `edges`; each pair `[a_i,b_i]` joins nodes `a_i` and `b_i`.

An array `good` classifies every node. Node `i` is **good** when `good[i] = 1` and **bad** when `good[i] = 0`.

The score of a subgraph is its number of good nodes minus its number of bad nodes. For every node `i`, determine the greatest score among all connected subgraphs that contain `i`.

Return an array of $n$ integers whose `i`th value is that maximum score for node `i`.

A **subgraph** selects some vertices and edges from the original tree. It is **connected** when every two selected vertices can reach one another using only selected edges.
