# Guided Example: All Nodes Distance K in Binary Tree

We trace the step-by-step parent pointer annotation, bidirectional graph conversion, multi-directional outward radial breadth/depth traversal, and distance-horizon node extraction on representative binary trees:

- **Input:**
  $$
  root = [3, 5, 1, 6, 2, 0, 8, \text{null}, \text{null}, 7, 4], \quad target = 5, \quad k = 2
  $$
- **Required output:** `[7, 4, 1]`
  - Binary tree structural layout:
    - Root $3$:
      - Left child $5$:
        - Left child $6$.
        - Right child $2$ (with children $7$ and $4$).
      - Right child $1$:
        - Left child $0$.
        - Right child $8$.
    - Target node is $5$, and distance threshold is $k = 2$.
    - Distance breakdown from target $5$:
      - Distance $0$: $\{5\}$.
      - Distance $1$:
        - Left child of $5$: $6$.
        - Right child of $5$: $2$.
        - Parent of $5$: $3$.
      - Distance $2$:
        - From $6$: no unvisited neighbors.
        - From $2$: unvisited children are $7$ and $4$.
        - From $3$: unvisited right child is $1$.
      - Nodes at distance $2$: $\{7, 4, 1\}$.
      - Output: **`[7, 4, 1]`** (in any order).
- **The Graphification & Radial Expansion Invariant:**
  - **The Missing Pointer Bottleneck:**
    - Standard binary tree nodes only possess downward pointers (`left` and `right`).
    - From target $5$, descendants (downward) can be reached trivially.
    - However, nodes reachable via ancestors (upward to $3$ and across to sibling subtree $1$) require upward traversal.
  - **Parent Link Construction:**
    - Perform a first pass (preorder traversal) establishing a parent link $g[u] = fa$ for every node $u$.
    - This effectively converts the directed tree into an **undirected unweighted graph** where every non-root node has degree at most $3$ (left child, right child, parent).
  - **Radial Search from Target:**
    - Starting at $target$, perform a radial depth-first search or breadth-first search.
    - For any current node $u$, explore all adjacent neighbors:
      $$
      nxt \in \{u.left, u.right, g[u]\}
      $$
    - Guard against immediate cycles by ensuring $nxt \ne fa$ (or maintaining a visited set).
    - Decrement distance counter $k \to k - 1$. When $k = 0$, record the node value!

---

## 1. Instance & Teaching Goal

Given the tree rooted at $3$, find all nodes at distance $k = 2$ from node $5$.

```text
               3
             /   \
           [5]     1
          /   \   / \
         6     2 0   8
              / \
             7   4

From Target [5]:
  Distance 1: Node 6 (down-left), Node 2 (down-right), Node 3 (up-parent)
  Distance 2:
    - from 6: none
    - from 2: Node 7, Node 4
    - from 3: Node 1 (down-right)

Nodes at distance 2: [7, 4, 1]
```

The teaching goal is to demonstrate how augmenting trees with parent pointers enables isotropic (direction-agnostic) shortest path expansions.

---

## 2. Conceptual Foundation & Invariants

### 1. Undirected Adjacency Mapping:
For any node $u \in V$:
$$
\text{Neighbors}(u) = \{v \mid v \in \{u.left, u.right, \text{parent}(u)\} \land v \ne \text{null}\}
$$

### 2. Radial Level Frontier Dynamics:
Let $L_d$ denote the set of nodes at exact geodesic distance $d$ from $target$:
$$
L_0 = \{target\}
$$
$$
L_{d+1} = \left( \bigcup_{u \in L_d} \text{Neighbors}(u) \right) \setminus (L_d \cup L_{d-1})
$$
The output is precisely the set $L_k$.

---

## 3. Step-by-Step Worked Execution

We trace $root = 3, target = 5, k = 2$:

---

### Phase 1: Construct Parent Map
- Traverse tree top-down:
  - $\text{parent}(3) = \text{null}$
  - $\text{parent}(5) = 3$
  - $\text{parent}(1) = 3$
  - $\text{parent}(6) = 5$
  - $\text{parent}(2) = 5$
  - $\text{parent}(0) = 1$
  - $\text{parent}(8) = 1$
  - $\text{parent}(7) = 2$
  - $\text{parent}(4) = 2$

---

### Phase 2: Radial DFS Outward from Target $5$ with Remaining Distance $k = 2$

---

#### Step 1: At Target $5$ (Remaining $k = 2$)
- Neighbors of $5$:
  1. Left child: $6$
  2. Right child: $2$
  3. Parent: $3$
