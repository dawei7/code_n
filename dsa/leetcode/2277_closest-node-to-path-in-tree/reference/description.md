## Description

You are given a tree with `n` nodes numbered from 0 through `n - 1`. Each pair `[u, v]` in `edges` is a bidirectional connection. Because the graph is a tree, exactly one simple path connects any two nodes.

Every query has the form `[start, end, node]`. Consider all vertices on the unique path from `start` to `end`, including both endpoints. Find the vertex on that path whose tree distance from `node` is smallest.

Return one selected vertex for every query in the original query order. The closest vertex is the unique projection of `node` onto the specified tree path.
