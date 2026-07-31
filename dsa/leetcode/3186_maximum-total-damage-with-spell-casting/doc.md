# Maximum Total Damage With Spell Casting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3186 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Dynamic Programming, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/) |

## Problem Description

### Goal

A magician owns several spells. The integer array `power` records the damage dealt by each spell, and separate spells may have the same damage value.

If the magician casts a spell whose damage is $x$, no spell with damage $x-2$, $x-1$, $x+1$, or $x+2$ may also be cast. Spells with damage exactly $x$ do not conflict with one another. Each individual spell can be cast at most once.

Choose a valid collection of spells and return the maximum total damage they can deal.

### Function Contract

**Inputs**

- `power`: A list of $n$ spell-damage values, where $1\le n\le10^5$ and $1\le\texttt{power[i]}\le10^9$.

**Return value**

- The maximum sum of the chosen spell damages subject to the stated conflict rule.

### Examples

**Example 1**

- Input: `power = [1, 1, 3, 4]`
- Output: `6`

Casting the two damage-1 spells and the damage-4 spell produces total damage 6. Damage values 1 and 4 differ by 3, so they may be used together.

**Example 2**

- Input: `power = [7, 1, 6, 6]`
- Output: `13`

The damage-1 spell can be combined with both damage-6 spells, producing $1+6+6=13$.
