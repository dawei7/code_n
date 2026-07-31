# Add Two Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2235 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/add-two-integers/) |

## Problem Description

### Goal

The input consists of two integers, `num1` and `num2`. Each value is supplied
independently and may be positive, negative, or zero. The task does not ask for
the values to be reordered, transformed, or combined through any operation
other than ordinary integer addition.

Compute the exact arithmetic sum of the two given values and return that single
integer. Positive and negative contributions therefore follow their usual
signs: equal opposite values cancel, two negative values produce a negative
sum, and adding zero leaves the other value unchanged.

### Function Contract

**Inputs**

- `num1`: An integer satisfying $-100\le\texttt{num1}\le 100$.
- `num2`: An integer satisfying $-100\le\texttt{num2}\le 100$.

**Return value**

Return the integer $\texttt{num1}+\texttt{num2}$.

### Examples

**Example 1**

- Input: `num1 = 12, num2 = 5`
- Output: `17`

**Example 2**

- Input: `num1 = -10, num2 = 4`
- Output: `-6`

**Example 3**

- Input: `num1 = -7, num2 = 7`
- Output: `0`
