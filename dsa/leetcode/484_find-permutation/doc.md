# Find Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 484 |
| Difficulty | Medium |
| Topics | Array, String, Stack, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/find-permutation/) |

## Problem Description
### Goal
Given a pattern string `s` containing only `I` and `D`, construct a permutation of the integers from `1` through `len(s) + 1`. At pattern position `i`, `I` requires the value at permutation position `i` to be smaller than the next value, while `D` requires it to be larger.

Return the lexicographically smallest permutation satisfying every adjacent comparison. Use each integer in the required range exactly once, preserve the pattern's left-to-right comparison positions, and do not return a merely valid permutation when a smaller valid prefix is possible. A run of consecutive `D` characters may require several values to appear in reverse order.

### Function Contract
**Inputs**

- `s`: a nonempty string containing only `I` and `D`

**Return value**

- The lexicographically smallest permutation whose adjacent comparisons match `s`

### Examples
**Example 1**

- Input: `s = "I"`
- Output: `[1, 2]`

**Example 2**

- Input: `s = "DI"`
- Output: `[2, 1, 3]`

**Example 3**

- Input: `s = "DDIIDI"`
- Output: `[3, 2, 1, 4, 6, 5, 7]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Start from the lexicographically smallest value order**

The ascending permutation $[1,2,\ldots,n+1]$ is the smallest possible sequence before enforcing decreases. An `I` already agrees with this order, so only maximal runs of `D` need to change it.

**A decrease run forces one reversed block**

If `s[left:right]` is a maximal run of `D`, the corresponding `right - left + 1` adjacent comparisons require `right - left + 2` values in descending order. Reverse exactly that block of the ascending permutation. Distinct decrease runs use disjoint blocks, so their total reversal work is linear.

**Why using the next smallest block is optimal**

At the start of each block, every smaller unused value must be placed before every larger unused value to minimize the earliest position where choices differ. The required descending order then uniquely determines the arrangement of those smallest available values. At an `I` boundary, the next untouched block begins with larger values, so the boundary comparison is automatically increasing. Thus every constraint holds and no valid permutation can have a smaller first differing value.

**Finish the trailing run**

Treat the position after the final pattern character like an `I` boundary. This closes and reverses a trailing `D` run, while a pattern ending in `I` merely reverses a one-element block.

#### Complexity detail

Building the initial permutation takes $O(n)$ time. Each position belongs to exactly one reversed block, so all swaps also total $O(n)$. The returned permutation uses $O(n)$ space; apart from that output, the algorithm uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Stack flush at each `I`:** push consecutive values and pop the entire stack at every increase boundary; it is also linear but uses $O(n)$ auxiliary stack space.
- **Repeated adjacent swaps:** can reverse each decrease block through bubble-like swaps, but a long `D` run takes $O(n^2)$ time.
- **Enumerate permutations:** eventually finds the lexicographic minimum but is factorial and unusable beyond tiny patterns.
- **All increases:** leaves the ascending permutation unchanged.
- **All decreases:** reverses the entire range into descending order.
- **Single character:** returns either `[1, 2]` for `I` or `[2, 1]` for `D`.
- **Separated decrease runs:** reverse each maximal run independently; do not combine values across an intervening `I`.

</details>
