# Sum of Scores of Built Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2223 |
| Difficulty | Hard |
| Topics | String, Binary Search, Rolling Hash, Suffix Array, String Matching, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-scores-of-built-strings/) |

## Problem Description

### Goal

Build a final string `s` by prepending one character at a time. The intermediate string of length $i$ is named $s_i$, and $s_n$ is the complete string. Equivalently, the intermediate strings are all suffixes of the final string.

The score of $s_i$ is the length of its longest common prefix with the complete string $s_n$. Return the sum of the scores of all $n$ intermediate strings, including the full string's score of $n$.

### Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

Let $n=\lvert s\rvert$.

**Return value**

Return the sum, over every suffix of `s`, of the suffix's longest common prefix length with `s`.

### Examples

#### Example 1

- **Input:** `s = "babab"`
- **Output:** `9`

#### Example 2

- **Input:** `s = "azbazbzaz"`
- **Output:** `14`

#### Example 3

- **Input:** `s = "aaaa"`
- **Output:** `10`
