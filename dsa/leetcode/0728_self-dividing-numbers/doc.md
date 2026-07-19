# Self Dividing Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 728 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/self-dividing-numbers/) |

## Problem Description
### Goal
A self-dividing number is divisible by every decimal digit it contains. Such a number cannot contain digit `0`, because division by zero is undefined.

Given positive integers `left` and `right`, return all self-dividing numbers in the inclusive range `[left, right]`. Test each number against all of its own digits, including repeated digits, and return the qualifying values in increasing numerical order. Both interval endpoints are candidates when they satisfy the definition.

### Function Contract
**Inputs**

- `left`: the positive lower endpoint of the interval
- `right`: the positive upper endpoint of the interval, with `left <= right`

**Return value**

- All self-dividing numbers from `left` through `right` in increasing order

### Examples
**Example 1**

- Input: `left = 1, right = 22`
- Output: `[1,2,3,4,5,6,7,8,9,11,12,15,22]`

**Example 2**

- Input: `left = 47, right = 85`
- Output: `[48,55,66,77]`

**Example 3**

- Input: `left = 128, right = 128`
- Output: `[128]`
