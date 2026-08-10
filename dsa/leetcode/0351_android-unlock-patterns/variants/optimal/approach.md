## General

An unlock pattern is an ordered sequence, so `[1, 2]` and `[2, 1]` are different. Every selected dot must also be distinct. The remaining rule is geometric: moving directly from one dot to another is forbidden only when the segment passes through the center of a third grid dot that has not already been selected. The exact solution enumerates all valid sequences with backtracking, but it avoids repeating equivalent work for rotationally or reflectively symmetric starting positions.

Number the grid in the usual row-major arrangement:

```text
1 2 3
4 5 6
7 8 9
```

**Representing the jump rule.**

The `cross` matrix answers one question for an attempted move from dot `i` to dot `j`: which dot, if any, lies exactly at the segment's midpoint? A zero means that the move does not pass through the center of another dot and therefore has no prerequisite. A nonzero value gives the dot that must already be visited.

Only the following undirected pairs have a grid dot exactly between their endpoints:

- `1` and `3` require `2`.
- `1` and `7` require `4`.
- `1` and `9` require `5`.
- `2` and `8` require `5`.
- `3` and `7` require `5`.
- `3` and `9` require `6`.
- `4` and `6` require `5`.
- `7` and `9` require `8`.

Every assignment is made in both directions because the same midpoint is crossed whether the segment is traversed forward or backward. For example, both `cross[1][3]` and `cross[3][1]` equal `2`.

Moves such as `2` to `9` receive zero. Although their segment may pass visually near other dots, it does not go through another dot's center, so it is legal without a prerequisite. This distinction is why a table of exact midpoint relationships is safer than trying to ban every long-looking segment.

**What the recursive state means.**

`dfs(i, cnt)` counts every valid pattern whose current last dot is `i`, whose current length is `cnt`, and whose earlier selected dots are represented by the shared `vis` array. On entry from a real parent call, the parent and all earlier dots are already marked, while `i` itself is not yet marked. The function marks `i` before exploring continuations and unmarks it before returning.

If `cnt > n`, the pattern is already too long, so the function returns zero immediately. Otherwise, the current prefix itself contributes one pattern exactly when `cnt >= m`. This is expressed by `int(cnt >= m)`: `True` converts to `1`, and `False` converts to `0`. The recursion does not wait until no moves remain because every valid prefix whose length lies in the inclusive range `[m, n]` is independently a valid answer.

**Choosing the next dot.**

The loop considers every label `j` from `1` through `9`. Two conditions decide whether it may follow `i`:

1. `not vis[j]` enforces the distinct-dot rule. A dot already selected in the current path cannot be selected again.
2. Let `x = cross[i][j]`. The move is geometrically legal when `x == 0`, meaning there is no midpoint dot, or when `vis[x]` is true, meaning the required midpoint appeared earlier in the sequence.

When both conditions hold, `dfs(j, cnt + 1)` counts every valid continuation using that next dot, and its result is added to the current total. Different choices of `j` produce different next sequence elements, so their resulting pattern sets cannot overlap.

Notice that the midpoint need only have appeared earlier; it does not have to be the immediately previous dot. For pattern `[2, 4, 1, 3]`, the final move from `1` to `3` is legal because `2` was selected at the beginning and remains marked in `vis`.

**Why backtracking is necessary.**

The `vis` array describes one recursion path, not every path explored so far. Before entering a child, the current dot is marked so the child cannot reuse it and may use it as a satisfied midpoint. After all children are counted, `vis[i] = False` restores the state that existed before this call. Without that restoration, dots used in one branch would incorrectly remain unavailable in its siblings.

For instance, after exploring patterns beginning `1, 2, ...`, the algorithm must be able to explore `1, 4, ...` with `2` initially unvisited. Backtracking supplies exactly that clean sibling state while retaining `1`, which is still marked by the caller until all of its branches finish.

**Counting only three starting positions.**

The square grid's rotations and reflections preserve adjacency, midpoint relationships, sequence length, and the visited/unvisited rule. The four corners `1`, `3`, `7`, and `9` are symmetric, so the number of valid patterns beginning at any one corner is identical. The four non-corner edge dots `2`, `4`, `6`, and `8` form another symmetric group. The center `5` is alone.

Consequently, the source computes `dfs(1) * 4` for all corner starts, `dfs(2) * 4` for all edge starts, and `dfs(5)` for the center. The visited array is empty again after each top-level call because every recursive invocation unmarks its own current dot. Multiplication does not merge patterns: it accounts for the four distinct rotated or reflected starting labels in each group.

**Why every valid pattern is counted exactly once.**

