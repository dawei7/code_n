## Description

You are given an undirected graph with $n$ nodes labeled from `0` through `n - 1`. Each entry `edges[i] = [u_i, v_i, w_i]` represents an edge joining `u_i` and `v_i`, with repair cost `w_i`. Initially, every edge is damaged.

Choose a nonnegative integer `money`. This repairs every edge whose cost is at most `money`; edges with larger costs stay damaged and cannot be traversed.

The repaired graph must contain a route from node `0` to node `n - 1` that uses at most `k` edges. Return the smallest possible value of `money`, or return `-1` when no amount can make such a route possible.
