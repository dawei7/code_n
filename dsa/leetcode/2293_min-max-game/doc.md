# Min Max Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2293 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/min-max-game/) |

## Problem Description

### Goal

Start with a 0-indexed integer array `nums` whose length is a power of two.
While more than one value remains, replace the current array of length $n$
with an array of length $n/2$.

For each new index $i$, combine the adjacent old values at indices `2 * i`
and `2 * i + 1`. Use their minimum when $i$ is even and their maximum when
$i$ is odd. The parity rule restarts from index zero in every newly created
array.

Return the single value left after repeating this reduction.

### Function Contract

**Inputs**

- `nums`: A nonempty integer array whose length is a power of two.

Let $n = \lvert\texttt{nums}\rvert$. The contract guarantees
$1 \le n \le 1024$ and $1 \le \texttt{nums}[i] \le 10^9$.

**Return value**

The final value produced by the repeated alternating minimum/maximum pair
reductions.

### Examples

#### Example 1

- **Input:** `nums = [1, 3, 5, 2, 4, 8, 2, 2]`
- **Output:** `1`

#### Example 2

- **Input:** `nums = [3]`
- **Output:** `3`