Every recursive path records one ordered sequence of distinct dots. The move filter accepts precisely the transitions allowed by the midpoint rule, so every counted prefix is valid. Conversely, take any valid pattern. Its first dot belongs to exactly one of the corner, edge, or center symmetry groups. Starting from the representative of that group, the corresponding rotated or reflected sequence follows allowed recursive choices at every position. It is included in the representative count and recovered by the group's multiplier.

Within a fixed start, a sequence corresponds to exactly one chain of next-dot choices, so it cannot be counted twice. Different lengths along that chain are legitimately different patterns and are counted separately when they lie in `[m, n]`. Thus the sum includes all and only the required unique patterns.

**The exact implementation is not the manifest's state dynamic program.**

The manifest describes propagating or storing counts for `(visited-mask, current-key)` states with $O(K^2 2^K)$ time and $O(K2^K)$ space. The checked-in `solution.py` has no bitmask and no memoization table. It explores valid ordered prefixes directly with a mutable Boolean visited array. Symmetry reduces the number of root searches, but equivalent subproblems reached through different orders are still recomputed. The algorithm and complexity must therefore be documented as backtracking, not as subset dynamic programming.

## Complexity detail

Let $K=9$ be the number of dots and let $N=n$ be the maximum requested pattern length. At a recursive state, the source loops over all $K$ possible next labels. The number of length-$\ell$ ordered sequences without repetition is at most

$$
P(K,\ell)=\frac{K!}{(K-\ell)!}.
$$

The geometry rule prunes many such sequences, and symmetry replaces nine root calls with three representative calls, but those improvements do not change a general upper-bound class. A precise useful upper bound for direct enumeration is

$$
O\!\left(K\sum_{\ell=1}^{N}P(K,\ell)\right),
$$

because each explored prefix scans $K$ candidate next dots. When $N=K$, this is $O(K\cdot K!)$ as a simple bound. One may also state the looser branching bound $O(K^{N+1})$. On the actual fixed $3\times3$ grid, $K$ is always `9` and $N\le9$, so the complete search is bounded by a fixed finite amount, but direct enumeration remains the meaningful description of the work.

This differs from the manifest's $O(K^2 2^K)$ bound, which would apply to a bitmask dynamic program that processes each `(mask, last)` state once and tries $K$ transitions. The source does not perform that caching.

The `cross` matrix contains $(K+1)^2$ entries, giving $O(K^2)$ storage in a generalized analysis. The visited array uses $O(K)$ space. Recursion depth is at most $N+1$ because calls beyond length $N$ return immediately, so the stack uses $O(N)$ space. Total auxiliary space is therefore $O(K^2+N)$, which is constant for the fixed nine-dot board. Again, it is not the manifest's $O(K2^K)$ state-table space because no such table exists.

## Alternatives and edge cases

- **Bitmask memoization:** Represent visited dots by a $K$-bit integer and cache the count for each `(mask, last)` state. This avoids recomputing continuations reached by different visit orders and gives the manifest-style $O(K^2 2^K)$ time and $O(K2^K)$ space, but it is not the checked-in solution.

- **Bottom-up subset dynamic programming:** Store how many valid sequences end at each dot for every visited mask, then extend them through legal transitions. It has similar state complexity and can sum states whose bit counts lie in `[m, n]`, but is less direct for beginners than backtracking.

- **Search all nine starts:** Calling the same DFS once per starting dot is correct and simpler to justify initially. The exact solution's symmetry factors remove six redundant root searches while producing the same total.

- **Length one:** When `m = n = 1`, each representative start counts itself, so the weighted total is $4+4+1=9$.

- **Maximum length nine:** Every dot must be selected exactly once. The recursion's visited test prevents repetition, while earlier midpoint dots can unlock jumps later in the path.

- **Center as a midpoint:** Moves `1` to `9`, `3` to `7`, `2` to `8`, and `4` to `6` require `5` only if it has not already been selected. Once `5` is visited, all four crossing pairs become legal in either direction.

- **A midpoint may not be selected during the jump:** Passing over an unvisited midpoint does not automatically add it to the pattern. The move is simply forbidden; the user must have selected that dot earlier.

- **Repeated dots remain forbidden:** Even when a dot would satisfy a midpoint condition, it cannot be chosen again as an endpoint because `not vis[j]` is checked separately.

- **Inclusive bounds:** A prefix of length exactly `m` is counted, and one of length exactly `n` is counted. Children at length `n + 1` return zero, preventing overlong patterns.

- **Assumed relation between bounds:** The reference states both values lie from `1` to `9` but does not separately display `m <= n`. The intended problem contract uses a minimum and maximum in that order. If `m > n`, the source naturally returns zero because no visited prefix can satisfy both the counting threshold and depth limit.
