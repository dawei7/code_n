# Build an Array With Stack Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1441 |
| Difficulty | Medium |
| Topics | Array, Stack, Simulation |
| Official Link | [build-an-array-with-stack-operations](https://leetcode.com/problems/build-an-array-with-stack-operations/) |

## Problem Description & Examples
### Goal
Read numbers from `1` upward and build the given target array using `Push` for every read number and `Pop` when a read number should be discarded.

### Function Contract
**Inputs**

- `target`: a strictly increasing list of desired values.
- `n`: the largest number available in the input stream `1..n`.

**Return value**

A list of operation names that builds `target`.

### Examples
**Example 1**

- Input: `target = [1,3], n = 3`
- Output: `["Push","Push","Pop","Push"]`

**Example 2**

- Input: `target = [1,2,3], n = 3`
- Output: `["Push","Push","Push"]`

**Example 3**

- Input: `target = [2,3,4], n = 4`
- Output: `["Push","Pop","Push","Push","Push"]`

---

## Underlying Base Algorithm(s)
Simulation. For each target value, push and immediately pop every skipped stream value, then push the target value itself.

---

## Complexity Analysis
- **Time Complexity**: `O(t + s)`, where `t` is target length and `s` is the number of skipped values before the last target.
- **Space Complexity**: `O(t + s)` for the returned operation list.
