# Flatten 2D Vector

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 251 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Design, Iterator |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/flatten-2d-vector/) |

## Problem Description
### Goal
Design an iterator over a two-dimensional vector whose inner rows may be empty. It must expose integers in row-major order: consume each row from left to right, then continue with the next nonempty row, skipping empty rows wherever they occur.

`next()` returns and advances past the next integer, while `hasNext()` reports whether another integer exists without consuming it. Calls to `next()` are valid only when a value remains. Maintain traversal state without eagerly copying the full flattened input. The app adapter returns the complete sequence produced by repeated calls, while the native interface preserves the same incremental behavior.

### Function Contract
**Inputs**

- `vec`: a list of integer lists; inner lists may be empty

**Return value**

The local batch adapter returns every value in the order produced by repeated `next()` calls. The native interface constructs `Vector2D(vec)` and supports `next()` and `hasNext()`.

### Examples
**Example 1**

- Input: `vec = [[1,2],[3],[4,5,6]]`
- Output: `[1,2,3,4,5,6]`

**Example 2**

- Input: `vec = [[],[7],[]]`
- Output: `[7]`

**Example 3**

- Input: `vec = []`
- Output: `[]`
