# Minimum Jumps to Reach End via Prime Teleportation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3629 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Breadth-First Search, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/) |

## Problem Description

### Goal

You are given an integer array `nums` with length $n$. Begin at index $0$ and reach index $n-1$ using as few jumps as possible.

From index `i`, an adjacent step may move to `i - 1` or `i + 1` when that index remains within the array. A second operation is available only when `nums[i]` is a prime number $p$: prime teleportation may jump directly to any different index `j` whose value is divisible by $p$, meaning `nums[j] % p == 0`.

Return the minimum number of jumps needed to reach the final index. Teleportation depends on the current value itself being prime; merely having a composite value with prime factors does not permit that operation.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.

Let $M = \max(\texttt{nums})$.

**Return value**

Return an integer equal to the minimum number of adjacent steps and prime teleportations required to move from index $0$ to index $n-1$.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 4, 6]`
- **Output:** `2`
- **Explanation:** Step from index 0 to index 1, then use the prime value 2 to teleport to index 3 because 6 is divisible by 2.

#### Example 2

- **Input:** `nums = [2, 3, 4, 7, 9]`
- **Output:** `2`
- **Explanation:** Step to index 1, whose value is the prime 3, then teleport to the final value 9.

#### Example 3

- **Input:** `nums = [4, 6, 5, 8]`
- **Output:** `3`
- **Explanation:** No prime teleportation shortens the route, so three adjacent steps reach the end.
