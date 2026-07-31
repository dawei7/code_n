# Unit Conversion II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3535 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unit-conversion-ii/) |

## Problem Description

### Goal

There are $n$ units labeled from `0` through `n - 1`. Each entry `[source, target, factor]` in `conversions` states that one unit of `source` is equal to `factor` units of `target`. The $n-1$ given conversions guarantee that unit `0` can be converted to every other unit through a unique sequence of conversions. A conversion may be followed either in its stated direction or in reverse.

Each query `[unitA, unitB]` asks how many units of `unitB` equal one unit of `unitA`. This value can be a fraction. Interpret division modulo the prime $10^9+7$: if the exact ratio is $p/q$, return

$$
p \cdot q^{-1} \bmod (10^9+7),
$$

where $q^{-1}$ is the modular multiplicative inverse of $q$. Return one modular conversion factor for every query, preserving query order.

### Function Contract

**Inputs**

- `conversions`: Exactly $n-1$ triples `[source, target, factor]`, where both unit labels lie in $[0,n-1]$ and $1 \le \texttt{factor} \le 10^9$.
- `queries`: Pairs `[unitA, unitB]` whose labels lie in $[0,n-1]$.

The number of units is $n = \lvert\texttt{conversions}\rvert+1$, with $2 \le n \le 10^5$. Let $Q=\lvert\texttt{queries}\rvert$, where $1 \le Q \le 10^5$.

**Return value**

- A list containing the requested conversion ratios modulo $10^9+7$.

### Examples

**Example 1**

- Input: `conversions = [[0,1,2],[0,2,6]], queries = [[1,2],[1,0]]`
- Output: `[3,500000004]`
- Explanation: One unit of `1` equals three units of `2`. Reversing the first conversion gives $1/2$, represented modulo $10^9+7$ by `500000004`.

**Example 2**

- Input: `conversions = [[0,1,2],[0,2,6],[0,3,8],[2,4,2],[2,5,4],[3,6,3]], queries = [[1,2],[0,4],[6,5],[4,6],[6,1]]`
- Output: `[3,12,1,2,83333334]`
- Explanation: Conversion chains may pass through their common root; for example, one unit of `0` equals twelve units of `4`.
