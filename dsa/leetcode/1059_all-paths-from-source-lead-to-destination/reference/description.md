## Description

An array `edges` describes a directed graph with `n` labeled nodes. Each entry `[a_i, b_i]` represents an edge directed from node `a_i` to node `b_i`. Two nodes are distinguished: every path under consideration starts at `source`, and every such path must eventually stop at `destination`.

The requirement has three parts:

- At least one path must exist from `source` to `destination`.
- Whenever a path from `source` reaches a node with no outgoing edges, that terminal node must be `destination`.
- There must be only finitely many possible paths from `source` to `destination`.

Consequently, a reachable dead end other than `destination` invalidates the graph, as does any cycle reachable from `source`: a path could remain in that cycle forever. The `destination` node itself must have no outgoing edges because a path is required to end when it reaches that node.

Return `true` if and only if all paths that begin at `source` satisfy these conditions and lead to `destination`.
