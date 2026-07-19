# Longest Common Subpath

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/longest-common-subpath/) |
| Frontend ID | 1923 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Rolling Hash, Suffix Array, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A country has `n` cities numbered from `0` through `n - 1`, with travel possible between every pair. Each of `m` friends records the cities visited along one path in their exact traversal order. A city may occur more than once in a path, although equal cities never appear consecutively.

A subpath is a contiguous sequence of cities from one recorded path. Find the greatest length of a subpath that occurs, with the same city order, in every friend's path. The occurrence may begin at a different index in each path. Return zero when the paths do not even share a single city.

### Function Contract

**Inputs**

- `n`: the number of cities, with $1 \le n \le 10^5$.
- `paths`: an array of $m$ city sequences, where $2 \le m \le 10^5$.
- Every city is in $[0,n-1]$, and the total number of path entries is at most $10^5$.

Let

$$
T = \sum_{p \in \texttt{paths}} \lvert p \rvert
$$

and let $L$ be the length of the shortest path.

**Return value**

- Return the maximum length of a contiguous city sequence appearing in every path.

### Examples

**Example 1**

- Input: `n = 5, paths = [[0,1,2,3,4], [2,3,4], [4,0,1,2,3]]`
- Output: `2`

The sequence `[2,3]` occurs contiguously in all three paths.

**Example 2**

- Input: `n = 3, paths = [[0], [1], [2]]`
- Output: `0`

No city is shared by every path.

**Example 3**

- Input: `n = 5, paths = [[0,1,2,3,4], [4,3,2,1,0]]`
- Output: `1`

The paths share cities, but no ordered adjacent pair.

### Required Complexity

- **Time:** $O(T \log L)$
- **Space:** $O(T)$

<details>
<summary>Approach</summary>

#### General

**Binary-search a monotone length**

If a sequence of length $k$ occurs in every path, then any contiguous prefix of that sequence proves that length $k-1$ is also feasible. Feasibility is therefore monotone from zero through the answer. Search this interval from zero to the shortest path length $L$.

**Represent every fixed-length window compactly**

For a candidate length $k$, compute a rolling hash for every window of each path. Removing the outgoing city and adding the incoming city updates a window in constant time. Use a pair of independent large prime moduli, so a window is identified by two residues rather than one.

Start with the shortest path's hash set and intersect it with the set from each remaining path. An empty intersection proves that no length-$k$ sequence is common. A surviving pair identifies a candidate present in every path. The accepted implementation uses double hashing, making an accidental equality between distinct windows negligibly unlikely while retaining linear work per feasibility check.

**Why the search returns the optimum**

Every feasible hash pair comes from a length-$k$ window in each path, so the predicate recognizes shared candidates. Conversely, a genuinely common subpath produces identical polynomial hashes in every occurrence and survives every intersection. Binary search keeps the feasible half when the intersection is nonempty and the infeasible half otherwise, finishing at the greatest feasible length.

#### Complexity detail

At one candidate length, rolling through all paths and intersecting their sets costs $O(T)$ expected time and stores at most $O(T)$ hash pairs. Binary search performs $O(\log L)$ feasibility checks, giving $O(T\log L)$ expected time and $O(T)$ space.

#### Alternatives and edge cases

- **Try every length:** Rebuilding fixed-length window sets for all $1$ through $L$ costs $O(TL)$ work.
- **Compare every pair of starts:** Direct element-by-element matching repeats prefixes and can become cubic.
- **Single rolling hash:** It is faster to describe but carries a materially higher collision risk than a modulus pair.
- **Suffix array or suffix automaton:** Deterministic string-index structures can solve the problem but require more involved multi-path ownership and boundary handling.
- **Reversed paths:** Shared city membership does not imply a shared ordered pair.
- **Repeated cities:** Separate occurrences are allowed, and rolling windows naturally preserve their positions and order.
- **No shared city:** The length-zero predicate remains feasible and the answer is zero.
- **Shortest path contained in all others:** The answer is exactly $L$.

</details>
