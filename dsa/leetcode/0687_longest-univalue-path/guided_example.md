# Guided Example: Longest Univalue Path

We trace the step-by-step bottom-up post-order tree dynamic programming, downward single-arm extension measurement ($l, r$), univalue edge qualification ($child.val == u.val$), apex two-arm path aggregation ($ans = \max(ans, l + r)$), single-branch upward return propagation ($\max(l, r)$), and edge-count path length maximization on representative binary trees:

- **Input:**
  - Tree: $root = [5, 4, 5, 1, 1, \text{null}, 5]$
  - Tree topology:
    ```text
            5
          /   \
         4     5
        / \     \
       1   1     5
    ```
- **Required output:** `2`
  - Univalue path criteria:
    - Every node along the path must have the **exact same value**.
    - The path does not need to pass through the root.
    - Path length is measured in the **number of edges** (not nodes).
    - For $[5, 4, 5, 1, 1, \text{null}, 5]$:
      - Path: $\text{Root } 5 \to \text{Right } 5 \to \text{Leaf } 5$ contains 3 nodes with value 5, connected by **2 edges**.
      - Maximum univalue edge count is **2**.
- **Post-Order Tree DP & Apex Extension Invariant:**
  - **Single-Arm Downward Extension:**
    - Let $dfs(u)$ return the length of the longest univalue path extending strictly downward from node $u$ into one of its subtrees.
    - Compute values recursively for children:
      $$
      L = dfs(u.left), \quad R = dfs(u.right)
      $$
    - If left child exists and has matching value ($u.left.val == u.val$):
      $$
      l = L + 1
      $$
      Otherwise, $l = 0$ (the univalue chain is broken).
    - If right child exists and has matching value ($u.right.val == u.val$):
      $$
      r = R + 1
      $$
      Otherwise, $r = 0$.
  - **Apex Path Concatenation:**
    - If node $u$ serves as the highest node (the apex/turnaround) of a univalue path, it can bridge both its qualifying left arm and right arm:
      $$
      \text{Path length through } u = l + r
      $$
    - Update global maximum:
      $$
      ans \leftarrow \max(ans, \; l + r)
      $$
  - **Upward Return Contract:**
    - When reporting back to $u$'s parent, the parent can only extend down **one single branch** through $u$ (a path cannot fork into two branches at an ancestor):
      $$
      dfs(u) = \max(l, \; r)
      $$
- **Step-by-Step Worked Execution Trace on $[5, 4, 5, 1, 1, \text{null}, 5]$:**
  - Global maximum tracker: $ans = 0$.
  - **Step 1: Leaves under Node 4 (Nodes $1_L$ and $1_R$):**
    - Both leaves have no children $\implies dfs(1) = 0$.
  - **Step 2: Node 4 ($val = 4$):**
    - Left child is 1 ($1 \ne 4 \implies l = 0$).
    - Right child is 1 ($1 \ne 4 \implies r = 0$).
    - Apex path: $l + r = 0 + 0 = 0$.
    - Return to parent: $\max(0, 0) = \mathbf{0}$.
  - **Step 3: Leaf Node $5_{RR}$ (Right child of Node $5_R$):**
    - Node has no children.
    - $l = 0, \; r = 0$.
    - Apex path: $0$.
    - Return to parent: $\max(0, 0) = \mathbf{0}$.
  - **Step 4: Intermediate Node $5_R$ (Right child of Root 5):**
    - Left child is null $\implies l = 0$.
    - Right child is Leaf $5_{RR}$:
      - Values match:
        $$
        5_{RR}.val == 5_R.val == 5 \implies r = R + 1 = 0 + 1 = \mathbf{1}
        $$
    - Apex path through Node $5_R$:
      $$
      l + r = 0 + 1 = \mathbf{1}
      $$
      $$
      ans \leftarrow \max(0, 1) = \mathbf{1}
      $$
    - Upward return to Root 5:
      $$
      dfs(5_R) = \max(l, r) = \max(0, 1) = \mathbf{1}
      $$
  - **Step 5: Root Node 5:**
    - Left child is Node 4:
      - Compare values: $4 \ne 5 \implies$ Mismatch!
      - Left univalue arm:
        $$
        l = \mathbf{0}
        $$
    - Right child is Node $5_R$:
      - Compare values: $5_R.val == 5 \implies \mathbf{Match!}$
      - Right univalue arm extends the arm from $5_R$:
        $$
        r = dfs(5_R) + 1 = 1 + 1 = \mathbf{2}
        $$
    - Apex path through Root 5:
      $$
      l + r = 0 + 2 = \mathbf{2}
      $$
      $$
      ans \leftarrow \max(1, 2) = \mathbf{2}
      $$
    - Upward return: $\max(0, 2) = 2$.
  - **Step 6: Traversal Complete:**
    - Longest univalue path length:
      $$
      ans = \mathbf{2}
      $$
