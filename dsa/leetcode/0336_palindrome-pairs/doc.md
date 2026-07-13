# Palindrome Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 336 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Trie, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-pairs/) |

## Problem Description
### Goal
Given a list of unique lowercase strings, find ordered pairs of distinct indices `[i, j]` such that concatenating `words[i]` followed by `words[j]` produces a palindrome. Reversing the pair changes the concatenation and is a separate candidate.

Return every valid ordered pair in any order, with no duplicate index pair and never pairing an index with itself. Both directions should appear when both concatenations are palindromic. The empty string may pair with any nonempty word that is already a palindrome. Evaluate the entire concatenated text; matching only a prefix or suffix is insufficient.

### Function Contract
**Inputs**

- `words`: unique lowercase strings, possibly including the empty string

**Return value**

A list of all ordered index pairs forming palindromic concatenations, in any outer-list order.

### Examples
**Example 1**

- Input: `words = ["abcd","dcba","lls","s","sssll"]`
- Output: `[[0,1],[1,0],[3,2],[2,4]]`

**Example 2**

- Input: `words = ["bat","tab","cat"]`
- Output: `[[0,1],[1,0]]`

**Example 3**

- Input: `words = ["a",""]`
- Output: `[[0,1],[1,0]]`

### Required Complexity

- **Time:** $O(n k^2 + P)$
- **Space:** $O(n k + P)$

<details>
<summary>Approach</summary>

#### General

**A valid partner is forced at a split boundary**

Map every word to its index. For each word, examine every split `word = prefix + suffix`, including empty pieces. If `prefix` is a palindrome, placing `reverse(suffix)` before the word creates
`reverse(suffix) + prefix + suffix`, which is a palindrome. Look up that forced preceding word in the map.

Symmetrically, if `suffix` is a palindrome, placing `reverse(prefix)` after the word creates `prefix + suffix + reverse(prefix)`. Look up that forced following word. In both directions, reject the word's own index because a pair must use distinct entries.

**The two directions cover unequal word lengths and the empty string**

Exact reversed words appear at an empty-prefix or empty-suffix boundary. A shorter word can pair with a longer one when the unmatched remainder of the longer word is palindromic; this is why checking only complete reversals is insufficient.

When the empty string exists, every palindromic word pairs with it in both directions. Those cases arise naturally at the two extreme split positions. Skip the suffix-palindrome branch when the suffix is empty, because the corresponding exact-reversal pair was already emitted by the prefix branch of the partner word.

For `"lls"`, splitting as `"ll" + "s"` finds palindromic prefix `"ll"` and forced preceding word `"s"`, producing pair `[3,2]`. For `"sssll"`, splitting as `"ss" + "sll"` finds palindromic prefix `"ss"` and forced preceding word `"lls"`, producing `[2,4]`.

**Every palindrome pair appears at one of these splits**

Consider a valid concatenation of two words. If the left word is no longer than the right, its mirrored characters force a reversed prefix of the right word, and the unmatched suffix of the right word must itself be palindromic. If the left word is longer, the symmetric argument leaves a palindromic prefix of the left word and forces the other word to equal the reverse of its suffix.

These are exactly the two split tests. Every emitted pair is palindromic by construction, and every valid pair satisfies one of the forced-complement cases, proving completeness.

#### Complexity detail

Let `n` be the number of words, `k` the maximum word length, and `P` the number of returned pairs. Each word has $O(k)$ splits; slicing, reversing, and palindrome checking can take $O(k)$ per split, for $O(n k^2 + P)$ time. The word map stores $O(nk)$ characters and the output stores $O(P)$ pairs.

#### Alternatives and edge cases

- **Test every ordered word pair:** is simple but costs $O(n^2 k)$ time.
- **Look up only complete reversed words:** misses pairs where a palindromic remainder belongs to the longer word.
- **A reversed-word trie:** can organize the same prefix/suffix logic and achieve comparable bounds.
- The empty string pairs only with palindromic words. Pair direction matters, and the outer result order does not.

</details>
