# Left and Right Sum Differences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2574 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [left-and-right-sum-differences](https://leetcode.com/problems/left-and-right-sum-differences/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` of length $n$. Define `leftSum[i]` as the sum of all elements strictly to the left of index $i$, using zero when that side is empty. Likewise, define `rightSum[i]` as the sum of all elements strictly to the right of $i$, again using zero when no such elements exist.

Construct an integer array `answer` of length $n$ such that

$$
\texttt{answer[i]} = \lvert \texttt{leftSum[i]} - \texttt{rightSum[i]} \rvert
$$

for every index, and return it.

### Function Contract

**Inputs**

- `nums`: A list of positive integers.

The length satisfies $1 \le n \le 1000$, and every value satisfies $1 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- Return a list whose entry at each index is the absolute difference between the sum strictly before that index and the sum strictly after it.

### Examples

**Example 1**

- Input: `nums = [10,4,8,3]`
- Output: `[15,1,11,22]`
- Explanation: The left sums are `[0,10,14,22]` and the right sums are `[15,11,3,0]`; taking the elementwise absolute differences gives the result.

**Example 2**

- Input: `nums = [1]`
- Output: `[0]`
- Explanation: There are no elements on either side of the only index.
