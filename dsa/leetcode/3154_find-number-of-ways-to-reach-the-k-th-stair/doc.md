# Find Number of Ways to Reach the K-th Stair

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3154 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Bit Manipulation, Memoization, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/) |

## Problem Description

### Goal

An infinite staircase is numbered upward from stair $0$. Alice begins on stair $1$ with an integer `jump` initially equal to $0$. From stair `i`, she may move down to `i - 1`, provided she is not on stair $0$ and her preceding operation was not another downward move.

Alternatively, she may move upward to `i + 2^jump`; after that operation, `jump` increases by one. Given a non-negative target `k`, return the number of operation sequences that reach stair `k`. Reaching `k` does not force Alice to stop: a longer sequence that leaves and later returns to `k` counts separately.

### Function Contract

**Inputs**

- `k`: The target stair, where $0 \le k \le 10^9$.

**Return value**

Return the total number of valid finite operation sequences whose endpoint is stair `k`, including the empty sequence when the starting stair is already the target.

### Examples

#### Example 1

- **Input:** `k = 0`
- **Output:** `2`
- **Explanation:** Alice can move down immediately, or move down, up by $2^0$, and move down again.

#### Example 2

- **Input:** `k = 1`
- **Output:** `4`
- **Explanation:** The empty sequence counts, and three longer valid sequences end at stair $1$.

#### Example 3

- **Input:** `k = 2`
- **Output:** `4`
- **Explanation:** Four distinct placements of legal downward operations among the first few upward jumps end at stair $2$.
