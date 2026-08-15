# Partition Array Such That Maximum Difference Is K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2294 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/) |

## Problem Description

### Goal

Partition every occurrence in the integer array `nums` into one or more
subsequences. Each original element must appear in exactly one subsequence,
and the relative order of elements assigned to the same subsequence is
preserved.

Within every chosen subsequence, the difference between its maximum and
minimum values must be at most `k`. Return the smallest possible number of
subsequences in such a partition.

Because any set of selected positions forms a subsequence when read in
increasing index order, feasibility depends on how values are grouped rather
than on their original arrangement.

### Function Contract

**Inputs**

- `nums`: A nonempty array of nonnegative integers whose occurrences must all be assigned.
- `k`: The maximum allowed difference between the largest and smallest value in one subsequence.

The contract guarantees $1 \le \lvert\texttt{nums}\rvert \le 10^5$,
$0 \le \texttt{nums}[i] \le 10^5$, and $0 \le k \le 10^5$.

**Return value**

The minimum number of subsequences needed to cover every occurrence while
keeping each subsequence's value range at most `k`.

### Examples

#### Example 1

- **Input:** `nums = [3, 6, 1, 2, 5]`, `k = 2`
- **Output:** `2`

#### Example 2

- **Input:** `nums = [1, 2, 3]`, `k = 1`
- **Output:** `2`

#### Example 3

- **Input:** `nums = [2, 2, 4, 5]`, `k = 0`
- **Output:** `3`
