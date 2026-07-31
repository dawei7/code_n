# Minimum Cost to Make Array Equalindromic

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2967 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/) |

## Problem Description
### Goal
You are given a 0-indexed integer array `nums`. In one special move, choose an
index and a positive integer `x`, add the absolute difference between the
current value and `x` to the total cost, then replace that array element with
`x`. You may perform any number of moves, including none.

A positive integer is palindromic when its decimal digits read identically from
left to right and right to left. The array is equalindromic when every element
equals one common palindromic integer `y` with $y<10^9$.

Return the minimum total cost required to make `nums` equalindromic.

### Function Contract
**Inputs**

- `nums`: the positive integer values to change to one permitted target

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees
$1\le N\le10^5$ and $1\le\texttt{nums[i]}\le10^9$.

**Return value**

The minimum value of $\sum_i\lvert\texttt{nums[i]}-y\rvert$ over all positive
palindromic integers $y<10^9$.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5]`
- Output: `6`
- Explanation: Choosing the palindromic target `3` costs `2 + 1 + 0 + 1 + 2`.

**Example 2**

- Input: `nums = [10,12,13,14,15]`
- Output: `11`
- Explanation: Changing every value to the palindrome `11` gives the minimum total cost.

**Example 3**

- Input: `nums = [22,33,22,33,22]`
- Output: `22`
- Explanation: The optimal target is `22`; only the two `33` values change, each at cost eleven.
