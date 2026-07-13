# Permutation in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 567 |
| Difficulty | Medium |
| Topics | Hash Table, Two Pointers, String, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/permutation-in-string/) |

## Problem Description
### Goal
Given two strings `s1` and `s2`, determine whether `s2` contains a permutation of `s1`. More precisely, look for a contiguous substring of `s2` whose characters can be rearranged to produce exactly `s1`; the order of those characters inside the substring does not have to match their order in `s1`.

Return `True` when at least one such substring exists and `False` otherwise. A valid substring must have length `len(s1)` and the same multiplicity of every lowercase English letter, so matching only the set of distinct characters is insufficient.

### Function Contract
**Inputs**

- `s1`: the lowercase string whose character multiset must be matched
- `s2`: the lowercase string to search

**Return value**

- `True` if some length-`len(s1)` substring of `s2` has exactly the same character frequencies; otherwise `False`

### Examples
**Example 1**

- Input: `s1 = "ab", s2 = "eidbaooo"`
- Output: `True`

**Example 2**

- Input: `s1 = "ab", s2 = "eidboaoo"`
- Output: `False`

**Example 3**

- Input: `s1 = "adc", s2 = "dcda"`
- Output: `True`

### Required Complexity

- **Time:** $O(m + n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A permutation is a frequency match**

Order inside the candidate substring does not matter. Because the inputs contain only lowercase English letters, represent `s1` and a window of `s2` with two fixed arrays of 26 counts.

**Use exactly the target length**

Only a substring of length `m = len(s1)` can contain the same multiset. Build the first window of that length, then move it one position at a time by removing its left character and adding the new right character.

**Track matching frequency slots**

Count how many of the 26 window frequencies currently equal their target frequencies. Before changing a letter count, remove its equality contribution; after the change, add the contribution back if equality was restored. All 26 slots matching means the current window is a permutation.

**Reject an impossible length immediately**

If `s1` is longer than `s2`, no complete target-length window exists.

**Why a match count of 26 is exact**

The window and target always describe strings of the same length. When all 26 per-letter counts agree, the two strings contain identical character multisets, so one is a permutation of the other. Conversely, any permutation substring has identical counts in every slot and will make the match count 26 when its window is examined.

#### Complexity detail

Building the target and first-window counts takes $O(m)$ time. Each of the remaining $n - m$ slides performs two constant-time updates, so total time is $O(m + n)$. Two 26-entry arrays use $O(1)$ space.

#### Alternatives and edge cases

- **Compare both 26-entry arrays after every slide:** is also linear because the alphabet size is constant, though it performs more fixed work per window.
- **Sort every substring:** is correct but costs $O((n - m + 1) m \log m)$ time.
- **Recount every window:** avoids sorting but still takes $O(nm)$ time.
- **Target longer than search text:** returns `False` immediately.
- **Equal strings:** the first window matches.
- **Repeated letters:** exact multiplicities, not only character membership, determine a permutation.
- **Match at the final window:** the entering and leaving updates must occur before the last equality check.

</details>
