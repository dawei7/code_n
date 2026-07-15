# Remove Vowels from a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1119 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/remove-vowels-from-a-string/) |

## Problem Description

### Goal

You are given a string `s` containing only lowercase English letters. Produce a new string after removing every occurrence of the lowercase vowels `a`, `e`, `i`, `o`, and `u`.

All consonants must remain in their original relative order. Removing a vowel closes the gap rather than replacing it with whitespace or another marker. If every character is a vowel, return the empty string; if there are no vowels, return `s` unchanged in value.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 1000$.

**Return value**

- The subsequence of `s` formed by retaining exactly those characters not in `{a, e, i, o, u}`.

### Examples

**Example 1**

- Input: `s = "leetcodeisacommunityforcoders"`
- Output: `"ltcdscmmntyfrcdrs"`

**Example 2**

- Input: `s = "aeiou"`
- Output: `""`

**Example 3**

- Input: `s = "rhythm"`
- Output: `"rhythm"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Use constant-time vowel membership:** Store the five vowels in a set. For each input character, test whether it belongs to that fixed set.

**Build only the retained subsequence:** Append a character to an output buffer exactly when it is not a vowel, then join the buffer once. Because the scan proceeds left to right, appended consonants preserve their source order automatically.

Every vowel is excluded by the membership condition, so none can appear in the result. Every consonant fails that condition and is appended once, so none is lost or duplicated. These two character classes cover the lowercase alphabet, proving the returned string is exactly the requested deletion result.

#### Complexity detail

The scan visits each of the $n$ characters once and membership in a fixed five-element set is expected $O(1)$, giving $O(n)$ time. The output buffer and returned string can contain $n$ consonants, so output-related storage is $O(n)$; the vowel set itself is constant size.

#### Alternatives and edge cases

- **Generator expression plus `join`:** It expresses the same one-pass filter compactly and has the same bounds.
- **Five whole-string replacements:** It is still linear up to a fixed factor of five, but repeatedly allocates intermediate strings.
- **Remove one vowel occurrence at a time:** Repeated searching and copying can require $O(n^2)$ time for an all-vowel input.
- **Repeated string concatenation:** Depending on the language, immutable-string growth can copy the accumulated prefix and become quadratic; use a buffer.
- **All vowels:** No character is appended, so joining the empty buffer returns `""`.
- **No vowels:** Every character is retained in its original order.
- **Repeated vowels:** Each occurrence is tested and removed independently.
- **Letter `y`:** It is not one of the five vowels specified by this contract and must remain.

</details>
