## Description

An undirected weighted graph has `n` nodes numbered from `0` through `n - 1`. Each edge joins two nodes and has a positive integer weight. For an integer threshold $T$, an edge is **light** when its weight is at most $T$ and **heavy** when its weight is greater than $T$.

A path from `source` to `target` is valid when it traverses at most `k` heavy edges; there is no separate limit on how many light edges it may use. Find the smallest integer threshold for which at least one valid path exists. Return `-1` when the two endpoints cannot be joined by any path, even after every graph edge is classified as light.
