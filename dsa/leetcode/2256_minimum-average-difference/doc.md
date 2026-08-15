# Minimum Average Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2256 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-average-difference/) |

## Problem Description

### Goal

For every index $i$ in the 0-indexed array `nums`, split the array immediately
after that position. The left part contains the first $i+1$ elements, and the
right part contains the remaining $n-i-1$ elements. Compute each part's average
using integer division, which rounds down because all values are nonnegative.
The average of the empty right part at the final index is defined as zero.

The average difference at $i$ is the absolute difference between those two
integer averages. Find the minimum difference over all split positions and
return its index. When several indices attain the same minimum, return the
smallest index.

### Function Contract

**Inputs**

- `nums`: A nonempty array of $n$ integers, where $1\le n\le10^5$ and $0\le\texttt{nums[i]}\le10^5$.

**Return value**

Return the smallest index minimizing

$$
\left|
\left\lfloor\frac{\sum_{j=0}^{i}\texttt{nums[j]}}{i+1}\right\rfloor
-
\left\lfloor\frac{\sum_{j=i+1}^{n-1}\texttt{nums[j]}}{n-i-1}\right\rfloor
\right|,
$$

where the second average is $0$ when $i=n-1$.

### Examples

#### Example 1

- **Input:** `nums = [2,5,3,9,5,3]`
- **Output:** `3`

#### Example 2

- **Input:** `nums = [0]`
- **Output:** `0`

#### Example 3

- **Input:** `nums = [1,1,1,1]`
- **Output:** `0`
