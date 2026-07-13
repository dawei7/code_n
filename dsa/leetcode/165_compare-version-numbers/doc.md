# Compare Version Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 165 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/compare-version-numbers/) |

## Problem Description
### Goal
Given two version numbers represented as strings of decimal revisions separated by dots, compare corresponding revisions from left to right. Interpret each revision as a nonnegative integer, so leading zeroes do not affect its value, and treat missing revisions beyond the end of a version as zero.

Return `-1` when `version1` is smaller, `1` when it is larger, and `0` when both represent the same revision sequence. Stop at the first unequal revision; trailing zero-valued revisions do not make a version larger. Comparison is numeric rather than lexicographic, so a revision such as `10` is greater than `2` despite its leading character.

### Function Contract
**Inputs**

- `version1`: first sequence of decimal revisions
- `version2`: second sequence of decimal revisions

**Return value**

`-1` when the first version is smaller, `1` when it is larger, and `0` when both represent the same revision sequence.

### Examples
**Example 1**

- Input: `version1 = "1.2", version2 = "1.10"`
- Output: `-1`

**Example 2**

- Input: `version1 = "1.01", version2 = "1.001"`
- Output: `0`

**Example 3**

- Input: `version1 = "1.0", version2 = "1.0.0.0"`
- Output: `0`

### Required Complexity

- **Time:** $O(m + n)$
- **Space:** $O(m + n)$

<details>
<summary>Approach</summary>

#### General

A version is an ordered sequence of integer revisions, not a decimal number and not an ordinary string. Thus `1.10` is greater than `1.2`, while `1.01` and `1.001` are equal because the second revisions both represent the integer one.

Split both strings at dots and compare corresponding revisions from left to right. If one sequence ends first, use zero for each missing revision. The first unequal pair decides the result; later revisions matter only while every earlier pair is equal.

When revision sizes fit comfortably in the language's integer type, parsing each component is enough. A representation-independent comparison avoids overflow:

1. Remove leading zeroes, treating an all-zero component as `"0"`.
2. A normalized component with more digits represents the larger integer.
3. If digit counts match, lexicographic order equals numeric order.

For `"1.0.12"` and `"1.00.3.0"`, revision one compares equal to one, zero compares equal to zero despite its spelling, and `12` exceeds `3`. The final `.0` is never reached because the first unequal revision has already fixed the ordering. Conversely, `"1"` and `"1.0.0"` compare equal because every absent component is interpreted as zero.

Normalizing a revision removes only leading zeroes, so it preserves its integer value. Digit-count comparison followed by lexicographic comparison therefore returns the exact order of two revision integers without numeric conversion. The algorithm processes revisions in their priority order and returns at the first unequal pair, exactly as lexicographic ordering of integer sequences requires. Padding the shorter sequence with zero implements the contract for omitted trailing revisions. If no pair differs, both versions represent the same revision sequence.

#### Complexity detail

Splitting, normalizing, and comparing visit $O(m + n)$ characters in total. Materialized component arrays and normalized strings use $O(m + n)$ space. A two-pointer parser can compare revisions directly from the original strings and reduce auxiliary space to $O(1)$ when desired.

#### Alternatives and edge cases

- Direct integer conversion is concise and safe in Python, but fixed-width languages may overflow on unusually long revisions.
- Comparing the complete strings lexicographically gives the wrong answer for `"1.2"` versus `"1.10"`.
- Comparing raw component strings mishandles both leading zeroes and different digit counts.
- Trailing zero revisions are insignificant: `"1"`, `"1.0"`, and `"1.0.0"` are equal.
- Many leading zeroes do not create a larger revision; an all-zero component normalizes to zero.

</details>
