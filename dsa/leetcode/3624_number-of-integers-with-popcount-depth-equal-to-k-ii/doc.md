# Number of Integers With Popcount-Depth Equal to K II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3624 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/) |

## Problem Description
### Goal

For a positive integer `x`, start with $p_0=x$ and repeatedly replace the current value by its popcount, the number of set bits in its binary representation. The popcount-depth is the smallest index $d\ge 0$ at which $p_d=1$; consequently, 1 has depth 0, while a power of two greater than 1 has depth 1.

Maintain an integer array `nums` while processing ordered queries. A query `[1, l, r, k]` asks how many current elements at inclusive indices from `l` through `r` have depth exactly `k`. An update `[2, idx, val]` replaces `nums[idx]` for all subsequent operations. Return the answers to type-1 queries in their original order; updates produce no output.

### Function Contract

**Inputs**

- `nums`: The initial array of positive integers.
- `queries`: An ordered list of range-count queries `[1, l, r, k]` and point updates `[2, idx, val]`.

Let $n=\lvert\texttt{nums}\rvert$ and $q=\lvert\texttt{queries}\rvert$. Both lie from 1 through $10^5$. Every stored value lies from 1 through $10^{15}$, indices and inclusive ranges are valid, and $0\le k\le5$.

**Return value**

Return one integer per type-1 query: the number of elements in its inclusive range whose current popcount-depth equals `k`.

### Examples

**Example 1**

- Input: `nums = [2,4], queries = [[1,0,1,1],[2,1,1],[1,0,1,0]]`
- Output: `[2,1]`
- Explanation: Both initial powers of two have depth 1; after index 1 becomes 1, exactly that position has depth 0.

**Example 2**

- Input: `nums = [3,5,6], queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]]`
- Output: `[3,1,0]`
- Explanation: All three initial values have depth 2. Replacing 5 by 4 changes index 1 to depth 1, and neither of the first two values has depth 0.

**Example 3**

- Input: `nums = [1,2], queries = [[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]]`
- Output: `[1,0,1]`
- Explanation: Initially only 2 has depth 1. Updating the first value to 3 gives it depth 2.
