# Check if Grid can be Cut into Sections

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3394 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/) |

## Problem Description

### Goal

An integer `n` defines an $n\times n$ grid whose origin is at its bottom-left corner. Each entry `[start_x, start_y, end_x, end_y]` in `rectangles` describes a non-overlapping axis-aligned rectangle: `(start_x, start_y)` is its bottom-left corner and `(end_x, end_y)` is its top-right corner.

Determine whether two complete horizontal cuts or two complete vertical cuts can divide the grid into three sections. The two cuts must have the same orientation. Every resulting section must contain at least one rectangle, and every rectangle must lie wholly inside exactly one section; a cut therefore cannot pass through a rectangle's interior. A cut may coincide with rectangle boundaries.

Return `True` when either orientation permits such a division, and `False` otherwise.

### Function Contract

**Inputs**

- `n`: The grid side length, with $3\le n\le10^9$.
- `rectangles`: A list of $r$ non-overlapping rectangles, where $3\le r\le10^5$. Each rectangle has the form `[start_x, start_y, end_x, end_y]` and satisfies $0\le\texttt{start_x}<\texttt{end_x}\le n$ and $0\le\texttt{start_y}<\texttt{end_y}\le n$.

**Return value**

- `True` if two horizontal cuts or two vertical cuts can form three nonempty valid sections; otherwise, `False`.

### Examples

#### Example 1

- **Input:** `n = 5, rectangles = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]`
- **Output:** `True`

Horizontal cuts at `y = 2` and `y = 4` assign every rectangle wholly to one of three nonempty sections.

#### Example 2

- **Input:** `n = 4, rectangles = [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]`
- **Output:** `True`

Vertical cuts at `x = 2` and `x = 3` satisfy all requirements.

#### Example 3

- **Input:** `n = 4, rectangles = [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]`
- **Output:** `False`

Neither two horizontal cuts nor two vertical cuts can create three valid nonempty sections.
