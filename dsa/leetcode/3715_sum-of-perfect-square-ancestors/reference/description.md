## Description

You are given an integer `n` and an undirected tree rooted at node `0`. Its nodes are numbered from `0` through `n - 1`, and `edges[i] = [u_i, v_i]` describes one undirected tree edge.

You are also given `nums`, where the positive integer `nums[i]` is assigned to node `i`.

For each node $i$, let $t_i$ be the number of its ancestors whose assigned value has a perfect-square product with `nums[i]`.

Return the sum of $t_i$ over all non-root nodes $i$ from `1` through `n - 1`.
