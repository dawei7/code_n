# Split Concatenated Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 555 |
| Difficulty | Medium |
| Topics | Array, String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/split-concatenated-strings/) |

## Problem Description
### Goal
Given an ordered list of strings, independently choose either the original or reversed form of each string. Concatenate the chosen forms in the given order to create a loop, so the end connects back to the beginning.

Split that loop at any character position and read one complete linear traversal. Return the lexicographically largest string obtainable over all orientation choices and split positions. Every source string contributes all its characters exactly once, the circular order of string blocks cannot be permuted, and the selected cut may occur inside a block rather than only between strings.

### Function Contract
**Inputs**

- `strs`: a non-empty list of non-empty lowercase strings

**Return value**

- The lexicographically largest string obtainable by orientations and one circular split

### Examples
**Example 1**

- Input: `strs = ["abc", "xyz"]`
- Output: `"zyxcba"`

**Example 2**

- Input: `strs = ["abc"]`
- Output: `"cba"`

**Example 3**

- Input: `strs = ["aaa"]`
- Output: `"aaa"`

### Required Complexity

- **Time:** $O(L^2)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Orient every intact block greedily**

For each string, precompute the lexicographically larger of the original and its reversal. Once the final split lies in some other string, this string appears as one intact block at a fixed position. Replacing that block by its larger orientation can only improve the complete candidate at the first differing character.

**Designate the string containing the split**

Try each string index as the block where the circular loop is opened. Concatenate the precomputed best orientations of all following blocks and then all preceding blocks; this is the fixed middle of every candidate for that split block.

**Try both orientations of the split block**

Greedy orientation is not sufficient for the block being cut because a suffix moves to the beginning and its prefix moves to the end. Test both the original string and its reversal.

**Rotate at every character**

For every cut position in the selected orientation, form `suffix + middle + prefix`. Compare the resulting full-length string with the best candidate seen so far.

**Why the search includes the optimum**

Any legal result has one particular string containing its split, one of that string's two orientations, and one cut position. Every other string is intact, so changing it independently to its larger orientation cannot make the candidate smaller and is part of some optimum. The algorithm enumerates the split index, both orientations, and every cut, while using those optimal intact blocks, so it evaluates an optimal result and returns the largest evaluated string.

#### Complexity detail

Let `L` be the total number of characters. There are `L` cut positions across all split blocks, and constructing or comparing each candidate can inspect $O(L)$ characters, giving $O(L^2)$ time. The oriented blocks, middle text, and one candidate use $O(L)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every orientation vector:** tries $2^{m}$ choices for `m` strings before considering rotations and is exponential.
- **Fix every string greedily, including the split block:** can miss the optimum because cutting changes which part of that block appears first.
- **Build one loop and test rotations only:** ignores alternative orientations and is not generally correct.
- **Single string:** compare every rotation of both its original and reversed forms.
- **Palindrome:** its two orientations are identical and harmless to test twice.
- **One-character strings:** orientation has no effect, but their circular starting position still does.
- **Repeated maximum candidates:** only the lexicographic value matters; any construction producing it is acceptable.

</details>
