# Minimum Element After Replacement With Digit Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3300 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/) |

## Problem Description

### Goal

You are given a non-empty list of positive integers. Replace every integer independently with the sum of its decimal digits. For example, `307` becomes `10` because $3+0+7=10$, while a one-digit number remains unchanged.

After applying this replacement to every position, return the smallest resulting value. The list itself does not need to be mutated; only the minimum among all computed digit sums is required.

### Function Contract

**Inputs**

- `nums`: A list of positive integers whose decimal digit sums are compared.

The list contains from 1 through 100 elements, and every element is from 1 through $10^4$. Let

$$
S=\sum_{x\in\texttt{nums}}\operatorname{digits}(x)
$$

be the total number of decimal digits across the input values.

**Return value**

- The minimum digit sum produced by replacing every element.

### Examples

**Example 1**

- Input: `nums = [10,12,13,14]`
- Output: `1`
- Explanation: The replacements are `[1,3,4,5]`.

**Example 2**

- Input: `nums = [1,2,3,4]`
- Output: `1`
- Explanation: Every one-digit value remains unchanged.

**Example 3**

- Input: `nums = [999,19,199]`
- Output: `10`
- Explanation: The digit sums are `[27,10,19]`, whose minimum is 10.
