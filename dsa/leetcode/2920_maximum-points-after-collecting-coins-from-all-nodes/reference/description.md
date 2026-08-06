## Description

There exists an undirected tree rooted at node `0` with `n` nodes labeled from `0` to `n - 1`. You are given a 2D **integer** array `edges` of length `n - 1`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree. You are also given a **0-indexed** array `coins` of size `n` where `coins[i]` indicates the number of coins in the vertex `i`, and an integer `k`.

Starting from the root, you have to collect all the coins such that the coins at a node can only be collected if the coins of its ancestors have been already collected.

Coins at `node_i` can be collected in one of the following ways:

<ul>
	<li>Collect all the coins, but you will get `coins[i] - k` points. If `coins[i] - k` is negative then you will lose `abs(coins[i] - k)` points.</li>
	<li>Collect all the coins, but you will get `floor(coins[i] / 2)` points. If this way is used, then for all the `node_j` present in the subtree of `node_i`, `coins[j]` will get reduced to `floor(coins[j] / 2)`.</li>
</ul>

Return *the **maximum points** you can get after collecting the coins from **all** the tree nodes.*
