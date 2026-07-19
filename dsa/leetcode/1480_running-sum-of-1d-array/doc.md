# Running Sum of 1d Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1480 |
| Difficulty | Easy |
| Topics | Array, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/) |

## Problem Description
### Goal

For an integer array `nums`, construct its running sum. At every index `i`, the returned value must equal the sum of the input elements from index `0` through `i`, inclusive.

Preserve the input order and return one prefix total for every input position. Negative values may reduce a later total, zeros leave it unchanged, and no sorting or omission is permitted.

### Function Contract
**Inputs**

Let $N$ be the length of `nums`.

- `nums`: an integer array with $1 \le N \le 1000$.
- Every value satisfies $-10^6 \le \texttt{nums[i]} \le 10^6$.

**Return value**

Return an array `runningSum` of length $N$ satisfying

$$
\texttt{runningSum[i]}=\sum_{j=0}^{i}\texttt{nums[j]}
$$

for every index $0 \le i < N$.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `[1,3,6,10]`
- Explanation: The prefixes contain one, two, three, and four input values respectively.

**Example 2**

- Input: `nums = [1,1,1,1,1]`
- Output: `[1,2,3,4,5]`

**Example 3**

- Input: `nums = [3,1,2,10,1]`
- Output: `[3,4,6,16,17]`
