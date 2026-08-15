# Number of Possible Sets of Closing Branches

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2959 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Bit Manipulation, Graph Theory, Heap (Priority Queue), Enumeration, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/) |

## Problem Description

### Goal

A company has $N$ branches numbered from `0` through `n - 1`. Undirected roads
connect some pairs of branches, and initially every branch is reachable from
every other. A road record `[u, v, w]` gives its two endpoints and positive
length. Several roads may connect the same pair.

The company may close any set of branches, including none or all of them. When
a branch closes, every road incident to it becomes unavailable, so a route
between remaining branches may use only other remaining branches. Distance is
the minimum total road length of such a route.

Count the closing sets for which every pair of branches left open has distance
at most `maxDistance`. A set leaving fewer than two branches open automatically
meets the pairwise condition.

### Function Contract

**Inputs**

- `n`: the number of branches
- `maxDistance`: the greatest allowed shortest-path distance between retained branches
- `roads`: undirected road records `[u, v, w]`

Let $N=n$ and $R=\lvert\texttt{roads}\rvert$. The contract guarantees
$1\le N\le10$, $1\le\texttt{maxDistance}\le10^5$, $0\le R\le1000$, valid
distinct endpoints from `0` through `n - 1`, and $1\le w\le1000$. The original
graph is connected, and parallel roads are allowed.

**Return value**

The number of branch sets that may be closed while keeping every pair of open
branches within `maxDistance` using only open branches and their roads.

### Examples

#### Example 1

- **Input:** `n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]`
- **Output:** `5`
- **Explanation:** Besides closing every branch, each choice that leaves at most one branch open is valid, and leaving only branches `0` and `1` open is also valid.

#### Example 2

- **Input:** `n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]`
- **Output:** `7`
- **Explanation:** All three branches are mutually within distance four, and every closing choice except the one that leaves only `0` and `1` open is valid.

#### Example 3

- **Input:** `n = 1, maxDistance = 10, roads = []`
- **Output:** `2`
- **Explanation:** Both keeping the sole branch open and closing it satisfy the condition.
