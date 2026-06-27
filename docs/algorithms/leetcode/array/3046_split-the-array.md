# Split the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3046 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [split-the-array](https://leetcode.com/problems/split-the-array/) |

## Problem Description & Examples
### Goal
Determine if an array of even length $n$ can be partitioned into two subsets of size $n/2$ such that each subset contains only unique elements. This is possible if and only if no element in the original array appears more than twice, and the total count of elements appearing exactly once or twice satisfies the constraints of the partition.

### Function Contract
**Inputs**

- `nums`: A list of integers where the length is always even.

**Return value**

- `bool`: Returns `True` if the array can be split into two subsets with unique elements, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [1, 1, 2, 2, 3, 4]`
- Output: `True`

**Example 2**

- Input: `nums = [1, 1, 1, 1]`
- Output: `False`

**Example 3**

- Input: `nums = [6, 1, 3, 1, 1, 8, 9, 2]`
- Output: `False`

---

## Underlying Base Algorithm(s)
Frequency counting using a Hash Map (or `collections.Counter`). The logic relies on the Pigeonhole Principle: if any number appears more than twice, it is impossible to distribute those instances into two separate subsets without having at least one subset contain a duplicate.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the array, as we iterate through the list once to count frequencies and once through the frequency map.
- **Space Complexity**: $O(k)$, where $k$ is the number of unique elements in the array, used to store the frequency counts.
