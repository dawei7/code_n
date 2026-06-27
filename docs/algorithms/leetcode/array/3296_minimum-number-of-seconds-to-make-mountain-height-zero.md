# Minimum Number of Seconds to Make Mountain Height Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3296 |
| Difficulty | Medium |
| Topics | Array, Math, Binary Search, Greedy, Heap (Priority Queue) |
| Official Link | [minimum-number-of-seconds-to-make-mountain-height-zero](https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/) |

## Problem Description & Examples
### Goal
Given an initial mountain height and a list of workers with varying efficiency levels, determine the minimum time required to reduce the mountain's height to zero. Each worker $i$ takes $w_i \times k$ seconds to reduce the height by $k$ units, where $k$ is the number of units reduced in a single session. Workers can work simultaneously.

### Function Contract
**Inputs**

- `mountainHeight`: An integer representing the total height to be reduced.
- `workerTimes`: A list of integers where each element represents the base time coefficient for a specific worker.

**Return value**

- An integer representing the minimum total time (in seconds) required to reduce the mountain height to zero.

### Examples
**Example 1**

- Input: `mountainHeight = 4, workerTimes = [2, 1, 4]`
- Output: `3`

**Example 2**

- Input: `mountainHeight = 10, workerTimes = [3, 2, 2, 4]`
- Output: `12`

**Example 3**

- Input: `mountainHeight = 5, workerTimes = [1]`
- Output: `15`

---

## Underlying Base Algorithm(s)
The problem is solved using **Binary Search on the Answer**. Since the time required to reduce the mountain is monotonic (if it can be reduced in $T$ seconds, it can also be reduced in $T+1$ seconds), we search for the smallest $T$ such that the sum of heights reduced by all workers within time $T$ is at least `mountainHeight`. For a given time $T$ and worker coefficient $w$, the number of units $k$ reduced is found by solving $w \cdot \frac{k(k+1)}{2} \le T$.

---

## Complexity Analysis
- **Time Complexity**: $O(W \log(\text{max\_time}))$, where $W$ is the number of workers and $\text{max\_time}$ is the upper bound of the search space (roughly $10^{18}$).
- **Space Complexity**: $O(1)$, as we only store a few variables for the binary search.
