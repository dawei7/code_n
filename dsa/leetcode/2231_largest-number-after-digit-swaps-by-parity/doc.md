# Largest Number After Digit Swaps by Parity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2231 |
| Difficulty | Easy |
| Topics | Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/) |

## Problem Description

### Goal

Given a positive integer `num`, its digits may be rearranged through any number of swaps, but a swap is allowed only between two digits of the same parity. Two odd digits may exchange positions, as may two even digits; an odd digit can never exchange with an even digit.

Return the greatest integer obtainable under those rules. Since same-parity swaps can realize any permutation within the odd positions and independently any permutation within the even positions, the parity pattern of the original decimal representation remains fixed while the digits assigned to each pattern position may change.

### Function Contract

**Inputs**

- `num`: A positive integer satisfying $1\le\texttt{num}\le 10^9$.

Its decimal representation has at most ten digits.

**Return value**

Return the numerically largest value reachable after any number of swaps between digit positions whose current digits have the same parity.

### Examples

**Example 1**

- Input: `num = 1234`
- Output: `3412`

**Example 2**

- Input: `num = 65875`
- Output: `87655`

**Example 3**

- Input: `num = 7`
- Output: `7`
