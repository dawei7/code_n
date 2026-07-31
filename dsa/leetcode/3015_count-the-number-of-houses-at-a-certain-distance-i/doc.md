# Count the Number of Houses at a Certain Distance I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3015 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Breadth-First Search, Graph Theory, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/) |

## Problem Description

### Goal

A city has houses numbered from $1$ through $n$. Consecutive houses $i$ and $i+1$ are joined by a street, and one additional street connects houses $x$ and $y$. The two shortcut endpoints may be equal, in which case that street does not shorten travel between distinct houses.

For every distance $k$ from $1$ through $n$, count ordered pairs of distinct houses `(house1, house2)` whose shortest route uses exactly $k$ streets. Reversing a pair creates a separate count. Return a length-$n$ list whose position $k-1$ stores the count for distance $k$.

### Function Contract

**Inputs**

- `n`: The number of houses, between $2$ and $100$.
- `x`: One endpoint of the additional street, between $1$ and $n$.
- `y`: The other endpoint of the additional street, between $1$ and $n$.

**Return value**

Return `counts`, where `counts[k - 1]` is the number of ordered pairs of distinct houses at shortest-path distance $k$ for every $1\le k\le n$.

### Examples

**Example 1**

- Input: `n = 3, x = 1, y = 3`
- Output: `[6,0,0]`

The shortcut completes a triangle, so every ordered pair of distinct houses is one street apart.

**Example 2**

- Input: `n = 5, x = 2, y = 4`
- Output: `[10,8,2,0,0]`

**Example 3**

- Input: `n = 4, x = 1, y = 1`
- Output: `[6,4,2,0]`

The self-loop does not improve the ordinary path distances.
