# Minimize the Maximum of Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2513 |
| Difficulty | Medium |
| Topics | Math, Binary Search, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/) |

## Problem Description

### Goal

Construct two initially empty arrays of positive integers. The first array must contain exactly `uniqueCnt1` distinct values, none divisible by `divisor1`. The second must contain exactly `uniqueCnt2` distinct values, none divisible by `divisor2`.

The two arrays must also be disjoint: an integer chosen for one array cannot appear in the other. Values that satisfy both divisibility restrictions may be assigned to either array, but not both.

Among all valid constructions, return the smallest possible value of the largest integer used in either array.

### Function Contract

**Inputs**

- `divisor1`: An integer divisor whose multiples cannot appear in the first array.
- `divisor2`: An integer divisor whose multiples cannot appear in the second array.
- `uniqueCnt1`: The required number of distinct positive integers in the first array.
- `uniqueCnt2`: The required number of distinct positive integers in the second array.

Both divisors lie from $2$ through $10^5$. Both requested counts are positive, and their sum is at most $10^9$.

**Return value**

The minimum possible maximum integer across two arrays satisfying every size, divisibility, distinctness, and disjointness condition.

### Examples

#### Example 1

- **Input:** `divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3`
- **Output:** `4`
- **Explanation:** The first array can be `[1]` and the second `[2,3,4]`, so all four smallest positive integers can be assigned legally.

#### Example 2

- **Input:** `divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1`
- **Output:** `3`
- **Explanation:** Arrays `[1,2]` and `[3]` satisfy the requirements and use no value above `3`.

#### Example 3

- **Input:** `divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2`
- **Output:** `15`
- **Explanation:** One valid construction is `[1,3,5,7,9,11,13,15]` and `[2,6]`; no construction can have a smaller maximum.
