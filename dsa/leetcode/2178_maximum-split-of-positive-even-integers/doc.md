# Maximum Split of Positive Even Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2178 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Backtracking, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-split-of-positive-even-integers/) |

## Problem Description

### Goal

Given an integer `finalSum`, represent it as a sum of as many distinct
positive even integers as possible. Every returned value must be used once,
and their total must equal `finalSum`.

Return any split having the maximum possible number of terms; neither the
order nor one particular choice of values is prescribed when several optimal
splits exist. If no valid split exists, return an empty list. In particular,
an odd total cannot be formed by summing only even integers.

### Function Contract

**Inputs**

- `finalSum`: an integer satisfying $1\le\texttt{finalSum}\le10^{10}$.

**Return value**

Return any list of unique positive even integers whose sum is `finalSum` and
whose length is maximum. Return `[]` when `finalSum` is odd.

### Examples

#### Example 1

- **Input:** `finalSum = 12`
- **Output:** `[2,4,6]`

#### Example 2

- **Input:** `finalSum = 7`
- **Output:** `[]`

#### Example 3

- **Input:** `finalSum = 28`
- **Output:** one valid answer is `[2,4,6,16]`; other four-term splits are also
  accepted.
