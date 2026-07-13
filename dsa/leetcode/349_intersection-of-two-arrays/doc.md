# Intersection of Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 349 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/) |

## Problem Description
### Goal
Given two integer arrays, identify the values that occur at least once in both arrays. Original positions and occurrence counts beyond the first presence do not affect membership in this intersection.

Each element in the result must be unique, and the result may be returned in any order. Duplicate occurrences in either input must not create duplicate output entries, while negative values and zero follow ordinary integer equality. If the arrays share no value, return an empty list. The function returns set-style shared values rather than index pairs or the multiset intersection.

### Function Contract
**Inputs**

- `nums1`: the first integer array
- `nums2`: the second integer array

**Return value**

- A list containing the unique intersection of the two arrays in any order.

### Examples
**Example 1**

- Input: `nums1 = [1, 2, 2, 1], nums2 = [2, 2]`
- Output: `[2]`

**Example 2**

- Input: `nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]`
- Output: `[4, 9]`

**Example 3**

- Input: `nums1 = [1, 2, 3], nums2 = [4, 5, 6]`
- Output: `[]`

### Required Complexity

- **Time:** $O(n + m)$
- **Space:** $O(\min(n, m))$

<details>
<summary>Approach</summary>

#### General

**Reduce both requirements to set membership**

Fast membership testing is the only information needed. Build a set from the shorter array so its duplicate values collapse and its elements can be queried in average constant time. Scan the longer array and add every value found in that set to a result set; the result set prevents repeated matches from appearing more than once.

**Why the result contains exactly the shared values**

For any returned value, membership in the shorter-array set and its occurrence during the longer-array scan prove that it belongs to both inputs. Conversely, every value shared by the arrays is present in the membership set and encountered in the scan, so it is added. Set uniqueness gives exactly one copy, establishing both directions of the required result.

**Trace duplicate input values**

With `[1, 2, 2, 1]` and `[2, 2]`, the shorter side becomes `{2}`. Both scanned occurrences match, but inserting them into the result set still produces only `{2}`.

#### Complexity detail

Let the input lengths be $n$ and $m$. Building the smaller set and scanning the other array take $O(n + m)$ expected time. The membership set and unique result each contain at most $\min(n,m)$ values, so space is $O(\min(n, m))$, including the returned collection.

#### Alternatives and edge cases

- **Sort both arrays and use two pointers:** takes $O(n \log n + m \log m)$ time but can avoid hash storage when mutating the inputs is acceptable.
- **Linear membership for every candidate:** can degrade to $O(nm)$, especially when the arrays are disjoint.
- If either input is empty, the intersection is empty.
- Negative values and zero are ordinary set keys.
- Duplicates on either or both sides never create duplicate output values.

</details>
