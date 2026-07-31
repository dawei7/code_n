# Find Common Elements Between Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2956 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-common-elements-between-two-arrays/) |

## Problem Description
### Goal
You are given two integer arrays, `nums1` and `nums2`, with lengths $N$ and
$M$. Determine two values based on whether each indexed element also occurs in
the other array.

The first value is the number of indices `i` in `nums1` for which the value
`nums1[i]` exists somewhere in `nums2`. The second is defined symmetrically for
indices in `nums2` whose values occur in `nums1`. Occurrences are counted by
index: if a shared value appears several times in one array, every one of those
positions contributes to that array's answer.

Return the two counts as `[answer1, answer2]`.

### Function Contract
**Inputs**

- `nums1`: the first integer array
- `nums2`: the second integer array

Let $N=\lvert\texttt{nums1}\rvert$ and $M=\lvert\texttt{nums2}\rvert$. The
contract guarantees $1\le N,M\le100$ and every array value lies from $1$ to
$100$, inclusive.

**Return value**

A two-element array whose first entry counts qualifying indices in `nums1` and
whose second entry counts qualifying indices in `nums2`.

### Examples
**Example 1**

- Input: `nums1 = [2,3,2], nums2 = [1,2]`
- Output: `[2,1]`
- Explanation: Both positions containing `2` in `nums1` count, while the single `2` in `nums2` counts once.

**Example 2**

- Input: `nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]`
- Output: `[3,4]`
- Explanation: The `2` and both `3` positions qualify in the first array; three `2` positions and the `3` qualify in the second.

**Example 3**

- Input: `nums1 = [3,4,2,3], nums2 = [1,5]`
- Output: `[0,0]`
- Explanation: The arrays share no value, so neither contains a qualifying index.
