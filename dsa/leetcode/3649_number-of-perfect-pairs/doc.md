# Number of Perfect Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3649 |
| Difficulty | Medium |
| Topics | Array, Math, Two Pointers, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-perfect-pairs/) |

## Problem Description
### Goal

For every index pair $(i,j)$ with $i<j$, let $a=\texttt{nums[i]}$ and $b=\texttt{nums[j]}$. The pair is perfect when both of these relations hold:

$$
\min(\lvert a-b\rvert,\lvert a+b\rvert)
\le \min(\lvert a\rvert,\lvert b\rvert),
$$

and

$$
\max(\lvert a-b\rvert,\lvert a+b\rvert)
\ge \max(\lvert a\rvert,\lvert b\rvert).
$$

Count and return all distinct index pairs satisfying both conditions. Equal values at different indices still form distinct pairs.

### Function Contract
**Inputs**

- `nums`: An array of $n$ integers, where $2\le n\le 10^5$ and every value lies in $[-10^9,10^9]$.

**Return value**

Return the number of perfect index pairs.

### Examples
**Example 1**

- Input: `nums = [0,1,2,3]`
- Output: `2`
- Explanation: The perfect pairs have values `(1, 2)` and `(2, 3)`.

**Example 2**

- Input: `nums = [-3,2,-1,4]`
- Output: `4`
- Explanation: Signs do not change the reduced magnitude condition; four index pairs have magnitudes within a factor of two.

**Example 3**

- Input: `nums = [1,10,100,1000]`
- Output: `0`
- Explanation: Every pair's larger magnitude is more than twice its smaller magnitude.
