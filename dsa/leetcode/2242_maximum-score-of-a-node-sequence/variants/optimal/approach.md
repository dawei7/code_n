## General

**Every four-node path has a middle edge**

A valid sequence of length four can be written `c - a - b - d`. Its three required edges are `(c, a)`, `(a, b)`, and `(b, d)`. Therefore, every valid sequence has some graph edge `(a, b)` as its middle pair, plus one outside neighbor of `a` and one outside neighbor of `b`.

The solution iterates every input edge as that middle pair. For each, it tries candidate neighbors `c` of `a` and `d` of `b`, checks that the four nodes are distinct, and evaluates their score sum.

**Build undirected adjacency**

For every edge `[a, b]`, the code appends `b` to `g[a]` and `a` to `g[b]`. This symmetric insertion reflects the undirected graph. A node absent from `g` has no edges and cannot participate in a four-node sequence.

**Keep only three highest-scoring neighbors per node**

Trying every pair from full adjacency lists could be quadratic in high degrees. The solution replaces each list with

`nlargest(3, g[k], key=lambda x: scores[x])`.

This retains up to three neighbors with the highest node scores.

Why are three enough? For endpoint `a` of middle edge `(a, b)`, outside node `c` cannot be `b` and cannot equal the chosen `d`. Those are at most two forbidden candidates among `a`'s neighbors. Among the top three, at least one candidate remains whenever any valid outside neighbor exists. Replacing a lower-scoring valid neighbor with that remaining top-three candidate cannot reduce the total.

The same reasoning applies to `d` at endpoint `b`, excluding `a` and `c`. Hence, an optimal sequence exists whose two outside nodes both belong to the retained top-three lists.

**Enumerate constant-size combinations**

For each edge `a, b`, the nested loops inspect at most three choices for `c` and three for `d`, at most nine pairs. A valid pair contributes

`scores[a] + scores[b] + scores[c] + scores[d]`.

`ans` begins at `-1`, the required sentinel if no length-four sequence exists. Scores are positive, so every valid sequence has a score above `-1` and updates it.

**Understand the exact distinctness check**

The code uses:

`if b != c != d != a`.

Python chained inequality means `b != c and c != d and d != a`. Other required inequalities follow from graph structure:

- `a != b` because input edges have distinct endpoints;
- `c != a` because `c` is a neighbor of `a` and there are no self-edges;
- `d != b` because `d` is a neighbor of `b` and there are no self-edges.

Together with the three explicit comparisons, all six pairwise collisions that could matter are excluded. In particular, `c` cannot be the middle node `b`, `d` cannot be middle node `a`, and the outside nodes cannot equal each other.

**Why every evaluated candidate is valid**

`c` comes from `g[a]`, so edge `c-a` exists. `a-b` is the current input edge. `d` comes from `g[b]`, so edge `b-d` exists. The distinctness condition makes all nodes unique. Thus, every score considered after the condition belongs to a valid four-node sequence.

**Why the optimum is not pruned away**

Start with any optimal sequence `c-a-b-d`. Its middle edge is visited. If `c` is outside `a`'s top three, at most `b` and `d` can invalidate top choices, so another retained neighbor is valid and scores at least as high; replace `c`. Then apply the analogous argument to `d`, excluding `a` and the possibly replaced `c`.

This produces a valid sequence with score no lower and both outside nodes retained. The nested loops examine it. Therefore, pruning cannot reduce the maximum answer.

**Graph direction and sequence reversal**

Because edges are undirected, reversing a valid sequence is also valid and has the same score. The method may encounter equivalent arrangements from different edge orientations or neighbor choices. Duplicate evaluation is harmless because only the maximum is stored.

## Complexity detail

Let `n` be the node count and `m` the edge count. Building adjacency takes `O(n + m)` logical storage and `O(m)` time. Selecting the largest three from a degree-`d` list costs `O(d \log 3) = O(d)`; summed degrees equal `2m`, so pruning takes `O(m)` time.

Each edge checks at most nine neighbor pairs, so final enumeration is `O(m)`. Total time is `O(n + m)`.

The initially built adjacency lists store `O(n + m)` information. They are then replaced by short lists, but peak space remains `O(n + m)`.

## Alternatives and edge cases

- **Try all neighbor pairs:** For each middle edge, combining full degrees can be too expensive in dense local neighborhoods.
- **Keep only the single best neighbor:** It may be the opposite middle endpoint or collide with the other outside node, so one is insufficient.
- **Keep only two neighbors:** Both can be forbidden by the middle endpoint and other outside choice; the third is the necessary fallback.
- **Enumerate all four-node permutations:** This ignores graph structure and is infeasible.
- **No edges:** No sequence exists and `ans` remains `-1`.
- **Path shorter than four distinct nodes:** Every candidate fails availability or distinctness, returning `-1`.
- **Triangle only:** A fourth distinct node is missing, so no valid length-four sequence exists.
- **High-degree hub:** Only its three highest-scoring neighbors are needed for each middle-edge role.
- **Tied scores:** `nlargest` may choose any tied neighbors; the top-three replacement argument still preserves an optimum score.
- **Disconnected graph:** Each component is handled through its own edges; the maximum valid sequence anywhere wins.
- **Undirected insertion:** Both adjacency directions are required.
- **Positive scores:** Any valid candidate exceeds the `-1` sentinel.
- **Chained inequality:** Its correctness also relies on no self-edges and distinct middle-edge endpoints supplied by the contract.
