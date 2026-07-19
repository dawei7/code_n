# Sum of Even Numbers After Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 985 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/sum-of-even-numbers-after-queries/) |

## Problem Description

### Goal

You are given an integer array `nums` and a sequence `queries`, where each query is `[val_i, index_i]`.

Process the queries in their given order. For query `i`, first perform the executable update `nums[index_i] = nums[index_i] + val_i`. Then compute the sum of every even value currently in `nums`. Return an array `answer` whose entry `answer[i]` is that even-value sum after the corresponding update. Updates persist, so every later query observes all earlier changes.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers with $1\le N\le10^4$ and $-10^4\le\texttt{nums[i]}\le10^4$.
- `queries`: a list of $Q$ pairs `[val_i, index_i]`, where $1\le Q\le10^4$, $-10^4\le\texttt{val_i}\le10^4$, and $0\le\texttt{index_i}<N$.

**Return value**

- A length-$Q$ list containing the sum of the current even array values after each query.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4], queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]`
- Output: `[8, 6, 2, 4]`
- Explanation: the successive arrays are `[2, 2, 3, 4]`, `[2, -1, 3, 4]`, `[-2, -1, 3, 4]`, and `[-2, -1, 3, 6]`.

**Example 2**

- Input: `nums = [1], queries = [[4, 0]]`
- Output: `[0]`
- Explanation: the updated value is `5`, which is odd.
