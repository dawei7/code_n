# Minimum Index Sum of Two Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 599 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-index-sum-of-two-lists/) |

## Problem Description
### Goal
Given two arrays of distinct strings, `list1` and `list2`, find their common strings. For a string appearing at `list1[i]` and `list2[j]`, define its index sum as $i + j$, using the string's position in each list.

Return every common string with the least index sum, in any order. More than one string may share that least sum, and all such ties must be included; common strings with a larger sum are excluded even when they rank highly in one list.

### Function Contract
**Inputs**

- `list1: list[str]`: the first preference list with distinct strings
- `list2: list[str]`: the second preference list with distinct strings

**Return value**

- Every common string minimizing `index_in_list1 + index_in_list2`
- Results may be returned in any order

### Examples
**Example 1**

- Input: `["Shogun","Tapioca Express","Burger King","KFC"]` and `["KFC","Shogun","Burger King"]`
- Output: `["Shogun"]`

**Example 2**

- Input: the same first list and `["KFC","Burger King","Tapioca Express","Shogun"]`
- Output: all four restaurant names in any order because every index sum is three

**Example 3**

- Input: `["happy","sad","good"]` and `["sad","happy","good"]`
- Output: `["happy","sad"]` in any order

### Required Complexity

- **Time:** $O(m + n)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**Index one preference list**

Build a hash map from every string in `list1` to its index. Distinct entries make each lookup unambiguous.

**Scan common strings in the second list**

For each string at index `j` in `list2`, use the map to find index `i` when it is common. Compare $i + j$ with the smallest sum seen.

**Replace on improvement and append on ties**

A smaller sum invalidates all previous candidates, so reset the result to the current string. An equal sum adds another valid answer. Larger sums are ignored.

**Why the result is complete and minimal**

Every possible common string is encountered exactly once during the second-list scan, and its exact index sum is computed from the map. The maintained best value is therefore the minimum among all processed common strings. Replacement removes nonminimal candidates, while tie appends preserve every string attaining that minimum; after the full scan, exactly all optimal strings remain.

#### Complexity detail

For list lengths `m` and `n`, building the map takes $O(m)$ expected time and scanning the second list takes $O(n)$, for $O(m + n)$ total time. The map stores `m` entries, so extra space is $O(m)$.

#### Alternatives and edge cases

- **Index the shorter list:** can reduce auxiliary space while preserving $O(m + n)$ expected time, provided index sums use the correct original positions.
- **Nested scans or repeated `list.index`:** use little extra space but can take $O(mn)$ time.
- **Sort strings with indices:** can find intersections but costs $O((m + n) \log(m + n))$ time.
- **One common string:** it is necessarily the answer.
- **Several tied strings:** return all of them.
- **Common strings with larger sums:** exclude them even if they appear early in one list.
- **Input order:** determines index sums and must not be sorted away before scoring.
- **Output order:** is unrestricted.

</details>
