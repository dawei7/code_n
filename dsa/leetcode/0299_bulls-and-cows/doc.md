# Bulls and Cows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 299 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bulls-and-cows/) |

## Problem Description
### Goal
Given equally long decimal strings `secret` and `guess`, compare their digit occurrences. A bull is a position where both strings contain the same digit. After removing all bulls, a cow is a remaining guess digit that can be paired with the same digit at a different secret position.

Return the hint as `"xAyB"`, where `x` is the bull count and `y` is the cow count. Each digit occurrence may participate in at most one match, so repeated digits must not be overcounted. Bulls take priority over cows, and unmatched occurrences contribute nothing. Leading zeroes remain ordinary digit positions because both inputs are strings.

### Function Contract
**Inputs**

- `secret`: a string of decimal digits
- `guess`: a decimal string with the same length as `secret`

**Return value**

A hint formatted as `"xAyB"`, where `x` is the number of exact-position matches (bulls) and `y` is the number of additional value-only matches (cows).

### Examples
**Example 1**

- Input: `secret = "1807", guess = "7810"`
- Output: `"1A3B"`

**Example 2**

- Input: `secret = "1123", guess = "0111"`
- Output: `"1A1B"`

**Example 3**

- Input: `secret = "1", guess = "0"`
- Output: `"0A0B"`
