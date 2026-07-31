# Maximum Bags With Full Capacity of Rocks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2279 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/) |

## Problem Description
### Goal
There are $n$ bags. Bag $i$ can hold at most `capacity[i]` rocks and currently
contains `rocks[i]` rocks. A bag is full exactly when its current number of
rocks equals its capacity.

Distribute at most `additionalRocks` more rocks among the bags. No bag may
receive more rocks than its remaining capacity, and unused rocks may be left
over. Return the greatest number of bags that can be made full.

### Function Contract
**Inputs**

- `capacity`: An integer array of length $n$ whose value at index $i$ is the maximum number of rocks bag $i$ can contain.
- `rocks`: An integer array of length $n$ whose value at index $i$ is the number of rocks already in bag $i$.
- `additionalRocks`: The number of extra rocks available for distribution.

Here, $1 \le n \le 5 \cdot 10^4$, both arrays have length $n$,
$1 \le \texttt{capacity[i]} \le 10^9$, and
$0 \le \texttt{rocks[i]} \le \texttt{capacity[i]}$.

**Return value**

The maximum number of bags that can be exactly full after distributing at most
the available additional rocks.

### Examples
**Example 1**

- Input: `capacity = [2, 3, 4, 5]`, `rocks = [1, 2, 4, 4]`, `additionalRocks = 2`
- Output: `3`

**Example 2**

- Input: `capacity = [10, 2, 2]`, `rocks = [2, 2, 0]`, `additionalRocks = 100`
- Output: `3`

**Example 3**

- Input: `capacity = [5, 5]`, `rocks = [5, 0]`, `additionalRocks = 1`
- Output: `1`
