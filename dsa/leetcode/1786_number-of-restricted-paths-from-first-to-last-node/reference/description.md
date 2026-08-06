## Description

There is an undirected weighted connected graph. You are given a positive integer `n` which denotes that the graph has `n` nodes labeled from `1` to `n`, and an array `edges` where each `edges[i] = [u_i, v_i, weight_i]` denotes that there is an edge between nodes `u_i` and `v_i` with weight equal to `weight_i`.

A path from node `start` to node `end` is a sequence of nodes `[z_0, z_1,_ z_2, ..., z_k]` such that `z_0 = start` and `z_k = end` and there is an edge between `z_i` and `z_i+1` where `0 <= i <= k-1`.

The distance of a path is the sum of the weights on the edges of the path. Let `distanceToLastNode(x)` denote the shortest distance of a path between node `n` and node `x`. A **restricted path** is a path that also satisfies that `distanceToLastNode(z_i) > distanceToLastNode(z_i+1)` where `0 <= i <= k-1`.

Return *the number of restricted paths from node* `1` *to node* `n`. Since that number may be too large, return it **modulo** `10^9 + 7`.
