# Number of Atoms

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 726 |
| Difficulty | Hard |
| Topics | Hash Table, String, Stack, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-atoms/) |

## Problem Description
### Goal
Given a valid chemical `formula`, count the total occurrence of every atom. An atom name begins with an uppercase letter followed by zero or more lowercase letters; an optional number greater than `1` multiplies the preceding atom or parenthesized formula, and parentheses may be nested.

Return one string containing atom names in lexicographic order. Append an atom's total count only when that count exceeds `1`; omit the number for count `1`. Multipliers apply to the complete immediately preceding atom or group, including all atoms and nested counts inside that group.

### Function Contract
**Inputs**

- `formula`: a nonempty valid formula containing atom names, parentheses, and optional positive integer counts

**Return value**

- One string containing each distinct atom name in sorted order, followed by its total count only when that count exceeds one

### Examples
**Example 1**

- Input: `formula = "H2O"`
- Output: `"H2O"`

**Example 2**

- Input: `formula = "Mg(OH)2"`
- Output: `"H2MgO2"`

**Example 3**

- Input: `formula = "K4(ON(SO3)2)2"`
- Output: `"K4N2O14S4"`
