# Minimum Time to Transport All Individuals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3594 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Graph Theory, Heap (Priority Queue), Shortest Path, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-transport-all-individuals/) |

## Problem Description

### Goal

There are `n` individuals at a base camp who must cross a river in one boat. The boat holds at most `k` people. Individual `i` has neutral crossing time `time[i]`, and a group travels at the maximum neutral time among its members. Environmental conditions cycle through `m` stages; departing during stage `j` multiplies the trip time by `mul[j]`.

After any trip lasting $d$ minutes, the stage advances by $\lfloor d\rfloor \bmod m$. A forward group reaches the destination with the boat. If anyone remains at the base, exactly one person currently at the destination must bring the boat back; that return trip uses the person's own neutral time and the multiplier at the new current stage, then advances the stage by the same rule.

Choose every forward group and returner to minimize the total elapsed time until all individuals are at the destination. Return `-1` when completion is impossible.

### Function Contract

**Inputs**

- `n`: The number of individuals, with $1 \leq n \leq 12$.
- `k`: The boat capacity, with $1 \leq k \leq 5$.
- `m`: The number of environmental stages, with $1 \leq m \leq 5$.
- `time`: The neutral solo crossing times, where `time.length == n` and $1 \leq \texttt{time[i]} \leq 100$.
- `mul`: The cyclic stage multipliers, where `mul.length == m` and $0.5 \leq \texttt{mul[j]} \leq 2.0$.

**Return value**

Return the minimum total time as a floating-point number, or `-1.0` if no valid sequence can transport everyone.

### Examples

**Example 1**

- Input: `n = 1, k = 1, m = 2, time = [5], mul = [1.0, 1.3]`
- Output: `5.00000`
- Explanation: The only individual crosses at stage `0` in five minutes, and no return is needed.

**Example 2**

- Input: `n = 3, k = 2, m = 3, time = [2, 5, 8], mul = [1.0, 1.5, 0.75]`
- Output: `14.50000`
- Explanation: Send individuals `0` and `2`, return individual `0` under the faster third stage, then send individuals `0` and `1`.

**Example 3**

- Input: `n = 2, k = 1, m = 2, time = [10, 10], mul = [2.0, 2.0]`
- Output: `-1.00000`
- Explanation: With capacity one, every forward trip before completion requires the same sole traveler to return, so no progress is possible.
