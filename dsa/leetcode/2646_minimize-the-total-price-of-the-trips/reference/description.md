## Description

There exists an undirected and unrooted tree with `n` nodes indexed from `0` to `n - 1`. You are given the integer `n` and a 2D integer array `edges` of length `n - 1`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

Each node has an associated price. You are given an integer array `price`, where `price[i]` is the price of the `i^th` node.

The **price sum** of a given path is the sum of the prices of all nodes lying on that path.

Additionally, you are given a 2D integer array `trips`, where `trips[i] = [start_i, end_i]` indicates that you start the `i^th` trip from the node `start_i` and travel to the node `end_i` by any path you like.

Before performing your first trip, you can choose some **non-adjacent** nodes and halve the prices.

Return *the minimum total price sum to perform all the given trips*.
