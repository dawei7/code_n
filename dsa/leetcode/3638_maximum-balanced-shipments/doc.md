# Maximum Balanced Shipments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3638 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Stack, Greedy, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-balanced-shipments/) |

## Problem Description
### Goal

An array `weight` lists parcel weights in their fixed line order. A shipment is any contiguous subarray. It is balanced when the final parcel's weight is strictly less than the maximum weight appearing anywhere in that shipment.

Choose as many non-overlapping balanced shipments as possible. A parcel may belong to at most one selected shipment, and parcels not used by any shipment are allowed.

Return the maximum number of balanced shipments.

### Function Contract
**Inputs**

- `weight`: A list of $n$ positive parcel weights, where $2 \le n \le 10^5$ and $1 \le \texttt{weight[i]} \le 10^9$.

**Return value**

Return the greatest number of pairwise non-overlapping contiguous shipments whose last weight is strictly below that shipment's maximum.

### Examples
**Example 1**

- Input: `weight = [2, 5, 1, 4, 3]`
- Output: `2`
- Explanation: Select `[2, 5, 1]` and `[4, 3]`; their final values 1 and 3 are below maxima 5 and 4.

**Example 2**

- Input: `weight = [4, 4]`
- Output: `0`
- Explanation: Equality is insufficient, and a one-parcel shipment cannot be balanced.
