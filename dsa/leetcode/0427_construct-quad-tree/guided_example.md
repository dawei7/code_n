# Guided Example: Construct Quad Tree

We trace the step-by-step recursive 2D spatial partitioning, quadrant uniformity verification, 4-way divide-and-conquer tree construction, and leaf-collapsing bottom-up synthesis on representative binary grid matrices:

- **Input:**
  $$
  grid = \begin{bmatrix}
  0 & 1 \\
  1 & 0
  \end{bmatrix}
  $$
- **Required output:** Non-leaf root node with four $1 \times 1$ leaf children:
  - `topLeft`: Leaf node with value `0`
  - `topRight`: Leaf node with value `1`
  - `bottomLeft`: Leaf node with value `1`
  - `bottomRight`: Leaf node with value `0`
- **Execution trace:**
  - Entire grid $[(0, 0) \dots (1, 1)]$:
    - Elements present: $\{0, 1\}$.
    - Since both $0$ and $1$ exist, the region is **heterogeneous** $\implies isLeaf = \text{False}$.
  - Divide into 4 quadrants around midpoints $r_{mid} = 0, c_{mid} = 0$:
    - **Top-Left $[(0, 0) \dots (0, 0)]:$** Single cell $grid[0][0] = 0 \implies$ Leaf node (`val = 0, isLeaf = True`)
    - **Top-Right $[(0, 1) \dots (0, 1)]:$** Single cell $grid[0][1] = 1 \implies$ Leaf node (`val = 1, isLeaf = True`)
    - **Bottom-Left $[(1, 0) \dots (1, 0)]:$** Single cell $grid[1][0] = 1 \implies$ Leaf node (`val = 1, isLeaf = True`)
    - **Bottom-Right $[(1, 1) \dots (1, 1)]:$** Single cell $grid[1][1] = 0 \implies$ Leaf node (`val = 0, isLeaf = True`)
  - Bottom-up synthesis:
    - Children values differ ($0, 1, 1, 0$) $\implies$ Cannot collapse into a single leaf.
    - Assemble internal node with $isLeaf = \text{False}$ pointing to the 4 children.
- **Homogeneous Grid Instance:** $grid = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \implies$ all values equal $\implies$ single leaf node (`val = 1, isLeaf = True`) without children.

