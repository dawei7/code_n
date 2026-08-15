# Minimum Number of Operations to Make All Array Elements Equal to 1

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2654 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` containing positive integers. In one operation, choose an index `i` with $0 \le i < n-1$, compute the greatest common divisor of the adjacent values `nums[i]` and `nums[i + 1]`, and replace either one of those two values with that gcd. The other value remains unchanged.

Apply this operation any number of times and return the minimum number needed to make every array element equal to `1`. If no sequence of permitted adjacent replacements can produce an all-ones array, return `-1`.

### Function Contract

**Inputs**

- `nums`: An array of $n$ positive integers, where $2 \le n \le 50$ and $1 \le \texttt{nums[i]} \le 10^6$.

**Return value**

- Return the minimum number of adjacent-gcd replacements needed to make all elements `1`, or `-1` when this is impossible.

### Examples

#### Example 1

- **Input:** `nums = [2,6,3,4]`
- **Output:** `4`
- **Explanation:** Combining `3` and `4` first creates a `1`; three more adjacent operations spread that value across the remaining positions.

#### Example 2

- **Input:** `nums = [2,10,6,14]`
- **Output:** `-1`
- **Explanation:** Every array value is even, so every gcd produced by an operation remains greater than `1`.
