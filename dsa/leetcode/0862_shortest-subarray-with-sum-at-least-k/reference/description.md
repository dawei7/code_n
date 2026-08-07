## Description

Given an integer array `nums` and an integer `k`, return *the length of the shortest non-empty **subarray** of *`nums`* with a sum of at least *`k`. If there is no such **subarray**, return `-1`.

A **subarray** is a **contiguous** part of an array.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [1], k = 1`
- **Output:** `1`
#### Example 2

- **Input:** `nums = [1,2], k = 4`
- **Output:** `-1`
#### Example 3

- **Input:** `nums = [2,-1,2], k = 3`
- **Output:** `3`
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$

- $1 \le k \le 10^{9}$