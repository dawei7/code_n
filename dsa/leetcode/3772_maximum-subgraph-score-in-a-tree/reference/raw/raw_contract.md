## Function Contract

**Inputs**

- `n`: The number of nodes, labeled from `0` through `n - 1`.
- `edges`: The undirected edges of a valid tree.
- `good`: A binary classification for each node, where `1` means good and `0` means bad.

Assign weight $+1$ to every good node and $-1$ to every bad node. The score of a selected connected subgraph is the sum of its node weights.

**Return value**

Return `answer`, where `answer[i]` is the maximum weight sum of any connected subgraph containing node `i`. Different nodes may attain their maxima with different subgraphs, and the maximizing subgraph need not be unique.
