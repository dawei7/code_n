# Guided Example: Detect Cycles in 2D Grid

## 1. Instance & Teaching Goal

We are given a 2D matrix $\text{grid}$ of size $R \times C$ containing lowercase English characters. Movement is permitted only between cardinally adjacent cells (up, down, left, right). A cycle is defined as a closed path of length $k \ge 4$ such that:
1. Every cell along the path contains the same character.
2. Every consecutive pair of cells on the path shares an edge, and the first and last cells share an edge.
3. No intermediate cell is visited more than once.

We must decide whether at least one such monochromatic cycle exists in the grid.

We select the representative grid containing a $2 \times 2$ cycle of character `'c'`:
$$\text{grid} = \begin{bmatrix} \text{'c'} & \text{'c'} & \text{'a'} \\ \text{'c'} & \text{'c'} & \text{'b'} \\ \text{'a'} & \text{'b'} & \text{'a'} \end{bmatrix}$$

The algorithm must return:
$$\text{true}$$

Our teaching goal is to walk through cycle detection in undirected monochromatic grid graphs using Depth-First Search with strict parent exclusion. We explain why trivial two-step oscillations ($u \to v \to u$) must be filtered out using predecessor tracking, and how encountering an already-visited cell that is not the immediate predecessor guarantees the existence of a chordless cycle of length at least four.

## 2. Conceptual Foundation & Invariants

We model the grid as an undirected graph $G = (V, E)$ where vertices are grid coordinates $(r, c)$, and edges connect orthogonal neighbors $(r_1, c_1)$ and $(r_2, c_2)$ if and only if $\text{grid}[r_1][c_1] = \text{grid}[r_2][c_2]$.

In any undirected graph, a cycle exists if and only if a depth-first or breadth-first traversal encounters a back-edge to an already-visited vertex other than the immediate predecessor (parent). Because the graph is embedded on a 2D square lattice, the shortest non-backtracking simple cycle must traverse at least $4$ distinct edges (such as a $2 \times 2$ square loop). Hence, any non-trivial back-edge automatically closes a cycle of length $k \ge 4$.

```
+-------------------------------------------------------------------------+
|                  PARENT-EXCLUSION CYCLE DETECTION                       |
|                                                                         |
| Grid slice:                                                             |
|   (0,0):'c' ----- (0,1):'c'                                             |
|       |               |                                                 |
|       |               |                                                 |
|   (1,0):'c' ----- (1,1):'c'                                             |
|                                                                         |
| Traversal sequence:                                                     |
|   Start at (0,0), parent = (-1,-1)                                      |
|   Move to  (0,1), parent = (0,0)                                        |
|   Move to  (1,1), parent = (0,1)                                        |
|   Move to  (1,0), parent = (1,1)                                        |
|   From (1,0), neighbor (0,0) is ALREADY VISITED and (0,0) != (1,1)      |
|   ==> Back-edge closes a valid 4-cycle! Return True.                    |
+-------------------------------------------------------------------------+
```

### State Parameter Reference

| Parameter | Type | Domain | Role in Traversal State Machine |
|---|---|---|---|
| $(r, c)$ | Coordinate Pair | $[0, R-1] \times [0, C-1]$ | Current active cell in DFS exploration |
| $(p_r, p_c)$ | Coordinate Pair | $([-1, R-1] \times [-1, C-1])$ | Immediate predecessor (parent) cell from which $(r, c)$ was reached |
| $\text{vis}[r][c]$ | 2D Boolean Array | $\{\text{False}, \text{True}\}$ | Marks cells that have already entered the traversal frontier |
| $\text{target\_char}$ | Character | Lowercase English letter | The fixed uniform character of the current connected component |
| $(nr, nc)$ | Coordinate Pair | $[0, R-1] \times [0, C-1]$ | Cardinal neighbor being considered |

> [!IMPORTANT]
> **Parent-Exclusion Invariant**:
> When exploring from $(r, c)$, an adjacent neighbor $(nr, nc)$ is an invalid cycle edge if $(nr, nc) = (p_r, p_c)$, representing an immediate reverse traversal along the incoming undirected edge. If $\text{vis}[nr][nc] = \text{True}$ and $(nr, nc) \neq (p_r, p_c)$, the edge connects to an ancestor along an alternate branch, proving a simple cycle of length $\ge 4$ exists.

