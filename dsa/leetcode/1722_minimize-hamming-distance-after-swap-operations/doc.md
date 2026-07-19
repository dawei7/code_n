# Minimize Hamming Distance After Swap Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1722 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Union-Find |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/) |

## Problem Description

### Goal

You are given equal-length integer arrays `source` and `target`. Each pair `[a, b]` in `allowedSwaps` permits swapping the values currently stored at the distinct 0-indexed positions `a` and `b`. Any permitted swap may be applied repeatedly and the operations may occur in any order.

The Hamming distance is the number of indices where the resulting `source` value differs from `target` at the same index. Rearrange `source` using the allowed operations and return the minimum Hamming distance achievable.

### Function Contract

**Inputs**

- `source`: an integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{source[i]} \le 10^5$.
- `target`: an integer array of the same length, where $1 \le \texttt{target[i]} \le 10^5$.
- `allowedSwaps`: at most $10^5$ distinct-index pairs `[a, b]` with $0 \le a,b<n$.
- Let $m = \lvert \texttt{allowedSwaps} \rvert$.

**Return value**

- Return the smallest possible number of indices where `source[i] != target[i]`.

### Examples

**Example 1**

- Input: `source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]`
- Output: `1`
- Explanation: The first component can place $2,1$ exactly, and the second can place $4$ but has no $5$.

**Example 2**

- Input: `source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []`
- Output: `2`
- Explanation: With no permitted swap, the two middle mismatches cannot be changed.

**Example 3**

- Input: `source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]`
- Output: `0`
- Explanation: All indices are connected transitively, so the source multiset can be permuted into the target order.
