# Separate the Digits in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2553 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Separate the Digits in an Array](https://leetcode.com/problems/separate-the-digits-in-an-array/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. Separate every integer into its decimal digits, preserving the left-to-right order of the digits within that integer. Append those digits to one result array while also preserving the original order of the integers in `nums`.

Return the resulting digit array. A one-digit value contributes itself, while zeroes that occur inside a value must remain in their original positions; for example, `10921` contributes `[1, 0, 9, 2, 1]`. Because every input value is positive, no sign character needs to be represented.

### Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers. Its length is between $1$ and $1000$, inclusive, and every value is between $1$ and $10^5$, inclusive.

Let $D$ be the total number of decimal digits across all values in `nums`.

**Return value**

- A list of exactly $D$ integers, each between $0$ and $9$, containing the separated digits in their original order.

### Examples

#### Example 1

- **Input:** `nums = [13, 25, 83, 77]`
- **Output:** `[1, 3, 2, 5, 8, 3, 7, 7]`
- **Explanation:** The four values contribute `[1, 3]`, `[2, 5]`, `[8, 3]`, and `[7, 7]` in that order.

#### Example 2

- **Input:** `nums = [7, 1, 3, 9]`
- **Output:** `[7, 1, 3, 9]`
- **Explanation:** Each input already consists of one digit.
