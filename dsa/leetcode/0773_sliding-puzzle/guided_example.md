# Guided Example: Sliding Puzzle

We trace the step-by-step $2 \times 3$ grid state serialization (length-6 string representation), empty tile coordinate location ($0$), 4-directional grid swap transitions (up, down, left, right), Breadth-First Search (BFS) level-order traversal, visited set cycle prevention ($vis$), target state convergence (`"123450"`), and parity unreachability detection ($-1$) on representative sliding board configurations:

- **Input:**
  $$
  board = \begin{bmatrix}
  1 & 2 & 3 \\
  4 & 0 & 5
  \end{bmatrix}
  $$
- **Required output:** `1`
  - Puzzle rules & target configuration:
    - The board is a $2 \times 3$ grid containing tiles $1, 2, 3, 4, 5$ and an empty space represented by $0$.
    - A legal move consists of sliding an adjacent tile (horizontally or vertically) into the empty space $0$.
    - Solved target configuration:
      $$
      \text{Target} = \begin{bmatrix}
      1 & 2 & 3 \\
      4 & 5 & 0
      \end{bmatrix} \iff \text{"123450"}
      $$
    - Objective: Find the **minimum number of moves** to reach the target, or return `-1` if impossible.
    - For $\begin{bmatrix} 1 & 2 & 3 \\ 4 & 0 & 5 \end{bmatrix}$:
      - Initial string: `"123405"`.
      - Empty space $0$ is at coordinate $(1, 1)$ (index 4).
      - Neighboring tiles:
        - Up: tile $2$ at $(0, 1)$
        - Left: tile $4$ at $(1, 0)$
        - Right: tile $5$ at $(1, 2)$
      - Swapping $0$ with right neighbor $5$ transforms `"123405"` directly into `"123450"`.
      - Target reached in exactly **1 move**.
- **State Space Boundedness & BFS Shortest Path Invariant:**
  - **Finite State Space ($6! = 720$):**
    - A $2 \times 3$ board has only $6$ positions.
    - The maximum number of distinct tile permutations is:
      $$
      6! = 720 \text{ states}
      $$
    - Due to alternating permutation parity invariants, the state graph splits into two disconnected components of $360$ states each.
    - Every reachable configuration lies at distance $\le 31$ moves from the target!
  - **Breadth-First Search (BFS) Optimality:**
    - Because each move has uniform unit weight ($+1$ step), standard queue-based BFS is mathematically guaranteed to discover the target state at the **minimum possible depth**:
      $$
      \text{depth}(target) = \min \text{ path length}
      $$
    - Use a hash set $vis$ to record all explored configurations, preventing cycles and infinite loops.
- **Step-by-Step Worked Execution Trace on $board = [[1, 2, 3], [4, 0, 5]]$:**
  - Initial configuration:
    $$
    start = \text{"123405"}, \quad target = \text{"123450"}
    $$
  - Check immediate match: $start \ne target$ ($`"123405" \ne "123450"`$).
  - **Level 0 (Initialization):**
    - Initialize queue: $q = [\text{"123405"}]$.
    - Initialize visited set: $vis = \{\text{"123405"}\}$.
    - Move counter: $ans = 0$.
  - **Level 1 (Expand $q$, $ans = 1$):**
    - Pop state: $x = \text{"123405"}$.
    - Map $x$ onto $2 \times 3$ grid:
      $$
      \begin{matrix}
      1 & 2 & 3 \\
      4 & \mathbf{0} & 5
      \end{matrix}
      $$
    - Locate position of empty tile $0$:
      $$
      \text{Row } i = 1, \quad \text{Column } j = 1 \quad (\text{string index } 4)
      $$
    - Generate all valid adjacent swaps:
      1. **Move Up ($x - 1, y = 0, 1$):**
         - Swap $(1, 1)$ with $(0, 1)$ (tile 2):
           $$
           \begin{matrix}
           1 & \mathbf{0} & 3 \\
           4 & \mathbf{2} & 5
           \end{matrix} \iff \mathbf{\text{"103425"}}
           $$
         - Target check: `"103425"` $\ne$ `"123450"`. Not visited $\implies$ add to $vis$ and $q$.
      2. **Move Left ($x, y - 1 = 1, 0$):**
         - Swap $(1, 1)$ with $(1, 0)$ (tile 4):
           $$
           \begin{matrix}
           1 & 2 & 3 \\
           \mathbf{0} & \mathbf{4} & 5
           \end{matrix} \iff \mathbf{\text{"123045"}}
           $$
         - Target check: `"123045"` $\ne$ `"123450"`. Not visited $\implies$ add to $vis$ and $q$.
      3. **Move Right ($x, y + 1 = 1, 2$):**
         - Swap $(1, 1)$ with $(1, 2)$ (tile 5):
           $$
           \begin{matrix}
           1 & 2 & 3 \\
           4 & \mathbf{5} & \mathbf{0}
           \end{matrix} \iff \mathbf{\text{"123450"}}
           $$
         - Target check:
           $$
           \text{"123450"} == target \implies \mathbf{Target\ State\ Discovered!}
           $$
         - Return current BFS depth:
           $$
           ans = \mathbf{1}
           $$