```mermaid
flowchart TD
    accTitle: Grid Cycle Detection Pipeline
    accDescr: Flowchart illustrating monochromatic DFS traversal with parent tracking and back-edge cycle detection.
    Start([Scan Grid Cells]) --> UnvisitedCheck{vis[r][c] == False?}
    UnvisitedCheck -- No --> NextCell[Move to next grid cell]
    UnvisitedCheck -- Yes --> InitDFS["Mark vis[r][c] = True, Push (r, c, -1, -1)"]
    InitDFS --> StackLoop{Stack Empty?}
    StackLoop -- Yes --> NextCell
    StackLoop -- No --> PopCell["Pop (x, y, px, py)"]
    PopCell --> CheckNeighbors[Iterate 4 cardinal neighbors nx, ny]
    CheckNeighbors --> ValidSame{"In bounds & same char?"}
    ValidSame -- No --> NextNeighbor[Next neighbor]
    ValidSame -- Yes --> ParentCheck{"(nx, ny) == (px, py)?"}
    ParentCheck -- Yes --> NextNeighbor
    ParentCheck -- No --> VisCheck{"vis[nx][ny] == True?"}
    VisCheck -- Yes --> CycleFound([Return True: Cycle Detected])
    VisCheck -- No --> VisitNext["Mark vis[nx][ny] = True, Push (nx, ny, x, y)"]
    VisitNext --> NextNeighbor
    NextNeighbor --> CheckNeighbors
    NextCell --> AllScanned{All cells scanned?}
    AllScanned -- No --> UnvisitedCheck
    AllScanned -- Yes --> NoCycle([Return False: No Cycle Found])
```

## 3. Step-by-Step Worked Execution

We trace the traversal of component `'c'` on our $3 \times 3$ grid:
- Row 0: `['c', 'c', 'a']`
- Row 1: `['c', 'c', 'b']`
- Row 2: `['a', 'b', 'a']`

We maintain the 2D boolean array $\text{vis}$ initialized to $\text{False}$.

### Step 1: Discover Component at $(0, 0)$
- Cell $(0, 0)$ has character `'c'` and $\text{vis}[0][0] = \text{False}$.
- Mark $\text{vis}[0][0] = \text{True}$.
- Initialize traversal stack with root $(0, 0)$ and parent $(-1, -1)$:
  $\text{stack} = [((0, 0), (-1, -1))]$.

### Step 2: Expand $(0, 0)$
- Pop $(x=0, y=0)$ with parent $(px=-1, py=-1)$.
- Examine neighbors:
  - Up $(-1, 0)$: Out of bounds.
  - Left $(0, -1)$: Out of bounds.
  - Down $(1, 0)$: Character is `'c'`. Not parent. $\text{vis}[1][0] = \text{False}$.
    (Assume traversal explores right first, or pushes both; we follow depth-first to $(0, 1)$).
  - Right $(0, 1)$: Character is `'c'`. Not parent. $\text{vis}[0][1] = \text{False}$.
- Mark $\text{vis}[0][1] = \text{True}$ and push $((0, 1), (0, 0))$.

### Step 3: Expand $(0, 1)$
- Pop $(x=0, y=1)$ with parent $(px=0, py=0)$.
- Examine neighbors:
  - Left $(0, 0)$: Matches parent $(px=0, py=0)$! Ignored by parent exclusion.
  - Right $(0, 2)$: Character is `'a'` $\neq \text{'c'}$. Ignored.
  - Down $(1, 1)$: Character is `'c'`. Not parent. $\text{vis}[1][1] = \text{False}$.
- Mark $\text{vis}[1][1] = \text{True}$ and push $((1, 1), (0, 1))$.

