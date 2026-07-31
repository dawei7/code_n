## Description

A tree is an undirected graph in which exactly one path connects every pair of vertices; equivalently, it is connected and has no simple cycle.

You receive such a tree with `n` nodes labeled from `0` through `n - 1` and exactly `n - 1` undirected edges. Any node may be selected as the root. Rooting the tree at node `x` gives it a height $h$, defined as the number of edges on the longest downward path from that root to a leaf.

A minimum height tree (MHT) is a rooting whose height is the smallest possible over all root choices. Return the labels of every MHT root in any order.
