# Guided Example: Maximum Depth of N-ary Tree

We trace the step-by-step bottom-up post-order depth-first search on arbitrary branching trees, child subtree depth aggregation ($mx = \max_{c} depth(c)$), leaf base case grounding ($1 + 0 = 1$), root-to-leaf path depth calculation ($1 + mx$), and global maximum depth extraction on representative N-ary trees:

- **Input:** $root = [1, [3, [5, 6]], 2, 4]$
  - Tree topology:
    - Root Node $1$ has three children: Node $3$, Node $2$, Node $4$.
    - Node $3$ has two children: Node $5$ and Node $6$.
    - Nodes $5, 6, 2, 4$ are leaves (zero children).
- **Required output:** `3`
  - Maximum depth definition: The total number of nodes along the longest simple path from the root node down to the farthest leaf node.
- **Bottom-Up Post-Order Depth Trace:**
  - Let $depth(node)$ return the maximum number of nodes from $node$ down to any leaf in its subtree.
  - **Recurrence Relation:**
    - If $node$ is `None`:
      $$
      depth(None) = 0
      $$
    - If $node$ has no children ($children = []$):
      $$
      depth(node) = 1 + 0 = \mathbf{1}
      $$
    - In general, for any node with children:
      $$
      depth(node) = 1 + \max_{child \in node.children} depth(child)
      $$
  - **Evaluating the Leaves:**
    - **Node 5:** $children = [] \implies mx = 0 \implies depth(5) = 1 + 0 = \mathbf{1}$.
    - **Node 6:** $children = [] \implies mx = 0 \implies depth(6) = 1 + 0 = \mathbf{1}$.
    - **Node 2:** $children = [] \implies mx = 0 \implies depth(2) = 1 + 0 = \mathbf{1}$.
    - **Node 4:** $children = [] \implies mx = 0 \implies depth(4) = 1 + 0 = \mathbf{1}$.
  - **Evaluating Internal Node 3:**
    - Children are Node 5 and Node 6.
    - Child depths:
      $$
      depth(5) = 1, \quad depth(6) = 1
      $$
    - Maximum child depth:
      $$
      mx = \max(1, 1) = \mathbf{1}
      $$
    - Total depth of Node 3:
      $$
      depth(3) = 1 + mx = 1 + 1 = \mathbf{2}
      $$
      *(Path: $3 \to 5$ or $3 \to 6$, length 2 nodes)*.
  - **Evaluating Root Node 1:**
    - Children are Node 3, Node 2, and Node 4.
    - Child depths:
      - From Node 3: $depth(3) = \mathbf{2}$
      - From Node 2: $depth(2) = \mathbf{1}$
      - From Node 4: $depth(4) = \mathbf{1}$
    - Maximum child depth:
      $$
      mx = \max(2, 1, 1) = \mathbf{2}
      $$
    - Total depth of Root:
      $$
      depth(1) = 1 + mx = 1 + 2 = \mathbf{3}
      $$
      *(Longest path: $1 \to 3 \to 5$, length 3 nodes)*.
  - Post-order traversal complete.
  - Maximum depth: **`3`**.
- **Empty Tree Instance ($root = None$):**
  - Base case triggers immediately $\implies \mathbf{0}$.
- **Single Node Tree ($root = [1]$):**
  - Node 1 has no children $\implies 1 + 0 = \mathbf{1}$.
- **Deep Linear Chain ($1 \to 2 \to 3 \to 4 \dots \to N$):**
  - Each node has 1 child; depth increments monotonically by 1 at each level $\implies \mathbf{N}$.

This instance demonstrates inductive tree depth aggregation across variable-degree branchings, mathematically proves why post-order child maximization yields the optimal root-to-leaf path length, and derives $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an N-ary tree:
Find its **maximum depth**.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

```text
N-ary Tree:
           1
        /  |  \
       3   2   4
      / \
     5   6

Longest Path: 1 -> 3 -> 5 (or 1 -> 3 -> 6)
Number of nodes = 3

Maximum Depth = 3
```

