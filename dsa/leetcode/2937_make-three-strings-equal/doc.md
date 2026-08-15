# Make Three Strings Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2937 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-three-strings-equal/) |

## Problem Description

### Goal

Given strings `s1`, `s2`, and `s3`, one operation chooses one string and
deletes its rightmost character. A string may never be made empty, and deleting
characters from any other position is not allowed. Perform operations until
all three strings are exactly equal.

Return the minimum number of operations needed. If the strings cannot be made
equal without emptying one of them, return `-1`. All three inputs are nonempty
lowercase English strings and may initially have different lengths.

### Function Contract

**Inputs**

- `s1`: The first nonempty lowercase string.
- `s2`: The second nonempty lowercase string.
- `s3`: The third nonempty lowercase string.

Each input length is between 1 and 100 inclusive. Let
$L=\min(\lvert\texttt{s1}\rvert,\lvert\texttt{s2}\rvert,\lvert\texttt{s3}\rvert)$.

**Return value**

- The minimum number of rightmost-character deletions that makes the strings equal, or `-1` if no nonempty result is possible.

### Examples

#### Example 1

- **Input:** `s1 = "abc", s2 = "abb", s3 = "ab"`
- **Output:** `2`
- **Explanation:** Delete the final character from `s1` and `s2`, leaving `"ab"` in all three strings.

#### Example 2

- **Input:** `s1 = "dac", s2 = "bac", s3 = "cac"`
- **Output:** `-1`
- **Explanation:** Their first characters differ, and right-end deletion cannot change that mismatch without emptying a string.
