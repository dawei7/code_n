# Guess Number Higher or Lower

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 374 |
| Difficulty | Easy |
| Topics | Binary Search, Interactive |
| Official Link | [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/) |

## Problem Description
### Goal
A hidden integer has been chosen from the inclusive range `1..n`. The provided `guess(value)` API reports whether a proposed value is correct or whether the hidden number is lower or higher than that proposal.

Return the hidden integer while minimizing API calls by using each response to discard an impossible half of the remaining range. A correct response ends the search, and the hidden value is guaranteed to lie within the initial bounds. Avoid midpoint overflow for large `n`. The app receives `pick` only to emulate the same external API; the native solution must not access the hidden value directly.

### Function Contract
**Inputs**

- `n`: the inclusive upper bound of the search range
- `pick`: the offline app's hidden value. Native LeetCode supplies only `n` and exposes the provided `guess(value)` API.

**Return value**

- The hidden integer.

### Examples
**Example 1**

- Input: `n = 10, pick = 6`
- Output: `6`

**Example 2**

- Input: `n = 1, pick = 1`
- Output: `1`

**Example 3**

- Input: `n = 100, pick = 100`
- Output: `100`
