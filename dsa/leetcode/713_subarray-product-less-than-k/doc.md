# Subarray Product Less Than K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 713 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/) |

## Problem Description
### Goal
Given an array `nums` of positive integers and an integer `k`, consider every nonempty contiguous subarray and multiply all values inside it.

Return the number of subarrays whose product is strictly less than `k`. Subarrays are counted by their index ranges, so equal value sequences at different positions contribute separately. A product equal to `k` does not qualify, and noncontiguous subsequences are not considered.

### Function Contract
**Inputs**

- `nums`: a nonempty list of positive integers
- `k`: the exclusive product limit

**Return value**

- The number of contiguous subarrays with product below `k`

### Examples
**Example 1**

- Input: `nums = [10,5,2,6], k = 100`
- Output: `8`

**Example 2**

- Input: `nums = [1,2,3], k = 0`
- Output: `0`

**Example 3**

- Input: `nums = [1,1,1], k = 2`
- Output: `6`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Handle an impossible threshold**

Every nonempty product is at least one because all values are positive. Therefore $k \le 1$ admits no valid subarray.

**Maintain a valid product window**

Multiply each new rightmost value into the current product. While the product is at least `k`, divide out the leftmost value and advance the left boundary. Positivity guarantees removing factors cannot increase the product.

**Count all suffixes ending at the right boundary**

Once `[left, right]` is valid, every shorter suffix ending at `right` is also valid: removing positive integer factors cannot increase its product. There are `right - left + 1` such suffixes, so add that count.

**Why no subarray is omitted or counted twice**

For each right endpoint, shrinking stops at the earliest valid left boundary; any earlier start still has product at least `k`, and every later start is valid. The formula therefore counts exactly all valid subarrays with that unique right endpoint. Summing across endpoints partitions the complete answer.

#### Complexity detail

The right boundary visits every element once, and the left boundary advances at most `n` times in total, so the time is $O(n)$. The algorithm stores two indices, the product, and the count, using $O(1)$ extra space.

#### Alternatives and edge cases

- **Prefix logarithms plus binary search:** transform products into sums and find a boundary for each endpoint; it takes $O(n \log n)$ time and requires care with floating-point comparisons.
- **Enumerate all intervals:** extend every starting position while multiplying values; it is correct but takes $O(n^2)$ time.
- $k \le 1$ always returns `0` for positive input values.
- The comparison is strict, so a product exactly equal to `k` is invalid.
- Values equal to one can produce many valid subarrays without changing the product.
- Integer division is exact because the maintained product contains every factor currently removed from its left edge.

</details>
