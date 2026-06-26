# Number of Pairs of Strings With Concatenation Equal to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2023 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Counting |
| Official Link | [number-of-pairs-of-strings-with-concatenation-equal-to-target](https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/) |

## Problem Description & Examples
### Goal
Count ordered pairs of different indices whose two strings concatenate exactly to `target`.

### Function Contract
**Inputs**

- `nums`: a list of strings.
- `target`: the required concatenation.

**Return value**

Return the number of ordered pairs `(i, j)` where `i != j` and `nums[i] + nums[j] == target`.

### Examples
**Example 1**

- Input: `nums = ["777","7","77","77"], target = "7777"`
- Output: `4`

**Example 2**

- Input: `nums = ["123","4","12","34"], target = "1234"`
- Output: `2`

**Example 3**

- Input: `nums = ["1","1","1"], target = "11"`
- Output: `6`

---

## Underlying Base Algorithm(s)
Count occurrences of each string. For every split of `target` into `left + right`, add `count[left] * count[right]`; when `left == right`, subtract self-pairings by using `count[left] * (count[left] - 1)`.

---

## Complexity Analysis
- **Time Complexity**: `O(L + n)`, ignoring string slicing cost, where `L = len(target)`.
- **Space Complexity**: `O(n)`
