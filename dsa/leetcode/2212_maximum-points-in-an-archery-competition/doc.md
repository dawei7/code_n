# Maximum Points in an Archery Competition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2212 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-points-in-an-archery-competition/) |

## Problem Description

### Goal

Alice and Bob each shoot exactly `numArrows` arrows at twelve scoring sections numbered from `0` through `11`. Alice shoots first. At section $k$, Alice receives $k$ points when her arrow count is at least Bob's; Bob receives $k$ points only when his count is strictly greater. If both counts are zero, neither player receives that section's points.

Given Alice's twelve counts, construct Bob's twelve-count allocation to maximize his score. Every one of Bob's arrows must be assigned. If several allocations achieve the same maximum score, any one of them is valid.

### Function Contract

**Inputs**

- `numArrows`: the total number of arrows used by each player, where $1 \le \texttt{numArrows} \le 10^5$.
- `aliceArrows`: twelve nonnegative counts whose sum is `numArrows`; index $k$ describes scoring section $k$.

Let $s=12$ be the fixed number of scoring sections.

**Return value**

Return a length-twelve nonnegative integer array `bobArrows` whose sum is `numArrows` and whose score is maximum.

### Examples

#### Example 1

- **Input:** `numArrows = 9`, `aliceArrows = [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]`
- **Output:** `[0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 3, 1]`
- **Explanation:** this allocation wins sections `4`, `5`, `8`, `9`, `10`, and `11` for `47` points.

#### Example 2

- **Input:** `numArrows = 3`, `aliceArrows = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2]`
- **Output:** `[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]`
- **Explanation:** winning sections `8`, `9`, and `10` yields the optimal score `27`.

#### Example 3

- **Input:** `numArrows = 1`, `aliceArrows = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- **Output:** `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]`
- **Explanation:** Bob spends the arrow on the highest section and earns `11`.
