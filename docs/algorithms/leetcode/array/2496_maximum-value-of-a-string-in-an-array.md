# Maximum Value of a String in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2496 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [maximum-value-of-a-string-in-an-array](https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/) |

## Problem Description & Examples
### Goal
Given an array of strings, determine the "value" of each string. If a string consists entirely of digits, its value is its integer representation. Otherwise, its value is the length of the string. The objective is to return the maximum value found among all strings in the array.

### Function Contract
**Inputs**

- `strs`: A list of strings (`List[str]`) where each string contains lowercase English letters and/or digits.

**Return value**

- An integer representing the maximum value calculated across all strings in the input list.

### Examples
**Example 1**

- Input: `strs = ["alic3","bob","3","4","00000"]`
- Output: `5`

**Example 2**

- Input: `strs = ["1","01","001","0001"]`
- Output: `1`

**Example 3**

- Input: `strs = ["abcde","abc","ab","a"]`
- Output: `5`

---

## Underlying Base Algorithm(s)
The solution utilizes a linear scan (iteration) over the array. For each string, we perform a membership check (or regex/type conversion check) to determine if it is numeric. If numeric, we convert it to an integer; otherwise, we calculate its length. We maintain a running maximum of these values.

---

## Complexity Analysis
- **Time Complexity**: O(N * L), where N is the number of strings in the array and L is the maximum length of a string. We iterate through each string once and perform a check that takes time proportional to the string's length.
- **Space Complexity**: O(1), as we only store the current maximum value and temporary variables, excluding the space required for the input itself.
