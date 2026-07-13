# Group Shifted Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 249 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/group-shifted-strings/) |

## Problem Description
### Goal
Two lowercase strings belong to the same shifting sequence when one can be transformed into the other by advancing every character by the same number of alphabet positions, wrapping cyclically from `z` back to `a`. A shift never changes a string's length or the relative differences between adjacent characters.

Given a list of nonempty strings, partition all entries into equivalence groups under this rule. Return every input string in exactly one group; group order and member order are unrestricted. Identical strings share a group, while equal-length strings with different cyclic difference patterns do not, even if their sets of letters look similar.

### Function Contract
**Inputs**

- `strings`: a list of non-empty lowercase strings

**Return value**

All equivalence groups; group order and member order may be arbitrary.

### Examples
**Example 1**

- Input: `strings = ["abc","bcd","acef","xyz","az","ba","a","z"]`
- Output: `[["abc","bcd","xyz"],["acef"],["az","ba"],["a","z"]]`

**Example 2**

- Input: `strings = ["a"]`
- Output: `[["a"]]`

**Example 3**

- Input: `strings = ["ab","za"]`
- Output: `[["ab","za"]]`

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Encode the shape, not the starting letter**

For each neighboring pair, record how far the second character lies after the first modulo 26. The resulting tuple captures every relative step while ignoring the absolute first letter. Strings of different lengths naturally produce keys of different lengths.

After processing a string, its key records its complete shift-invariant shape, and the hash bucket contains exactly the earlier strings with that shape.

**Equal step sequences are exactly equal shift groups**

A uniform alphabet shift preserves every adjacent modular difference, so shifted strings must share a key. Conversely, suppose two strings share every recorded step. Shift the first string so its first character matches the second; because their first steps agree, their second characters then match, and repeating this argument aligns every later character. Equal keys are therefore sufficient as well as necessary.

#### Complexity detail

If `L` is the total number of input characters, building all keys and groups takes $O(L)$ time and space including the returned grouping.

#### Alternatives and edge cases

- **Shift each string until it starts with `a`:** is also linear but constructs another normalized string.
- All one-character strings share the empty-difference key; wraparound such as `az` and `ba` is handled modulo 26.

</details>
