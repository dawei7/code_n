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

### Required Complexity

- **Time:** $O(S+T^2)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Count available string values**

Build a frequency map for `nums`. Any valid ordered pair divides `target` at
one boundary between characters: its first value must equal the prefix before
that boundary, and its second value must equal the remaining suffix.

**Evaluate every nonempty split**

For each split position from `1` through `T - 1`, look up the prefix and suffix
counts. When the two strings differ, every prefix occurrence can pair with
every suffix occurrence, contributing their count product. When they are
equal, the second index cannot reuse the first, so a frequency `c` contributes
`c * (c - 1)` ordered choices.

Every qualifying index pair has one unique split determined by the length of
its first string, so it is counted exactly once. Conversely, each product
selects existing indices with the required prefix and suffix values, and the
equal-value formula excludes precisely the forbidden self-pairs. The sum is
therefore the requested number of ordered pairs.

#### Complexity detail

Building the frequency map reads $S$ input characters. Across all $T - 1$
split points, Python string slicing copies a total of $O(T^2)$ characters;
hash lookups are expected constant time after hashing those slices. Thus the
total expected time is $O(S+T^2)$. The frequency keys occupy $O(S)$ space in
the worst case, while temporary split strings use $O(T)$ space at a time.

#### Alternatives and edge cases

- **Nested index pairs:** Testing every `(i, j)` directly is simple and
  automatically handles duplicates, but takes $O(N^2T)$ time.
- **Scan each source as a prefix:** For every `nums[i]`, derive the needed
  suffix and use its frequency, subtracting the same index when necessary.
  This also works but may repeat prefix tests for duplicate values.
- The split endpoints are excluded because input strings are nonempty.
- Equal values may pair only when their frequency is at least two.
- A pair is ordered; a valid reversed pair is counted separately.
- A string equal to all of `target` cannot form a pair because the missing
  partner would be empty.

</details>
