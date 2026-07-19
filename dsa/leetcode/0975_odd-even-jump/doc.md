# Odd Even Jump

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 975 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Sorting, Monotonic Stack, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/odd-even-jump/) |

## Problem Description

### Goal

Given an integer array `arr`, consider a sequence of forward jumps from a chosen starting index. The first, third, fifth, and subsequent alternating jumps are odd-numbered jumps; the second, fourth, sixth, and remaining alternating jumps are even-numbered jumps. The parity describes the jump count, not an array index.

From index `i`, every destination `j` must satisfy $i<j$. On an odd-numbered jump, choose a destination whose value is at least `arr[i]`; among all legal values, its value must be the smallest, and a tie is resolved by choosing the smallest destination index. On an even-numbered jump, choose a value at most `arr[i]`; take the largest legal value, again breaking ties toward the smallest index. A required jump may have no legal destination.

A starting index is good when this forced sequence can reach the final index. Reaching it with zero jumps is allowed, so the final index is always good. Return the number of good starting indices.

### Function Contract

**Inputs**

- `arr`: a list of $N$ integers, where $1 \le N \le 2\cdot10^4$ and $0 \le \texttt{arr[i]} < 10^5$.

For each index $i$, let $H_i$ be its forced odd-jump destination and $L_i$ its forced even-jump destination, or let either be absent when no legal destination exists.

**Return value**

- The number of starting indices from which the prescribed alternating jumps can reach index $N-1$.

### Examples

**Example 1**

- Input: `arr = [10, 13, 12, 14, 15]`
- Output: `2`
- Explanation: indices `3` and `4` are the only good starts.

**Example 2**

- Input: `arr = [2, 3, 1, 1, 4]`
- Output: `3`
- Explanation: indices `1`, `3`, and `4` can reach the end. Equal values at indices `2` and `3` demonstrate the smallest-index tie rule.

**Example 3**

- Input: `arr = [5, 1, 3, 4, 2]`
- Output: `3`
- Explanation: the good starting indices are `1`, `2`, and `4`.
