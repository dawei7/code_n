# Verifying an Alien Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 953 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [verifying-an-alien-dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/) |

## Problem Description

### Goal

An alien language uses the same 26 lowercase English letters, but its alphabet may place them in a different order. The string `order` is a permutation of those letters from smallest to largest.

Given a sequence of alien `words`, determine whether it is sorted lexicographically according to that alphabet. At the first differing character, the word containing the earlier alien letter must come first. If one word is a prefix of the other, the shorter word must come first.

### Function Contract

Define

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Inputs**

- `words`: a list of 1 through 100 strings, each containing 1 through 20 lowercase English letters.
- `order`: a length-26 permutation of the lowercase English letters.

**Return value**

Return `true` exactly when `words` is in non-decreasing alien lexicographic order.

### Examples

**Example 1**

- Input: `words = ["hello","leetcode"]`, `order = "hlabcdefgijkmnopqrstuvwxyz"`
- Output: `true`
- Explanation: The first differing letters are `h` and `l`, and `h` comes earlier in the alien alphabet.

**Example 2**

- Input: `words = ["word","world","row"]`, `order = "worldabcefghijkmnpqstuvxyz"`
- Output: `false`
- Explanation: In the first pair, `d` comes after `l` in the supplied order.

**Example 3**

- Input: `words = ["apple","app"]`, `order = "abcdefghijklmnopqrstuvwxyz"`
- Output: `false`
- Explanation: `"app"` is a prefix of `"apple"` and therefore must appear first.

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Translate letters into alien ranks.** Build a 26-entry map from each character in `order` to its index. Comparing rank integers then implements the alien alphabet without modifying the words.

**Only adjacent pairs need checking.** A sequence is sorted under a total lexicographic order exactly when every adjacent pair is ordered. Compare `words[i]` with `words[i + 1]` from left to right until their first unequal characters. Their ranks decide the pair immediately: a larger rank in the first word makes the whole sequence invalid, while a smaller rank finishes that pair successfully.

**Handle a shared prefix explicitly.** If no compared character differs, the shorter word must precede the longer one. Reject the pair when the first word is longer; equal words and a shorter first word are valid. If all adjacent pairs pass, transitivity of lexicographic order proves every earlier word is no greater than every later word, so the full sequence is sorted.

#### Complexity detail

The rank table has fixed size 26. Across adjacent comparisons, no word's characters are examined more than a constant number of times, so the total time is $O(S)$. The fixed alphabet table uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Transform then compare:** Replace every character by its alien rank sequence and use ordinary lexicographic comparison. This is clear but stores $O(S)$ additional data.
- **Compare every word pair:** Verifying all earlier/later pairs is correct but can cost $O(NS)$ time instead of using transitivity through adjacent pairs.
- **Sort and compare:** Sorting a copy under an alien comparator and comparing it with the input adds unnecessary $O(S\log N)$ comparison work and extra storage.
- **Prefix inversion:** `"apple"` must not precede `"app"`, even though all characters of the shorter word match.
- **Equal words:** Equality is allowed because the requested sequence is non-decreasing.
- **One word:** With no adjacent pair to violate the order, the sequence is sorted.

</details>
