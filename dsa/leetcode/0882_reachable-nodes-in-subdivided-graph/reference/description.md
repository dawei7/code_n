## Description

You are given an undirected graph (the **"original graph"**) with `n` nodes labeled from `0` to `n - 1`. You decide to **subdivide** each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The graph is given as a 2D array of `edges` where `edges[i] = [u_i, v_i, cnt_i]` indicates that there is an edge between nodes `u_i` and `v_i` in the original graph, and `cnt_i` is the total number of new nodes that you will **subdivide** the edge into. Note that `cnt_i == 0` means you will not subdivide the edge.

To **subdivide** the edge `[u_i, v_i]`, replace it with `(cnt_i + 1)` new edges and `cnt_i` new nodes. The new nodes are `x_1`, `x_2`, ..., `x_cnt<sub>i</sub>`, and the new edges are `[u_i, x_1]`, `[x_1, x_2]`, `[x_2, x_3]`, ..., `[x_cnt<sub>i-1</sub>, x_cnt<sub>i</sub>]`, `[x_cnt<sub>i</sub>, v_i]`.

In this **new graph**, you want to know how many nodes are **reachable** from the node `0`, where a node is **reachable** if the distance is `maxMoves` or less.

Given the original graph and `maxMoves`, return *the number of nodes that are **reachable** from node *`0`* in the new graph*.
