## General

**Dynamic programming by ending value**

When processing a value `v` from left to right, define its best subsequence length as one plus the best earlier subsequence whose final value `p` satisfies:

$$
v-k\le p\le v-1.
$$

The upper bound `v-1` enforces strict increase. The lower bound ensures the adjacent difference is at most `k`.

Only the best length for each possible ending value matters. A segment tree stores these lengths and can return the maximum across the allowed predecessor-value interval.

**Why processing order preserves subsequence order**

The loop reads `nums` from left to right. Before value `v` is queried, the tree contains information only from earlier indices. Any predecessor chosen from it therefore respects original index order.

After computing the best length ending at the current index, the tree is updated at coordinate `v` for use by later elements.

**Segment-tree contents**

The tree covers value coordinates `1` through `max(nums)`. A leaf at coordinate `x` stores the best ideal increasing-subsequence length seen so far that ends with value `x`.

Every internal node stores the maximum of its two children. Consequently, a range query can combine $O(\log M)$ covered nodes to find the best predecessor length, where $M=\max(\texttt{nums})$.

`build` explicitly records every node's left and right coordinate boundaries. `pushup` restores the maximum after a leaf modification.

**Query the exact legal predecessor range**

For current `v`, the source calls:

```python
tree.query(1, v - k, v - 1)
```

Values smaller than `v-k` would create too large a jump. Value `v` itself is excluded because the subsequence must be strictly increasing, so repeated equal values cannot directly extend one another.

If no earlier value lies in the interval, the query returns zero and `t = 1`, representing the singleton subsequence containing only `v`.

When `v-k < 1`, the requested lower boundary extends below the built domain. The recursive containment logic effectively considers only actual tree coordinates. For `v = 1`, the upper boundary is zero, an empty legal predecessor range; the exact tree's zero-initialized unused nodes cause the query to return zero. A production implementation would more explicitly clamp the left boundary to one and handle an empty interval before querying.

**Update the current ending value**

The code sets:

```python
t = best_predecessor + 1
tree.modify(1, v, t)
```

`modify` overwrites the leaf rather than taking a maximum there. This is safe even when value `v` appears repeatedly. A later occurrence sees every predecessor available to an earlier occurrence plus possibly more processed values. Since equal `v` is not itself in the query range, the best legal predecessor maximum cannot decrease. Therefore, the newly computed `t` is at least the previous stored length for value `v`.

`ans` tracks the largest `t` across processed indices.

**Trace the difference restriction**

For current value eight with `k = 3`, legal predecessors lie in `[5,7]`. A best subsequence ending at four cannot extend directly to eight because the gap is four, even if four is numerically smaller.

The range maximum selects the best length among all ending values five, six, and seven without scanning them individually.

**Why the recurrence is correct**

Any valid subsequence ending at current value `v` is either the singleton or has a previous selected value `p` in the legal interval. Removing `v` leaves a valid subsequence represented by the tree's stored state at `p`. Thus, no candidate can exceed one plus the queried maximum.

Conversely, appending `v` to the subsequence that realizes the queried maximum preserves index order, strict increase, and the gap bound. The computed length is achievable.

Induction over input positions proves every update is exact. The maximum update then returns the longest valid subsequence ending anywhere.

**Why ordinary LIS tails are insufficient**

Classic patience-sorting LIS tracks the smallest tail for each length. The added maximum-gap constraint makes predecessor feasibility depend on a value interval, not merely being smaller. The segment tree supports precisely that interval maximum.

## Complexity detail

Let $n$ be input length and $M=\max(\texttt{nums})$. Explicitly building the tree takes $O(M)$ time and allocates $O(M)$ nodes.

Each of $n$ values performs one range query and one point modification, each $O(\log M)$. Exact total time is:

$$
O(M+n\log M).
$$

The manifest's $O(n\log M)$ omits the explicit build term, which may be absorbed only when $M=O(n)$ or when using a lazily built tree. Exact space is $O(M)$ for roughly four times $M$ nodes. Recursion depth per operation is $O(\log M)$.

## Alternatives and edge cases

- **Fenwick tree with transformed queries:** A standard Fenwick tree gives prefix maxima, not arbitrary interval maxima; additional techniques or a segment tree are needed for `[v-k,v-1]`.
- **Coordinate-compressed segment tree:** Compress occurring values and binary-search range endpoints. This reduces space when $M$ is much larger than the number of distinct values.
- **Quadratic DP:** Check every earlier index for each current value. It is simple but costs $O(n^2)$.
- **Repeated value:** It cannot precede itself under strict increase, but later best state for that value safely overwrites an earlier no-larger state.
- **`v = 1`:** No smaller positive predecessor exists, so the best length is one.
- **`k` larger than `v`:** The effective lower bound is the tree's minimum coordinate one.
- **No legal predecessor:** Zero query result produces a singleton.
- **Increasing gap too large:** The lower range bound excludes that predecessor.
- **Input order:** Tree updates occur only after querying the current item, preserving subsequence index order.
