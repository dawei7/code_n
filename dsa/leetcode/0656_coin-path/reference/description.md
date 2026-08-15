### 1. Description

You are given an integer array `coins` (**1-indexed**) of length `n` and an integer `maxJump`. You can jump to any index `i` of the array `coins` if $\text{coins}[i] \neq -1$ and you have to pay $\text{coins}[i]$ when you visit index `i`. In addition to that, if you are currently at index `i`, you can only jump to any index $i + k$ where $i + k \le n$ and `k` is a value in the range `[1, maxJump]`.

You are initially positioned at index `1` ($\text{coins}[1]$ is not `-1`). You want to find the path that reaches index n with the minimum cost.

Return an integer array of the indices that you will visit in order so that you can reach index n with the minimum cost. If there are multiple paths with the same cost, return the **lexicographically smallest** such path. If it is not possible to reach index n, return an empty array.

A path $p1 = [\text{Pa}_{1}, \text{Pa}_{2}, ..., \text{Pa}_{x}]$ of length `x` is **lexicographically smaller** than $p2 = [\text{Pb}_{1}, \text{Pb}_{2}, ..., \text{Pb}_{x}]$ of length `y`, if and only if at the first `j` where $\text{Pa}_{j}$ and $\text{Pb}_{j}$ differ, $\text{Pa}_{j} < \text{Pb}_{j}$; when no such `j` exists, then `x < y`.

### 2. Function Contract

$solve(coins: \text{list}[int], maxJump: int) -> \text{list}[int]$

**Inputs**

- `coins`: visit costs in source position order; $\text{coins}[0]$ represents source index `1`, and `-1` marks a position that cannot be visited.
- `maxJump`: the inclusive maximum number of positions one forward jump may cross.

The path starts at source index `1` and must end at source index `n`. Each jump advances by at least one and at most `maxJump`. The total cost includes every visited position, including the start and destination. The first position is guaranteed to be valid, but the destination may be blocked or otherwise unreachable.

**Return value**

Return the one-based indices of the lexicographically smallest minimum-cost path. Return `[]` when no valid path reaches index `n`.

### 3. Examples

#### Example 1

- **Input:** $coins = [1,2,4,-1,2], maxJump = 2$
- **Output:** `[1,3,5]`

#### Example 2

- **Input:** $coins = [1,2,4,-1,2], maxJump = 1$
- **Output:** `[]`

### 4. Constraints

- $1 \le \text{coins.length} \le 1000$

- $-1 \le \text{coins}[i] \le 100$

- $\text{coins}[1] \neq -1$

- $1 \le maxJump \le 100$
