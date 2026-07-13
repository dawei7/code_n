# Valid Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 125 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-palindrome/) |

## Problem Description
### Goal
Given a string containing letters, digits, spaces, and punctuation, form its comparison sequence by retaining only alphanumeric characters. Treat uppercase and lowercase forms of the same letter as equal, while retaining digits as meaningful characters.

Return `True` when this normalized sequence reads the same from left to right as from right to left; otherwise return `False`. Character order must remain unchanged during normalization. A string containing no letters or digits reduces to the empty sequence and is therefore a palindrome, as is any normalized sequence containing just one character.

### Function Contract
**Inputs**

- `s`: the original string containing letters, digits, spaces, or punctuation

**Return value**

`True` when the normalized alphanumeric sequence is a palindrome; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "A man, a plan, a canal: Panama"`
- Output: `True`

**Example 2**

- Input: `s = "race a car"`
- Output: `False`

**Example 3**

- Input: `s = " "`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Skip characters that do not exist in the normalized sequence**

Place pointers at both raw-string ends. Independently advance the left pointer and retreat the right pointer while their characters are not alphanumeric. Skipped punctuation, whitespace, and symbols have no position in the conceptual normalized sequence, so no output buffer is required.

**Compare the next retained mirrored pair case-insensitively**

When both pointers reference retained characters and have not crossed, compare their case-normalized forms. A mismatch is decisive. After a match, move both inward and repeat the skip phases to locate the next conceptual pair.

Digits compare directly; case folding affects letters only. Use the language's alphanumeric and lowercase semantics consistently with the platform contract.

**Pointer crossing means every normalized pair has matched**

All retained characters outside the current pointer interval have already been paired successfully in mirrored order. Skipped characters do not belong to the normalized sequence.

**Trace punctuation and case normalization**

In `A man, a plan, a canal: Panama`, spaces and punctuation are skipped. Mirrored letters compare case-insensitively, leaving the normalized sequence `amanaplanacanalpanama`.

**Skipping ignored characters exposes normalized mirror pairs**

After each pointer skips non-alphanumeric characters, the two selected characters are exactly the next outer pair of the implicitly normalized string. Case folding makes their comparison identical to comparing the normalized characters.

A mismatch proves the normalized string cannot be palindromic. If every outer pair matches until the pointers meet, all mirrored positions agree, which is sufficient for a palindrome without ever allocating the normalized string.

#### Complexity detail

Each pointer moves across the string at most once, giving $O(n)$ time. Only two indices are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Build and reverse a normalized string:** is concise but uses $O(n)$ extra space.
- **Compare raw characters:** mishandles punctuation and case.
- **Use repeated deletion:** can cause quadratic string copying.
- A string with no alphanumeric characters normalizes to empty and is palindromic. A single retained character is also palindromic.
- The approach compares Unicode-aware or ASCII-aware character classes according to the implementation API; do not mix inconsistent normalization rules.

</details>
