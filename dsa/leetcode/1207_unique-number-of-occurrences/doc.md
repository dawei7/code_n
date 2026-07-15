# Unique Number of Occurrences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1207 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-number-of-occurrences/) |

## Problem Description

### Goal

You are given an integer array `arr`. For each distinct integer appearing in the array, its number of occurrences is the count of positions that contain that value. The values themselves may be equal only when they represent the same distinct integer; positive, negative, and zero values are all counted in the same way.

Determine whether these occurrence counts are unique across the distinct values. Return `true` exactly when no two different integers occur the same number of times. If any pair of distinct integers has an equal occurrence count, return `false`.

### Function Contract

**Inputs**

- `arr`: An integer array of length $n$, where $1\le n\le1000$ and every value lies between $-1000$ and $1000$, inclusive.
- Let $k$ be the number of distinct values in `arr`.

**Return value**

- `true` if all $k$ occurrence counts are pairwise distinct; otherwise `false`.

### Examples

**Example 1**

- Input: `arr = [1,2,2,1,1,3]`
- Output: `true`

The values `1`, `2`, and `3` occur three, two, and one time respectively.

**Example 2**

- Input: `arr = [1,2]`
- Output: `false`

Both distinct values occur once.

**Example 3**

- Input: `arr = [-3,0,1,-3,1,1,1,-3,10,0]`
- Output: `true`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Count values before comparing counts.** Traverse `arr` once and store each value's frequency in a hash map. At the end, that map contains exactly one integer count for each of the $k$ distinct input values.

**Use a second set for the codomain.** Traverse the frequency values. If a count is already in a set of previously observed counts, two distinct input values share that frequency, so return `false` immediately. Otherwise insert the count and continue. Reaching the end means every frequency was new and the answer is `true`.

This test is exact because the map associates one frequency with every distinct array value, and set insertion detects precisely whether the mapping from values to frequencies is one-to-one. The identities and signs of the input values do not matter after their counts are known.

#### Complexity detail

Building the frequency map takes $O(n)$ expected time, and checking its $k$ values takes $O(k)$ expected time. Since $k\le n$, total expected time is $O(n)$. The map and frequency set together store $O(k)$ entries.

#### Alternatives and edge cases

- **Sort the array:** Equal values become contiguous and their run lengths can be inserted into a set, but sorting raises the time bound to $O(n\log n)$.
- **Recount each distinct value:** Calling a full-array count for every value takes $O(nk)$ time.
- **Pairwise frequency comparison:** After counting, comparing every pair of the $k$ frequencies takes $O(k^2)$ time instead of using a set.
- **Single distinct value:** Its only frequency is necessarily unique, so the result is `true`.
- **All values distinct:** When $n>1$, every value has frequency one, so the result is `false`.
- **Negative and zero values:** Hash keys handle them exactly like positive values.
- **Late collision:** Equal frequencies must be detected even when the corresponding values occur far apart in the array.

</details>
