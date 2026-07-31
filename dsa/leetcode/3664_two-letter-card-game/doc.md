# Two-Letter Card Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3664 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-letter-card-game/) |

## Problem Description
### Goal

A deck is represented by an array `cards`, where every card is a two-letter lowercase string. A separate letter `x` identifies which cards may participate in the game.

On each turn, remove two compatible cards that both contain `x` in at least one position and gain one point. Two cards are compatible exactly when their strings differ at one of the two positions and match at the other; identical cards and cards differing at both positions cannot be paired.

Continue until no compatible pair remains. Each physical occurrence in `cards` is independently available, even when several cards display the same string. Return the largest score achievable by choosing removal pairs optimally.

### Function Contract

**Inputs**

- `cards`: an array of $n$ two-character strings, where $2\le n\le10^5$.
- `x`: one lowercase letter.

Every card character and `x` belongs to the range `'a'` through `'j'`. Duplicate card strings are allowed.

**Return value**

Return the maximum number of disjoint compatible pairs in which both selected cards contain `x`.

### Examples

**Example 1**

- Input: `cards = ["aa", "ab", "ba", "ac"]`, `x = "a"`
- Output: `2`
- Pair `"ab"` with `"ac"`, then pair `"aa"` with `"ba"`.

**Example 2**

- Input: `cards = ["aa", "ab", "ba"]`, `x = "a"`
- Output: `1`
- Only one disjoint compatible pair can be removed.

**Example 3**

- Input: `cards = ["aa", "ab", "ba", "ac"]`, `x = "b"`
- Output: `0`
- The two cards containing `b` are `"ab"` and `"ba"`, which differ in both positions.
