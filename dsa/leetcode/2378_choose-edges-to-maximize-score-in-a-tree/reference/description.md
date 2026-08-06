## Description

A weighted tree has nodes numbered from $0$ through $n-1$ and is rooted at node `0`. For every non-root node `i`, `edges[i] = [parent, weight]` describes the edge joining `i` to its parent and that edge's possibly negative weight; `edges[0]` is the sentinel `[-1,-1]`.

Choose a set of edges whose total weight is as large as possible, subject to no two chosen edges sharing a node. Choosing no edges is allowed and has score zero. Return the maximum attainable sum of chosen edge weights.
