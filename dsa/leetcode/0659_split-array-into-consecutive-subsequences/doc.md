# Split Array into Consecutive Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 659 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) |

## Problem Description
### Goal
You are given an integer array `nums` sorted in non-decreasing order. Determine whether all of its occurrences can be split into one or more subsequences such that every subsequence is a consecutive increasing sequence, with each integer exactly one greater than the previous integer.

Every resulting subsequence must have length `3` or more. Return `True` if such a complete split is possible and `False` otherwise. Each input occurrence must belong to exactly one subsequence; duplicate values are separate occurrences, and relative order is preserved within each subsequence.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers sorted in non-decreasing order; duplicate values represent distinct occurrences

**Return value**

- `True` if all occurrences can be partitioned into valid consecutive subsequences; otherwise `False`

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 3, 4, 5]`
- Output: `True`

**Example 2**

- Input: `nums = [1, 2, 3, 3, 4, 4, 5, 5]`
- Output: `True`

**Example 3**

- Input: `nums = [1, 2, 3, 4, 4, 5]`
- Output: `False`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Protect subsequences that have already started**

Count the unused occurrences of every value. Also record how many constructed subsequences currently end at each value. When processing an unused value `x`, first try to append it to a subsequence ending at $x - 1$. Such a subsequence may still be shorter than three, so abandoning it could make an otherwise valid partition impossible.

**Start a new subsequence only when it can be made valid immediately**

If no existing subsequence needs `x`, a new one may start only when unused occurrences of $x + 1$ and $x + 2$ are available. Consume all three values together and record a subsequence ending at $x + 2$. If neither extension nor a complete three-value start is possible, this occurrence cannot belong to any valid partition.

**Why extension before creation is the safe greedy choice**

Extending an existing sequence uses only `x`. Starting a new sequence commits `x`, $x + 1$, and $x + 2$. If an old sequence ending at $x - 1$ is left unextended, no later value can repair its missing consecutive step; using `x` to extend it therefore preserves at least as many future options. When no sequence needs `x`, reserving the next two values proves the new sequence already meets the minimum length. Every consumed occurrence belongs to exactly one recorded sequence, so completing the scan proves a valid partition.

#### Complexity detail

Building frequencies and processing the sorted array each take $O(N)$ expected time. Every occurrence is consumed once. The unused-frequency and sequence-end maps contain at most $O(N)$ distinct keys, using $O(N)$ space.

#### Alternatives and edge cases

- **Grouped counts of lengths one, two, and at least three:** processes each distinct value in linear time and constant state per group, but its transitions are less immediately intuitive.
- **Heap of sequence lengths by ending value:** always extends the shortest eligible sequence and is correct, but heap operations raise the worst-case time to $O(N \log N)$.
- **Backtracking over assignments:** explores many equivalent placements of duplicates and can grow exponentially.
- Fewer than three total values can never form a valid nonempty partition.
- A gap may end sequences of length at least three, but any length-one or length-two sequence before the gap makes the partition invalid.
- Duplicate values may start or extend different subsequences; one subsequence itself remains strictly consecutive.
- Negative values behave exactly like positive values because only differences of one matter.

</details>
