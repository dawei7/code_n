# Most Frequent Number Following Key In an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2190 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [most-frequent-number-following-key-in-an-array](https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/) |

## Problem Description & Examples
### Goal
Among values immediately following an occurrence of `key`, return the one that appears most often. The input guarantees a unique most frequent follower.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `key`: the value whose following elements are counted.

**Return value**

The most frequent value at index `i + 1` among indices where `nums[i] == key`.

### Examples
**Example 1**

- Input: `nums = [1, 100, 200, 1, 100]`, `key = 1`
- Output: `100`

**Example 2**

- Input: `nums = [2, 2, 2, 2, 3]`, `key = 2`
- Output: `2`

**Example 3**

- Input: `nums = [4, 5, 4, 6, 4, 6]`, `key = 4`
- Output: `6`

---

## Underlying Base Algorithm(s)
Scan through the penultimate index. Whenever the current value equals `key`, increment the frequency of the next value and track the follower with the largest count.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(u)`, where `u` is the number of distinct followers