This instance demonstrates recursive quad-tree spatial decomposition, mathematically proves the quadrant homogeneity condition that allows compression from $O(N^2)$ cells to minimal tree nodes, and derives $O(N^2 \log N)$ runtime and $O(\log N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ binary matrix $grid$ (where $n = 2^k$):
Construct a **Quad-Tree** to represent the grid.
A Quad-Tree is a tree data structure in which each internal node has exactly four children:
`topLeft`, `topRight`, `bottomLeft`, and `bottomRight`.

```text
Input Grid:
  +---+---+
  | 0 | 1 |
  +---+---+
  | 1 | 0 |
  +---+---+

Quad-Tree Structure:
         [ Internal Node (isLeaf=False) ]
         /        |             |        \
        /         |             |         \
 [Top-Left]  [Top-Right]  [Bottom-Left]  [Bottom-Right]
  (Leaf: 0)   (Leaf: 1)     (Leaf: 1)      (Leaf: 0)
```

### The Quad-Tree Invariant
1. **Homogeneous Region:** If all cells in the current sub-grid have the same value $v \in \{0, 1\}$, the node is a **leaf** (`isLeaf = True, val = v`) and has **no children** (`None`).
2. **Heterogeneous Region:** If the current sub-grid contains both $0$ and $1$, the node is an **internal node** (`isLeaf = False`), and is recursively partitioned into 4 equal-sized sub-grids of size $\frac{n}{2} \times \frac{n}{2}$.

---

## 2. Conceptual Foundation & Invariants

### 1. Spatial Quadrant Coordinates:
Given sub-grid boundaries $[r_1, c_1]$ (top-left) to $[r_2, c_2]$ (bottom-right):
Compute midpoints:
$$
r_{mid} = \lfloor (r_1 + r_2) / 2 \rfloor, \quad c_{mid} = \lfloor (c_1 + c_2) / 2 \rfloor
$$
The four sub-quadrants are:
1. **Top-Left ($TL$):** $[r_1, c_1]$ to $[r_{mid}, c_{mid}]$
2. **Top-Right ($TR$):** $[r_1, c_{mid} + 1]$ to $[r_{mid}, c_2]$
3. **Bottom-Left ($BL$):** $[r_{mid} + 1, c_1]$ to $[r_2, c_{mid}]$
4. **Bottom-Right ($BR$):** $[r_{mid} + 1, c_{mid} + 1]$ to $[r_2, c_2]$

### 2. Bottom-Up Collapsing Rule:
Alternatively, one can recursively construct the 4 quadrant subtrees first.
If all 4 children are leaves AND share the exact same value:
$$
TL.isLeaf \land TR.isLeaf \land BL.isLeaf \land BR.isLeaf \land (TL.val == TR.val == BL.val == BR.val)
$$
Then all four quadrants are identical: collapse them into a single leaf node (`val = TL.val, isLeaf = True`), discarding the four child subtrees.

> **Invariant.** A node is marked as a leaf if and only if every single grid cell within its spatial bounding box has the identical binary value.

---

## 3. Step-by-Step Worked Execution

We trace the $2 \times 2$ grid:
$$
r_1 = 0, c_1 = 0, \quad r_2 = 1, c_2 = 1
$$

---

### Step 1: Uniformity Scan on Root Region $[(0, 0) \dots (1, 1)]$
Scan all cells in the $2 \times 2$ window:
- $(0, 0) = 0$
- $(0, 1) = 1$
- $(1, 0) = 1$
- $(1, 1) = 0$
Both $0$ and $1$ are detected. The region is **not uniform**.
Compute midpoints:
$$
r_{mid} = \lfloor (0 + 1) / 2 \rfloor = 0, \quad c_{mid} = \lfloor (0 + 1) / 2 \rfloor = 0
$$

---

### Step 2: Recursively Build 4 Sub-Quadrants

#### 1. Top-Left Quadrant $[(0, 0) \dots (0, 0)]$:
- Area: $1 \times 1$.
- Only value is $grid[0][0] = 0$.
- Uniform $\implies$ Leaf Node:
  $$
  TL = \text{Node}(val = 0, isLeaf = \text{True})
  $$

#### 2. Top-Right Quadrant $[(0, 1) \dots (0, 1)]$:
- Area: $1 \times 1$.
- Only value is $grid[0][1] = 1$.
- Uniform $\implies$ Leaf Node:
  $$
  TR = \text{Node}(val = 1, isLeaf = \text{True})
  $$

#### 3. Bottom-Left Quadrant $[(1, 0) \dots (1, 0)]$:
- Area: $1 \times 1$.
- Only value is $grid[1][0] = 1$.
- Uniform $\implies$ Leaf Node:
  $$
  BL = \text{Node}(val = 1, isLeaf = \text{True})
  $$

#### 4. Bottom-Right Quadrant $[(1, 1) \dots (1, 1)]$:
- Area: $1 \times 1$.
- Only value is $grid[1][1] = 0$.
- Uniform $\implies$ Leaf Node:
  $$
  BR = \text{Node}(val = 0, isLeaf = \text{True})
  $$

---

### Step 3: Root Node Assembly
- Check collapse condition:
  - $TL.val = 0, TR.val = 1 \implies$ Values are not identical.
  - Cannot collapse.
- Construct Root Internal Node:
  $$
  \text{Root} = \text{Node}(val = 1, isLeaf = \text{False}, topLeft = TL, topRight = TR, bottomLeft = BL, bottomRight = BR)
  $$

---

## 4. Complete Execution Trace

| Node Scope | Rows $[r_1, r_2]$ | Cols $[c_1, c_2]$ | Size | Values in Region | Uniform? | Constructed Node Type | Children Pointers |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$TL$** | $[0, 0]$ | $[0, 0]$ | $1 \times 1$ | $\{0\}$ | **Yes** | Leaf ($val = 0$) | `None` |
| **$TR$** | $[0, 0]$ | $[1, 1]$ | $1 \times 1$ | $\{1\}$ | **Yes** | Leaf ($val = 1$) | `None` |
| **$BL$** | $[1, 1]$ | $[0, 0]$ | $1 \times 1$ | $\{1\}$ | **Yes** | Leaf ($val = 1$) | `None` |
| **$BR$** | $[1, 1]$ | $[1, 1]$ | $1 \times 1$ | $\{0\}$ | **Yes** | Leaf ($val = 0$) | `None` |
| **Root** | $[0, 1]$ | $[0, 1]$ | $2 \times 2$ | $\{0, 1\}$ | **No** | Internal ($isLeaf = \text{False}$) | $[TL, TR, BL, BR]$ |

---

## 5. Boundary Cases & Failure Modes

- **$1 \times 1$ Grid ($grid = [[1]]$):** Base case triggers immediately $\implies$ single leaf node (`val = 1, isLeaf = True`).
- **All Identical Large Grid ($4 \times 4$ of all $0$s):** Scans region, detects only $0$s $\implies$ returns a single leaf node (`val = 0, isLeaf = True`) without subdividing or allocating child nodes.
- **Checkerboard Grid ($4 \times 4$ alternating $0$ and $1$):** Subdivides fully down to $1 \times 1$ leaves, resulting in a full 3-level tree of depth $\log_2(4) = 2$.

---

## 6. Traps & Common Anti-Patterns

- **Missing Bottom-Up Collapse:** Failing to check if all 4 children are identical leaves results in excessive internal nodes where a single leaf node should represent the entire uniform block.
- **Midpoint Coordinate Calculation Off-By-One:** When dividing $[b, d]$, the right half starts at $c_{mid} + 1 = \lfloor (b+d)/2 \rfloor + 1$. Forgetting the $+1$ creates overlapping infinite recursion.
- **Allocating Children on Leaf Nodes:** A leaf node must have `topLeft = topRight = bottomLeft = bottomRight = None`. Setting children on a leaf violates the Quad-Tree specification.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the side length of the grid. Total cells = $N^2$.
  - At depth $k$, there are $4^k$ sub-grids of size $(N / 2^k) \times (N / 2^k)$.
  - In the worst case (full checkerboard), checking uniformity takes $O(N^2)$ per level across $\log_2 N$ levels.
  - Total Time: $\mathcal{O}(N^2 \log N)$ (or $\mathcal{O}(N^2)$ with 2D prefix sums or bottom-up merge). For $N \le 64$, $64^2 \log_2(64) \approx 2.4 \times 10^4$ operations, completing in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\log N)$ recursion call stack depth.
  - The returned tree contains at most $O(N^2)$ nodes.