# Minimum Number of Operations to Make Array XOR Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2997 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/) |

## Problem Description
### Goal
You are given an integer array `nums` and an integer `k`. In one operation,
choose any element and flip one bit of its binary representation. Leading zero
bits may also be flipped, so a new higher bit can be introduced.

Apply any number of operations until the bitwise XOR of all final array values
equals `k`. Return the minimum number of bit flips required.

### Function Contract
**Inputs**

- `nums`: the nonnegative array values
- `k`: the target XOR

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees $1\le N\le10^5$
and $0\le\texttt{nums[i]},k\le10^6$.

**Return value**

Return the minimum number of single-bit flips needed to change the array-wide
XOR to `k`.

### Examples
**Example 1**

- Input: `nums = [2,1,3,4], k = 1`
- Output: `2`

**Example 2**

- Input: `nums = [2,0,2,0], k = 0`
- Output: `0`

**Example 3**

- Input: `nums = [0], k = 8`
- Output: `1`
- Explanation: Flipping one leading zero bit introduces the `8` bit.
