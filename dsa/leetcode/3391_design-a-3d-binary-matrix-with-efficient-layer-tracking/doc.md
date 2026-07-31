# Design a 3D Binary Matrix with Efficient Layer Tracking

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3391 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Design, Heap (Priority Queue), Matrix, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/) |

## Problem Description

### Goal

Maintain a binary cube with dimensions $n\times n\times n$. Every cell begins at zero. A `setCell(x, y, z)` operation changes the selected cell to one, while `unsetCell(x, y, z)` changes it to zero. Applying either operation when the cell already has the requested value leaves the state unchanged.

The cube consists of $n$ two-dimensional layers indexed by the first coordinate $x$. A `largestMatrix()` query must return the layer containing the greatest number of ones. When several layers have the same count—including when every cell is zero—choose the largest layer index.

### Function Contract

**Inputs**

- `operations`: A sequence beginning with `"Matrix3D"`, followed by `"setCell"`, `"unsetCell"`, and `"largestMatrix"` calls.
- `arguments`: A parallel sequence of argument lists. The constructor receives `[n]`, updates receive `[x, y, z]`, and a query receives `[]`.

The dimension satisfies $1\le n\le100$, and each coordinate satisfies $0\le x,y,z<n$. There are at most $10^5$ update calls and at most $10^4$ `largestMatrix` calls. Let $m$ be the total number of operations in one sequence.

**Return value**

- A parallel result list. Constructor and update calls contribute `null`; each `largestMatrix` call contributes the selected layer index.

### Examples

**Example 1**

- Input: `operations = ["Matrix3D", "setCell", "largestMatrix", "setCell", "largestMatrix", "setCell", "largestMatrix"]`, `arguments = [[3], [0, 0, 0], [], [1, 1, 2], [], [0, 0, 1], []]`
- Output: `[null, null, 0, null, 1, null, 0]`

Layer zero first leads alone, then layer one wins their one-cell tie because its index is larger. The final update gives layer zero two ones.

**Example 2**

- Input: `operations = ["Matrix3D", "setCell", "largestMatrix", "unsetCell", "largestMatrix"]`, `arguments = [[4], [2, 1, 1], [], [2, 1, 1], []]`
- Output: `[null, null, 2, null, 3]`

After the only one is removed, all four layers tie at zero, so the largest index is 3.
