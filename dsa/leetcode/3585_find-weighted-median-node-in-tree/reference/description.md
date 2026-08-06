## Description

You are given an integer `n` and an **undirected, weighted** tree rooted at node 0 with `n` nodes numbered from 0 to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i, w_i]` indicates an edge from node `u_i` to `v_i` with weight `w_i`.

The **weighted median node** is defined as the **first** node `x` on the path from `u_i` to `v_i` such that the sum of edge weights from `u_i` to `x` is **greater than or equal to half** of the total path weight.

You are given a 2D integer array `queries`. For each `queries[j] = [u_j, v_j]`, determine the weighted median node along the path from `u_j` to `v_j`.

Return an array `ans`, where `ans[j]` is the node index of the weighted median for `queries[j]`.
