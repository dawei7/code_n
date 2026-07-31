# Find if Digit Game Can Be Won

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3232 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-if-digit-game-can-be-won/) |

## Problem Description

### Goal

You are given an array of positive integers. Alice chooses either every single-digit number in the array or every double-digit number; Bob receives all numbers in the other group. Alice wins when the sum of her chosen numbers is strictly greater than Bob's sum.

Return whether Alice has a winning choice. Alice may select whichever of the two complete groups is more favorable, but she cannot take only part of a digit-length group.

### Function Contract

**Inputs**

- `nums`: An array with $1 \leq \lvert\texttt{nums}\rvert \leq 100$ and $1 \leq \texttt{nums[i]} \leq 99$.

**Return value**

Return `True` if choosing all one-digit values or all two-digit values gives Alice a strictly larger sum; otherwise return `False`.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4, 10]`
- Output: `False`
- Explanation: Both groups sum to $10$, so neither choice wins strictly.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5, 14]`
- Output: `True`
- Explanation: Alice can choose the single-digit values, whose sum is $15$.

**Example 3**

- Input: `nums = [5, 5, 5, 25]`
- Output: `True`
- Explanation: Alice can choose the double-digit value, whose sum is $25$.
