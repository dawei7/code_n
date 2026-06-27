# Neither Minimum nor Maximum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2733 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [neither-minimum-nor-maximum](https://leetcode.com/problems/neither-minimum-nor-maximum/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value. If no such number exists, return `-1`.

### Function Contract
**Inputs**

- `nums`: `List[int]` - An array of distinct positive integers.

**Return value**

- `int` - Any value in `nums` that is strictly greater than the minimum value and strictly less than the maximum value of the array. Returns `-1` if no such element exists.

### Examples
**Example 1**

- Input: `nums = [3, 2, 1, 4]`
- Output: `2` (or `3`)
- Explanation: The minimum value is `1` and the maximum value is `4`. Both `2` and `3` are neither the minimum nor the maximum. Returning either is correct.

**Example 2**

- Input: `nums = [1, 2]`
- Output: `-1`
- Explanation: Since there are only two elements, one must be the minimum and the other must be the maximum. Thus, no number satisfies the condition.

**Example 3**

- Input: `nums = [2, 1, 3]`
- Output: `2`
- Explanation: The minimum is `1` and the maximum is `3`. The value `2` is neither, so we return `2`.

---

## Underlying Base Algorithm(s)
The problem asks us to find any element that is neither the minimum nor the maximum of the entire array. 

### Naive Approach
We could find the global minimum and global maximum of the array in $O(N)$ time, then iterate through the array to find any element that is not equal to either.

### Optimal $O(1)$ Approach
Since the elements in the array are distinct, we can optimize this to $O(1)$ time and space:
1. If the array has fewer than 3 elements, it is impossible to have an element that is neither the minimum nor the maximum. In this case, we immediately return `-1`.
2. If the array has 3 or more elements, we can simply take the first 3 elements of the array.
3. Sort these 3 elements. The middle element (the second element in the sorted order) is guaranteed to be strictly between the smallest and largest of these three.
4. Because all elements in the array are distinct, this middle element cannot be the absolute minimum of the entire array (since at least one element in our triplet is smaller) and cannot be the absolute maximum of the entire array (since at least one element in our triplet is larger). Thus, it is guaranteed to be neither the minimum nor the maximum of the entire array.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(1)$ — We only inspect and sort at most the first 3 elements of the array, which takes constant time regardless of the size of `nums`.
- **Space Complexity**: $\mathcal{O}(1)$ — We only use a constant amount of extra space to store and sort the 3 elements.
