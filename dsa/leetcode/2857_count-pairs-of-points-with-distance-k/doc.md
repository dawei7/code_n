# Count Pairs of Points With Distance k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2857 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-pairs-of-points-with-distance-k/) |

## Problem Description

### Goal

You are given a 2D integer array `coordinates`, where `coordinates[i] = [x_i, y_i]` describes the point at index $i$, and an integer target `k`.

For points $(x_1, y_1)$ and $(x_2, y_2)$, define their distance as

$$
(x_1 \mathbin{\mathrm{XOR}} x_2) + (y_1 \mathbin{\mathrm{XOR}} y_2),
$$

where `XOR` is the bitwise exclusive-or operation. Count the index pairs `(i, j)` with $i < j$ whose distance is exactly `k`. Equal coordinate rows remain distinct points and can therefore contribute multiple index pairs.

### Function Contract

**Inputs**

- `coordinates`: A list of 2D points `[x_i, y_i]`.
- `k`: The required XOR-distance.

Let $n = \lvert\texttt{coordinates}\rvert$. The constraints guarantee $2 \le n \le 50000$, $0 \le x_i, y_i \le 10^6$, and $0 \le \texttt{k} \le 100$.

**Return value**

The number of index pairs `(i, j)` with $i < j$ for which `(x_i XOR x_j) + (y_i XOR y_j) = k`.

### Examples

#### Example 1

- **Input:** `coordinates = [[1, 2], [4, 2], [1, 3], [5, 2]], k = 5`
- **Output:** `2`

Pairs `(0, 1)` and `(2, 3)` have the required distance.

#### Example 2

- **Input:** `coordinates = [[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]], k = 0`
- **Output:** `10`

Every pair of the five identical points has distance zero.

#### Example 3

- **Input:** `coordinates = [[0, 0], [1, 2], [2, 1], [3, 0]], k = 3`
- **Output:** `3`

The point `[0, 0]` forms a qualifying pair with each of the other three points.
