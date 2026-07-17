# Graph Connectivity With Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1627 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Union-Find, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/graph-connectivity-with-threshold/) |

## Problem Description
### Goal
There are $n$ cities labeled from 1 through $n$. Two distinct cities `x` and `y` have a direct bidirectional road exactly when they share some divisor $z$ that is strictly greater than `threshold`: both `x % z == 0` and `y % z == 0` must hold.

For every pair in `queries`, determine whether its two cities are connected either by one such road or indirectly through a path of roads. Return the answers in query order. Duplicate queries are allowed, and reversing a pair does not change its answer.

### Function Contract
**Inputs**

- `n`: the number of cities, where $2 \le n \le 10^4$.
- `threshold`: the exclusive lower bound for a usable common divisor, where $0 \le \texttt{threshold} \le n$.
- `queries`: an array of $q$ distinct-city pairs, where $1 \le q \le 10^5$ and every city label lies from 1 through $n$.

**Return value**

Return a length-$q$ boolean array whose entry is `true` exactly when the corresponding two cities lie in the same connected component of the road graph.

### Examples
**Example 1**

- Input: `n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]`
- Output: `[false,false,true]`

Only cities 3 and 6 share a divisor greater than 2.

**Example 2**

- Input: `n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]`
- Output: `[true,true,true,true,true]`

Divisor 1 is usable, so all cities belong to one component.

**Example 3**

- Input: `n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]`
- Output: `[false,false,false,false,false]`

Cities 2 and 4 have a road, but none of the queried pairs lies within that component.

### Required Complexity
- **Time:** $O(n\log n+q\alpha(n))$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Generate roads by divisor, not by city pair.** A divisor $d>\texttt{threshold}$ directly connects every pair of its multiples. It is unnecessary to materialize that clique: union `d` with `2d`, `3d`, and every later multiple through $n$. After this star of unions, all multiples of $d$ share one disjoint-set representative and therefore have exactly the connectivity contributed by divisor $d$.

**Accumulate transitive connectivity.** Repeat the multiple sweep for every usable divisor. Union-find naturally merges overlapping divisor groups. For example, with threshold 1, cities 2 and 3 do not directly share a usable divisor, but unions through city 6 place both in one component. Path compression and union by size keep representative operations nearly constant amortized time.

**Answer after preprocessing.** Once every divisor group has been merged, query `[a,b]` is true exactly when `find(a) == find(b)`. The construction adds only valid roads, because both endpoints of each union are divisible by its current divisor. Conversely, every direct road has a witnessing divisor above the threshold, and its endpoints are joined through that divisor's union star. Union-find's transitive closure therefore matches path connectivity in the full road graph.

#### Complexity detail

The divisor sweep performs at most

$$
\sum_{d=1}^{n}\left\lfloor\frac{n}{d}\right\rfloor=O(n\log n)
$$

union attempts; beginning at `threshold + 1` can only reduce this work. Each disjoint-set operation costs amortized $O(\alpha(n))$, which is conventionally absorbed into the sieve term here. The $q$ queries add $O(q\alpha(n))$ time. Parent and size arrays use $O(n)$ space; answers use output space proportional to $q$.

#### Alternatives and edge cases

- **Compare every city pair:** Computing `gcd(x,y)` for all $O(n^2)$ pairs and unioning qualifying pairs is correct but exceeds the required preprocessing bound.
- **Graph traversal per query:** Building explicit roads and searching separately for every query repeats connectivity work and can be prohibitive for $10^5$ queries.
- **Prime-factor grouping:** Factoring labels and merging through factors above the threshold can also derive components, but composite divisors and shared-factor chains make the bookkeeping less direct.
- When `threshold == 0`, divisor 1 connects every city, so every valid query is true.
- When `threshold >= n/2`, no usable divisor has two distinct multiples at most $n$, so every city is isolated.
- City 1 is isolated whenever the threshold is positive.
- Connectivity can be indirect even when the queried endpoints' own greatest common divisor is not above the threshold.

</details>
