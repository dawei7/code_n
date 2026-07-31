## Description

A directed, weighted graph has `n` nodes numbered from `0` through `n - 1`. Each entry `[u, v, w]` in `edges` gives a directed edge from `u` to `v` with positive weight `w`. The string `labels` assigns the character `labels[i]` to node `i`.

Reading the labels of the nodes along a route produces a string that includes both its starting and ending nodes. A route is valid only when no run in that string contains more than `k` consecutive copies of the same character. In particular, the label of node `0` begins the first run, and taking an edge to a node with a different label resets the run length to one.

Find the minimum sum of edge weights among all valid routes from node `0` to node `n - 1`. Return `-1` when the destination cannot be reached without violating the consecutive-label limit.
