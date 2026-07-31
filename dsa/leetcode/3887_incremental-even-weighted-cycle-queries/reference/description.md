## Description

An undirected graph has $n$ vertices labelled from $0$ through $n-1$ and initially contains no edges. A sequence `edges` supplies distinct weighted edges in a fixed order. Each entry `[u, v, w]` connects two different vertices and has binary weight $w \in \{0,1\}$.

Process the sequence from left to right. A proposed edge is retained only when, after retaining it, every cycle in the current graph has an even total edge weight. A rejected edge does not change the graph, and later proposals are evaluated against only the edges retained so far.

Return the total number of proposals that are successfully added.
