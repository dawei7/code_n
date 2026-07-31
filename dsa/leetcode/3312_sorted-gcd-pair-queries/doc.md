# Sorted GCD Pair Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3312 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Binary Search, Combinatorics, Counting, Number Theory, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sorted-gcd-pair-queries/) |

## Problem Description

### Goal

For every unordered index pair $(i,j)$ with $0\leq i<j<n$, compute $\gcd(\texttt{nums[i]},\texttt{nums[j]})$. Collect all $n(n-1)/2$ results with multiplicity and sort them in ascending order to form a conceptual array `gcdPairs`.

Each value in `queries` is a valid zero-based index into that conceptual array. Return the GCD stored at every requested position, preserving query order and repeated queries. The pair array can be quadratic in `nums`, so the task requires answering without materializing all pairs.

### Function Contract

**Inputs**

- `nums`: An array of $n$ positive integers, where $2\leq n\leq10^5$ and $1\leq\texttt{nums[i]}\leq5\cdot10^4$.
- `queries`: Between 1 and $10^5$ zero-based positions, each smaller than $n(n-1)/2$.

**Return value**

Return an integer array where each element is `gcdPairs[queries[i]]` for the ascending multiset of all pair GCDs.

### Examples

**Example 1**

- Input: `nums = [2, 3, 4], queries = [0, 2, 2]`
- Output: `[1, 2, 2]`

The sorted pair GCDs are `[1, 1, 2]`.

**Example 2**

- Input: `nums = [4, 4, 2, 1], queries = [5, 3, 1, 0]`
- Output: `[4, 2, 1, 1]`

Here `gcdPairs = [1, 1, 1, 2, 2, 4]` after sorting.

**Example 3**

- Input: `nums = [2, 2], queries = [0, 0]`
- Output: `[2, 2]`
