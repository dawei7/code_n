# Maximum Square Area by Removing Fences From a Field

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2975 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/) |

## Problem Description
### Goal
A rectangular field has corners at `(1, 1)` and `(m, n)`, so its dimensions
are `(m - 1)` by `(n - 1)`. Each value in `hFences` gives the row coordinate of
a horizontal fence spanning the field, and each value in `vFences` gives the
column coordinate of a vertical fence spanning the field.

You may remove any number of the listed internal fences, including none. The
four boundary fences at rows `1` and `m` and columns `1` and `n` cannot be
removed. Choose two surviving horizontal fences and two surviving vertical
fences that bound a square, and maximize its area.

Return that maximum area modulo $10^9+7$, or `-1` if no square can be formed.

### Function Contract
**Inputs**

- `m`: the lower boundary's row coordinate
- `n`: the right boundary's column coordinate
- `hFences`: unique internal horizontal-fence coordinates
- `vFences`: unique internal vertical-fence coordinates

Let $H=\lvert\texttt{hFences}\rvert+2$ and
$V=\lvert\texttt{vFences}\rvert+2$, including boundary fences. The contract
guarantees $3\le m,n\le10^9$, $1\le H-2,V-2\le600$, and every internal fence
lies strictly between its corresponding boundaries.

**Return value**

The greatest attainable square area modulo $10^9+7$, or `-1` when the two
orientations have no common positive fence separation.

### Examples
**Example 1**

- Input: `m = 4`, `n = 3`, `hFences = [2,3]`, `vFences = [2]`
- Output: `4`
- Explanation: A horizontal and vertical span of length `2` can bound a square.

**Example 2**

- Input: `m = 6`, `n = 7`, `hFences = [2]`, `vFences = [4]`
- Output: `-1`
- Explanation: No separation occurs between a pair of fences in both orientations.
