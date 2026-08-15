# Remove Digit From Number to Maximize Result

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2259 |
| Difficulty | Easy |
| Topics | String, Greedy, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/) |

## Problem Description

### Goal

A string `number` represents a positive decimal integer using digits from `1`
through `9`. A separate one-character string `digit` is guaranteed to occur in
`number`.

Remove exactly one occurrence of `digit`. The remaining characters keep their
original order and form another decimal representation with one fewer digit.
Among every valid occurrence that could be removed, choose the result with the
greatest numerical value and return that result as a string. Repeated
occurrences are separate choices even when some choices produce equal strings.

### Function Contract

**Inputs**

- `number`: A string of $n$ digits from `1` through `9`, where $2\le n\le100$.
- `digit`: One digit from `1` through `9` that occurs at least once in `number`.

**Return value**

Return the length-$n-1$ string obtained by deleting exactly one occurrence of
`digit` whose decimal value is greatest.

### Examples

#### Example 1

- **Input:** `number = "123", digit = "3"`
- **Output:** `"12"`

#### Example 2

- **Input:** `number = "1231", digit = "1"`
- **Output:** `"231"`

#### Example 3

- **Input:** `number = "551", digit = "5"`
- **Output:** `"51"`
