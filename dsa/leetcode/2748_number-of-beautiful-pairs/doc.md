# Number of Beautiful Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2748 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Counting, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-beautiful-pairs/) |

## Problem Description

### Goal

Given a 0-indexed array `nums` of positive integers, consider every ordered pair of indices $i<j$. Extract the first decimal digit of `nums[i]` and the last decimal digit of `nums[j]`. The direction matters: the first digit always comes from the earlier value, while the last digit always comes from the later one.

Call the index pair beautiful when those two digits are coprime, meaning their greatest common divisor is $1$. Count and return all beautiful pairs. Every input value has a nonzero last digit, and the array contains at least two values.

### Function Contract

Let $n$ be the length of `nums`.

**Inputs**

- `nums`: An array of positive integers where $2 \le n \le 100$, $1 \le \texttt{nums[i]} \le 9999$, and `nums[i] % 10 != 0`.

**Return value**

Return the number of pairs $(i,j)$ with $i<j$ for which the first digit of `nums[i]` and last digit of `nums[j]` have greatest common divisor $1$.

### Examples

**Example 1**

- Input: `nums = [2,5,1,4]`
- Output: `5`
- Explanation: Every index pair is beautiful except `(0,3)`, whose relevant digits are $2$ and $4$.

**Example 2**

- Input: `nums = [11,21,12]`
- Output: `2`
- Explanation: The pairs beginning at index `0` are beautiful; the relevant digits for `(1,2)` are both $2$.
