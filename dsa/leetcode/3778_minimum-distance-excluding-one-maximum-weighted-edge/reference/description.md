## Description

You are given a positive integer `n` and an edge list describing a weighted, connected, simple undirected graph. Its nodes are labeled from `0` through `n - 1`, and every entry `[u_i, v_i, w_i]` represents a positive-weight edge between `u_i` and `v_i`.

For any path, add its edge weights but omit the edge having the maximum weight. When that maximum occurs more than once along the path, only its first occurrence is omitted; every other edge, including later edges with the same weight, remains in the sum.

Return the minimum possible cost among paths from node `0` to node `n - 1`.
