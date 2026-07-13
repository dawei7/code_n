# Find Anagram Mappings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 760 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-anagram-mappings/) |

## Problem Description

### Goal

Given integer arrays `nums1` and `nums2` containing the same values with the same multiplicities, construct an index mapping from the first array into the second.

For every index `i` in `nums1`, choose an index `j` such that `nums1[i] = nums2[j]`, and return all chosen `j` values in first-array order. When a value occurs more than once, any occurrence with that value is an acceptable mapping; the problem does not require a unique assignment among duplicates.

### Function Contract

**Inputs**

- `nums1`: the source integer array.
- `nums2`: an anagram of `nums1`, possibly with duplicate values.

**Return value**

- A list `mapping` of the same length where `nums1[i] = nums2[mapping[i]]` for every index `i`.

### Examples

**Example 1**

- Input: `nums1 = [12,28,46,32,50]`, `nums2 = [50,12,32,46,28]`
- Output: `[1,4,3,2,0]`
- Explanation: Each returned index locates the corresponding value from `nums1` in `nums2`.

**Example 2**

- Input: `nums1 = [1,2,1]`, `nums2 = [1,1,2]`
- Output: `[1,2,1]`
- Explanation: Either index `0` or `1` is valid for either occurrence of value `1`, so other valid mappings exist.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reverse the lookup direction**

The required output asks where each `nums1` value occurs in `nums2`. Build a hash table from every value in `nums2` to one of its indices. Then scan `nums1` and replace each value with its stored index.

**Why one stored index is enough**

For a value appearing multiple times, the contract accepts any matching occurrence; it does not require a unique assignment of occurrences. Overwriting an earlier index while building the table is therefore safe. For every output position `i`, the lookup was created from an actual position in `nums2` holding `nums1[i]`, so the returned mapping satisfies `nums1[i] = nums2[mapping[i]]`. Because the arrays are anagrams, every lookup is guaranteed to exist.

#### Complexity detail

Building the table and producing the mapping each take $O(n)$ expected time. The table and returned list each use $O(n)$ space in the worst case.

#### Alternatives and edge cases

- **Linear search for every source value:** Calling `nums2.index(value)` is simple and correct but can take $O(n^2)$ time.
- **Value-to-stack of indices:** Keeping every occurrence and popping indices creates a one-to-one occurrence assignment in $O(n)$ time, but that stronger property is unnecessary here.
- **Sort indexed pairs:** Sorting both arrays with original indices can construct a mapping in $O(n \log n)$ time and avoids hashing.
- **Duplicate values:** Reusing any index containing the requested value is valid.
- **Negative or large integers:** Hash-table keys handle them without requiring a bounded-value array.
- **Single-element arrays:** The only valid mapping is `[0]`.

</details>
