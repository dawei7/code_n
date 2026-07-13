# Split Array Largest Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 410 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/split-array-largest-sum/) |

## Problem Description
### Goal
Given a nonnegative integer array and a valid integer `m`, place $m - 1$ boundaries to divide the complete array into exactly `m` nonempty contiguous subarrays. Every input position must belong to one group and original order cannot change.

For each split, consider the largest sum among its groups. Return the minimum possible value of that largest sum over all valid boundary placements. The result balances groups rather than minimizing their total, which is fixed. A group may contain one element, and when $m = 1$ the answer is the whole-array sum.

### Function Contract
**Inputs**

- `nums`: the nonnegative integer array
- `m`: the exact number of contiguous groups

**Return value**

- Return the minimum achievable value of the largest group sum.

### Examples
**Example 1**

- Input: `nums = [7,2,5,10,8], m = 2`
- Output: `18`

**Example 2**

- Input: `nums = [1,2,3,4,5], m = 2`
- Output: `9`

**Example 3**

- Input: `nums = [1,4,4], m = 3`
- Output: `4`

### Required Complexity

- **Time:** $O(n \log S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Search the possible largest sum**

No group limit can be below `max(nums)`, because every element belongs to some group. A limit of `sum(nums)` always works as one group and therefore also permits at most `m` groups. Binary-search this inclusive numeric interval, whose width is denoted by `S`.

**Greedily count groups under a candidate limit**

Scan left to right, extending the current group while its sum stays within the limit. When the next value would exceed it, start a new group. Because values are nonnegative, delaying each cut as long as possible minimizes the number of groups needed under that limit.

**Use monotonic feasibility**

If the greedy scan needs at most `m` groups, the candidate is feasible: any group can be split further at element boundaries until exactly `m` nonempty groups exist, without increasing a sum. Every larger limit is also feasible. If more than `m` groups are necessary, every smaller limit is impossible.

**Why the converged bound is optimal**

Binary search discards only ranges proved entirely feasible or infeasible by the monotone predicate. When the bounds meet, that value is feasible and its predecessor is not, so it is exactly the minimum possible largest group sum.

#### Complexity detail

Each feasibility check scans `n` values in $O(n)$ time. Binary search performs $O(\log S)$ checks over the range from the largest element to the total sum, giving $O(n \log S)$ time. Only scalar bounds and counters use $O(1)$ space.

#### Alternatives and edge cases

- **Partition dynamic programming:** tries every prior cut for every group and endpoint, taking $O(mn^2)$ time and $O(n)$ optimized space.
- **Enumerate all cut combinations:** grows combinatorially.
- **Greedily balance group sums without a tested limit:** local equalization choices do not guarantee a global optimum.
- With $m = 1$, the answer is the total sum.
- With $m = n$, the answer is the largest element.
- Zero values allow cuts without increasing any group sum.
- Nonnegativity is what makes greedy feasibility and monotonic splitting valid.

</details>
