## Description

There is a **simple directed graph** with `n` nodes labeled from `0` to `n - 1`. The graph would form a **tree** if its edges were bi-directional.

You are given an integer `n` and a **2D** integer array `edges`, where `edges[i] = [u_i, v_i]` represents a **directed edge** going from node `u_i` to node `v_i`.

An **edge reversal** changes the direction of an edge, i.e., a directed edge going from node `u_i` to node `v_i` becomes a directed edge going from node `v_i` to node `u_i`.

For every node `i` in the range `[0, n - 1]`, your task is to **independently** calculate the **minimum** number of **edge reversals** required so it is possible to reach any other node starting from node `i` through a **sequence** of **directed edges**.

Return *an integer array *`answer`*, where *`answer[i]`* is the** * ***minimum** number of **edge reversals** required so it is possible to reach any other node starting from node *`i`* through a **sequence** of **directed edges**.*
