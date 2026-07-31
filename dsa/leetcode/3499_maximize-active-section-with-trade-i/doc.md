# Maximize Active Section with Trade I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3499 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-active-section-with-trade-i/) |

## Problem Description

### Goal

A binary string `s` describes a sequence of sections: each `'1'` is active and each `'0'` is inactive. You may perform at most one trade. A trade first changes one contiguous block of `'1'`s that is surrounded on both sides by `'0'`s into `'0'`s. It then changes one contiguous block of `'0'`s that is surrounded on both sides by `'1'`s into `'1'`s.

Interpret the trade on the augmented string `t = '1' + s + '1'`. The two added active sections establish the boundary surroundings but are not included in the returned count. Choose whether and where to trade so that the original $n$ sections contain as many `'1'`s as possible, and return that maximum count.

### Function Contract

**Inputs**

- `s`: A binary string with length $n$, where $1 \le n \le 10^5$.

Every character of `s` is either `'0'` or `'1'`.

**Return value**

Return the maximum number of active sections obtainable after at most one valid trade.

### Examples

**Example 1**

- Input: `s = "01"`
- Output: `1`
- Explanation: No block of active sections is surrounded by inactive sections, so no trade is possible.

**Example 2**

- Input: `s = "0100"`
- Output: `4`
- Explanation: In the augmented string `"101001"`, changing the middle `'1'` to `'0'` merges the two neighboring zero blocks. Changing that merged block to `'1'` activates all four original sections.

**Example 3**

- Input: `s = "1000100"`
- Output: `7`
- Explanation: Trading around the single active section between the zero blocks of lengths three and two makes every original section active.

**Example 4**

- Input: `s = "01010"`
- Output: `4`
- Explanation: Either internal active block joins two adjacent one-character zero blocks, increasing the original active count by two.
