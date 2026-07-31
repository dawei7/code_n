# Maximum Hamming Distances

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3141 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-hamming-distances/) |

## Problem Description
### Goal
You are given an integer array `nums` and a bit width `m`. Every value lies between $0$ and $2^m-1$, so each one has an $m$-bit binary representation; leading zeroes are included when necessary.

The Hamming distance between two values is the number of bit positions in which their $m$-bit representations differ. For every index $i$, find the maximum Hamming distance between `nums[i]` and an element of `nums`. Return those per-index maxima in their original order.

### Function Contract
**Inputs**

- `nums`: A list of integers represented with exactly `m` bits for distance comparisons.
- `m`: The fixed positive bit width.

Let $n = \lvert\texttt{nums}\rvert$. The constraints are $1 \le m \le 17$, $2 \le n \le 2^m$, and $0 \le \texttt{nums[i]} < 2^m$.

**Return value**

Return a length-$n$ list whose entry at index $i$ is the greatest $m$-bit Hamming distance between `nums[i]` and a value present in `nums`.

### Examples
**Example 1**

- Input: `nums = [9, 12, 9, 11], m = 4`
- Output: `[2, 3, 2, 3]`
- Explanation: In four bits the values are `1001`, `1100`, `1001`, and `1011`. The greatest available distances are respectively $2$, $3$, $2$, and $3$.

**Example 2**

- Input: `nums = [3, 4, 6, 10], m = 4`
- Output: `[3, 3, 2, 3]`
- Explanation: The fixed-width forms are `0011`, `0100`, `0110`, and `1010`. For example, `0011` and `0100` differ in three positions, while no available value differs from `0110` in more than two.
