# Sort Characters By Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 451 |
| Difficulty | Medium |
| Topics | Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/) |

## Problem Description
### Goal
Given a string containing letters and digits, sort it in decreasing order based on the frequency of each case-sensitive character.

Return the sorted string, grouping each character's occurrences together according to decreasing frequency. When several characters have equal counts, return any valid group order. Preserve every occurrence exactly once and do not merge uppercase and lowercase forms. The task returns one valid reordered string rather than the frequency table.

### Function Contract
**Inputs**

- `s`: a string containing letters and digits

**Return value**

- A permutation of `s` ordered by nonincreasing character frequency. Characters with equal frequencies may appear in any relative order.

### Examples
**Example 1**

- Input: `s = "tree"`
- Output: `"eetr"`

**Example 2**

- Input: `s = "cccaaa"`
- Output: `"cccaaa"` (the tied groups may be reversed)

**Example 3**

- Input: `s = "Aabb"`
- Output: `"bbAa"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Count before arranging**

Scan the string once and map every distinct character to its total occurrence count. The largest possible count is `n`, so a count itself can serve as a bucket index.

**Bucket characters by frequency**

Create $n + 1$ buckets. Put each distinct character into the bucket matching its count, then visit bucket indices from `n` down to `1`. For a character in bucket `f`, append exactly `f` copies. Every input occurrence is emitted once, and descending bucket order directly enforces the requested frequency order.

**Why tie order is irrelevant**

Characters sharing a bucket have the same total frequency. Emitting either one first cannot violate nonincreasing frequency, so no secondary sort is needed. The result preserves the input multiset because each counted character contributes precisely its recorded number of copies.

#### Complexity detail

Counting and emitting account for $O(n)$ work. Scanning the $n + 1$ buckets is also $O(n)$, so total time is $O(n)$. The frequency table, buckets, and output pieces use $O(n)$ space.

#### Alternatives and edge cases

- **Maximum heap over distinct characters:** emits groups in frequency order in $O(n + k \log k)$ time for `k` distinct characters and avoids $n + 1$ buckets.
- **Sort distinct characters:** sorting the `k` frequency entries costs $O(n + k \log k)$ and is often concise.
- **Sort every occurrence:** using its character frequency as a key costs $O(n \log n)$ and stores redundant keys.
- **Repeated full-string counting:** calling a linear count operation for every occurrence can degrade to $O(n^2)$.
- **Equal frequencies:** any ordering among tied character groups is valid.
- **Case sensitivity:** uppercase and lowercase characters are different keys.
- **Single character or empty input:** return the input unchanged.

</details>
