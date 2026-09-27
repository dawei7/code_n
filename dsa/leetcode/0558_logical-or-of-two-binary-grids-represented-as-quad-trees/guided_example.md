# Guided Example: Logical OR of Two Binary Grids Represented as Quad-Trees

We trace the step-by-step recursive 4-quadrant tree alignment ($topLeft, topRight, bottomLeft, bottomRight$), short-circuit boolean annihilation laws ($1 \lor X = 1, \; 0 \lor X = X$), post-order quadrant child merging, and canonical leaf node collapse verification ($isLeaf \land sameVal$) on representative quad-tree grids:

- **Input:**
  - Quad-Tree 1 ($t_1$): Internal root node with 4 quadrants:
    - $t_1.topLeft = \text{Leaf}(1)$
    - $t_1.topRight = \text{Leaf}(1)$
    - $t_1.bottomLeft = \text{Leaf}(0)$
    - $t_1.bottomRight = \text{Leaf}(0)$
  - Quad-Tree 2 ($t_2$): Internal root node with 4 quadrants:
    - $t_2.topLeft = \text{Leaf}(1)$
    - $t_2.topRight = \text{Leaf}(0)$
    - $t_2.bottomLeft = \text{Leaf}(1)$
    - $t_2.bottomRight = \text{Leaf}(0)$
- **Required output:**
  - A consolidated Quad-Tree representing the bitwise OR of the two underlying $2 \times 2$ grids.
  - Matrix projection:
    $$
    G_1 = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}, \quad
    G_2 = \begin{bmatrix} 1 & 0 \\ 1 & 0 \end{bmatrix}
    $$
    $$
    G_1 \lor G_2 = \begin{bmatrix} 1 \lor 1 & 1 \lor 0 \\ 0 \lor 1 & 0 \lor 0 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}
    $$
- **Recursive Quad-Tree Merging Trace:**
  - Let $dfs(t_1, t_2)$ evaluate the logical OR of corresponding spatial subgrids.
  - **Boolean Short-Circuit Identities:**
    1. If $t_1$ is a Leaf with value $1$: Since $1 \lor X = 1$, the entire region becomes all 1s $\implies$ Return $t_1$ immediately (Short-circuit pruning!).
    2. If $t_1$ is a Leaf with value $0$: Since $0 \lor X = X$, the result is identical to $t_2 \implies$ Return $t_2$ directly!
    3. Symmetrically, if $t_2$ is a Leaf with value $1$, return $t_2$; if $t_2$ is a Leaf with value $0$, return $t_1$.
    4. If both are internal nodes, recurse into all 4 quadrants and apply the **Collapse Check**.
  - **Evaluating the 4 Quadrants on $t_1$ and $t_2$:**
    - **Quadrant 1 (Top-Left):**
      - $t_1.topLeft = \text{Leaf}(1), \; t_2.topLeft = \text{Leaf}(1)$.
      - Both are leaves: $1 \lor 1 = \mathbf{1}$.
      - Result:
        $$
        res.topLeft = \mathbf{\text{Leaf}(1)}
        $$
    - **Quadrant 2 (Top-Right):**
      - $t_1.topRight = \text{Leaf}(1), \; t_2.topRight = \text{Leaf}(0)$.
      - $t_1.val == 1 \implies 1 \lor 0 = \mathbf{1}$.
      - Result:
        $$
        res.topRight = \mathbf{\text{Leaf}(1)}
        $$
    - **Quadrant 3 (Bottom-Left):**
      - $t_1.bottomLeft = \text{Leaf}(0), \; t_2.bottomLeft = \text{Leaf}(1)$.
      - $0 \lor 1 = \mathbf{1}$.
      - Result:
        $$
        res.bottomLeft = \mathbf{\text{Leaf}(1)}
        $$
    - **Quadrant 4 (Bottom-Right):**
      - $t_1.bottomRight = \text{Leaf}(0), \; t_2.bottomRight = \text{Leaf}(0)$.
      - Both are leaves: $0 \lor 0 = \mathbf{0}$.
      - Result:
        $$
        res.bottomRight = \mathbf{\text{Leaf}(0)}
        $$
  - **Post-Order Canonical Collapse Check:**
    - Examine all 4 resulting children:
      - Are all 4 children leaves?
        $$
        \text{topLeft}, \text{topRight}, \text{bottomLeft}, \text{bottomRight} \text{ are all leaves } \implies \mathbf{True}
        $$
      - Do all 4 children share the same value?
        $$
        1 == 1 == 1 \ne 0 \implies \mathbf{False}
        $$
    - Because the 4 quadrants are not all identical ($[1, 1, 1, 0]$), the parent **cannot be collapsed** into a single leaf.
    - Return the parent node with `isLeaf = False` and the 4 computed child quadrants.
