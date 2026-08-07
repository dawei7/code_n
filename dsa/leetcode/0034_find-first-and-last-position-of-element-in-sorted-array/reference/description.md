## Description

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.
### Function Contract

**Inputs**

- `nums`: An integer array sorted in non-decreasing order.
- `target`: The integer whose occupied range is requested.

**Return value**

Return `[first, last]`, where `first` and `last` are the target's earliest and latest indices. Return `[-1, -1]` when the target is absent.

### Examples
#### Example 1

- **Input:** `nums = [5,7,7,8,8,10], target = 8`
- **Output:** `[3,4]`
#### Example 2

- **Input:** `nums = [5,7,7,8,8,10], target = 6`
- **Output:** `[-1,-1]`
#### Example 3

- **Input:** `nums = [], target = 0`
- **Output:** `[-1,-1]`
### Constraints

- $0 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$

- `nums` is a non-decreasing array.

- $-10^{9} \le target \le 10^{9}$