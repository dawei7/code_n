# Reverse String II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 541 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-string-ii/) |

## Problem Description
### Goal
Given a string `s` and positive integer `k`, process consecutive blocks of `2k` characters from left to right. In every full block, reverse the first `k` characters and leave the following `k` characters in their existing order.

For the final partial block, reverse all remaining characters when fewer than `k` remain. When at least `k` but fewer than `2k` remain, reverse only its first `k` and leave the rest unchanged. Return the resulting string with every original character present exactly once; block boundaries are based on original positions, not on character values.

### Function Contract
**Inputs**

- `s`: a lowercase string
- `k`: a positive reversal length

**Return value**

- The transformed string after applying the rule independently to each `2k` block

### Examples
**Example 1**

- Input: `s = "abcdefg", k = 2`
- Output: `"bacdfeg"`

**Example 2**

- Input: `s = "abcd", k = 2`
- Output: `"bacd"`

**Example 3**

- Input: `s = "abcdef", k = 2`
- Output: `"bacdfe"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**View the string as independent `2k` blocks**

Start at indices `0, 2k, 4k, ...`. The rule for one block never depends on another, so each start identifies exactly one segment whose prefix must be reversed.

**Reverse only the available first half**

Convert the immutable string to a character array. For a block beginning at `start`, reverse the half-open slice ending at `min(start + k, n)`. Characters from that endpoint through the end of the block remain untouched.

**Let the endpoint encode both tail rules**

If fewer than `k` characters remain, the endpoint becomes `n` and all remaining characters reverse. If between `k` and `2k` remain, exactly the first `k` reverse and the rest stay in place. No separate branch is required.

**Why every character receives the required treatment**

The block starts partition the string into disjoint intervals of length at most `2k`. Within each interval, the slice operation reverses precisely its first `min(k, remaining)` characters and never changes its suffix. Therefore each full and partial block matches the contract exactly once.

#### Complexity detail

Each character participates in at most one reversal or remains untouched, so time is $O(n)$. The mutable character array and final string require $O(n)$ space in Python.

#### Alternatives and edge cases

- **Two-pointer swaps:** performs the same reversals explicitly inside the character array and has identical bounds.
- **Build transformed chunks and join once:** is also linear when chunks are accumulated in a list.
- **Repeatedly concatenate the growing result:** is correct but can copy the existing prefix on every block and degrade to $O(n^2)$ time.
- **$k = 1$:** reversing one character leaves the string unchanged.
- **Fewer than `k` characters remain:** reverse the complete tail.
- **Between `k` and `2k` remain:** reverse exactly `k` and preserve the rest.
- **Exact multiple of `2k`:** every block is processed uniformly.

</details>