### Step 4: Expand $(1, 1)$
- Pop $(x=1, y=1)$ with parent $(px=0, py=1)$.
- Examine neighbors:
  - Up $(0, 1)$: Matches parent $(px=0, py=1)$! Ignored by parent exclusion.
  - Right $(1, 2)$: Character is `'b'` $\neq \text{'c'}$. Ignored.
  - Down $(2, 1)$: Character is `'b'` $\neq \text{'c'}$. Ignored.
  - Left $(1, 0)$: Character is `'c'`. Not parent. $\text{vis}[1][0] = \text{False}$.
- Mark $\text{vis}[1][0] = \text{True}$ and push $((1, 0), (1, 1))$.

### Step 5: Expand $(1, 0)$ and Detect Cycle
- Pop $(x=1, y=0)$ with parent $(px=1, py=1)$.
- Examine neighbors:
  - Right $(1, 1)$: Matches parent $(px=1, py=1)$! Ignored by parent exclusion.
  - Down $(2, 0)$: Character is `'a'` $\neq \text{'c'}$. Ignored.
  - Left $(1, -1)$: Out of bounds.
  - Up $(0, 0)$: Character is `'c'`.
    - Check parent: $(0, 0) \neq (1, 1)$. True (not parent).
    - Check visited: $\text{vis}[0][0] = \text{True}$!
- **Cycle Detected**: A back-edge connects $(1, 0)$ to $(0, 0)$.
- The closed path is $(0, 0) \to (0, 1) \to (1, 1) \to (1, 0) \to (0, 0)$ with $4$ distinct cells.
- The algorithm immediately terminates and returns $\text{true}$.

## 4. Complete Execution Trace

| Step | Active Cell $(x, y)$ | Parent $(px, py)$ | Neighbor $(nx, ny)$ | Grid Value | Condition Check | Resulting Action |
|---|---|---|---|---|---|---|
| 1 | $(0, 0)$ | $(-1, -1)$ | $(0, 1)$ | `'c'` | Unvisited, $\neq$ parent | Mark visited, push to stack |
| 2 | $(0, 1)$ | $(0, 0)$ | $(0, 0)$ | `'c'` | $(nx, ny) == (px, py)$ | **Skip (Immediate Parent)** |
| 3 | $(0, 1)$ | $(0, 0)$ | $(0, 2)$ | `'a'` | $\text{grid}[0][2] \neq \text{'c'}$ | Skip (Different Character) |
| 4 | $(0, 1)$ | $(0, 0)$ | $(1, 1)$ | `'c'` | Unvisited, $\neq$ parent | Mark visited, push to stack |
| 5 | $(1, 1)$ | $(0, 1)$ | $(0, 1)$ | `'c'` | $(nx, ny) == (px, py)$ | **Skip (Immediate Parent)** |
| 6 | $(1, 1)$ | $(0, 1)$ | $(1, 2)$ | `'b'` | $\text{grid}[1][2] \neq \text{'c'}$ | Skip (Different Character) |
| 7 | $(1, 1)$ | $(0, 1)$ | $(2, 1)$ | `'b'` | $\text{grid}[2][1] \neq \text{'c'}$ | Skip (Different Character) |
| 8 | $(1, 1)$ | $(0, 1)$ | $(1, 0)$ | `'c'` | Unvisited, $\neq$ parent | Mark visited, push to stack |
| 9 | $(1, 0)$ | $(1, 1)$ | $(1, 1)$ | `'c'` | $(nx, ny) == (px, py)$ | **Skip (Immediate Parent)** |
| 10 | $(1, 0)$ | $(1, 1)$ | $(2, 0)$ | `'a'` | $\text{grid}[2][0] \neq \text{'c'}$ | Skip (Different Character) |
| 11 | $(1, 0)$ | $(1, 1)$ | $(0, 0)$ | `'c'` | Visited AND $(0,0) \neq (1,1)$ | **CYCLE FOUND: Return True** |

### Path Reconstruction

$$\text{Path} = \{(0, 0) \to (0, 1) \to (1, 1) \to (1, 0) \to (0, 0)\}$$
Total distinct vertices visited: $4$. All vertices share label `'c'`. The cycle condition is fully satisfied.

## 5. Algorithmic Correctness

### Soundness (No False Positives)

