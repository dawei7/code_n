# Greatest Common Divisor Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2709 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Union-Find, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/greatest-common-divisor-traversal/) |

## Problem Description

### Goal

The 0-indexed integer array `nums` defines a graph over its indices. Two distinct indices `i` and `j` have a direct traversal edge exactly when $\gcd(\texttt{nums[i]},\texttt{nums[j]})>1$.

Determine whether every pair of indices is connected by some sequence of these traversals. The sequence may pass through any intermediate indices, so the endpoints do not need to share a factor directly. Return `true` precisely when the entire index graph is one connected component. A one-element array is connected without requiring an edge.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^5$.

Let $M=\max(\texttt{nums})$.

**Return value**

Return `true` if every index can reach every other index through one or more valid GCD edges; otherwise return `false`.

### Examples

**Example 1**

- Input: `nums = [2,3,6]`
- Output: `true`
- Explanation: Value $6$ shares factor $2$ with the first index and factor $3$ with the second, connecting all three.

**Example 2**

- Input: `nums = [3,9,5]`
- Output: `false`
- Explanation: The value $5$ shares no prime factor with either other value.

**Example 3**

- Input: `nums = [4,3,12,8]`
- Output: `true`
- Explanation: The value $12$ links the factor-$2$ indices to the factor-$3$ index.