- Explore each neighbor with $k - 1 = 1$.

---

#### Step 2: Explore Branch to Node $6$ ($k = 1$, Parent is $5$)
- Current: Node $6$.
- Neighbors:
  - Left: $\text{null}$
  - Right: $\text{null}$
  - Parent: $5$ (origin, skipped because $nxt == fa$).
- No further branches. Backtrack.

---

#### Step 3: Explore Branch to Node $2$ ($k = 1$, Parent is $5$)
- Current: Node $2$.
- Neighbors:
  - Left child: Node $7$ (unvisited, recurse with $k = 0$).
  - Right child: Node $4$ (unvisited, recurse with $k = 0$).
  - Parent: $5$ (origin, skipped).
- **At Node $7$ ($k = 0$):**
  - Remaining distance is $0$ $\implies$ **Target reached!**
  - Record value: **$7$**.
- **At Node $4$ ($k = 0$):**
  - Remaining distance is $0$ $\implies$ **Target reached!**
  - Record value: **$4$**.
- Backtrack to $5$.

---

#### Step 4: Explore Branch to Node $3$ ($k = 1$, Child origin is $5$)
- Current: Node $3$.
- Neighbors:
  - Left child: $5$ (origin, skipped).
  - Right child: Node $1$ (unvisited, recurse with $k = 0$).
  - Parent: $\text{null}$.
- **At Node $1$ ($k = 0$):**
  - Remaining distance is $0$ $\implies$ **Target reached!**
  - Record value: **$1$**.
- Backtrack.

---

### Termination:
All radial paths up to distance $2$ explored.
- Result set: **`[7, 4, 1]`**.

---

## 4. Complete Execution Trace

| Traversal Path | Current Node | From (Ancestor/Origin) | Remaining $k$ | Action Taken | Nodes Collected |
|:---|:---:|:---:|:---:|:---|:---:|
| Root start | $5$ | None | $2$ | Expand neighbors: $6, 2, 3$ | $[\,]$ |
| $5 \to 6$ | $6$ | $5$ | $1$ | No unvisited neighbors; backtrack | $[\,]$ |
| $5 \to 2$ | $2$ | $5$ | $1$ | Expand children: $7, 4$ | $[\,]$ |
| $5 \to 2 \to 7$ | **$7$** | $2$ | **$0$** | **$k = 0 \implies$ Collect 7** | $[7]$ |
| $5 \to 2 \to 4$ | **$4$** | $2$ | **$0$** | **$k = 0 \implies$ Collect 4** | $[7, 4]$ |
| $5 \to 3$ | $3$ | $5$ | $1$ | Expand right child: $1$ | $[7, 4]$ |
| $5 \to 3 \to 1$ | **$1$** | $3$ | **$0$** | **$k = 0 \implies$ Collect 1** | **`[7, 4, 1]`** |

---

## 5. Boundary Cases & Failure Modes

- **$k = 0$:** Target node itself is at distance $0$. Returns `[target.val]`.
- **$k$ Exceeds Tree Diameter:** No node exists at distance $k$. Returns empty list `[]`.
- **Target is the Tree Root:** Upward traversal parent is `null`; search only descends down left and right subtrees.
- **Target is a Leaf:** Upward traversal through parent is the only viable path.

---

## 6. Traps & Common Anti-Patterns

- **Infinite Ping-Pong Recursion:** Traversing to a neighbor and immediately recursing back to the previous node without an `nxt != fa` check causes infinite loops and recursion stack overflows.
- **Searching Only Descendants:** Looking only downward misses all nodes in parent and sibling subtrees.
- **Rebuilding Full Graph Matrices:** Storing an $\mathcal{O}(N^2)$ adjacency matrix wastes memory; a simple hash map or dictionary from child to parent provides full bidirectional navigation in $\mathcal{O}(N)$ memory.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Pass 1 (Parent mapping DFS): Visits every node once $\implies \mathcal{O}(N)$.
  - Pass 2 (Radial DFS from target): Visits nodes up to depth $k$ without revisiting $\implies \mathcal{O}(N)$.
  - Total Time: strictly $\mathcal{O}(N)$, completing in $< 5$ ms for $N \le 500$.
- **Auxiliary Space Complexity:**
  - Parent pointer map: stores $N$ entries $\implies \mathcal{O}(N)$.
  - Recursion call stack: bounded by tree height/depth $\mathcal{O}(N)$.
  - Total Space: $\mathcal{O}(N)$.