- **Collapsing Example (When 4 Quadrants Unite):**
  - Suppose $G_1 = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$ and $G_2 = \begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix}$.
  - $G_1 \lor G_2 = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$.
  - All 4 children evaluate to $\text{Leaf}(1)$.
  - Collapse check triggers: $1 == 1 == 1 == 1 \land \text{all leaves} \implies$ collapses to a single $\mathbf{\text{Leaf}(1)}$!
- **Trivial Zero-Leaf Identity ($t_1 = \text{Leaf}(0), t_2 = \text{Leaf}(1)$):**
  - $0 \lor 1 = \mathbf{\text{Leaf}(1)}$ returned in $O(1)$ without creating subtrees.

This instance demonstrates spatial quad-tree algebra and canonical form normalization, mathematically proves why short-circuiting on identity/annihilator leaves achieves optimal branch pruning, and derives $O(N^2)$ worst-case runtime and $O(\log N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two Quad-Trees $t_1$ and $t_2$ representing two $N \times N$ binary grids:
Return the Quad-Tree representing the **bitwise logical OR** of the two grids.

A Quad-Tree node has:
- `val`: 1 or 0.
- `isLeaf`: `True` if all cells in the subgrid have the same value; `False` otherwise.
- `topLeft`, `topRight`, `bottomLeft`, `bottomRight`: Four child Quad-Tree nodes if `isLeaf == False`.

```text
Grid 1 (t1):        Grid 2 (t2):        Result (t1 OR t2):
  [ 1,  1 ]           [ 1,  0 ]           [ 1,  1 ]
  [ 0,  0 ]     OR    [ 1,  0 ]     =     [ 1,  0 ]

Four Quadrants of Result:
  topLeft:     Leaf(1)
  topRight:    Leaf(1)
  bottomLeft:  Leaf(1)
  bottomRight: Leaf(0)
Values differ -> Remains an internal node with 4 leaf children.
```

### The Canonical Reduction Rule
- A Quad-Tree must always be stored in its **simplest canonical representation**.
- If after performing the OR operation, all 4 children of a node:
  1. Are leaf nodes (`isLeaf == True`).
  2. Have the exact same value (`val`).
  they **must be collapsed** into a single leaf node representing the entire region!

---

## 2. Conceptual Foundation & Invariants

### 1. Boolean Algebra Short-Circuits:
- **Annihilator Law for OR ($1 \lor X = 1$):**
  If a node is a leaf with `val == 1`, the entire subgrid becomes all 1s.
  We can return this node immediately without exploring the other tree!
- **Identity Law for OR ($0 \lor X = X$):**
  If a node is a leaf with `val == 0`, $0 \lor X = X$.
  The result is simply the other tree (whether it is a leaf or a deep subtree)!

### 2. The Recurrence:
$$
dfs(t_1, t_2):
$$
1. If $t_1$ is leaf: return $t_1$ if $t_1.val == 1$ else $t_2$.
2. If $t_2$ is leaf: return $t_2$ if $t_2.val == 1$ else $t_1$.
3. Otherwise, recursively compute the 4 quadrants:
   - $TL = dfs(t_1.TL, t_2.TL)$
   - $TR = dfs(t_1.TR, t_2.TR)$
   - $BL = dfs(t_1.BL, t_2.BL)$
   - $BR = dfs(t_1.BR, t_2.BR)$
4. **Collapse Check:**
   If all 4 are leaves AND $TL.val == TR.val == BL.val == BR.val$:
   Return a single leaf with that common value.
   Else, return an internal node with the 4 children.

> **Canonical Form Invariant.** Merging 4 homogeneous leaves into a single parent leaf maintains the minimal tree depth invariant for uniform binary matrices.

---

## 3. Step-by-Step Worked Execution

We trace the $2 \times 2$ grid merge:

---

### Step 1: Root Node Check
Neither $t_1$ nor $t_2$ is a leaf (both have 4 children).
Recurse into the 4 quadrants:

---

### Step 2: Solve 4 Quadrants
1. **Top-Left:**
   - $dfs(t_1.TL, t_2.TL) = dfs(\text{Leaf}(1), \text{Leaf}(1))$.
   - $t_1$ is leaf with value $1 \implies$ returns $\mathbf{\text{Leaf}(1)}$.
2. **Top-Right:**
   - $dfs(t_1.TR, t_2.TR) = dfs(\text{Leaf}(1), \text{Leaf}(0))$.
   - $t_1$ is leaf with value $1 \implies$ returns $\mathbf{\text{Leaf}(1)}$.
3. **Bottom-Left:**
   - $dfs(t_1.BL, t_2.BL) = dfs(\text{Leaf}(0), \text{Leaf}(1))$.
   - $t_2$ is leaf with value $1 \implies$ returns $\mathbf{\text{Leaf}(1)}$.
4. **Bottom-Right:**
   - $dfs(t_1.BR, t_2.BR) = dfs(\text{Leaf}(0), \text{Leaf}(0))$.
   - Both are 0-leaves $\implies$ returns $\mathbf{\text{Leaf}(0)}$.

---

### Step 3: Check Parent Collapse
- Resulting children:
  - $TL = \text{Leaf}(1)$
  - $TR = \text{Leaf}(1)$
  - $BL = \text{Leaf}(1)$
  - $BR = \text{Leaf}(0)$
- Check:
  - Are all 4 leaves? Yes.
  - Are all 4 values equal?
    $$
    1 == 1 == 1 == 0 \implies \mathbf{False}
    $$
- Do not collapse! Return internal node with the 4 computed leaf children.

---

## 4. Complete Execution Trace

| Quadrant | $t_1$ Node | $t_2$ Node | Short-Circuit Law Applied | Sub-Result |
|:---:|:---:|:---:|:---:|:---:|
| **Top-Left** | $\text{Leaf}(1)$ | $\text{Leaf}(1)$ | $1 \lor X = 1$ | $\text{Leaf}(1)$ |
| **Top-Right** | $\text{Leaf}(1)$ | $\text{Leaf}(0)$ | $1 \lor 0 = 1$ | $\text{Leaf}(1)$ |
| **Bottom-Left** | $\text{Leaf}(0)$ | $\text{Leaf}(1)$ | $0 \lor 1 = 1$ | $\text{Leaf}(1)$ |
| **Bottom-Right** | $\text{Leaf}(0)$ | $\text{Leaf}(0)$ | $0 \lor 0 = 0$ | $\text{Leaf}(0)$ |
| **Root Check** | Internal | Internal | Values $\{1, 1, 1, 0\}$ differ | **Internal node with 4 children** |

---

## 5. Boundary Cases & Failure Modes

- **One Tree is All 1s ($t_1 = \text{Leaf}(1)$):** Short-circuits immediately at the root, returning $\text{Leaf}(1)$ in $O(1)$ time regardless of how deep $t_2$ is!
- **One Tree is All 0s ($t_1 = \text{Leaf}(0)$):** $0 \lor X = X \implies$ returns $t_2$ directly in $O(1)$ time.
- **Both Trees Require Collapsing:** If 4 quadrants all yield $\text{Leaf}(1)$, returning `res.topLeft` collapses the node into a single $\text{Leaf}(1)$.
- **Deeply Nested Asymmetric Trees:** Recursion traverses only down to the depth of the shallower tree whenever a leaf is encountered.

---

## 6. Traps & Common Anti-Patterns

- **Unconditionally Creating Subtrees When a Leaf is 1:** If $t_1$ is a leaf of 1, recursing into all 4 children of $t_2$ creates redundant identical 1-leaves that must subsequently be collapsed. Returning $t_1$ directly avoids creating and destroying thousands of nodes.
- **Forgetting the Collapse Check:** Leaving 4 identical leaf children under an internal parent violates the canonical Quad-Tree specification and fails automated tree equality judges.
- **Checking `sameVal` When Children Are Not Leaves:** If children have `isLeaf == False`, their `.val` attribute is arbitrary and meaningless. The collapse condition must verify that all 4 children are leaves **before** checking value equality.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In the worst case, both trees are fully divided to depth $\log_2 N$.
  - The recursion visits each quad-tree node at most once.
  - Number of nodes in a complete quad-tree is $O(N^2)$.
  - Total Time: $\mathcal{O}(N^2)$ worst-case, but frequently $\mathcal{O}(1)$ to $\mathcal{O}(K)$ due to short-circuit pruning on 1-leaves and 0-leaves.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\log N)$ call stack space proportional to the maximum tree depth.