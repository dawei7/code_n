# Two Furthest Houses With Different Colors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2078 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-furthest-houses-with-different-colors/) |

## Problem Description

### Goal

There are $n$ evenly spaced houses in a line, numbered by zero-based index. The integer `colors[i]` identifies the paint color of house $i$.

Choose two houses with different colors and maximize their distance. For indices $i$ and $j$, that distance is $\lvert i-j\rvert$. At least two houses are guaranteed to have different colors, so a valid pair always exists.

### Function Contract

**Inputs**

- `colors`: an integer list of length $n$, where $2 \le n \le 100$ and $0 \le \texttt{colors[i]} \le 100$.

**Return value**

- Return the maximum value of $\lvert i-j\rvert$ over all pairs with `colors[i] != colors[j]`.

### Examples

**Example 1**

- Input: `colors = [1,1,1,6,1,1,1]`
- Output: `3`
- Explanation: The lone house of color 6 is three positions from either endpoint.

**Example 2**

- Input: `colors = [1,8,3,8,3]`
- Output: `4`
- Explanation: Houses 0 and 4 have different colors and span the entire street.

**Example 3**

- Input: `colors = [0,1]`
- Output: `1`
- Explanation: The only two houses have different colors and are one position apart.
