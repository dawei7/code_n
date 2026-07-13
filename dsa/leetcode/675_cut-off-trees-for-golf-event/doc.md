# Cut Off Trees for Golf Event

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 675 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Heap (Priority Queue), Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/cut-off-trees-for-golf-event/) |

## Problem Description
### Goal
A forest is represented by an $m \times n$ matrix: `0` is a cell that cannot be walked through, `1` is empty walkable ground, and a value greater than `1` is a walkable tree whose value is its height. Begin at `(0, 0)` and move one step north, east, south, or west at a time.

Cut every tree in order from shortest to tallest; all tree heights are distinct, and a cut tree's cell becomes `1`. Return the minimum total number of steps required to cut them all. If any required tree cannot be reached in that order, return `-1`. Cutting while standing on a tree costs no additional walking step.

### Function Contract
**Inputs**

- `forest`: a nonempty rectangular integer grid containing obstacles, ground, and uniquely ranked trees

**Return value**

- The minimum number of steps needed to visit and cut every tree in ascending height order, or `-1` when the required route is impossible

### Examples
**Example 1**

- Input: `forest = [[1,2,3],[0,0,4],[7,6,5]]`
- Output: `6`

**Example 2**

- Input: `forest = [[1,2,3],[0,0,0],[7,6,5]]`
- Output: `-1`

**Example 3**

- Input: `forest = [[2,3,4],[0,0,5],[8,7,6]]`
- Output: `6`

### Required Complexity

- **Time:** $O(T \log T + TRC)$
- **Space:** $O(RC)$

<details>
<summary>Approach</summary>

#### General

**The height order fixes the sequence of destinations**

Collect every cell whose value exceeds one and sort those cells by height. Tree heights are distinct, so there is no choice about which destination comes next. Cutting a tree changes its value to open ground but does not change whether the cell is traversable, so all shortest-path searches use the same obstacle layout.

**Use breadth-first search for each required leg**

From the current position, run BFS through nonzero cells until reaching the next tree. BFS explores positions in nondecreasing step count, making the first arrival the shortest possible distance for that leg. Add the distance and continue from that tree. If a BFS exhausts the reachable region, the mandatory destination is impossible and the entire answer is `-1`.

**Why independently shortest legs minimize the total**

Every valid walk must visit the same sorted sequence of tree positions. Its portion between two consecutive required positions cannot be shorter than the grid shortest-path distance between them. BFS attains that lower bound for each leg, and concatenating these shortest legs is valid because each endpoint is the next leg's start. Their sum is therefore the minimum possible total.

#### Complexity detail

Let `T` be the number of trees in an `R` by `C` grid. Sorting destinations costs $O(T \log T)$. Each of up to `T` breadth-first searches visits at most `RC` cells and edges, giving $O(T \log T + TRC)$ total time. A queue and visited set for one BFS use $O(RC)$ auxiliary space and are reused between legs.

#### Alternatives and edge cases

- **A* search for each leg:** Manhattan distance is an admissible heuristic and may inspect fewer cells in practice, but the same grid-sized worst case remains.
- **Bidirectional BFS:** can reduce explored layers for distant targets, though it adds two frontier and visited structures for every leg.
- **All-pairs shortest paths:** precomputes every passable-cell distance, but Floyd-Warshall takes $O((RC)^3)$ time and $O((RC)^2)$ space.
- A tree at the starting cell costs zero steps to cut before moving onward.
- If there are no trees, the required total is zero.
- If the start is blocked and any tree exists elsewhere, the first required tree is unreachable.

</details>
