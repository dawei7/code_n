## General

**Every water component can be harvested completely**

A fisher can move only between horizontally or vertically adjacent positive cells. Therefore, starting in one water cell permits reaching exactly its connected component of positive cells.

Every cell in that component can be visited and all its fish caught. No land cell can be crossed, so fish in a different component are unreachable from the same start.

The problem reduces to:

> Find the sum of each positive connected component and return the largest sum.

**Use zero as both land and visited marker**

The input already uses zero to mean land. When DFS visits a positive cell, it stores its fish count locally and writes:

`grid[i][j] = 0`.

That cell now behaves like land for future searches, preventing revisits and cycles.

This removes the need for a separate visited matrix but intentionally mutates the input grid.

**Generate the four directions compactly**

The sequence:

`(-1, 0, 1, 0, -1)`

passed through `pairwise` yields:

$$
(-1,0),\ (0,1),\ (1,0),\ (0,-1).
$$

These are up, right, down, and left.

For each offset $(a,b)$, neighbor coordinates are $(i+a,j+b)$. Bounds checks ensure the cell exists, and `grid[x][y]` truthiness ensures it still contains positive fish.

**Accumulate one component recursively**

`dfs(i,j)` starts:

`cnt = grid[i][j]`.

It marks the cell zero, recursively visits every adjacent positive neighbor, and adds each returned component portion to `cnt`.

Because a neighbor is zeroed before its own recursion explores further, every water cell is counted at most once even when several paths connect to it.

The returned `cnt` is the total original fish in the connected component containing the starting cell.

**Outer scan discovers every component**

The nested loops inspect every grid position.

- A zero cell is land or already visited and is skipped.
- A positive cell has not yet belonged to an earlier DFS, so it starts a new component traversal.

The algorithm compares that component sum with `ans`.

After DFS finishes, every cell in the component is zero, so later scan positions inside it do not start duplicate traversals.

**Trace the first example**

The component containing values three and four in the rightmost column has sum seven. DFS starting at either unvisited cell reaches both and returns seven.

Another component containing four and one on the left has sum five, while the bottom component containing three and two also sums five.

The outer maximum retains seven.

**Why movement order does not affect the sum**

DFS may explore up before right and so on, but addition is independent of traversal order. The visited marking guarantees the set of reached cells is exactly the component.

Any depth-first or breadth-first ordering would collect the same component sum.


When `dfs(i,j)` begins, $(i,j)$ is an unvisited positive cell. It adds that cell's original fish once and marks it visited.

For every adjacent unvisited water cell, recursion returns the sum of the portion reachable through it. Marking prevents overlap from being counted twice.

Connectivity guarantees every component cell can be reached by a sequence of such neighbor steps, so recursive exploration eventually visits all of them. It never crosses a zero, so no outside cell is included.

Thus the returned value is exactly the component's fish total.


Every positive component has a first cell encountered by the outer scan. That cell starts exactly one DFS, so all component totals are considered once.

A fisher starting in a component can catch its entire total and cannot reach another component. Therefore, the best possible catch is the maximum considered sum, which `ans` stores.

If no positive cell exists, no DFS runs and initialized zero is returned.

**Why mutation is safe inside the algorithm**

The original fish value is copied into `cnt` before the grid entry becomes zero. No later computation needs that cell's original value because its contribution is already included in the active recursive sum.

Mutation is a deliberate visited-state optimization. If callers required the original grid afterward, a separate Boolean matrix or a copied grid would be needed.

**Recursion depth**

In the worst case, all $mn$ cells form one component and the DFS path can use $O(mn)$ call frames.

Here $m,n\le10$, so at most 100 frames are involved, safely small for ordinary recursion.

## Complexity detail

Every cell is scanned by the outer loops, and every positive cell is entered by DFS exactly once. Each entry checks four neighbors. Total time is $O(mn)$.

The recursion stack can hold $O(mn)$ frames in the worst case. No separate visited matrix is allocated because the grid is modified in place.

## Alternatives and edge cases

- **Breadth-first search:** Uses an explicit queue and has the same $O(mn)$ bounds.
- **Separate visited matrix:** Preserves the grid at the cost of $O(mn)$ additional storage.
- **Union-find:** Can merge adjacent water cells and track component sums, but is heavier than a grid traversal.
- **All land:** No component starts and answer remains zero.
- **Single water cell:** Its fish value is one complete component total.
- **Diagonal water cells:** They are not connected because only four directions count.
- **Cycles within water:** Zeroing on entry prevents infinite recursion and double counting.
- **Several equal maximum components:** Only the maximum sum is returned, so identity does not matter.
- **Input mutation:** Every visited water cell becomes zero.
- **Small dimensions:** Recursion depth is bounded by at most 100 cells under the contract.
