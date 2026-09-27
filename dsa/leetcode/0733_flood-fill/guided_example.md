# Guided Example: Flood Fill

We trace the step-by-step 4-directional connected component traversal, initial color preservation ($oc = image[sr][sc]$), identical target color short-circuit guard ($oc == color \implies \text{halt}$), depth-first search recursive expansion, in-place pixel repainting ($image[i][j] \leftarrow color$), barrier isolation (disconnected islands unchanged), and grid mutation on representative 2D raster images:

- **Input:**
  $$
  image = \begin{bmatrix}
  1 & 1 & 1 \\
  1 & 1 & 0 \\
  1 & 0 & 1
  \end{bmatrix}, \quad sr = 1, \quad sc = 1, \quad color = 2
  $$
- **Required output:**
  $$
  \begin{bmatrix}
  2 & 2 & 2 \\
  2 & 2 & 0 \\
  2 & 0 & 1
  \end{bmatrix}
  $$
  - Flood fill specifications:
    - Starting pixel: $(sr, sc) = (1, 1)$ with initial color $oc = image[1][1] = 1$.
    - Replace the color of the starting pixel and all pixels connected to it 4-directionally (up, down, left, right) that share the **exact same original color** $oc$.
    - Pixels with a different color (such as `0`) act as impenetrable barriers.
    - Pixels that share the original color but are isolated behind barriers (such as bottom-right pixel $(2, 2)$) must **not** be modified.
    - Target replacement color: $color = 2$.
- **Connected Component Invariant & Color Mutation Tracking:**
  - **The Graph Representation:**
    - The grid represents an undirected graph where vertices are pixels $(i, j)$ and edges connect 4-directional adjacent neighbors sharing color $oc$.
    - The goal is to traverse the entire connected component containing seed $(sr, sc)$.
  - **The Identical Color Infinite Loop Guard:**
    - If the new color is identical to the original color ($oc == color$):
      - Performing DFS without an explicit visited set would re-visit the same pixels indefinitely because $image[x][y] == oc$ would always remain true!
      - Check upfront: if $oc == color$, return the original image immediately without any operations.
  - **Implicit Visited Set via In-Place Repainting:**
    - When $oc \ne color$:
      - Setting $image[i][j] \leftarrow color$ immediately transforms the pixel away from $oc$.
      - Subsequent neighbor checks will see $image[i][j] == color \ne oc$, naturally preventing re-traversal!
      - No auxiliary visited array or hash set is needed; the grid itself serves as the visited record.
- **Step-by-Step Worked Execution Trace on the $3 \times 3$ Image:**
  - Dimensions: $m = 3, n = 3$.
  - Original seed color:
    $$
    oc = image[1][1] = \mathbf{1}
    $$
  - New target color:
    $$
    color = \mathbf{2}
    $$
  - Verification: $oc \ne color$ ($1 \ne 2$) $\implies$ proceed with DFS!
  - **Call 1: `dfs(1, 1)`:**
    - Paint current pixel:
      $$
      image[1][1] \leftarrow \mathbf{2}
      $$
    - Check 4 neighbors of $(1, 1)$:
      1. Up $(0, 1)$: inside grid and $image[0][1] == 1 == oc \implies$ recurse `dfs(0, 1)`.
  - **Call 2: `dfs(0, 1)`:**
    - Paint pixel: $image[0][1] \leftarrow \mathbf{2}$.
    - Check neighbors:
      - Left $(0, 0)$: $image[0][0] == 1 \implies$ recurse `dfs(0, 0)`.
  - **Call 3: `dfs(0, 0)`:**
    - Paint pixel: $image[0][0] \leftarrow \mathbf{2}$.
    - Check neighbors:
      - Down $(1, 0)$: $image[1][0] == 1 \implies$ recurse `dfs(1, 0)`.
  - **Call 4: `dfs(1, 0)`:**
    - Paint pixel: $image[1][0] \leftarrow \mathbf{2}$.
    - Check neighbors:
      - Down $(2, 0)$: $image[2][0] == 1 \implies$ recurse `dfs(2, 0)`.
  - **Call 5: `dfs(2, 0)`:**
    - Paint pixel: $image[2][0] \leftarrow \mathbf{2}$.
    - Check neighbors:
      - Right $(2, 1)$: $image[2][1] = 0 \ne oc \implies$ Barrier! Stop.
      - Other neighbors out of bounds or already painted. Backtrack to `dfs(1, 0)`.
  - Backtrack up to `dfs(0, 1)`:
    - Check Right $(0, 2)$: $image[0][2] == 1 \implies$ recurse `dfs(0, 2)`.
  - **Call 6: `dfs(0, 2)`:**
    - Paint pixel: $image[0][2] \leftarrow \mathbf{2}$.
    - Check neighbors:
      - Down $(1, 2)$: $image[1][2] = 0 \ne oc \implies$ Barrier! Stop.
  - **All Accessible Paths Exhausted:**
    - Backtrack unwinds to root call `dfs(1, 1)`.
    - Check remaining neighbors of $(1, 1)$:
      - Right $(1, 2)$: $0 \ne oc$.
      - Down $(2, 1)$: $0 \ne oc$.
    - Entire component painted.
  - **Inspect Untouched Pixels:**
    - Pixel $(1, 2) = 0$ (Barrier, unchanged).
    - Pixel $(2, 1) = 0$ (Barrier, unchanged).
    - Pixel $(2, 2) = 1$:
      - Neighbors of $(2, 2)$ are $(1, 2) = 0$ and $(2, 1) = 0$.
      - Completely walled off from the component by 0s!
      - Remains strictly **1**.
  - **Output Grid:**
    $$
    ans = \begin{bmatrix}
    \mathbf{2} & \mathbf{2} & \mathbf{2} \\
    \mathbf{2} & \mathbf{2} & 0 \\
    \mathbf{2} & 0 & \mathbf{1}
    \end{bmatrix}
    $$
