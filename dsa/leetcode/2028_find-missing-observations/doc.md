# Find Missing Observations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2028 |
| Difficulty | Medium |
| Topics | Array, Math, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/find-missing-observations/) |

## Problem Description

### Goal

A collection originally contained the outcomes of $M + N$ rolls of a
six-sided die, with every outcome between $1$ and $6$. The values of $M$
rolls are available in `rolls`, while the other $N$ observations are missing.
The integer average of all original observations is known as `mean`.

Construct any list of exactly $N$ legal die values that makes the average over
the observed and reconstructed rolls exactly `mean`. Different valid lists
are equally acceptable. Return an empty list when no such reconstruction is
possible.

### Function Contract

Let $M$ be the length of `rolls`, and let $N$ be the given missing count.

**Inputs**

- `rolls`: a list of $M$ observed die values, each from $1$ through $6$, where
  $1 \le M \le 10^5$.
- `mean`: the required average of all $M + N$ observations, where
  $1 \le \text{mean} \le 6$.
- `n`: the missing count $N$, where $1 \le N \le 10^5$.

**Return value**

- Any list of $N$ integers from $1$ through $6$ whose addition gives the
  required overall average, or an empty list if that sum is unattainable.

### Examples

**Example 1**

- Input: `rolls = [3, 2, 4, 3], mean = 4, n = 2`
- Output: `[6, 6]`
- Explanation: The six rolls then sum to `24`, so their average is `4`.

**Example 2**

- Input: `rolls = [1, 5, 6], mean = 3, n = 4`
- Output: `[2, 3, 2, 2]`
- Explanation: Any four legal values summing to `9` are valid.

**Example 3**

- Input: `rolls = [1, 2, 3, 4], mean = 6, n = 4`
- Output: `[]`
- Explanation: The missing rolls would need a sum greater than the maximum
  possible value $6N$.
