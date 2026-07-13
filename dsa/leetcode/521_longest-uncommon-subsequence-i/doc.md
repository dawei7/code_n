# Longest Uncommon Subsequence I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 521 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-uncommon-subsequence-i/) |

## Problem Description
### Goal
A subsequence is formed by deleting zero or more characters without changing the relative order of those retained. Given strings `a` and `b`, an uncommon subsequence is a string that is a subsequence of exactly one input: it belongs to one string but not the other.

Return the maximum possible length of an uncommon subsequence, or `-1` when none exists. The candidate may equal one complete input string, and it need not be contiguous inside its source. If the two inputs are identical, every subsequence of one also belongs to the other; otherwise their unequal complete texts determine the longest possible length.

### Function Contract
**Inputs**

- `a`, `b`: two lowercase English strings

**Return value**

- The longest uncommon-subsequence length, or `-1` when every subsequence is shared

### Examples
**Example 1**

- Input: `a = "aba", b = "cdc"`
- Output: `3`

**Example 2**

- Input: `a = "aaa", b = "bbb"`
- Output: `3`

**Example 3**

- Input: `a = "aaa", b = "aaa"`
- Output: `-1`

### Required Complexity

- **Time:** $O(|a| + |b|)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Equal strings share every subsequence**

If $a = b$, selecting any index sequence from one string selects the same characters from the other. No subsequence can belong to exactly one input, so return `-1`.

**Different lengths make the longer whole string uncommon**

When lengths differ, the longer input is a subsequence of itself but cannot be a subsequence of the shorter input. Its full length is therefore achievable, and no subsequence can be longer than its source string.

**Different strings of equal length are uncommon in full**

A subsequence having the same length as its source must retain every character. Thus one equal-length input could be a subsequence of the other only if the strings were identical. When they differ, either complete string is uncommon and their shared length is optimal.

**Collapse all cases into one expression**

The two nonidentical cases both return `max(len(a),len(b))`; only equality returns `-1`. No subsequence enumeration or dynamic programming is needed.

#### Complexity detail

String equality may inspect all characters and lengths are constant-time metadata, giving $O(|a| + |b|)$ worst-case time. The method uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate all subsequences:** is correct but creates exponentially many candidates.
- **Longest-common-subsequence DP:** computes much more information than needed and takes $O(|a| \cdot |b|)$ time.
- **Explicit subsequence tests of both whole strings:** reaches the same conclusion but adds unnecessary scans.
- **Identical strings:** return `-1`, including identical one-character strings.
- **One string longer:** its whole length is immediately optimal.
- **Equal lengths but one differing position:** each complete string is already uncommon.
- **Repeated characters:** do not change the equality-based reasoning.

</details>
