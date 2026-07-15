# Minimum Number of Steps to Make Two Strings Anagram

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1347 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/) |

## Problem Description

### Goal

You are given two lowercase strings, `s` and `t`, of the same length. In one step, you may choose one character in `t` and replace it with any other lowercase English letter.

Return the minimum number of steps needed to make `t` an anagram of `s`. The order of characters does not matter in an anagram; the two strings must contain every letter with the same multiplicity.

### Function Contract

**Inputs**

- `s`: a nonempty string of lowercase English letters.
- `t`: a lowercase English string with the same length as `s`.
- Let $n$ be the common string length.

**Return value**

- Return the minimum number of character replacements in `t` needed to make its letter frequencies equal those of `s`.

### Examples

**Example 1**

- Input: `s = "bab", t = "aba"`
- Output: `1`
- Explanation: Replacing one `a` in `t` with `b` gives matching frequencies.

**Example 2**

- Input: `s = "leetcode", t = "practice"`
- Output: `5`

**Example 3**

- Input: `s = "anagram", t = "mangaar"`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Measure the needed supply of each letter.** Keep an array of 26 balances. For every aligned pair of characters, increment the entry for the character from `s` and decrement the entry for the character from `t`. After the scan, a positive balance for a letter is exactly the number of additional copies that `t` needs, while a negative balance represents copies that `t` has in excess.

Because the strings have equal length, the total positive balance equals the magnitude of the total negative balance. One replacement can remove one surplus character and supply one missing character at the same time. Therefore the sum of all positive balances is both achievable and a lower bound: every missing copy must be created, and exactly that many replacements can pair all deficits with all surpluses.

#### Complexity detail

The paired scan takes $O(n)$ time. Summing the 26 positive balances takes constant time. The balance array always contains 26 integers, so auxiliary space is $O(1)$ with respect to $n$.

#### Alternatives and edge cases

- **Two frequency maps:** Separate counters for `s` and `t` also give $O(n)$ time, but one difference array states the needed replacements more directly.
- **Repeated search and removal:** Matching each character of `s` against a mutable list of `t` is correct but can require $O(n^2)$ time.
- **Already anagrams:** Every balance is zero, so no replacement is needed even when the character orders differ.
- **Completely different strings:** Every position may need replacement, making the answer $n$.
- **Repeated letters:** Multiplicity, not mere membership, determines the deficit.

</details>