### Depth Aggregation in N-ary Trees
- Unlike a binary tree where each node has at most two children (`left` and `right`), an N-ary tree node can have $0, 1, 2, \dots, K$ children stored in a list `children`.
- The recursive logic remains identical:
  - The depth of a node is 1 plus the maximum depth among all of its children.
  - If a node has no children, its child maximum is 0, so its depth is $1 + 0 = 1$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Recursive Formulation:
$$
depth(root) =
\begin{cases}
0 & \text{if } root \text{ is None} \\
1 + \max_{c \in root.children} depth(c) & \text{if } root.children \ne \emptyset \\
1 & \text{if } root.children = \emptyset
\end{cases}
$$

### 2. Post-Order Invariant:
A parent node cannot compute its own depth until the depths of **all of its children** have been fully evaluated and returned.

> **Subtree Height Monotonicity Invariant.** Adding 1 to the maximum child depth guarantees that any ancestor at distance $k$ from a leaf has depth at least $k + 1$.

---

## 3. Step-by-Step Worked Execution

We trace the sample tree rooted at Node 1:

---

### Step 1: Base Case Check
Root is not None. Initialize child maximum: $mx = 0$.

---

### Step 2: Recurse on Children of Node 1
1. **Explore Child 3:**
   - Node 3 has children $[5, 6]$.
   - Recurse on Node 5: leaf $\implies depth(5) = 1$.
   - Recurse on Node 6: leaf $\implies depth(6) = 1$.
   - For Node 3: $mx = \max(1, 1) = 1$.
   - Depth of Node 3: $1 + 1 = \mathbf{2}$.
2. **Explore Child 2:**
   - Node 2 has no children $\implies depth(2) = 1 + 0 = \mathbf{1}$.
3. **Explore Child 4:**
   - Node 4 has no children $\implies depth(4) = 1 + 0 = \mathbf{1}$.

---

### Step 3: Compute Root Depth
- Child depths collected: $[2, 1, 1]$.
- Maximum child depth:
  $$
  mx = \max(2, 1, 1) = \mathbf{2}
  $$
- Depth of Root:
  $$
  1 + mx = 1 + 2 = \mathbf{3}
  $$

---

## 4. Complete Execution Trace

| Node Evaluated | Children Visited | Subtree Depths | Maximum Child Depth $mx$ | Returned Node Depth $1 + mx$ |
|:---:|:---:|:---:|:---:|:---:|
| Node 5 | None | — | $0$ | $1$ |
| Node 6 | None | — | $0$ | $1$ |
| **Node 3** | Nodes 5, 6 | $[1, 1]$ | $1$ | **$2$** |
| Node 2 | None | — | $0$ | $1$ |
| Node 4 | None | — | $0$ | $1$ |
| **Node 1 (Root)** | Nodes 3, 2, 4 | $[2, 1, 1]$ | $2$ | **$3$** |
| **Done** | — | — | — | **Result: $3$** |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = None$):** Checked at line 1 $\implies \mathbf{0}$.
- **Single Node Tree ($root = [1], children = []$):** Loop over children does not run $\implies mx = 0 \implies 1 + 0 = \mathbf{1}$.
- **Wide Flat Tree (Star Graph: 1 root with 1000 children):** All 1000 children report depth 1 $\implies 1 + \max(1) = \mathbf{2}$.
- **Deep Unary Tree (Linked List of 1000 nodes):** Depth reaches $\mathbf{1000}$.

---

## 6. Traps & Common Anti-Patterns

- **Assuming Tree is Binary:** Accessing `.left` or `.right` causes runtime `AttributeError`. N-ary nodes store children in a list `.children`.
- **Calling `max()` on an Empty List:** If a leaf node calls `max(depth(c) for c in root.children)` without a default value, Python raises `ValueError: max() arg is an empty sequence`. Initializing `mx = 0` cleanly prevents this exception.
- **Counting Edges Instead of Nodes:** The maximum depth of an N-ary tree is explicitly defined as the number of **nodes** along the path. A single root node has depth 1, not 0.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - DFS visits each of the $N$ nodes in the tree exactly once.
  - At each node, iterating through its children examines each directed edge once.
  - In a tree with $N$ nodes, there are exactly $N - 1$ edges.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ call stack space where $H$ is the tree height ($O(\log N)$ balanced, $O(N)$ worst-case).
