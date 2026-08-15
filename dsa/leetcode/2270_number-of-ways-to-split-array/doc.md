# Number of Ways to Split Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2270 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-split-array/) |

## Problem Description

### Goal

The 0-indexed integer array `nums` has length $n$. Splitting after index $i$
creates a left part containing indices $0$ through $i$ and a right part
containing indices $i+1$ through $n-1$.

A split is valid when both parts are nonempty and the sum of the left part is
greater than or equal to the sum of the right part. Thus only indices
$0\le i<n-1$ may be used.

Return the number of indices that define valid splits. Array values may be
negative, so the comparison must use the actual signed sums rather than
lengths or magnitudes.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $2\le n\le10^5$.

Every element satisfies $-10^5\le\texttt{nums[i]}\le10^5$.

**Return value**

Return the number of split indices $i$ with $0\le i<n-1$ for which

$$
\sum_{j=0}^{i}\texttt{nums[j]}
\ge
\sum_{j=i+1}^{n-1}\texttt{nums[j]}.
$$

### Examples

#### Example 1

- **Input:** `nums = [10,4,-8,7]`
- **Output:** `2`

Splits after indices `0` and `1` have left sums at least as large as their
right sums. The split after index `2` has sums $6$ and $7$ and is invalid.

#### Example 2

- **Input:** `nums = [2,3,1,0]`
- **Output:** `2`

The valid split indices are `1` and `2`.
