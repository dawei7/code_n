## Description

You are given an **undirected connected** graph of `n` nodes, numbered from `0` to `n - 1`. Each node is connected to **at most** 2 other nodes.

The graph consists of `m` edges, represented by a 2D array `edges`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i`.

<p data-end="502" data-start="345">You have to assign a **unique** value from <code data-end="391" data-start="388">1</code> to <code data-end="398" data-start="395">n</code> to each node. The value of an edge will be the **product** of the values assigned to the two nodes it connects.

<p data-end="502" data-start="345">Your score is the sum of the values of all edges in the graph.

Return the **maximum** score you can achieve.
