# Couples Holding Hands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 765 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Greedy, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/couples-holding-hands/) |

## Problem Description

### Goal

There are `n` couples seated in a row of `2n` seats, with seats grouped as adjacent pairs `(0, 1)`, `(2, 3)`, and so on. People `0` and `1` are a couple, people `2` and `3` are the next couple, following the same numbering rule.

In one move, swap the people in any two seats. Return the minimum number of swaps needed so that every couple occupies one adjacent seat pair. Couples may appear in any order after rearrangement; only sitting together matters.

### Function Contract

**Inputs**

- `row`: an even-length permutation of the people numbered from `0` through `len(row) - 1`.

**Return value**

- The minimum number of arbitrary two-person swaps that makes every adjacent seat pair a couple.

### Examples

**Example 1**

- Input: `row = [0,2,1,3]`
- Output: `1`
- Explanation: Swap people `2` and `1` so both seat pairs contain couples.

**Example 2**

- Input: `row = [3,2,0,1]`
- Output: `0`
- Explanation: Both couples already sit together, regardless of order within a pair.

**Example 3**

- Input: `row = [0,2,4,1,3,5]`
- Output: `2`
- Explanation: The three couples form one misplacement cycle, which requires two swaps.
