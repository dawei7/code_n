# Average Salary Excluding the Minimum and Maximum Salary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1491 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [average-salary-excluding-the-minimum-and-maximum-salary](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/) |

## Problem Description & Examples
### Goal
Compute the average salary after excluding exactly the minimum and maximum salary values.

### Function Contract
**Inputs**

- `salary`: a list of unique salary values.

**Return value**

The average of the remaining salaries.

### Examples
**Example 1**

- Input: `salary = [4000,3000,1000,2000]`
- Output: `2500.0`

**Example 2**

- Input: `salary = [1000,2000,3000]`
- Output: `2000.0`

**Example 3**

- Input: `salary = [6000,5000,4000,3000,2000,1000]`
- Output: `3500.0`

---

## Underlying Base Algorithm(s)
Single-pass aggregate using sum, minimum, and maximum.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
