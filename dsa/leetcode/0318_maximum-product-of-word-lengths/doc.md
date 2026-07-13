# Maximum Product of Word Lengths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 318 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-word-lengths/) |

## Problem Description
### Goal
Given a list of lowercase words, choose two different list positions whose words share no letter. Repeated occurrences of a letter inside one word affect its length but do not create additional character types for the disjointness test.

Return the maximum product of the two selected word lengths. Different words may have equal text or length, but a pair qualifies only when their sets of letters are disjoint. If no valid pair exists, return `0`. The function returns only the largest product, not the selected words or their indices, and every pair must use two different positions from the supplied list.

### Function Contract
**Inputs**

- `words`: a list of strings containing lowercase English letters

**Return value**

The largest product `len(words[i]) * len(words[j])` over pairs with no shared letter, or zero if no such pair exists.

### Examples
**Example 1**

- Input: `words = ["abcw","baz","foo","bar","xtfn","abcdef"]`
- Output: `16`

**Example 2**

- Input: `words = ["a","ab","abc","d","cd","bcd","abcd"]`
- Output: `4`

**Example 3**

- Input: `words = ["a","aa","aaa","aaaa"]`
- Output: `0`

### Required Complexity

- **Time:** $O(C + n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reduce every word to the property pairs actually need**

Pair validity depends only on which letters occur, not on their order or multiplicity. Encode that set in a 26-bit integer: bit `k` is one when the word contains the `k`-th lowercase letter. Two words are disjoint exactly when the bitwise expression $\mathit{mask}_{a} \mathbin{\&} \mathit{mask}_{b}$ is zero.

Building all masks scans every character once. Afterward, checking a pair is a constant-time integer operation instead of repeatedly building sets or comparing characters.

**Words with the same mask have one dominant representative**

If two words contain exactly the same set of letters, either both are compatible with another mask or neither is. Only the longer word can produce the larger product, so retain the maximum length for each distinct mask.

Compare every pair of retained `(mask, length)` entries. Whenever their masks have zero intersection, update the answer with the product of their stored maximum lengths. This compression is not required for correctness, but it avoids redundant pair checks when many words have the same letter set.

**Mask compatibility is equivalent to word compatibility**

Every letter present in a word sets its unique bit. Therefore a shared letter produces a shared set bit, making the bitwise AND nonzero. Conversely, a nonzero AND identifies a bit set by some letter in both words. The mask test accepts exactly the valid word pairs.

For each mask, replacing all its words by the longest preserves every possible compatibility relationship and dominates their products. Thus the maximum over retained compatible mask pairs equals the maximum over all original compatible word pairs.

#### Complexity detail

Let `C` be the total number of input characters, `n` the number of words, and `u` the number of distinct masks. Mask construction costs $O(C)$, and comparing retained pairs costs $O(u^2)$, which is at most $O(n^2)$. The mask-to-maximum-length table uses $O(u)$ and therefore $O(n)$ space.

#### Alternatives and edge cases

- **Build character sets inside the pair loop:** is correct but can repeatedly scan long words, taking $O(n^2 L)$ time for length `L`.
- **Precompute a set per word:** meets the same broad bound for a fixed 26-letter alphabet, but bitwise intersections are smaller and simpler.
- **Compare only word lengths:** cannot determine whether a pair shares a letter.
- Repeated letters do not change a mask. Equal masks retain only their longest word, and an input with no disjoint pair leaves the answer at zero.

</details>
