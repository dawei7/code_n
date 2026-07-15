# Decrypt String from Alphabet to Integer Mapping

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1309 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/) |

## Problem Description
### Goal
A valid encoded string `s` represents lowercase English letters with digits and `#` markers. The letters `a` through `i` use the one-character codes `1` through `9`, respectively. The letters `j` through `z` use `10#` through `26#`, respectively.

Decode every token in order and return the resulting lowercase string. The input is guaranteed to follow this encoding and to have a unique valid interpretation, so malformed codes do not need a fallback result.

### Function Contract
**Inputs**

- `s`: a valid encoded string containing digits and possibly `#`.
- Its length $n$ satisfies $1\le n\le1000$.
- Every token is either one digit from `1` to `9` or a two-digit value from `10` to `26` followed by `#`.

**Return value**

The lowercase English string obtained by replacing each encoded integer $v$ with the $v$th letter of the alphabet.

### Examples
**Example 1**

- Input: `s = "10#11#12"`
- Output: `"jkab"`
- Explanation: `10#` and `11#` decode to `j` and `k`; the final `1` and `2` decode separately.

**Example 2**

- Input: `s = "1326#"`
- Output: `"acz"`

**Example 3**

- Input: `s = "123456789"`
- Output: `"abcdefghi"`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Let the marker identify a three-character token**

Scan from left to right with index `i`. If `i + 2` is inside the string and `s[i + 2] == "#"`, the next token must be the two digits at `s[i:i + 2]` together with that marker. Convert those digits to a value from 10 through 26 and advance `i` by 3.

Otherwise, the current character is a complete one-digit token from 1 through 9; convert it and advance by 1. The validity guarantee ensures that looking two positions ahead never chooses an invalid three-character group.

For either token value $v$, the corresponding lowercase character is `chr(ord("a") + v - 1)`. Appending one decoded character per token preserves the encoded order. Because each branch consumes exactly one valid token, the scan covers the entire input once and returns precisely its unique decoding.

#### Complexity detail

Each encoded character is inspected a constant number of times and consumed once, so decoding takes $O(n)$ time. The list of decoded characters and final returned string require $O(n)$ space in the worst case. Apart from the returned output, the scan uses $O(n)$ temporary list space and constant scalar state.

#### Alternatives and edge cases

- **Scan backward:** A `#` encountered from right to left makes the preceding two digits unambiguous, but the decoded characters must then be reversed.
- **Repeated prefix validation:** Rescanning every consumed character whenever a marked token is found preserves the decoding but can inspect $O(n^2)$ total characters.
- **One-digit suffix:** A final digit without `#` is decoded independently even when earlier tokens used markers.
- **Values 10 and 26:** `10#` and `26#` are the inclusive endpoints of the marked range and decode to `j` and `z`.
- **Only one-digit codes:** A string without `#` maps character by character.
- **Maximum length:** The iterative scan handles a 1000-character encoding without recursion or repeated slicing.

</details>
