# Count Special Quadruplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1995 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/count-special-quadruplets/) |

## Problem Description

### Goal

Given a zero-indexed integer array `nums`, count the distinct quadruplets of indices $(a,b,c,d)$ whose values satisfy

$$
\texttt{nums[a]}+\texttt{nums[b]}+\texttt{nums[c]}=\texttt{nums[d]}.
$$

The four positions must also occur in strict order: $a<b<c<d$. Quadruplets are distinguished by their indices, so repeated array values may participate in several different valid choices.

### Function Contract

**Inputs**

- `nums`: an array of length $N$, where $4 \le N \le 50$ and $1 \le \texttt{nums[i]} \le 100$.
- Let $V$ denote the number of possible differences `nums[d] - nums[c]` under the value constraints.

**Return value**

Return the number of ordered index quadruplets satisfying both the value equation and $a<b<c<d$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 6]`
- Output: `1`
- Explanation: Only $(0,1,2,3)$ works because $1+2+3=6$.

**Example 2**

- Input: `nums = [3, 3, 6, 4, 5]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 1, 3, 5]`
- Output: `4`
- Explanation: One quadruplet ends at the value `3`, and three index-distinct choices of two earlier ones accompany `3` to produce `5`.
