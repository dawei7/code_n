# Integer Break

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 343 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/integer-break/) |

## Problem Description
### Goal
Given an integer `n` from `2` through `58`, split it into a sum of at least two positive integers. You may choose any number of parts and may repeat the same part value when their total remains exactly `n`.

Return the maximum product obtainable by multiplying all chosen parts. The one-part decomposition `[n]` is forbidden even when it would have a larger product than a required split. Different decompositions may tie, and only the largest product is returned rather than the selected parts. Every part must be positive, so zero and negative padding are invalid.

### Function Contract
**Inputs**

- `n`: an integer from `2` through `58`

**Return value**

- The maximum product of a decomposition of `n` into two or more positive integers.

### Examples
**Example 1**

- Input: `n = 10`
- Output: `36`
- Explanation: $10 = 3 + 3 + 4$, whose product is $3 \cdot 3 \cdot 4 = 36$.

**Example 2**

- Input: `n = 3`
- Output: `2`

**Example 3**

- Input: `n = 2`
- Output: `1`
