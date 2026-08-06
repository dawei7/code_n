## Description

You are given an integer `n` and an undirected graph with `n` nodes labeled from 0 to `n - 1`. This is represented by a 2D array `edges`, where `edges[i] = [u_i, v_i, time_i]` indicates an undirected edge between nodes `u_i` and `v_i` that can be removed at `time_i`.

You are also given an integer `k`.

Initially, the graph may be connected or disconnected. Your task is to find the **minimum** time `t` such that after removing all edges with `time <= t`, the graph contains **at least** `k` connected components.

Return the **minimum** time `t`.

A **connected component** is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
