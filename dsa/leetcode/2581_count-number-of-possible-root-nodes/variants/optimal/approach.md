## General

Choosing a root orients every tree edge from parent to child. A guess `[u, v]` is true exactly when that rooted orientation directs the edge from `u` to `v`.

**Score one reference root:** Root the tree temporarily at node `0`. Build a parent array and a parent-before-child traversal order iteratively, avoiding recursion depth limits on a chain of $10^5$ nodes. A guess `(parent[node], node)` is true under this root, so scanning the non-root nodes gives the initial correct-guess count.

**Move the root across one edge:** Suppose the root moves from a node `u` to its child `v` in the reference orientation. Only the edge between `u` and `v` reverses; every other edge keeps the same parent-child direction. Consequently,

$$
\operatorname{score}(v)
= \operatorname{score}(u)
- [\,(u,v) \text{ is guessed}\,]
+ [\,(v,u) \text{ is guessed}\,].
$$

Store directed guesses in a hash set so both indicator checks are constant-time on average. Process nodes in the previously built parent-before-child order, derive each score from its parent's score, and count scores at least `k`.

The reference score is counted directly. For every reroot transition, the formula changes exactly the one edge whose orientation changes, preserving the correct score for the new root. Induction along the traversal order therefore establishes the score for every possible root, so the final threshold count is exact.

## Complexity detail

Let $n$ be the node count and $g$ the number of guesses. Building the graph and guess set, orienting the tree once, counting the reference score, and rerooting all take $O(n+g)$ expected time. The adjacency list, hash set, parent order, and score array use $O(n+g)$ space. Expected bounds assume standard constant-time hash-set operations.

## Alternatives and edge cases

- **Recompute from every root:** Rooting the tree separately at all $n$ nodes is correct but takes $O(n(n+g))$ time instead of reusing neighboring scores.
- **Recursive depth-first search:** The same reroot recurrence works recursively, but a legal chain can exceed Python's recursion limit; an explicit order is safer.
- **Zero threshold:** When `k = 0`, every one of the $n$ nodes is a valid root regardless of the guesses.
- **Opposite guesses on one edge:** Both directions may appear as distinct guesses, but exactly one can be true for any chosen root.
- **No qualifying root:** If every rerooted score is below `k`, the accumulated answer remains `0`.
