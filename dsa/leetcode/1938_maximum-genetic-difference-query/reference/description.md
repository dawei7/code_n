## Description

There is a rooted tree consisting of `n` nodes numbered `0` to `n - 1`. Each node's number denotes its **unique genetic value** (i.e. the genetic value of node `x` is `x`). The **genetic difference** between two genetic values is defined as the **bitwise-****XOR** of their values. You are given the integer array `parents`, where `parents[i]` is the parent for node `i`. If node `x` is the **root** of the tree, then `parents[x] == -1`.

You are also given the array `queries` where `queries[i] = [node_i, val_i]`. For each query `i`, find the **maximum genetic difference** between `val_i` and `p_i`, where `p_i` is the genetic value of any node that is on the path between `node_i` and the root (including `node_i` and the root). More formally, you want to maximize `val_i XOR p_i`.

Return *an array *`ans`* where *`ans[i]`* is the answer to the *`i^th`* query*.
