# Rings and Rods

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2103 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/rings-and-rods/) |

## Problem Description

### Goal

There are ten rods labeled from `0` through `9` and $n$ rings. Every ring is red, green, or blue. The string `rings` has length $2n$ and encodes one ring per consecutive character pair: the first character is its color (`"R"`, `"G"`, or `"B"`), and the second is the digit labeling its rod.

For example, `"R3G2B1"` places a red ring on rod `3`, a green ring on rod `2`, and a blue ring on rod `1`. Count how many rods hold at least one ring of every color.

### Function Contract

**Inputs**

- `rings`: a string containing $n$ color-rod pairs, where $1 \le n \le 100$. Every even index contains `"R"`, `"G"`, or `"B"`, and every following index contains a digit from `"0"` through `"9"`.

**Return value**

Return the number of rods containing red, green, and blue rings.

### Examples

**Example 1**

- Input: `rings = "B0B6G0R6R0R6G9"`
- Output: `1`
- Explanation: Rod `0` has all three colors; rod `6` lacks green and rod `9` has only green.

**Example 2**

- Input: `rings = "B0R0G0R9R0B0G0"`
- Output: `1`
- Explanation: Repeated rings do not change that only rod `0` has every color.

**Example 3**

- Input: `rings = "G4"`
- Output: `0`
- Explanation: A single ring cannot supply all three colors.
