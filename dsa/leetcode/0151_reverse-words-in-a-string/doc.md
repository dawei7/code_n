# Reverse Words in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 151 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/) |

## Problem Description
### Goal
Given a string containing at least one word and space characters, treat each maximal sequence of non-space characters as one word. Reverse the order of the words so the last original word appears first and the first original word appears last.

Return the reordered words joined by exactly one space. Discard all original leading and trailing spaces, and collapse every internal run of multiple spaces instead of preserving its width. Characters inside each word must remain in their original order; only whole-word positions are reversed. The result must contain no space at either end.

### Function Contract
**Inputs**

- `s`: a string containing words separated by one or more space characters

**Return value**

The words in reverse order, joined by exactly one space with no space at either end.

### Examples
**Example 1**

- Input: `s = "the sky is blue"`
- Output: `"blue is sky the"`

**Example 2**

- Input: `s = "  hello world  "`
- Output: `"world hello"`

**Example 3**

- Input: `s = "a good   example"`
- Output: `"example good a"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Word extraction performs spacing normalization before reversal**

Extract nonempty words by splitting on whitespace without a literal single-space separator. This discards leading/trailing whitespace and collapses internal runs conceptually into one boundary. Using `split(" ")` would instead produce empty fields between repeated spaces.

**Reverse whole-word positions, not characters**

Traverse or reverse the extracted word list. Each word remains an unchanged substring; only its position among words changes. Character-level reversal would produce different words and requires a second repair step.

**One join establishes all output-space guarantees**

Join the reversed sequence with exactly one ordinary space. Join inserts separators only between elements, so it creates neither leading nor trailing whitespace.

**Extracted and emitted word sequences preserve content exactly**

After appending `k` output words, they are exactly the final `k` input words in reverse order, with one separator between adjacent words and no extra separators.

**Trace a run of several spaces**

For `"a good   example"`, extraction yields `['a','good','example']` with no empty words. Reversing gives `['example','good','a']`, and joining yields `"example good a"`.

**Normalized tokens determine the unique output**

Word extraction yields every maximal non-space token exactly once, in its original order, while discarding only separator whitespace. Reversing that list changes no word content and places the words in precisely the required order. Joining with one literal space then creates the unique normalized result: no leading or trailing space and exactly one space between adjacent words.

#### Complexity detail

Splitting, reversing, and joining inspect or copy a total linear number of characters. The word list and returned string require $O(n)$ space because Python strings are immutable.

#### Alternatives and edge cases

- **Manual two-pointer scan:** offers precise control and is useful in mutable-buffer languages, but Python's word extraction already expresses the invariant safely.
- **Reverse all characters twice:** can be in-place with mutable storage, but Python must allocate a new string anyway.
- **Literal `split(" ")`:** incorrectly retains empty fields for repeated spaces.
- A one-word string returns that word without surrounding spaces. Arbitrarily long space runs collapse to one separator.
- The LeetCode contract guarantees at least one word; a broader all-whitespace input would naturally produce an empty output under this extraction method.

</details>
