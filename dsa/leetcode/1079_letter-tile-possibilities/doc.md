# Letter Tile Possibilities

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1079 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/letter-tile-possibilities/) |

## Problem Description

### Goal

You have $n$ tiles, and each tile has the uppercase English letter `tiles[i]` printed on it. A tile can be used at most once, while different physical tiles bearing the same letter are indistinguishable in the sequence they produce.

Count the possible non-empty sequences of letters that can be made from the printed letters. A sequence may use any positive number of the available tiles, so arrangements of different lengths and different letter orders are all included, but duplicate strings formed by exchanging equal-letter tiles are counted only once.

### Function Contract

**Inputs**

- `tiles`: a string of $n$ uppercase English letters, where $1 \le n \le 7$.
- Let $D$ be the number of distinct letters, and let $c_j$ be the available count of distinct letter $j$.
- Define the number of possible remaining-count states as

$$
M = \prod_{j=1}^{D}(c_j+1).
$$

**Return value**

- The number of distinct non-empty letter sequences constructible without using any tile more often than it occurs.

### Examples

**Example 1**

- Input: `tiles = "AAB"`
- Output: `8`

The sequences are `"A"`, `"B"`, `"AA"`, `"AB"`, `"BA"`, `"AAB"`, `"ABA"`, and `"BAA"`.

**Example 2**

- Input: `tiles = "AAABBC"`
- Output: `188`

**Example 3**

- Input: `tiles = "V"`
- Output: `1`
