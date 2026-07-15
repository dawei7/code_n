# Divide Array in Sets of K Consecutive Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1296 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/) |

## Problem Description
### Goal
Given an integer array `nums` and a positive integer `k`, determine whether every array element can be assigned to a set of exactly `k` consecutive integer values. A set beginning at $x$ must contain $x, x+1, \ldots, x+k-1$, using one occurrence of each value.

The sets form a partition: every occurrence in `nums` must be used once, duplicate values may belong to different sets, and the original array order is irrelevant. Return `true` when such a division exists and `false` otherwise.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `k`: the required size of every set, where $1 \le k \le n$.

**Return value**

`true` if all occurrences can be partitioned into sets of `k` consecutive numbers; otherwise, `false`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,3,4,4,5,6]`, `k = 4`
- Output: `true`
- Explanation: The sets can be `[1,2,3,4]` and `[3,4,5,6]`.

**Example 2**

- Input: `nums = [3,2,1,2,3,4,3,4,5,9,10,11]`, `k = 3`
- Output: `true`
- Explanation: One partition is `[1,2,3]`, `[2,3,4]`, `[3,4,5]`, and `[9,10,11]`.

**Example 3**

- Input: `nums = [1,2,3,4]`, `k = 3`
- Output: `false`
- Explanation: Four elements cannot be split into sets of three.

### Required Complexity
- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Why the smallest unused value fixes a group start**

Count every value and process distinct values in ascending order. Suppose `start` is the smallest value whose remaining frequency is positive. It cannot be placed later inside a consecutive set: that would require a still-smaller unused predecessor, contradicting the choice of `start`. Therefore every remaining copy of `start` must begin a set.

Let `copies = counts[start]`. Those `copies` sets each need one occurrence of every value from `start` through `start + k - 1`. If any required frequency is below `copies`, no valid partition can exist. Otherwise subtract `copies` from all of those frequencies at once.

Processing starts from left to right never takes a value needed by an earlier undecided set, because all sets beginning at smaller values have already been forced and removed. If every subtraction succeeds, all occurrences have been assigned to valid sets, so the partition exists. A preliminary divisibility check rejects lengths that cannot be split into equal groups.

#### Complexity detail

Building the frequency map takes $O(n)$ time. Sorting at most $n$ distinct keys costs $O(n \log n)$. Across all positive starts, the bulk-subtraction loops perform at most $n$ value visits because each such visit accounts for at least one consumed occurrence. The frequency map and sorted keys use $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Min-heap of distinct values:** Repeatedly extracting the current minimum can implement the same greedy rule, but heap operations add bookkeeping without improving the $O(n \log n)$ bound.
- **Repeated minimum-map scans:** Finding the smallest remaining key by scanning the entire map is correct, but it can degrade to $O(n^2)$.
- **Length not divisible by `k`:** A partition is impossible before any frequency work begins.
- **Duplicate values:** All remaining copies of the smallest value must start separate sets simultaneously; subtracting their full frequency enforces this.
- **`k = 1`:** Every element forms a valid singleton set.
- **Missing successor:** A gap or insufficient successor frequency makes the required subtraction fail immediately.

</details>
