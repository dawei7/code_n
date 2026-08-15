# Number of Ways to Select Buildings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2222 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-select-buildings/) |

## Problem Description

### Goal

A 0-indexed binary string describes buildings along a street. Character `0` represents an office, while `1` represents a restaurant.

Select exactly three buildings at strictly increasing indices. To provide variety, adjacent buildings within the selected triple must have different types, so the chosen types must form either `010` or `101`. Return the number of distinct index triples satisfying this condition.

### Function Contract

**Inputs**

- `s`: A binary string containing at least three characters.

Let $n=\lvert s\rvert$.

**Return value**

Return the number of increasing index triples whose selected characters alternate.

### Examples

#### Example 1

- **Input:** `s = "001101"`
- **Output:** `6`

#### Example 2

- **Input:** `s = "11100"`
- **Output:** `0`

#### Example 3

- **Input:** `s = "010"`
- **Output:** `1`
