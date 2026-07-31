# Maximum Value of a String in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2496 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/) |

## Problem Description

### Goal

Each alphanumeric string has a value determined by its contents. If every character is a decimal digit, its value is the base-10 integer represented by the complete string. Leading zeroes are allowed and do not change that numeric value. If at least one character is a lowercase English letter, the string's value is instead its number of characters.

Given an array `strs` containing such strings, evaluate every element under this rule and return the greatest value obtained. A mixed letter-and-digit string is never parsed partially; the presence of any letter makes its full length the value.

### Function Contract

**Inputs**

- `strs`: A non-empty list of alphanumeric strings. The list contains at most `100` strings, and each string has length from `1` through `9`.

Every character is either a lowercase English letter or a decimal digit. Let

$$
S = \sum_{s \in \texttt{strs}} \lvert s \rvert
$$

be the total number of input characters.

**Return value**

Return the maximum string value as an integer, using numeric interpretation only for strings made entirely of digits and length otherwise.

### Examples

**Example 1**

- Input: `strs = ["alic3", "bob", "3", "4", "00000"]`
- Output: `5`
- Explanation: `"alic3"` has value `5` by length, while `"00000"` is numeric and has value `0`.

**Example 2**

- Input: `strs = ["1", "01", "001", "0001"]`
- Output: `1`
- Explanation: Every string is numeric and represents the integer `1`, regardless of its leading zeroes.

**Example 3**

- Input: `strs = ["abcde", "999", "12x"]`
- Output: `999`
- Explanation: The three values are `5`, `999`, and `3`, respectively.
