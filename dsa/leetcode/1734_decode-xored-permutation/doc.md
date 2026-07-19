# Decode XORed Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1734 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-xored-permutation/) |

## Problem Description

### Goal

An integer array `perm` is a permutation of the first $n$ positive integers, and $n$ is odd. The permutation was replaced by a length-$(n-1)$ array `encoded`, where each entry is the bitwise XOR of one adjacent pair:

`encoded[i] = perm[i] ^ perm[i + 1]`.

Recover and return the original permutation. The input guarantees $3 \le n < 10^5$, and guarantees that exactly one valid original permutation exists.

### Function Contract

**Inputs**

- `encoded`: a length-$(n-1)$ integer list produced from adjacent entries of a permutation of $1$ through $n$, where $n$ is odd.

**Return value**

- Return the unique original length-$n$ permutation.

### Examples

**Example 1**

- Input: `encoded = [3,1]`
- Output: `[1,2,3]`
- Explanation: The adjacent XOR values are `1 ^ 2 = 3` and `2 ^ 3 = 1`.

**Example 2**

- Input: `encoded = [6,5,4,6]`
- Output: `[2,4,1,5,3]`
- Explanation: XORing every adjacent pair of the returned permutation recreates `encoded`.

**Example 3**

- Input: `encoded = [4,3,1,7]`
- Output: `[5,1,2,3,4]`
- Explanation: The odd length and permutation range determine the otherwise missing first value.
