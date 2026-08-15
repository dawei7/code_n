# Sort the People

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2418 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-the-people/) |

## Problem Description

### Goal

Two parallel arrays describe the same group of people. At every index $i$, `names[i]` is the person's name and `heights[i]` is that person's height. Heights are positive and pairwise distinct, although different people may have the same name.

Reorder the names so that their corresponding people appear from tallest to shortest. The association between each name and its height must be preserved while sorting; return only the reordered names, not the heights or the original indices.

### Function Contract

**Inputs**

- `names`: An array of names containing uppercase and lowercase English letters.
- `heights`: A same-length array of distinct positive heights paired by index with `names`.

Let $n = \lvert\texttt{names}\rvert = \lvert\texttt{heights}\rvert$. The contract guarantees $1 \le n \le 1000$, name lengths from 1 through 20, and heights from 1 through $10^5$.

**Return value**

Return the names ordered by strictly descending corresponding height.

### Examples

#### Example 1

- **Input:** `names = ["Mary","John","Emma"]`, `heights = [180,165,170]`
- **Output:** `["Mary","Emma","John"]`

#### Example 2

- **Input:** `names = ["Alice","Bob","Bob"]`, `heights = [155,185,150]`
- **Output:** `["Bob","Alice","Bob"]`

#### Example 3

- **Input:** `names = ["Alex"]`, `heights = [100]`
- **Output:** `["Alex"]`
