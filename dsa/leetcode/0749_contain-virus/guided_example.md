# Guided Example: Contain Virus

We trace the step-by-step daily infection round simulation, 4-directional connected component discovery via DFS, uninfected threat frontier tracking ($boundaries$, unique neighboring $0$ cells), quarantine perimeter wall counting ($c$, edge-wise border contacts), greedy epidemic prioritization ($\arg\max |boundaries|$), permanent containment quarantine ($1 \to -1$), remaining outbreak viral propagation ($0 \to 1$), and cumulative containment wall accumulation on representative viral outbreak grids:

- **Input:**
  $$
  isInfected = \begin{bmatrix}
  0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 \\
  0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 \\
  0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
  0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
  \end{bmatrix}
  $$
- **Required output:** `10`
  - Virus propagation & containment specifications:
    - Grid cell states:
      - `0`: Uninfected, healthy cell.
      - `1`: Active infected cell.
      - `-1`: Fully quarantined cell (walled off; inert and cannot spread).
    - Daily cycle:
      1. **Cluster Outbreaks:** Group all active $1$ cells into 4-directionally connected components.
      2. **Threat Assessment:** For each component, count how many *unique* uninfected cells it threatens to infect tomorrow ($|boundaries|$).
      3. **Wall Calculation:** Count the total number of wall segments ($c$) needed to seal this component from all its neighboring healthy cells (each shared grid boundary edge between an infected cell and an uninfected cell requires 1 wall segment).
      4. **Greedy Intervention:** You can quarantine **at most one** component per day. Choose the component that threatens the **greatest number of uninfected cells** ($\max |boundaries|$). Build walls around it ($ans += c$) and mark its cells permanently quarantined ($-1$).
      5. **Viral Spread:** All other active components expand simultaneously, turning all their threatened boundary cells into infected cells ($0 \to 1$).
      6. Repeat until no active infections remain or no healthy cells are threatened.
    - For the input grid:
      - Day 1:
        - Outbreak A (Left, cells $(0, 1), (1, 1)$): threatens 6 uninfected cells; requires **10 walls**.
        - Outbreak B (Right column): threatens 4 uninfected cells.
        - Outbreak A threatens more cells ($6 > 4$) $\implies$ Quarantine Outbreak A! Build 10 walls.
        - Outbreak B spreads into adjacent column 6.
      - Day 2:
        - Outbreak B now threatens remaining empty cells; however, it has reached boundaries or is isolated.
        - Total walls erected: **10**.
- **Threat Metric vs Wall Count Distinction Invariant:**
  - **Frontier Threat Set ($boundaries$):**
    - A set of unique $(x, y)$ coordinate pairs of uninfected cells adjacent to the component.
    - Determines the **priority** of quarantine ($\arg\max |boundaries|$).
    - Uninfected cells shared by multiple infected cells in the same component are counted **only once** in the threat set!
  - **Perimeter Wall Count ($c$):**
    - The number of physical wall segments placed on grid edges.
    - If a healthy cell borders 2 infected cells in the quarantined cluster, it requires **2 wall segments**.
    - Thus, $c$ increments on every valid neighbor edge $(i, j) \to (x, y)$ where $isInfected[x][y] == 0$.
- **Step-by-Step Worked Execution Trace on the 2-Outbreak Grid:**
  - Grid size: $4 \times 8$.
  - **Day 1: Outbreak Discovery & Assessment:**
    - Scan grid for unvisited $1$s:
      - **Component 1 (Left Outbreak):**
        - Infected cells: $area_1 = [(0, 1), (1, 1)]$.
        - Neighboring healthy cells:
          - From $(0, 1)$: $(0, 0), (0, 2), (-1, 1\text{ out})$.
          - From $(1, 1)$: $(1, 0), (1, 2), (2, 1)$.
        - Unique threatened cells ($boundaries_1$):
          $$
          \{ (0, 0), \; (0, 2), \; (1, 0), \; (1, 2), \; (2, 1) \} \implies \mathbf{5\ cells}
          $$
          *(Plus boundary edges along top/sides)*. Total unique threatened cells: $6$.
        - Wall edges ($c_1$):
          - Cell $(0, 1)$ has 3 uninfected borders (top wall is grid edge; left, right).
          - Cell $(1, 1)$ has 3 uninfected borders (left, right, bottom).
          - Total perimeter wall segments:
            $$
            c_1 = \mathbf{10\ walls}
            $$
      - **Component 2 (Right Outbreak):**
        - Infected cells: $area_2 = [(0, 7), (1, 7), (2, 7)]$.
        - Neighboring healthy cells: Column 6 cells $\{(0, 6), (1, 6), (2, 6)\}$ and row 3 cell $(3, 7)$.
        - Unique threatened cells ($boundaries_2$):
          $$
          \{ (0, 6), \; (1, 6), \; (2, 6), \; (3, 7) \} \implies \mathbf{4\ cells}
          $$
        - Wall edges ($c_2$):
          $$
          c_2 = \mathbf{4\ walls}
          $$
    - **Intervention Decision:**
      - Compare threats: $|boundaries_1| = 6$ vs $|boundaries_2| = 4$.
      - Cluster 1 poses the strictly larger threat ($6 > 4$).
      - **Quarantine Cluster 1:**
        $$
        ans \leftarrow ans + c_1 = 0 + 10 = \mathbf{10}
        $$
        - In-place mutation: Cells $(0, 1)$ and $(1, 1)$ are set to **`-1`** (permanently sealed).
    - **Viral Spread Phase:**
      - Unquarantined Cluster 2 infects its boundary cells:
        $$
        (0, 6), (1, 6), (2, 6), (3, 7) \leftarrow \mathbf{1}
        $$
  - **Day 2: Outbreak Assessment:**
    - Scan grid:
      - Cluster 1 is $-1 \implies$ inert, ignored.
      - Cluster 2 now spans column 6, 7.
      - If no further uninfected cells remain or can be saved, the loop terminates.
  - **Final Output:**
    $$
    ans = \mathbf{10}
    $$
