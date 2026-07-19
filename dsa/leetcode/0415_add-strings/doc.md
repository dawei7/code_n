# Add Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 415 |
| Difficulty | Easy |
| Topics | Math, String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/add-strings/) |

## Problem Description
### Goal
Given normalized decimal strings `num1` and `num2` representing nonnegative integers, compute their arithmetic sum. The inputs may contain more digits than fit in a built-in numeric type, and digits must be interpreted from their base-ten positions.

Return the normalized decimal representation of `num1 + num2`, propagating carries across as many positions as necessary and adding a new leading digit when required. Do not convert either complete operand to an integer or use arbitrary-precision library shortcuts. Zero inputs and unequal lengths must work normally, with no leading zeroes in the result except the single string `"0"`.

### Function Contract
**Inputs**

- `num1`: the first normalized nonnegative decimal string
- `num2`: the second normalized nonnegative decimal string

**Return value**

- Return the normalized decimal representation of `num1 + num2`.

### Examples
**Example 1**

- Input: `num1 = "11", num2 = "123"`
- Output: `"134"`

**Example 2**

- Input: `num1 = "456", num2 = "77"`
- Output: `"533"`

**Example 3**

- Input: `num1 = "0", num2 = "0"`
- Output: `"0"`
