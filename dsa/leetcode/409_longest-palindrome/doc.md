# Longest Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 409 |
| Difficulty | Easy |
| Topics | Hash Table, String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindrome/) |

## Problem Description
### Goal
Given a string containing lowercase and uppercase English letters, select any subset of its character occurrences and rearrange them to form a palindrome. Character comparison is case-sensitive, so `A` and `a` are different values.

Return the maximum possible palindrome length. Every paired character contributes two symmetric positions, and at most one leftover odd occurrence may occupy the center. Other unmatched occurrences can be discarded. The task asks only for the greatest length, not an actual palindrome. A one-character string yields `1`, and every nonempty input can contribute at least one center character.

### Function Contract
**Inputs**

- `s`: a string containing lowercase and uppercase English letters

**Return value**

- Return the maximum number of characters that can be rearranged into a palindrome.

### Examples
**Example 1**

- Input: `s = "abccccdd"`
- Output: `7`

**Example 2**

- Input: `s = "a"`
- Output: `1`

**Example 3**

- Input: `s = "bb"`
- Output: `2`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Every symmetric contribution is a matching pair**

Maintain a set of character kinds that currently have one unmatched occurrence. When a character is absent, insert it. When it is present, remove it and add two to the usable length; those two copies can occupy mirrored positions.

**Reserve at most one center**

After all occurrences are processed, a nonempty unmatched set means at least one odd leftover occurrence exists. A palindrome can use exactly one such character at its center, so add one regardless of how many unmatched kinds remain.

**Why greedy pairing loses nothing**

Every palindrome position outside the center must be paired with the same character on the opposite side. Taking every available pair is always beneficial and pairs of different characters do not compete. Conversely, no construction can use more than `floor(count / 2)` pairs of a character or more than one unpaired center, so the computed length is an upper bound that is achievable.

**Keep letter case distinct**

Uppercase and lowercase letters represent different character kinds. The set uses the original characters as keys, ensuring `"A"` cannot pair with `"a"`.

#### Complexity detail

Each of the `n` characters triggers one constant-time expected set operation, for $O(n)$ time. At most 52 English letter kinds can remain unmatched, so space is $O(1)$ under the fixed alphabet.

#### Alternatives and edge cases

- **Frequency array or counter:** sum the even part of every count and add one if any count is odd; it has the same bounds.
- **Sort the characters:** makes pairs adjacent but costs $O(n \log n)$ time.
- **Search explicitly for one unused mate per occurrence:** is correct but can take $O(n^2)$ time.
- A one-character string forms a palindrome of length one.
- Several odd counts contribute only one center character.
- All-even counts use every character.
- Uppercase and lowercase occurrences do not pair.

</details>
