# Number of Pairs of Strings With Concatenation Equal to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2023 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/) |

## Problem Description

### Goal

Given a list `nums` of digit strings and another digit string `target`, count
ordered pairs of indices `(i, j)` for which $i \ne j$ and concatenating
`nums[i]` followed by `nums[j]` produces exactly `target`.

Index order matters: `(i, j)` and `(j, i)` are different pairs when both
concatenations qualify. Equal string values at different indices also remain
distinct choices.

### Function Contract

Let $N$ be the number of strings, let $T$ be the length of `target`, and define

$$
S = \sum_{x \in \texttt{nums}} \lvert x \rvert.
$$

**Inputs**

- `nums`: a list of $N$ digit strings without leading zeros, where
  $2 \le N \le 100$ and each string has length from $1$ through $100$.
- `target`: a digit string without a leading zero, where $2 \le T \le 100$.

**Return value**

- The number of ordered pairs of different indices whose values concatenate
  to `target`.

### Examples

**Example 1**

- Input: `nums = ["777", "7", "77", "77"], target = "7777"`
- Output: `4`
- Explanation: The qualifying value pairs are `"777" + "7"`,
  `"7" + "777"`, and the two ordered choices of distinct `"77"` indices.

**Example 2**

- Input: `nums = ["123", "4", "12", "34"], target = "1234"`
- Output: `2`

**Example 3**

- Input: `nums = ["1", "1", "1"], target = "11"`
- Output: `6`
- Explanation: Any of three indices can be first and either remaining index
  can be second.
