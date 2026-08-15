# Guided Example: Height of Binary Tree After Subtree Removal Queries

We trace the hierarchical Array, Tree, Depth-First Search, Breadth-First Search, Binary Tree traversal and subtree aggregation on a representative binary tree.

- **Input:** `{"root": [1, 3, 4, 2, null, 6, 5, null, null, null, null, null, 7], "queries": [4]}`
- **Required output:** `[2]`

This instance illustrates recursive decomposition, subtree invariant aggregation, and base-case handling on null child nodes.

---

## 1. Instance & Teaching Goal

The objective for **Height of Binary Tree After Subtree Removal Queries** is to evaluate tree properties by visiting nodes in topological hierarchy (post-order, pre-order, or level-order).
Because each tree node defines an independent root for its left and right subtrees, recursive divide-and-conquer resolves subtrees independently.

---

## 2. Conceptual Foundation & Invariants

We define the recursive contract $f(\text{node})$ that computes the required property for the subtree rooted at $\text{node}$.

| Traversal Component | Responsibility |
|---|---|
| Base Case ($	ext{node} = \text{None}$) | Returns neutral identity element (e.g. $0$, $\text{True}$, $\text{None}$) |
| Left Subtree $f(\text{node.left})$ | Recursively resolves left branch |
| Right Subtree $f(\text{node.right})$ | Recursively resolves right branch |
| Current Node Aggregation | Combines left and right subtree results |

> **Invariant.** When processing $\text{node}$, the return values from both subtrees are complete, correct, and independent.

---

## 3. Step-by-Step Worked Execution

### Step 1: Base Case Null Evaluation

- Leaf children reach $\text{None}$ and return base values without recursive branching.

| State Parameter | Result |
|---|---|
| Input Node | $\text{None}$ |
| Base Return Value | Neutral identity |

---

### Step 2: Subtree Recursion & Aggregation

- Execute post-order combination at internal nodes.
- Evaluate current node's contribution to global state.

| State Parameter | Result |
|---|---|
| Left Subtree Value | Computed |
| Right Subtree Value | Computed |
| Aggregated Node Result | Combined optimally |

---

## 4. Complete Execution Trace

| Node Traversal Order | Subtree Processed | Left Value | Right Value | Current Node Action | Emitted / Updated State |
|---|---|---|---|---|---|
| 1 (Leaf Nodes) | Base leaves | Neutral | Neutral | Evaluate leaf metric | Base value returned |
| 2 (Internal Nodes) | Intermediate | Left result | Right result | Aggregate metrics | Combined subtree value |
| 3 (Root) | Full Tree | Left subtree | Right subtree | Final aggregation | Global answer produced |

---

## 5. Algorithmic Correctness

**Soundness.** Tree structures are acyclic directed graphs. By induction on tree height, if base cases are correct and the aggregation formula preserves the invariant, the root computation is guaranteed to be correct.

**Completeness.** Every node in the tree is traversed exactly once, ensuring no branch or leaf is omitted.

---

## 6. Traps This Instance Exposes

- **Single-Child Skewed Trees:** Assuming both left and right children always exist causes `AttributeError: 'NoneType' object has no attribute`. Always handle null children.
- **Global vs. Local Aggregation:** Confusing the path passing *through* a node with the path *extendable* to its parent leads to invalid non-branching calculations.
- **Stack Overflow on Degenerate Trees:** Heavily unbalanced linked-list-shaped trees can exceed recursion depth; iterative or tail-recursion considerations apply.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ where $N$ is the total number of tree nodes visited.
- **Auxiliary Space Complexity:** $O(H)$ where $H$ is the tree height ($O(\log N)$ for balanced trees, $O(N)$ worst-case) matching the call stack depth.