# Find a Value of a Mysterious Function Closest to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1521 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Bit Manipulation, Segment Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/) |

## Problem Description
### Goal

For indices `l` and `r`, the given function takes the bitwise AND of every array value in the inclusive range from `min(l, r)` through `max(l, r)`. Thus every function result is the AND of one nonempty contiguous subarray.

Choose any legal pair of indices so that the absolute difference between this AND value and `target` is as small as possible. Return that minimum difference; the indices and the chosen subarray itself are not returned.

### Function Contract
**Inputs**

Let $n$ be the array length and $M$ its maximum value.

- `arr`: A list of $n$ positive integers, where $1 \leq n \leq 10^5$ and every value is at most $10^6$.
- `target`: An integer satisfying $0 \leq \texttt{target} \leq 10^7$.

**Return value**

Return the minimum of

$$
\left\lvert\left(\mathop{\mathtt{AND}}_{k=l}^{r}\texttt{arr}[k]\right)-\texttt{target}\right\rvert
$$

over every nonempty contiguous interval with $0 \leq l \leq r < n$.

### Examples
**Example 1**

- Input: `arr = [9, 12, 3, 7, 15], target = 5`
- Output: `2`
- Explanation: Reachable AND values include 3 and 7, both two away from 5.

**Example 2**

- Input: `arr = [1000000, 1000000, 1000000], target = 1`
- Output: `999999`
- Explanation: Every nonempty subarray has AND value 1000000.

**Example 3**

- Input: `arr = [1, 2, 4, 8, 16], target = 0`
- Output: `0`
- Explanation: The AND of any adjacent pair is zero.
