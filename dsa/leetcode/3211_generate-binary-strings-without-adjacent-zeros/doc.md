# Generate Binary Strings Without Adjacent Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3211 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/) |

## Problem Description

### Goal

Given a positive length `n`, generate every binary string of exactly that length for which each contiguous substring of length two contains at least one `"1"`.

The condition is evaluated for every neighboring pair in the string, including overlapping pairs at consecutive positions.

Equivalently, a valid result may contain zeros, but it must never contain two adjacent zeros. Return all such strings in any order, with each valid string appearing once.

### Function Contract

**Inputs**

- `n`: The required binary-string length, with $1 \le n \le 18$.

Let $V_n$ denote the number of valid length-$n$ strings. It follows the Fibonacci-style recurrence $V_n=V_{n-1}+V_{n-2}$.

**Return value**

- A list containing every length-$n$ binary string without the substring `"00"`. Result order is unrestricted.

### Examples

#### Example 1

- **Input:** `n = 3`
- **Output:** `["010","011","101","110","111"]`
- **Explanation:** These are exactly the five length-three strings that contain no adjacent zeros.

#### Example 2

- **Input:** `n = 1`
- **Output:** `["0","1"]`
- **Explanation:** A one-character string has no substring of length two, so both binary choices are valid.
