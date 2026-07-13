# Palindrome Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 266 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-permutation/) |

## Problem Description
### Goal
Given a string `s`, determine whether all of its characters can be rearranged to form a palindrome. Reordering may place characters anywhere, but every original occurrence must be used exactly once and no new character may be introduced.

Return `True` when at least one palindromic permutation exists and `False` otherwise. Character identity is exact, so case, spaces, and other supported characters retain their distinctions. An even-length palindrome requires every character count to be even, while an odd-length palindrome may have exactly one odd count. The empty string and any one-character string are valid.

### Function Contract
**Inputs**

- `s`: a string whose character multiplicities may be rearranged

**Return value**

`True` exactly when some permutation of `s` reads the same forward and backward.

### Examples
**Example 1**

- Input: `s = "code"`
- Output: `false`

**Example 2**

- Input: `s = "aab"`
- Output: `true`

**Example 3**

- Input: `s = "carerac"`
- Output: `true`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Only parity matters for mirrored pairs**

Toggle each character in a set: add it on an odd occurrence and remove it on the next occurrence. At completion the set contains exactly the characters with odd counts.

After every processed prefix, membership in the set is equivalent to having odd frequency in that prefix.

**At most one odd count can occupy the center**

Every noncentral palindrome position has a mirrored partner containing the same character, consuming occurrences in pairs. Thus all counts must be even except possibly one character assigned to the unique center of an odd-length result. This condition is also sufficient: place half of every pair on each side and put the lone odd character, if any, in the center.

#### Complexity detail

One expected-constant-time toggle per character gives $O(n)$ time. At most `k` distinct characters are stored.

#### Alternatives and edge cases

- **Count each character by rescanning the string:** can take $O(n^2)$.
- Empty and one-character strings qualify; character matching is case-sensitive.

</details>
