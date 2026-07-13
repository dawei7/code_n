# Intersection of Two Arrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 350 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/intersection-of-two-arrays-ii/) |

## Problem Description
### Goal
Given two integer arrays, compute their multiset intersection. For each value, the output may use only occurrences supported independently by both inputs rather than treating repeated values as one set member.

If a value occurs $a$ times in the first array and $b$ times in the second, include it exactly $\min(a,b)$ times. Return all such occurrences in any order. Values appearing in only one array contribute nothing, and each input occurrence can be matched at most once. If no value is shared, the result is empty; otherwise duplicates must be preserved up to the shared multiplicity.

### Function Contract
**Inputs**

- `nums1`: the first integer array
- `nums2`: the second integer array

**Return value**

- A list containing each shared value with the multiplicity supported by both arrays, in any order.

### Examples
**Example 1**

- Input: `nums1 = [1, 2, 2, 1], nums2 = [2, 2]`
- Output: `[2, 2]`

**Example 2**

- Input: `nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]`
- Output: `[4, 9]`

**Example 3**

- Input: `nums1 = [1, 2], nums2 = [1, 1]`
- Output: `[1]`

### Required Complexity

- **Time:** $O(n + m)$
- **Space:** $O(\min(n, m))$

<details>
<summary>Approach</summary>

#### General

**Treat each occurrence as consumable supply**

Unlike the unique-set version, a membership bit is insufficient: every match consumes one available occurrence. Count values from the shorter array so the auxiliary map is as small as possible. Then scan the longer array. When its current value has a positive remaining count, append the value and decrement that count; otherwise skip it.

**Why every multiplicity is exact**

For each value $x$, the counter begins at its occurrence count in the shorter array. The scan can append $x$ no more than once per occurrence in the longer array, and decrementing prevents it from appending more than the shorter side provides. Thus $x$ appears at most $\min(\operatorname{count}_1(x),\operatorname{count}_2(x))$ times. Every scan occurrence is accepted until one side's supply is exhausted, so that upper bound is reached exactly.

**Trace a fully consumed count**

For `[1, 2, 2, 1]` and `[2, 2]`, count the shorter array as `{2: 2}`. The first two encountered `2` values are appended and reduce the remaining supply to zero; additional copies would be ignored.

#### Complexity detail

Counting the shorter array and scanning the longer one take $O(n + m)$ expected time. The frequency map has at most $\min(n,m)$ keys, and the result can contain at most that many elements, so total space is $O(\min(n, m))$ including output.

#### Alternatives and edge cases

- **Sort both arrays and use two pointers:** costs $O(n \log n + m \log m)$ but is attractive when inputs are already sorted or sequential external-memory access matters.
- **Search and remove each match:** can take $O(nm)$ because both list membership and removal are linear.
- An empty input produces an empty intersection.
- Negative values and zero need no special handling.
- Duplicate output is intentional, but each value's multiplicity cannot exceed its smaller input frequency.

</details>
