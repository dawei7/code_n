# Count Words Obtained After Adding a Letter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2135 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Bit Manipulation, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/) |

## Problem Description
### Goal
You are given two arrays of lowercase English words. No letter appears more
than once within any individual word. To convert a start word, append exactly
one lowercase letter that is not already present, then rearrange all letters
in any order.

For each target word, determine independently whether at least one unchanged
word from `startWords` can be converted into it. The start words are only
tested as possibilities and are not consumed or modified between targets.
Return the number of obtainable target occurrences.

### Function Contract
**Inputs**

- `startWords`: Between $1$ and $5\cdot 10^4$ distinct-letter lowercase
  words, each of length from $1$ through $26$.
- `targetWords`: Between $1$ and $5\cdot 10^4$ target words under the same
  letter and length guarantees.

Let $L$ be the total number of characters across both arrays, and let $s$ be
the number of distinct letter sets represented by `startWords`.

**Return value**

The number of target word occurrences obtainable by adding exactly one new
letter to some start word and rearranging.

### Examples
**Example 1**

- Input: `startWords = ["ant","act","tack"]`,
  `targetWords = ["tack","act","acti"]`
- Output: `2`
- Explanation: `"tack"` and `"acti"` can come from `"act"`. The target
  `"act"` is not obtainable merely because it is already a start word; one
  new letter must be appended.

**Example 2**

- Input: `startWords = ["ab","a"]`, `targetWords = ["abc","abcd"]`
- Output: `1`