- **Target Color Matches Original Color ($image = [[0, 0], [0, 0]], color = 0$):**
  - $oc = 0 == color = 0$.
  - Returns original grid immediately, avoiding infinite recursion.
- **Single Pixel Grid ($image = [[5]], sr = 0, sc = 0, color = 8$):**
  - $oc = 5 \ne 8$.
  - Paints single cell to 8, returns `[[8]]`.

This instance demonstrates connected component graph flood filling and implicit in-place state marking, mathematically proves why color-shift mutation guarantees acyclic traversal over finite planar lattices, and derives $O(M \cdot N)$ runtime and $O(M \cdot N)$ recursion depth bounds.

---

## 1. Instance & Teaching Goal

Given a 2D image, starting pixel $(sr, sc)$, and a new `color`:
Perform a **flood fill**: change the color of the starting pixel and all 4-directionally connected pixels of the same original color to `color`.
Disconnected pixels remain unchanged.

```text
image:
  1 1 1
  1 1 0
  1 0 1  <- Note (2, 2) is disconnected from (1, 1) by zeros!

Start at (1, 1) with original color 1.
Repaint connected component with color 2:
  2 2 2
  2 2 0
  2 0 1  <- (2, 2) remains 1!

Result: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
```

### The Invariant of the Implicit Visited State
- Checking `if oc != color` before starting guarantees that painting `image[i][j] = color` acts as an automatic visited mark.
- When $image[i][j] \leftarrow color$, subsequent checks see $image[x][y] \ne oc$ and will not re-traverse it.

---

## 2. Conceptual Foundation & Invariants

### 1. Guard Condition:
$$
oc = image[sr][sc]
$$
$$
\text{if } oc == color \implies \text{return } image
$$

### 2. DFS Component Expansion:
For pixel $(i, j)$:
$$
image[i][j] \leftarrow color
$$
$$
\forall (x, y) \in \text{Adj}_4(i, j): \quad \text{if } (x, y) \in \text{bounds} \land image[x][y] == oc \implies \text{dfs}(x, y)
$$

> **Connected Component Invariance.** The connected component $C(v)$ of the vertex $v = (sr, sc)$ in the planar subgraph induced by the fiber $f^{-1}(oc)$ is uniquely traversed in finite steps by DFS, with state mutation $f(u) \leftarrow color$ guaranteeing termination without auxiliary memory.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Initialize
- $oc = image[1][1] = 1, color = 2$.
- $1 \ne 2 \implies$ Proceed.

---

### Step 2: Flood DFS
- Paint $(1, 1) \to 2$.
- Paint $(0, 1) \to 2$.
- Paint $(0, 0) \to 2$.
- Paint $(1, 0) \to 2$.
- Paint $(2, 0) \to 2$.
- Paint $(0, 2) \to 2$.

---

### Step 3: Barriers & Disconnected Cells
- Cells $(1, 2)$ and $(2, 1)$ are 0 $\implies$ barrier.
- Cell $(2, 2)$ is 1, but unreachable $\implies$ remains 1.

---

### Step 4: Output
$$
\begin{bmatrix}
2 & 2 & 2 \\
2 & 2 & 0 \\
2 & 0 & 1
\end{bmatrix}
$$

---

## 4. Complete Execution Trace

| DFS Step | Pixel Visited $(i, j)$ | Previous Color | Action Taken | Neighbors Checked | Valid Paths Found |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $(1, 1)$ | $1$ | Paint to $2$ | Up, Down, Left, Right | Up $(0, 1)$ |
| $2$ | $(0, 1)$ | $1$ | Paint to $2$ | Left, Right | Left $(0, 0)$, Right $(0, 2)$ |
| $3$ | $(0, 0)$ | $1$ | Paint to $2$ | Down | Down $(1, 0)$ |
| $4$ | $(1, 0)$ | $1$ | Paint to $2$ | Down | Down $(2, 0)$ |
| $5$ | $(2, 0)$ | $1$ | Paint to $2$ | Right $(2, 1) = 0$ | Dead end (Barrier) |
| $6$ | $(0, 2)$ | $1$ | Paint to $2$ | Down $(1, 2) = 0$ | Dead end (Barrier) |
| **End** | **$(2, 2)$** | **$1$** | **Untouched** | **Isolated by 0s** | **Preserved as 1** |

---

## 5. Boundary Cases & Failure Modes

- **New Color Equals Old Color ($oc == color$):** Caught by the guard `if oc != color`; returns immediately without running DFS.
- **Entire Grid One Color ($3 \times 3$ of 1s):** Repaints all 9 pixels to `color`.
- **Single Pixel Grid ($1 \times 1$):** Repaints single cell safely.
- **No Neighbors of Same Color:** Only the starting pixel $(sr, sc)$ is repainted.

---

## 6. Traps & Common Anti-Patterns

- **Missing $oc == color$ Guard (RecursionError):** If $image[sr][sc] == color$, DFS attempts to paint cells to their existing color, looping between neighbors until maximum recursion depth is exceeded.
- **Diagonal Traversal:** Flood fill strictly specifies **4-directional** connectivity (horizontal and vertical only). Do not traverse diagonally.
- **Boundary Index Errors:** Always check $0 \le x < m$ and $0 \le y < n$ before indexing into $image[x][y]$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Visits each pixel in the connected component at most once.
  - In each visit, inspects at most 4 cardinal directions: $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(M \cdot N)$ where $M, N \le 50$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ in the worst case for the call stack during deep recursion (e.g. a snake-like component), or $\mathcal{O}(1)$ beyond recursion memory.
