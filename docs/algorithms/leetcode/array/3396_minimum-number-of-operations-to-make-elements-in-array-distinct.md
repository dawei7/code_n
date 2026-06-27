# Minimum Number of Operations to Make Elements in Array Distinct

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3396 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [minimum-number-of-operations-to-make-elements-in-array-distinct](https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/) |

## Problem Description & Examples
### Goal
Given an array of integers, determine the minimum number of increment operations required to ensure that all elements in the array are unique. An increment operation consists of increasing an element's value by one.

### Function Contract
**Inputs**

- `nums`: A list of integers.

**Return value**

- An integer representing the minimum number of operations to make all elements in `nums` distinct.

### Examples
**Example 1**

- Input: `nums = [3, 2, 1, 2, 1, 7]`
- Output: `6`
- Explanation:
  - The array is `[3, 2, 1, 2, 1, 7]`.
  - To make elements distinct, we can transform it to `[3, 4, 1, 5, 2, 7]`.
  - Operations:
    - `2` becomes `4` (2 operations)
    - `1` becomes `2` (1 operation)
    - `2` becomes `5` (3 operations)
  - Total operations: `2 + 1 + 3 = 6`.

**Example 2**

- Input: `nums = [1, 1, 1]`
- Output: `3`
- Explanation:
  - The array is `[1, 1, 1]`.
  - We can transform it to `[1, 2, 3]`.
  - Operations:
    - The first `1` remains `1` (0 operations).
    - The second `1` becomes `2` (1 operation).
    - The third `1` becomes `3` (2 operations).
  - Total operations: `0 + 1 + 2 = 3`.

**Example 3**

- Input: `nums = [0, 0, 0, 0]`
- Output: `6`
- Explanation:
  - The array is `[0, 0, 0, 0]`.
  - We can transform it to `[0, 1, 2, 3]`.
  - Operations:
    - The first `0` remains `0` (0 operations).
    - The second `0` becomes `1` (1 operation).
    - The third `0` becomes `2` (2 operations).
    - The fourth `0` becomes `3` (3 operations).
  - Total operations: `0 + 1 + 2 + 3 = 6`.

---

## Underlying Base Algorithm(s)
The core idea is to iterate through the array and, for each number, ensure it's unique. If a number is already present, we need to increment it until it becomes a unique value. A hash set (or a frequency map) is an efficient way to keep track of the numbers we've already encountered and assigned.

A greedy approach works here: sort the array first. Then, iterate through the sorted array. For each element `nums[i]`, if it's less than or equal to the previous element `nums[i-1]`, we must increment `nums[i]` to `nums[i-1] + 1`. The number of operations for this element will be `(nums[i-1] + 1) - nums[i]`. We then update `nums[i]` to this new value for subsequent comparisons.

Alternatively, without sorting, we can use a hash set to keep track of seen numbers. For each number `num` in the input array, we check if `num` is already in our `seen` set. If it is, we repeatedly increment `num` and add 1 to our total operations count until `num` is not in `seen`. Once `num` is unique, we add it to the `seen` set.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)` if sorting is used, where N is the number of elements in `nums`. If a hash set is used without sorting, in the worst case (e.g., `[0, 0, 0, ..., 0]`), each element might require multiple increments, leading to a potential `O(N^2)` complexity in the worst-case scenario for the hash set approach. However, if the range of numbers is limited or the distribution is not extremely skewed, the average case for the hash set approach can be closer to `O(N)`. The sorting approach is generally more predictable.
- **Space Complexity**: `O(1)` if sorting is done in-place and no auxiliary data structures are used beyond a few variables. If a hash set is used, the space complexity is `O(N)` in the worst case to store all unique elements.
