# Maximum XOR for Each Query

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-xor-for-each-query/) |
| Frontend ID | 1829 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given an ascending array `nums` of $n$ non-negative integers and a bit width `maximumBit`. Perform exactly $n$ queries on a current array that initially contains every element of `nums`.

For each query, choose a non-negative integer $k < 2^{\texttt{maximumBit}}$ that maximizes the XOR of $k$ with every element in the current array. Record that $k$, remove the current array's last element, and continue. Return the recorded values in query order.

### Function Contract

**Inputs**

- `nums`: an ascending array of $n$ integers, where $1 \le n \le 10^5$.
- `maximumBit`: the permitted answer width, where $1 \le \texttt{maximumBit} \le 20$.
- Every value satisfies $0 \le \texttt{nums[i]} < 2^{\texttt{maximumBit}}$.

**Return value**

- Return an array of length $n$. Entry $i$ is the value $k$ that maximizes the XOR for the current prefix before the $i$th removal.

### Examples

**Example 1**

- Input: `nums = [0,1,1,3], maximumBit = 2`
- Output: `[0,3,2,3]`

The largest two-bit result is 3. Before the first removal, the array XOR is 3, so `k = 0`; after removing 3, the remaining XOR is 0, so `k = 3`.

**Example 2**

- Input: `nums = [2,3,4,7], maximumBit = 3`
- Output: `[5,2,6,5]`

**Example 3**

- Input: `nums = [0,1,2,2,5,7], maximumBit = 3`
- Output: `[4,3,6,4,6,7]`