- **Two-Arm Turnaround Path Trace ($root = [1, 4, 5, 4, 4, \text{null}, 5]$):**
  - Node 4 has left child 4 and right child 4.
  - Left child 4 returns 0 $\implies l = 0 + 1 = 1$.
  - Right child 4 returns 0 $\implies r = 0 + 1 = 1$.
  - Apex path through Node 4 connects both arms:
    $$
    l + r = 1 + 1 = \mathbf{2}
    $$
    (Path: Left 4 $\leftrightarrow$ Parent 4 $\leftrightarrow$ Right 4).
  - Max edges: **`2`**.
- **No Identical Adjacent Nodes ($root = [1, 2, 3]$):**
  - All values differ $\implies l = 0, r = 0$ everywhere.
  - Max edges: **`0`**.

This instance demonstrates tree diameter dynamic programming over monochromatic connected components, mathematically proves why single-arm return propagation preserves simple path linearity across tree ancestors, and derives $O(N)$ execution time and $O(H)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a binary tree:
Find the length (number of edges) of the **longest path where all nodes have the same value**.
The path does not have to go through the root.

```text
Tree:
        5
      /   \
     4     5  <-- MATCH! (edge 1)
    / \     \
   1   1     5  <-- MATCH! (edge 2)

Univalue path: 5 -> 5 -> 5
Number of edges = 2
Result: 2
```

### The Invariant of Single-Arm Return vs Two-Arm Apex
- At each node $u$:
  - A path can **turn around** at $u$, using both left and right matching branches: length $= l + r$.
  - But when reporting upward to $u$'s parent, only **one single branch** can be extended: $\max(l, r)$.

---

## 2. Conceptual Foundation & Invariants

### 1. Child Matching Arm Computation:
$$
l = \begin{cases} dfs(u.left) + 1 & \text{if } u.left \land u.left.val == u.val \\ 0 & \text{otherwise} \end{cases}
$$
$$
r = \begin{cases} dfs(u.right) + 1 & \text{if } u.right \land u.right.val == u.val \\ 0 & \text{otherwise} \end{cases}
$$

### 2. Global Apex Update and Return:
$$
ans \leftarrow \max(ans, \; l + r)
$$
$$
\text{return } \max(l, \; r)
$$

> **Monochromatic Geodesic Bipartition Invariant.** In any tree, a simple path monochromatic with respect to vertex coloration admits a unique top-most ancestor (the apex), decomposing the path into at most two directed monochromatic geodesics descending from that apex.

---

## 3. Step-by-Step Worked Execution

We trace $root = [5, 4, 5, 1, 1, \text{null}, 5]$:

---

### Step 1: Leaf $5_{RR}$
- $dfs(5_{RR}) = 0$.

---

### Step 2: Node $5_R$
- Right child is $5 \implies r = 0 + 1 = 1$.
- Left child null $\implies l = 0$.
- $ans \leftarrow \max(0, 0 + 1) = 1$.
- Returns $\max(0, 1) = 1$.

---

### Step 3: Node 4
- Children are 1 ($1 \ne 4 \implies l = 0, r = 0$).
- Returns 0.

---

### Step 4: Root 5
- Left child is 4 ($4 \ne 5 \implies l = 0$).
- Right child is 5 ($5 == 5 \implies r = 1 + 1 = 2$).
- Apex: $l + r = 0 + 2 = 2$.
- $ans \leftarrow \max(1, 2) = \mathbf{2}$.

---

### Step 5: Output
$$
\mathbf{2}
$$

---

## 4. Complete Execution Trace

| Node Evaluated | Node Value | Left Arm $l$ | Right Arm $r$ | Apex Path ($l + r$) | Global Max $ans$ | Returned to Parent $\max(l, r)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Leaf $1_L$ | $1$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| Leaf $1_R$ | $1$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| Node $4$ | $4$ | $0$ ($1 \ne 4$) | $0$ ($1 \ne 4$) | $0$ | $0$ | $0$ |
| Leaf $5_{RR}$ | $5$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| Node $5_R$ | $5$ | $0$ | $1$ ($5 = 5$) | $1$ | $1$ | $1$ |
| **Root $5$** | **$5$** | **$0$ ($4 \ne 5$)** | **$2$ ($5 = 5$)** | **$2$** | **`2`** | $2$ |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = \text{null}$):** Returns 0.
- **Single Node Tree:** Returns 0 (0 edges).
- **All Nodes Identical:** Max path equals tree diameter (left height + right height).
- **All Nodes Distinct:** Every match fails $\implies$ returns 0.

---

## 6. Traps & Common Anti-Patterns

- **Counting Nodes Instead of Edges:** A path of 3 nodes has 2 edges. Using node count returns 3 instead of 2.
- **Returning Both Branches Upward ($l + r$):** Returning $l + r$ to a parent allows a path to branch in three directions, which is not a legal simple path. Upward propagation must return $\max(l, r)$.
- **Searching Subtrees Separately ($O(N^2)$):** Re-traversing subtrees from each node causes quadratic overhead. A single post-order DFS evaluates every node in strictly $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard post-order DFS visits every node exactly once: $\mathcal{O}(N)$.
  - Each visit performs constant number of comparisons: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 1$ ms for $N = 1000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ auxiliary space for the recursion call stack, where $H$ is the tree height.
