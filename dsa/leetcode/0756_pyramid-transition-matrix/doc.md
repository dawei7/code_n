# Pyramid Transition Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 756 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/pyramid-transition-matrix/) |

## Problem Description

### Goal

Blocks are labeled by letters and stacked into a centered pyramid in which each row has one fewer block than the row below. Every allowed three-letter pattern `XYZ` permits a block `Z` to sit directly above adjacent lower blocks `X` and `Y`, in that left-to-right order.

Given the bottom row and all allowed patterns, return `True` if some sequence of valid choices can build rows until one top block remains, and `False` otherwise. Each adjacent pair may allow several possible upper blocks, and choices in one row jointly determine which pairs exist in the next row.

### Function Contract

**Inputs**

- `bottom`: the initial row of uppercase labels.
- `allowed`: a list of three-character transition rules.

**Return value**

- `True` if at least one sequence of legal upper rows reaches a one-block top; otherwise `False`.

### Examples

**Example 1**

- Input: `bottom = "BCD"`, `allowed = ["BCC", "CDE", "CEA", "FFF"]`
- Output: `True`
- Explanation: `BCD` can produce `CE`, and `CE` can produce `A`.

**Example 2**

- Input: `bottom = "AAAA"`, `allowed = ["AAB", "AAC", "BCD", "BBE", "DEF"]`
- Output: `False`
- Explanation: Every possible construction eventually reaches a pair with no legal top block.
