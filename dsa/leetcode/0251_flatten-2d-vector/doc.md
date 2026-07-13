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

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Represent the next value with two coordinates**

Store the current row and column instead of flattening the input. A helper advances the row coordinate past every exhausted or empty row and resets the column to zero.

After normalization, either the row coordinate is past the vector or `(row, column)` identifies the next unconsumed integer. `hasNext()` only normalizes and checks that state; `next()` reads it and advances the column.

**Normalization skips containers, never values**

The helper advances beyond a row only when the column index has reached that row's length, so every skipped row is empty or fully consumed. Once normalized, the coordinates identify the earliest remaining value in row-major order. `next()` returns that value and advances once, making the same statement true for the following call.

#### Complexity detail

Although one normalization may skip several empty rows, each row is skipped once over the iterator's lifetime. Thus operations are amortized $O(1)$ and the iterator uses two indices, or $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Pre-flatten the vector:** simplifies iteration but requires $O(n)$ initialization time and auxiliary storage.
- Leading, trailing, and consecutive empty rows are handled by the same normalization rule; an entirely empty vector has no next value.

</details>
