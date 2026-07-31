## Description

You are given an undirected tree containing `n` nodes numbered from `0` through `n - 1`. The array `edges` has length `n - 1`; entry `edges[i] = [a_i, b_i]` is the edge with index `i` and joins nodes `a_i` and `b_i`.

Two binary strings of length `n` describe the node colors. Character `start[x]` is node `x`'s initial color, while `target[x]` is the color that node must have after all operations.

In one operation, choose an edge index `i`. If `edges[i] = [u, v]`, toggle both endpoints: the colors of `u` and `v` each change from `'0'` to `'1'` or from `'1'` to `'0'`.

Return edge indices whose operations transform `start` into `target`. The sequence must use the minimum possible number of operations, and its edge indices must be returned in increasing order.

If the transformation cannot be performed, return `[-1]`.
