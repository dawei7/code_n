# Minimum Unique Word Abbreviation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 411 |
| Difficulty | Hard |
| Topics | Array, String, Backtracking, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-unique-word-abbreviation/) |

## Problem Description
### Goal
Given a target word and a dictionary, create a generalized abbreviation by retaining selected target letters and replacing each maximal run of omitted characters with its positive length. Only dictionary words having the same length can conflict with such an abbreviation.

Return any abbreviation with minimum token length that matches `target` but matches no dictionary word. A retained letter and an entire numeric run each count as one abbreviation token under this contract. Several shortest answers may exist. If no same-length dictionary word constrains the target, abbreviating all characters is valid; otherwise retained positions must distinguish the target from every competitor.

### Function Contract
**Inputs**

- `target`: the word to abbreviate
- `dictionary`: words against which the abbreviation must be unique

**Return value**

- Return any minimum-token abbreviation of `target` that matches no same-length dictionary word.

### Examples
**Example 1**

- Input: `target = "apple", dictionary = ["blade"]`
- Output: `"a4"`

**Example 2**

- Input: `target = "apple", dictionary = ["plain","amber","blade"]`
- Output: `"1p3"`

**Example 3**

- Input: `target = "aaaa", dictionary = []`
- Output: `"4"`
