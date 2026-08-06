## Description

A connected, undirected, weighted graph has $n$ nodes numbered from $0$ through $n-1$. Each entry `[u, v, w]` in `edges` represents one edge between $u$ and $v$ whose positive weight is $w$. The graph contains neither self-loops nor repeated edges.

Given distinct source and destination nodes `s` and `d`, a path may use a special hop operation on at most $k$ of its traversed edges. Hopping over an edge makes that traversal contribute zero instead of its stored weight. Return the minimum possible total weight of a path from `s` to `d`; fewer than $k$ hops may be used.
