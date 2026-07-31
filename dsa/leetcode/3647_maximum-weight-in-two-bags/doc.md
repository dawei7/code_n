# Maximum Weight in Two Bags

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3647 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-weight-in-two-bags/) |

## Problem Description
### Goal

You have a collection of indivisible items described by `weights` and two bags with capacities `w1` and `w2`. Each item may be left unpacked, placed in the first bag, or placed in the second bag, but it cannot be placed in both.

The sum of weights assigned to bag 1 must be at most `w1`, and the corresponding sum for bag 2 must be at most `w2`. Choose the assignments that maximize the combined packed weight across both bags and return that maximum.

### Function Contract
**Inputs**

- `weights`: Between 1 and 100 positive item weights, each at most 100.
- `w1`: The first bag's capacity, between 1 and 300.
- `w2`: The second bag's capacity, between 1 and 300.

**Return value**

Return the maximum sum of item weights that can be assigned across the two bags without exceeding either capacity or reusing an item.

### Examples
**Example 1**

- Input: `weights = [1,4,3,2]`, `w1 = 5`, `w2 = 4`
- Output: `9`
- Explanation: Pack 3 and 2 in the first bag and 4 in the second, filling both capacities.

**Example 2**

- Input: `weights = [3,6,4,8]`, `w1 = 9`, `w2 = 7`
- Output: `15`
- Explanation: Put 8 in the first bag and 3 plus 4 in the second.

**Example 3**

- Input: `weights = [5,7]`, `w1 = 2`, `w2 = 3`
- Output: `0`
- Explanation: Neither item fits in either bag.
