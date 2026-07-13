# Isomorphic Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 205 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/isomorphic-strings/) |

## Problem Description
### Goal
Given two strings `s` and `t` of equal length, decide whether the characters of `s` can be replaced consistently to produce `t`. Every occurrence of one source character must map to the same target character while preserving character positions and order.

The mapping must also be one-to-one: two different source characters cannot both map to the same target character, although a character may map to itself. Return `True` exactly when such a complete correspondence exists. Matching character counts alone is insufficient when their occurrence patterns differ, and the strings themselves must not be modified during the comparison.

### Function Contract
**Inputs**

- `s`: the source string
- `t`: a string of the same length

**Return value**

`True` exactly when each source character maps to one target character and no two source characters share a target.

### Examples
**Example 1**

- Input: `s = "egg", t = "add"`
- Output: `True`

**Example 2**

- Input: `s = "foo", t = "bar"`
- Output: `False`

**Example 3**

- Input: `s = "paper", t = "title"`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

Isomorphism requires a bijection between the characters that actually occur: each source character always maps to the same target character, and two different source characters cannot map to the same target.

Scan the strings position by position while maintaining both directions:

- `source_to_target[s_char] = t_char`
- `target_to_source[t_char] = s_char`

If a source character already maps to a different target, repeated occurrences are inconsistent. If a target character already maps from a different source, the mapping is not one-to-one. When neither character has appeared, install both entries together.

The reverse map is not redundant. A forward-only check accepts `s = "ab"`, `t = "aa"` by assigning both source characters to `a`, but that replacement cannot be reversed and is forbidden by the contract.

For `"paper"` and `"title"`, the pairs establish `p -> t`, `a -> i`, `e -> l`, and `r -> e`; the repeated `p` and repeated `t` appear in corresponding positions, so both maps remain consistent.

After every processed position, the two maps are inverse functions on all encountered character pairs. Adding a previously unseen pair preserves that property; either conflict test detects exactly a violation of forward consistency or reverse uniqueness. If the scan finishes, replacing each source character by its mapped target reproduces every position of `t`, and the reverse map proves the replacement is injective. Conversely, any non-isomorphic pair has a first position where one of those two conditions fails, so the algorithm rejects it.

#### Complexity detail

The scan performs expected $O(1)$ hash-map work for each of `n` positions, giving expected $O(n)$ time. If `k` distinct characters occur, the two maps store $O(k)$ entries.

#### Alternatives and edge cases

- A source-to-target map alone misses many-to-one collisions.
- Encoding each string by the sequence of first-occurrence indices and comparing those patterns is elegant, but materializes normalized sequences unless streamed carefully.
- Trying explicit substitutions explores a combinatorial space needlessly.
- Identical strings are isomorphic. Repetition patterns must match exactly, and distinct source characters require distinct targets.
- The contract supplies equal-length strings; otherwise unequal length is an immediate rejection.

</details>