- **Unreachable Parity Inversion Trace ($board = [[1, 2, 3], [5, 4, 0]]$):**
  - Start string: `"123540"`.
  - Notice tiles 4 and 5 are inverted relative to target `"123450"`.
  - Grid swaps preserve the permutation parity invariant.
  - The BFS explores all 360 states in its connected component without encountering `"123450"`.
  - Queue empties $\implies$ returns **`-1`**.
- **Already Solved Grid ($[[1, 2, 3], [4, 5, 0]]$):**
  - $start == target$ initially.
  - Returns **`0`** immediately.

This instance demonstrates state space Cayley graph traversal and level-order shortest path tree expansion, mathematically proves why breadth-first exploration guarantees minimal transition sequences on unweighted state digraphs, and derives $O(V + E)$ runtime ($V \le 720$) and $O(V)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a $2 \times 3$ sliding puzzle board:
Tiles 1 to 5 and an empty space 0.
Find the **minimum number of moves** to reach target `[[1, 2, 3], [4, 5, 0]]`, or `-1` if impossible.

```text
board:
  1 2 3
  4 0 5

Move 1: Slide 5 left into the 0 space:
  1 2 3
  4 5 0  (Target reached!)

Result: 1 move
```

### The Invariant of the Small State Space BFS
- Total permutations of 6 items is only $6! = 720$.
- Because each move has weight 1, Breadth-First Search (BFS) finds the shortest path to target.
- A visited set prevents revisiting previously explored board strings.

---

## 2. Conceptual Foundation & Invariants

### 1. State Serialization:
$$
\text{State } s = \text{str}(board[0][0]) + \dots + \text{str}(board[1][2]) \in S_6
$$
$$
target = \text{"123450"}
$$

### 2. Transition Generation:
Locate position $(i, j)$ of $0$:
$$
(x, y) \in \{(i-1, j), (i+1, j), (i, j-1), (i, j+1)\} \cap [0, 1] \times [0, 2]
$$
$$
s' = \text{swap}(s, \; (i, j), \; (x, y))
$$

> **Cayley Graph Parity Invariant.** The 15-puzzle and 5-puzzle state transitions form generators of the alternating group $A_6$. States with odd permutation parity relative to the target have geodesic distance $\infty$ in the state manifold, correctly terminating BFS with $-1$.

---

## 3. Step-by-Step Worked Execution

We trace $board = [[1, 2, 3], [4, 0, 5]]$:

---

### Step 1: Initial State
- $start = \text{"123405"}$.
- $0$ is at $(1, 1)$.

---

### Step 2: Level 1 Expansion
- Move up: `"103425"`.
- Move left: `"123045"`.
- Move right: `"123450"` $\implies$ Matches Target!

---

### Step 3: Return Depth
- Distance = **`1`**.

---

## 4. Complete Execution Trace

| BFS Level $ans$ | Explored State String | Position of 0 | Neighbors Generated | Target Match? | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `"123405"` | $(1, 1)$ | — | No | Seed $q$ and $vis$ |
| $1$ | `"123405"` | $(1, 1)$ | `"103425"` (Up) | No | Enqueue |
| $1$ | `"123405"` | $(1, 1)$ | `"123045"` (Left) | No | Enqueue |
| **$1$** | **`"123405"`** | **$(1, 1)$** | **`"123450"` (Right)** | **Yes** | **Return `1`** |

---

## 5. Boundary Cases & Failure Modes

- **Already Solved ($"123450"$):** Returns 0 immediately.
- **Unreachable Parity ($"123540"$):** BFS exhausts all 360 accessible states and returns -1.
- **Max Depth:** Longest minimal path in 6-puzzle is 31 moves; BFS finishes within 31 levels.
- **Cycles in Graph:** Visited set $vis$ prevents infinite loops.

---

## 6. Traps & Common Anti-Patterns

- **DFS instead of BFS:** Depth-First Search does not find the shortest path and easily blows the recursion limit or explores long suboptimal paths. Shortest path in unweighted graphs requires BFS.
- **Grid Copy Overhead:** Recreating 2D lists for each state creates high object allocation overhead. Representing states as 6-character strings is fast, hashable, and clean.
- **Missing Boundaries on 0:** The empty space at $(0, 2)$ cannot move right or up; coordinate validation $0 \le x < 2$ and $0 \le y < 3$ prevents invalid moves.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Total states $|V| \le 720 / 2 = 360$ reachable states.
  - Each state has at most 3 transitions $|E| \le 3 \times 360 = 1080$.
  - Total Time: strictly bounded $\mathcal{O}(|V| + |E|) \le 1500$ operations. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(|V|) \le 720$ strings stored in the visited set and BFS queue.
