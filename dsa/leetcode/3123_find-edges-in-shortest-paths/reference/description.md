## Description

You are given an undirected weighted graph of `n` nodes numbered from 0 to `n - 1`. The graph consists of `m` edges represented by a 2D array `edges`, where `edges[i] = [a_i, b_i, w_i]` indicates that there is an edge between nodes `a_i` and `b_i` with weight `w_i`.

Consider all the shortest paths from node 0 to node `n - 1` in the graph. You need to find a **boolean** array `answer` where `answer[i]` is `true` if the edge `edges[i]` is part of **at least** one shortest path. Otherwise, `answer[i]` is `false`.

Return the array `answer`.

**Note** that the graph may not be connected.
