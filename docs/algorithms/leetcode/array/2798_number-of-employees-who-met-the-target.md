# Number of Employees Who Met the Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2798 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [number-of-employees-who-met-the-target](https://leetcode.com/problems/number-of-employees-who-met-the-target/) |

## Problem Description & Examples
### Goal
Given a list of integers representing the number of hours each employee has worked, and a target integer, determine how many employees have met or exceeded the target number of hours.

### Function Contract
**Inputs**

- `hours`: A list of integers where `hours[i]` represents the hours worked by the i-th employee.
- `target`: An integer representing the minimum hours required to meet the goal.

**Return value**

- An integer representing the count of employees whose worked hours are greater than or equal to the target.

### Examples
**Example 1**

- Input: `hours = [0, 1, 2, 3, 4], target = 2`
- Output: `3`

**Example 2**

- Input: `hours = [5, 1, 4, 2, 2], target = 6`
- Output: `0`

**Example 3**

- Input: `hours = [10, 20, 30], target = 15`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem utilizes a simple linear scan (or filtering) algorithm. We iterate through the array once, evaluating a boolean condition for each element and maintaining a running count of elements that satisfy the condition.

---

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of elements in the `hours` list, as we must inspect each element exactly once.
- **Space Complexity**: O(1), as we only use a single integer variable to store the count, regardless of the input size.
