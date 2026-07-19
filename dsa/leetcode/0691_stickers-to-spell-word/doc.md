# Stickers to Spell Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 691 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/stickers-to-spell-word/) |

## Problem Description
### Goal
You have infinitely many copies of each supplied sticker, and every sticker contains one lowercase English word. You may cut individual letters from chosen stickers and rearrange them to spell the string `target`; each physical sticker copy contributes each printed letter at most once.

Return the minimum number of sticker copies needed to provide all target letters with their required multiplicities. Unused letters on a chosen sticker are allowed. If no combination of the available sticker types can form `target`, return `-1`.

### Function Contract
**Inputs**

- `stickers`: reusable lowercase sticker strings
- `target`: the lowercase string whose letter multiset must be covered

**Return value**

- The minimum sticker count covering every target letter, or `-1` if impossible

### Examples
**Example 1**

- Input: `stickers = ["with","example","science"], target = "thehat"`
- Output: `3`

**Example 2**

- Input: `stickers = ["notice","possible"], target = "basicbasic"`
- Output: `-1`

**Example 3**

- Input: `stickers = ["these","guess","about","garden","him"], target = "atomher"`
- Output: `3`
