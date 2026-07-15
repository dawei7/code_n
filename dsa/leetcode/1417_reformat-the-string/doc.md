# Reformat The String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1417 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/reformat-the-string/) |

## Problem Description

### Goal

The string `s` contains only lowercase English letters and decimal digits. Rearrange all of its characters so that every adjacent pair contains one letter and one digit; equivalently, character types must alternate throughout the result.

Return any rearrangement satisfying that rule while preserving every original character occurrence. If no such arrangement exists, return the empty string. Characters of the same type may appear in any relative order, so more than one returned string can be correct.

### Function Contract

**Inputs**

- `s`: a string of length $n$, where $1 \le n \le 500$, containing only lowercase English letters and digits.

**Return value**

- Any permutation of `s` whose adjacent characters alternate between letter and digit, or `""` if no such permutation exists.

### Examples

**Example 1**

- Input: `s = "a0b1c2"`
- Output: `"0a1b2c"`

**Example 2**

- Input: `s = "leetcode"`
- Output: `""`

**Example 3**

- Input: `s = "covid2019"`
- Output: `"c2o0v1i9d"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Separate the two character types.** Collect the letters in one list and the digits in another. An alternating sequence can use at most one more character of one type than of the other. Therefore, if their counts differ by more than one, no valid answer exists.

**Start with the larger group.** When the counts are equal, either type may come first. When one group has one extra character, that group must occupy both the first and last positions. Select the larger group as the first sequence and append one character from each group in turn, adding its final unmatched character when necessary.

The construction preserves every occurrence because each collected character is consumed exactly once. Consecutive output positions come from different groups by construction. The count condition is also sufficient: equal groups pair completely, while a one-character surplus fits at one end. Thus returning empty precisely when the difference exceeds one is correct.

#### Complexity detail

Classifying and interleaving the $n$ characters each take $O(n)$ time. The two groups and the output together use $O(n)$ space.

#### Alternatives and edge cases

- **Repeated search and removal:** Find the next required type in a mutable character list. It is correct but repeated scans and shifts can take $O(n^2)$ time.
- **In-place swapping:** Place one type at even indices and the other at odd indices. This can reduce temporary grouping but is easier to implement incorrectly when counts differ.
- **Equal counts:** Either a letter or a digit may occupy the first position.
- **One-character input:** A single letter or digit already satisfies the adjacency rule.
- **Duplicate characters:** Preserve multiplicity; character uniqueness is not required.
- **Impossible imbalance:** Two or more extra characters of either type force two same-type neighbors.
- **Semantic output:** Any valid alternating permutation is acceptable, not only the example ordering.

</details>
