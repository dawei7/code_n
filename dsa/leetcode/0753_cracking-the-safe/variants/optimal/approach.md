## General

**The output must contain every possible password as a window**

There are `k^n` possible passwords of length `n`. A typed string unlocks the safe for every possible password only if each of those strings occurs somewhere as a consecutive length-`n` window.

Writing every password separately would use `n * k^n` characters. The goal is to overlap passwords as much as possible. If one password’s final `n - 1` digits equal another password’s first `n - 1` digits, the second needs only one new typed digit.

This is exactly the structure of a de Bruijn sequence.

**Build an implicit directed graph**

Treat every length-`n - 1` digit sequence as a graph node. A length-`n` password is an edge:

- Its first `n - 1` digits identify the source node.
- Its final `n - 1` digits identify the destination node.
- Its final digit is the edge label appended while moving.

For each node, appending any digit from zero through `k - 1` creates one outgoing edge. Every password corresponds to exactly one such edge.

**Encode nodes and edges as integers**

The solution represents the current `n - 1` digits as integer `u`. Appending digit `x` creates

`e = u * 10 + x`.

Because `k <= 10`, every symbol is one decimal digit. The edge integer uniquely represents the full length-`n` sequence, including conceptual leading zeroes within the fixed-width context.

The next node is

`v = e % 10^(n - 1)`,

which discards the oldest digit and retains the newest `n - 1` digits. For `n = 1`, the modulus is one and the only node is zero.

**Traverse every password edge once**

`vis` stores edge encodings already used. DFS at node `u` tries every possible appended digit. An unused edge is marked before recursion, then traversal continues at its suffix node.

This graph has equal indegree and outdegree `k` at every node and is connected in the relevant directed sense. It therefore has an Eulerian circuit: a closed walk that uses every edge exactly once.

Using every edge once is equivalent to including every length-`n` password once.

**Why digits are appended after recursion**

The method follows Hierholzer’s Eulerian-tour construction. It explores an unused edge recursively and appends that edge’s digit only while backtracking.

Postorder appending splices cycles correctly. If a node has several outgoing edges, recursion completely consumes the continuation before recording the edge that entered it. The resulting list of edge labels is an Eulerian circuit ordering.

Appending during the forward descent would record a greedy walk before nested cycles were spliced and would not generally yield the correct complete ordering.

**Linearize the cycle**

An Eulerian circuit’s edge labels form a cyclic de Bruijn sequence. To make every cyclic length-`n` window visible in an ordinary linear string, the solution appends `n - 1` zeroes, corresponding to the starting node.

The final length is

`k^n + n - 1`.

A string of length `L` has at most `L - n + 1` length-`n` windows. Since at least `k^n` distinct windows are required, no valid string can be shorter than `k^n + n - 1`. The constructed result reaches this lower bound and is therefore minimum length.

**Why leading zeroes are not lost**

Integer encodings omit written leading zeroes, but node and edge widths are known from `n`. State zero represents the all-zero suffix, and appending digit zero still creates the correct fixed-width edge. Membership and modulus calculations distinguish edges by their full transition context, not by formatting a password integer as text.


Each possible length-`n` password corresponds bijectively to one graph edge. DFS marks and traverses every reachable edge exactly once, and the de Bruijn graph’s structure makes all edges part of one Eulerian circuit. Hierholzer postorder produces that circuit’s labels.

Adding the starting node’s `n - 1` zeroes linearizes the circuit, so every edge appears as one length-`n` window. The lower-bound argument proves the length is minimal.

## Complexity detail

There are `E = k^n` edges. The visited set and output contain `O(E)` items, and recursion can also be linear in `E`, so space is `O(k^n)`.

The exact DFS is invoked once per traversed edge, and each invocation loops over all `k` candidate digits. A literal bound is `O(kE) = O(k^(n + 1))` candidate checks. Since `k <= 10` is a small bounded alphabet, this is commonly reported as `O(k^n)` time, proportional to the unavoidable output size.

An implementation that maintains a per-node next-edge iterator can make the edge-processing bound explicitly `O(k^n)` even when `k` is treated as a variable.

## Alternatives and edge cases

- **Concatenate every password:** It is easy but produces `n * k^n` characters rather than the minimum.

- **Backtracking over output strings:** Searching arrangements directly creates enormous repeated work. Eulerian structure gives a constructive solution.

- **Append labels before recursion:** This loses Hierholzer’s cycle-splicing guarantee. Edge labels belong in postorder.

- **Per-node edge cursor:** Avoid retesting already used outgoing edges on repeated node visits and gives a strict linear-in-edges traversal.

- **`n = 1`:** There is one graph node and one edge per digit; the result contains every digit exactly once in some order.

- **`k = 1`:** The only password is all zeroes, and the output is exactly `n` zeroes.

- **Leading-zero passwords:** Fixed-width graph states include them even though node integers do not display leading zeroes.

- **Minimum length:** The number-of-windows lower bound is essential; merely containing all passwords does not by itself prove optimal length.
