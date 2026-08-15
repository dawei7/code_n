# Unique Substrings With Equal Digit Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2168 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Rolling Hash, Counting, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/) |

## Problem Description

### Goal

Given a string `s` made only of decimal digits, consider every nonempty
substring. A substring qualifies when all digits that occur in it have the
same frequency. Digits absent from that substring do not participate in the
comparison.

Count how many different substring values qualify. Uniqueness is based on the
digit sequence itself rather than its positions in `s`, so multiple
occurrences of identical text contribute only once.

### Function Contract

**Inputs**

- `s`: a string of length $n$, where $1\le n\le 1000$ and every character is a
  digit from `0` through `9`.

A substring is a contiguous, nonempty section of `s`.

**Return value**

Return the number of distinct substring strings in which every present digit
occurs equally often.

### Examples

#### Example 1

- **Input:** `s = "1212"`
- **Output:** `5`

The qualifying values are `"1"`, `"2"`, `"12"`, `"21"`, and `"1212"`.
Although `"12"` occurs twice, it is counted once.

#### Example 2

- **Input:** `s = "12321"`
- **Output:** `9`

The qualifying values are the three one-character strings, `"12"`, `"23"`,
`"32"`, `"21"`, `"123"`, and `"321"`.

#### Example 3

- **Input:** `s = "000"`
- **Output:** `3`

The distinct values `"0"`, `"00"`, and `"000"` each contain only one
present digit, so all three qualify.
