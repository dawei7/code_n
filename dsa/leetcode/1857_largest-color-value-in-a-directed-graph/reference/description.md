## Description

There is a **directed graph** of `n` colored nodes and `m` edges. The nodes are numbered from `0` to `n - 1`.

You are given a string `colors` where `colors[i]` is a lowercase English letter representing the **color** of the `i^th` node in this graph (**0-indexed**). You are also given a 2D array `edges` where `edges[j] = [a_j, b_j]` indicates that there is a **directed edge** from node `a_j` to node `b_j`.

A valid **path** in the graph is a sequence of nodes `x_1 -> x_2 -> x_3 -> ... -> x_k` such that there is a directed edge from `x_i` to `x_i+1` for every `1 <= i < k`. The **color value** of the path is the number of nodes that are colored the **most frequently** occurring color along that path.

Return *the **largest color value** of any valid path in the given graph, or *`-1`* if the graph contains a cycle*.
