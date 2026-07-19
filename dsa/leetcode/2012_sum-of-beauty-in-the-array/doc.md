# Sum of Beauty in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2012 |
| Difficulty | Medium |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-beauty-in-the-array/) |

## Problem Description

### Goal

For every interior index $i$ of the zero-indexed array `nums`, assign a beauty
score using strict comparisons.

The score is $2$ when every earlier value is smaller than `nums[i]` and every
later value is larger. If that global condition fails but the immediate
neighbors satisfy `nums[i - 1] < nums[i] < nums[i + 1]`, the score is $1$.
Otherwise, it is $0$. Return the sum of the scores for indices $1$ through
$N-2$; the first and last elements never receive a score.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $3\le N\le10^5$ and
  $1\le\texttt{nums[i]}\le10^5$.

**Return value**

Return the sum of all interior beauty scores.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `2`
- Explanation: The only interior value is greater than everything before it
  and smaller than everything after it.

**Example 2**

- Input: `nums = [2, 4, 6, 4]`
- Output: `1`
- Explanation: `4` lies strictly between its neighbors but fails the global
  condition; `6` has beauty zero.

**Example 3**

- Input: `nums = [3, 2, 1]`
- Output: `0`
- Explanation: The only interior value satisfies neither condition.
