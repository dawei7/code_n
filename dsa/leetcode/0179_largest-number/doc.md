# Largest Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 179 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-number/) |

## Problem Description
### Goal
Given a list of nonnegative integers, arrange all of them in an order whose decimal-string concatenation has the greatest possible numerical value. Every input element must be used exactly once, and digits inside an individual integer cannot be rearranged.

Return the maximum concatenation as a string because the result may exceed ordinary integer ranges. Ordering by numeric value or by the first digit alone is not sufficient when prefixes overlap, such as values whose concatenations compare differently in opposite orders. If every input value is zero, normalize the result to exactly `"0"` rather than returning several leading zeroes.

### Function Contract
**Inputs**

- `nums`: a list of nonnegative integers

**Return value**

The maximum concatenation as a decimal string, normalized to `"0"` when every value is zero.

### Examples
**Example 1**

- Input: `nums = [10,2]`
- Output: `"210"`

**Example 2**

- Input: `nums = [3,30,34,5,9]`
- Output: `"9534330"`

**Example 3**

- Input: `nums = [0,0]`
- Output: `"0"`