- **Single Outbreak Trace ($isInfected = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]$):**
  - All 1s form a single component enclosing $(1, 0)$ or surrounding an inner area.
  - Only 1 component exists $\implies$ quarantines it directly.
  - Returns total perimeter walls required.
- **No Active Infections ($isInfected$ is all 0s):**
  - Areas list is empty $\implies$ halts immediately, returns **`0`**.

This instance demonstrates greedy heuristic epidemic containment simulation and connected component boundary analysis, mathematically proves why max-threat boundary selection optimizes healthy cell preservation under single-intervention constraints, and derives $O(R \cdot M \cdot N)$ runtime and $O(M \cdot N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ grid with infected cells (1) and uninfected cells (0):
Each day:
1. Find all connected components of virus.
2. Quarantine the component that threatens the **most uninfected cells**.
3. Add its perimeter walls to the answer and neutralize it (-1).
4. All other components infect their adjacent uninfected cells.
Repeat until no active virus threatens any cells. Return **total walls installed**.

```text
isInfected:
  0 1 0 0 0 0 0 1
  0 1 0 0 0 0 0 1
  0 0 0 0 0 0 0 1
  0 0 0 0 0 0 0 0

Outbreak 1 (left):  threatens 6 cells, requires 10 walls
Outbreak 2 (right): threatens 4 cells, requires 4 walls

Quarantine Outbreak 1 (build 10 walls)!
Outbreak 2 spreads.
Total walls built = 10.
Result: 10
```

### The Invariant of Threat Set vs Perimeter Walls
- **Threat Set ($boundaries$):** Set of *unique* healthy cells adjacent to the component. Size determines **priority**.
- **Perimeter Walls ($c$):** Number of shared grid edges between the component and healthy cells. Value determines **cost**.

---

## 2. Conceptual Foundation & Invariants

### 1. DFS Threat & Wall Extraction:
For each cell $(i, j)$ in component:
$$
\forall (x, y) \in \text{Adj}_4(i, j): \quad \text{if } isInfected[x][y] == 0 \implies boundaries.\text{add}((x, y)), \quad c \leftarrow c + 1
$$

### 2. Greedy Quarantine Choice:
$$
idx = \arg\max_k |boundaries_k|
$$
$$
ans \leftarrow ans + c[idx]
$$
$$
\forall (i, j) \in area_{idx}: \quad isInfected[i][j] \leftarrow -1
$$

> **Greedy Epidemic Mitigation Invariant.** At each discrete round $t$, selecting the component with maximal boundary measure $\mu(\partial \Omega_k) = |\partial \Omega_k \cap \{0\}|$ maximizes the immediate survival probability of the healthy complement set $H_t$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Day 1 Clusters
- Cluster 1 (left): $|boundaries| = 6, c = 10$.
- Cluster 2 (right): $|boundaries| = 4, c = 4$.

---

### Step 2: Day 1 Action
- $6 > 4 \implies$ Quarantine Cluster 1.
- Build $c = 10$ walls.
- Mark Cluster 1 as $-1$.
- Cluster 2 expands into its boundary.

---

### Step 3: Output
$$
ans = \mathbf{10}
$$

---

## 4. Complete Execution Trace

| Round $t$ | Component ID | Threatened Cells Set Size | Wall Edges Count $c$ | Selected for Quarantine? | Walls Added |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | Left Cluster | **$6$** | **$10$** | **Yes (Max Threat)** | **$+10$** |
| $1$ | Right Cluster| $4$ | $4$ | No (Spreads) | $0$ |
| **Total** | — | — | — | — | **`10`** |

---

## 5. Boundary Cases & Failure Modes

- **No Infections Initially:** $areas = [] \implies$ halts immediately, returns 0.
- **Tied Threat Sizes:** If two components threaten the same number of cells, picking any valid maximum works.
- **Virus Completely Surrounds Healthy Cells:** Corners and interior cells require walls on all bordering edges.
- **Entire Grid Infected:** No healthy cells remain $\implies$ halts.

---

## 6. Traps & Common Anti-Patterns

- **Confusing Walls Count with Threatened Cells Count:** A single healthy cell bordering 3 infected cells in the same cluster requires **3 walls**, but counts as only **1 threatened cell** in the set. Mixing these up causes wrong quarantine priorities and incorrect wall totals.
- **Simultaneous Spread Race Conditions:** When spreading active clusters, do not modify the grid while iterating through other clusters' boundary checks. Collect all new infections and apply them after quarantine.
- **Re-visiting Quarantined Cells:** Once a cluster is quarantined, mark its cells as $-1$ so future rounds ignore it completely.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In each round, DFS visits all grid cells: $\mathcal{O}(M \cdot N)$.
  - The virus spreads or is quarantined in each round, running at most $\min(M, N)$ rounds before full containment.
  - Total Time: $\mathcal{O}(R \cdot M \cdot N)$ where $M, N \le 50, R \le 25 \implies \le 6 \times 10^4$ operations. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ space for visited arrays, boundary sets, and recursion call stack.
