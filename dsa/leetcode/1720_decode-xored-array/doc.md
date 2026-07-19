# Decode XORed Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1720 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-xored-array/) |

## Problem Description

### Goal

A hidden array `arr` contains $n$ non-negative integers. It was transformed into an array `encoded` of length $n-1$ by setting `encoded[i] = arr[i] XOR arr[i + 1]` for every adjacent pair. You are given this encoded data together with `first`, the known value of `arr[0]`.

Reconstruct and return the entire original array. The supplied values always describe one valid answer, and knowing the first element makes that answer unique.

### Function Contract

**Inputs**

- `encoded`: an integer array of length $n-1$, where $2 \le n \le 10^4$ and $0 \le \texttt{encoded[i]} \le 10^5$.
- `first`: the first original element, where $0 \le \texttt{first} \le 10^5$.

**Return value**

- Return the unique original array `arr` of length $n$.

### Examples

**Example 1**

- Input: `encoded = [1,2,3], first = 1`
- Output: `[1,0,2,1]`
- Explanation: The adjacent XOR values are `1 XOR 0 = 1`, `0 XOR 2 = 2`, and `2 XOR 1 = 3`.

**Example 2**

- Input: `encoded = [6,2,7,3], first = 4`
- Output: `[4,2,0,7,4]`
- Explanation: Each next element is recovered from the previous decoded value and the corresponding encoded value.

**Example 3**

- Input: `encoded = [0], first = 100000`
- Output: `[100000,100000]`
- Explanation: Two equal values have XOR zero.
