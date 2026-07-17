# Map of Highest Peak

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1765 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/map-of-highest-peak/) |

## Problem Description

### Goal

An $m \times n$ integer matrix `isWater` describes a map of land and water. A value of `1` marks water, while `0` marks land.

Assign a non-negative integer height to every cell. Every water cell must have height $0$, and the absolute height difference between any two cells sharing a side must be at most $1$. Diagonal cells are not adjacent.

Among all assignments satisfying these rules, maximize the greatest height appearing anywhere in the map. Return any height matrix that attains that maximum.

### Function Contract

**Inputs**

- `isWater`: an $R \times C$ binary matrix, with $1 \le R,C \le 10^3$.
- `isWater[r][c] = 1` denotes water and `isWater[r][c] = 0` denotes land.
- At least one cell is water.

**Return value**

- Return an $R \times C$ integer matrix whose water cells have height $0$, whose heights are non-negative, and whose side-adjacent cells differ by at most $1$.
- The maximum value in the returned matrix must be as large as any valid assignment permits.

### Examples

**Example 1**

- Input: `isWater = [[0,1],[0,0]]`
- Output: `[[1,0],[2,1]]`
- Explanation: The water cell is at height $0$; moving one step away raises the height by one.

**Example 2**

- Input: `isWater = [[0,0,1],[1,0,0],[0,0,0]]`
- Output: `[[1,1,0],[0,1,1],[1,2,2]]`
- Explanation: The greatest attainable height is $2$. Any valid assignment attaining that value is acceptable.

**Example 3**

- Input: `isWater = [[1]]`
- Output: `[[0]]`
- Explanation: The only cell is water, so its required height is $0$.

### Required Complexity

- **Time:** $O(RC)$
- **Space:** $O(RC)$

<details>
<summary>Approach</summary>

#### General

**Turn the adjacency rule into an upper bound**

Consider a cell and any water cell at Manhattan distance $d$. Along a shortest path of $d$ side-adjacent moves, the height can rise by at most one per move from the water's required height $0$. Consequently, that cell's height cannot exceed $d$. Taking the nearest water source gives the strongest bound: every valid assignment has

$$
\text{height}(r,c)\le \min_{\text{water }(x,y)}\bigl(\lvert r-x\rvert+\lvert c-y\rvert\bigr).
$$

**Use the distance bound as the assignment**

Assign each cell exactly its distance to the nearest water cell. Water then has distance $0$, all values are non-negative, and moving across one grid edge changes a shortest-path distance by at most one. The assignment is therefore valid and reaches every cell's individual upper bound. In particular, no other valid assignment can have a larger overall maximum.

**Start breadth-first search from all water cells**

Place every water cell in one queue at height $0$. This is a multi-source breadth-first search: rather than running a separate search from each source, all distance-zero cells form the first layer. Whenever a cell is removed, assign each still-unvisited neighbor its height plus one and append that neighbor.

**Why the first visit is final**

The queue processes cells in nondecreasing distance layers. A cell first reached from layer $d$ has a water path of length $d+1`; any undiscovered alternative path is no shorter. Marking the cell when it is enqueued both fixes its nearest-water distance and prevents duplicate work. Since at least one water cell exists and the rectangular grid is connected, every cell is eventually assigned.

#### Complexity detail

There are $RC$ cells. Each cell enters and leaves the queue once, and at most four neighbors are inspected for it, so the running time is $O(RC)$. The returned height matrix and the breadth-first queue can each contain $O(RC)$ entries, giving $O(RC)$ space.

#### Alternatives and edge cases

- **Search separately from every water cell:** Repeating breadth-first search can require $O(WRC)$ time for $W$ water cells, even though all sources can share one traversal.
- **Compare every cell with every water coordinate:** Direct Manhattan-distance minimization is correct but also takes $O(WRC)$ time.
- **Two dynamic-programming sweeps:** Forward and backward distance passes can solve this rectangular Manhattan-distance problem in $O(RC)$ time, but the boundary dependencies are easier to implement incorrectly than multi-source BFS.
- **Single water cell:** Heights become ordinary Manhattan distances from that source.
- **All cells are water:** Every source begins at height $0$, and the returned matrix is all zeros.
- **Multiple equidistant sources:** The identity of the source does not matter; only the shared minimum distance determines the height.
- **No diagonal movement:** Only north, east, south, and west neighbors contribute one BFS step.
- **One-row or one-column maps:** The same traversal reduces to distances along a line.
- **Maximum dimensions:** Iterative BFS avoids recursion depth and visits each cell only once.

</details>
