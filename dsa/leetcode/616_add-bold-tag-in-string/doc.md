# Add Bold Tag in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 616 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Trie, String Matching |
| Official Link | [LeetCode](https://leetcode.com/problems/add-bold-tag-in-string/) |

## Problem Description
### Goal
Given a string `s` and an array `words`, add $<b>$ and $</b>$ around every part of `s` that matches an occurrence of any word in the array. Matches may begin at any position, and all characters covered by at least one complete word occurrence must be bold.

Return the resulting string with the fewest necessary tag pairs. When covered intervals overlap or are consecutive, combine them into one bold region; leave every uncovered character unchanged. Empty gaps must not be invented, and a word that does not occur in `s` contributes no tags.

### Function Contract
**Inputs**

- `s`: the source string
- `words`: nonempty dictionary strings to locate in `s`

**Return value**

- `s` with maximal covered regions surrounded by bold tags
- Characters not covered by any word occurrence remain unchanged
- Overlapping and consecutive matches share one tag pair

### Examples
**Example 1**

- Input: `s = "abcxyz123"`, `words = ["abc", "123"]`
- Output: `"<b>abc</b>xyz<b>123</b>"`

**Example 2**

- Input: `s = "aaabbcc"`, `words = ["aaa", "aab", "bc"]`
- Output: `"<b>aaabbc</b>c"`

### Required Complexity

- **Time:** $O(N + D)$
- **Space:** $O(N + D)$

<details>
<summary>Approach</summary>

#### General

**Build one matcher for the whole dictionary**

Insert all words into a trie, then add failure links breadth-first. A missing transition follows the current state's failure transition, so each source character advances the Aho–Corasick automaton in constant time over the problem's fixed letter-and-digit alphabet. Each state records the longest dictionary word that ends there or at one of its failure ancestors.

**Why the longest ending match is enough**

When the scan reaches index `end`, a recorded length `length` marks `[end - length + 1, end]`. Any shorter dictionary match ending at the same index lies completely inside this longest interval, so omitting its separate mark cannot change the covered-character union.

**Accumulate coverage with boundary differences**

For every nonzero match length, add one at the interval start and subtract one immediately after its end. A prefix sum over this difference array says whether each character belongs to at least one match. Overlaps naturally keep the sum positive, and adjacent intervals keep consecutive positions covered without inserting a gap.

**Render only coverage transitions**

Walk `s` once more. Emit $<b>$ when coverage changes from false to true and $</b>$ when it changes from true to false, appending each original character once. Close a final open region after the last character. These transition points are exactly the boundaries of maximal covered ranges, so the output uses the fewest valid tag pairs.

#### Complexity detail

Let `N` be the length of `s` and `D` the total number of dictionary characters. The alphabet of letters and digits is fixed, so building the trie, completing failure transitions, scanning the string, accumulating coverage, and rendering take $O(N + D)$ time. The automaton and coverage arrays occupy $O(N + D)$ space.

#### Alternatives and edge cases

- **Check every word at every position:** mark each successful `startswith` range; it is simple but can cost $O(N \cdot W \cdot L)$ for `W` words of maximum length `L`.
- **Collect and merge match intervals:** any string-matching method can emit intervals and then sort or merge them; storing every occurrence can be much larger than the final union.
- **Trie scan from every start:** avoids comparing unrelated word prefixes but can still take $O(N \cdot L)$ time.
- Overlapping matches combine into one bold region.
- Adjacent matches also combine; no plain character separates their coverage.
- Repeated and contained matches do not create nested tags.
- If no word occurs, return `s` unchanged.
- A word longer than `s` simply never reaches a terminal match.

</details>
