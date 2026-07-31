# Sum of Good Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3452 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-good-numbers/) |

## Problem Description
### Goal
For each element `nums[i]`, examine the positions exactly `k` places to its left and right. A position outside the array contributes no comparison. The element is good when it is strictly greater than every one of those comparison elements that exists.

Thus an element near an end may need to beat only one comparison value, while an element with neither comparison index would automatically be good. Equality is insufficient because the comparisons are strict. Return the sum of the values of all good elements.

### Function Contract
**Inputs**

- `nums`: A list of $n$ positive integers.
- `k`: The exact index distance used for the left and right comparisons.

The constraints are $2 \le n \le 100$, $1 \le \texttt{nums[i]} \le 1000$, and $1 \le k \le \lfloor n / 2 \rfloor$.

**Return value**

Return the sum of every `nums[i]` that is strictly greater than the existing elements at indices $i-k$ and $i+k$.

### Examples
**Example 1**

- Input: `nums = [1, 3, 2, 1, 5, 4], k = 2`
- Output: `12`

**Example 2**

- Input: `nums = [2, 1], k = 1`
- Output: `2`

**Example 3**

- Input: `nums = [4, 4], k = 1`
- Output: `0`