Let $u = (x, y)$ be the active vertex and $v = (nx, ny)$ be an adjacent vertex such that:
1. $\text{grid}[u] = \text{grid}[v] = C$.
2. $\text{vis}[v] = \text{True}$.
3. $v \neq p(u)$, where $p(u)$ is the unique tree predecessor of $u$.

Because $v$ is already marked visited in the active DFS tree, $v$ was reached earlier in the traversal. In a depth-first search tree, any non-tree edge $(u, v)$ to an already-visited vertex must connect $u$ to an ancestor in the DFS tree.
Since $v \neq p(u)$, the distance from $v$ to $u$ along tree edges is at least $2$. Adding the back-edge $(u, v)$ completes a simple cycle $C_{\text{simple}} = (v = w_0, w_1, \dots, w_k = u, v)$ containing at least $3$ edges.
Furthermore, the underlying graph is a square grid graph (bipartite). A square lattice contains no odd cycles (triangles). Hence, any simple cycle in a grid graph must have an even length $\ge 4$. Thus, the detected cycle provably has length at least $4$, establishing soundness.

### Completeness (No False Negatives)

Suppose the grid contains at least one monochromatic cycle $K$ of length $\ge 4$.
The cycle $K$ lies entirely within some monochromatic connected component.
When the outer nested loop iterates to the first unvisited vertex $s \in K$, it initiates a traversal covering the component containing $K$.
Because $K$ contains a cycle, the connected component is not a tree; it has $|E| \ge |V|$. A spanning forest construction by DFS over any graph with a cycle must discover at least one back-edge.
Since the back-edge connects two vertices in the same connected component that are not parent and child, the algorithm is guaranteed to trigger the condition $\text{vis}[v] = \text{True} \land v \neq p(u)$ and return $\text{true}$.

## 6. Traps This Instance Exposes

1. **Failure to Track Predecessor / Parent**:
   Because movement between adjacent cells is bidirectional, moving from $u$ to $v$ immediately presents $u$ as a visited neighbor of $v$. Without parent exclusion, the algorithm misidentifies every single step $u \to v \to u$ as a cycle of length $2$, returning `true` on every multi-cell component.

2. **Cross-Component Bleeding**:
   Cells must be compared against the component's root character (or adjacent cells must have matching values). If neighbor checking fails to verify $\text{grid}[nx][ny] == \text{grid}[x][y]$, cycles spanning multiple distinct letters will be erroneously reported.

3. **Global Visited Set vs. Current Path Set**:
   In directed graph cycle detection, one must track an active recursion stack (`in_path`). In an undirected graph, however, a single global $\text{vis}$ array suffices: any back-edge within an undirected connected component proves the existence of a cycle, so vertices do not need to be un-visited upon backtracking.

4. **Call Stack Overflow on Deep Grid Components**:
   A grid of size $500 \times 500$ can have a serpentine path of $250\,000$ cells. Unbounded recursive DFS will trigger a maximum recursion depth error (stack overflow). Using an explicit stack (iterative DFS) or BFS avoids stack exhaustion.

## 7. Complexity Derivation

### Time Complexity

Let $R$ and $C$ be the number of rows and columns, respectively. The total number of cells is $V = R \cdot C \le 500 \times 500 = 250\,000$.
- **Outer Loops**: Every cell is examined at most once by the outer nested loops: $\mathcal{O}(R \cdot C)$.
- **Inner Traversal**:
  - Each cell is pushed and popped from the traversal stack at most once due to the $\text{vis}$ guard.
  - From each cell, exactly $4$ cardinal neighbors are inspected.
  - Each edge in the grid graph is evaluated at most twice (once from each endpoint).

Total time complexity is strictly:
$$\mathcal{O}(R \cdot C)$$
With $R, C \le 500$, at most $10^6$ operations are performed, executing in under 60 milliseconds.

### Auxiliary Space Complexity

- **Visited Matrix**: A 2D boolean array of dimensions $R \times C$ requires $R \cdot C$ bytes.
- **Traversal Stack**: In the worst case (a single non-branching snake component covering the entire grid), the stack holds at most $R \cdot C$ tuples of coordinates.

Total auxiliary space complexity is:
$$\mathcal{O}(R \cdot C)$$
Proportional to the grid area.
