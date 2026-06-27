# Minimum Number of Operations to Make Array Empty

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2870 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Counting |
| Official Link | [minimum-number-of-operations-to-make-array-empty](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/) |

## Problem Description & Examples
### Goal
Given an integer array, determine the minimum number of operations required to empty the array. In one operation, you can either remove two elements with the same value or three elements with the same value. If it is impossible to empty the array, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the collection of elements.

**Return value**

- An integer representing the minimum operations needed, or -1 if the array cannot be emptied.

### Examples
**Example 1**

- Input: `nums = [2,3,3,2,2,4,2,3,4]`
- Output: `4`

**Example 2**

- Input: `nums = [2,1,2,2,3,3]`
- Output: `-1`

**Example 3**

- Input: `nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]`
- Output: `7`

---

## Underlying Base Algorithm(s)
The problem is solved using a Greedy approach combined with Frequency Counting. By calculating the frequency of each unique number, we observe that for any count `n`:
1. If `n == 1`, it is impossible to empty the array (return -1).
2. If `n % 3 == 0`, we need `n / 3` operations.
3. If `n % 3 == 1`, we can use two groups of 2 (total 4) and the rest in groups of 3, requiring `(n - 4) / 3 + 2` operations.
4. If `n % 3 == 2`, we use one group of 2 and the rest in groups of 3, requiring `(n - 2) / 3 + 1` operations.
Mathematically, this simplifies to `ceil(n / 3)` for all `n > 1`.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of elements in the array, as we iterate through the array once to count frequencies and once through the unique counts.
- **Space Complexity**: `O(K)`, where `K` is the number of unique elements in the array, used to store the frequency map.
