# Fibonacci Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `dp_01` |
| Frontend ID | 509 |
| Difficulty | Easy |
| Topics | Math, Dynamic Programming, Recursion, Memoization |
| Official Link | [fibonacci-number](https://leetcode.com/problems/fibonacci-number/) |

## Problem Description & Examples
### Goal
Compute the n-th Fibonacci number.
fib(0)=0, fib(1)=1, fib(n) = fib(n-1) + fib(n-2)
Requirement: O(n) - naive recursion (O(2^n)) will FAIL!
Use memoization or bottom-up DP.
Source: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

### Function Contract
**Inputs**

- `n`: index of the Fibonacci number to compute.

**Return value**

the n-th Fibonacci number (fib(0)=0, fib(1)=1).

### Examples
**Example 1**

- Input: `n = 0`
- Output: `0`

**Example 2**

- Input: `n = 5`
- Output: `5`

**Example 3**

- Input: `n = 8`
- Output: `21`

---

## Underlying Base Algorithm(s)
dynamic

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `TODO`
