# Minimum Knight Moves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1197 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-knight-moves/) |

## Problem Description

### Goal

An infinite chessboard has integer coordinates extending without bound in every direction, and a knight begins at `[0,0]`. Each legal knight move travels two squares along one coordinate axis and one square along the other axis, giving eight possible signed displacements.

Given target coordinates `[x,y]`, return the minimum number of legal moves required to reach that square. A route is guaranteed to exist, including for targets with negative coordinates and for the starting square itself.

### Function Contract

**Inputs**

- `x`: The target horizontal coordinate, where $-300\le x\le300$.
- `y`: The target vertical coordinate, where $-300\le y\le300$.
- The target also satisfies $0\le\lvert x\rvert+\lvert y\rvert\le300$.

**Return value**

- The minimum number of knight moves from `[0,0]` to `[x,y]`.

### Examples

**Example 1**

- Input: `x = 2`, `y = 1`
- Output: `1`

One legal knight move reaches the target directly.

**Example 2**

- Input: `x = 5`, `y = 5`
- Output: `4`

One shortest route is `[0,0] -> [2,1] -> [4,2] -> [3,4] -> [5,5]`.

**Example 3**

- Input: `x = 0`, `y = 0`
- Output: `0`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Fold the board by symmetry.** Reflections across either axis and swapping the coordinates preserve knight distances. Replace both coordinates by their absolute values and arrange them as $a\ge b\ge0$. Only this first-octant target needs to be analyzed.

**Combine two unavoidable lower bounds.** One move changes either coordinate by at most 2, so at least $\lceil a/2\rceil$ moves are needed. It changes Manhattan distance by at most 3, so at least $\lceil(a+b)/3\rceil$ moves are needed. Start with

$$
d=\max\left(\left\lceil\frac{a}{2}\right\rceil,\left\lceil\frac{a+b}{3}\right\rceil\right).
$$

A knight changes square color on every move. Therefore the parity of the move count must match the parity of $a+b$; if `d + a + b` is odd, increment `d`. Away from the two small exceptional configurations, these coordinate, Manhattan, and parity constraints are also sufficient: knight moves can be paired and oriented to distribute the required progress across both coordinates without exceeding any bound.

**Repair the local exceptions.** The target $(1,0)$ needs three moves even though the global bounds suggest one, because no first move can land there and the knight must loop around. The target $(2,2)$ needs four moves rather than two for the same local-geometry reason. Handle those two symmetric forms explicitly; the bound-and-parity value is exact for every other target, including the origin.

#### Complexity detail

The method performs a fixed number of absolute-value, ordering, ceiling-division, maximum, parity, and exception checks regardless of coordinate magnitude. It therefore takes $O(1)$ time and uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Incremental move-count search:** Testing successive move counts until all coordinate, Manhattan, and parity bounds hold is correct after the two exceptions, but takes $O(r)$ time for distance scale $r$.
- **Breadth-first search:** BFS over board positions directly guarantees the shortest path, but explores $O(r^2)$ positions and uses $O(r^2)$ space for target distance scale $r$.
- **Bidirectional breadth-first search:** Expanding from both endpoints reduces constants but still maintains growing frontiers and visited maps.
- **Origin:** Both lower bounds and parity yield zero, so no special positive move count is introduced.
- **Negative coordinates:** Absolute values are safe because reflecting every move reflects an entire shortest route.
- **Swapped coordinates:** A 90-degree rotation exchanges axes without changing path length.
- **Target `(1,0)`:** The generic global bounds miss the three-move local detour.
- **Target `(2,2)`:** The generic two-move estimate is geometrically impossible and must become four.
- **Parity:** Raising a valid lower bound by one is necessary whenever its color parity differs from the target square.

</details>
