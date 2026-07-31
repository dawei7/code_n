# Form Smallest Number From Two Digit Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2605 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/) |

## Problem Description

### Goal

You are given two arrays, `nums1` and `nums2`, each containing unique digits from $1$ through $9$. The arrays may share digits, but no digit is repeated within either individual array.

Form a positive integer whose decimal representation contains at least one digit selected from `nums1` and at least one digit selected from `nums2`. A single digit satisfies both requirements when it occurs in both arrays; otherwise, the chosen digits may be arranged as a two-digit number. Return the smallest integer obtainable under these rules.

### Function Contract

**Inputs**

- `nums1`: A nonempty list of unique digits from $1$ through $9$.
- `nums2`: A nonempty list of unique digits from $1$ through $9$.

Each array contains at most $9$ elements.

**Return value**

- The smallest integer containing at least one digit from each input array.

### Examples

**Example 1**

- Input: `nums1 = [4,1,3], nums2 = [5,7]`
- Output: `15`

There is no shared digit. Using the smallest digit from each array and placing $1$ first produces the smallest valid two-digit number.

**Example 2**

- Input: `nums1 = [3,5,2,6], nums2 = [3,1,7]`
- Output: `3`

The digit $3$ occurs in both arrays, so the one-digit number $3$ satisfies both requirements.
