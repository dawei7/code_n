# Guided Example: N-ary Tree Postorder Traversal

We trace the step-by-step bottom-up post-order visit sequence ($\text{children} \to \text{root}$), post-order recursive stack unwinding, left-to-right sibling processing, leaf-first evaluation, and parent node consolidation on representative $N$-ary tree hierarchies:

- **Input:**
  - $N$-ary tree with root $1$:
    - Node $1$ has three children: Node $3$, Node $2$, and Node $4$.
    - Node $3$ has two children: Node $5$ and Node $6$.
    - Nodes $5, 6, 2, 4$ are leaf nodes (empty child lists).
- **Required output:** `[5, 6, 3, 2, 4, 1]`
  - Traversal invariant: In a **post-order** traversal, all children and descendants of a node must be visited **strictly before** the parent node itself is visited. Children are explored in left-to-right sequence.
- **Recursive Depth-First Postorder Trace:**
  - Traversal rule $dfs(u)$:
    1. If $u$ is `null`, return.
    2. For each child $c_i \in u.children$:
       Recurse: $dfs(c_i)$.
    3. Record current node's value: $\text{visit}(u)$.
  - **Step 1: Arrive at Root Node 1:**
    - Children to explore: $[3, 2, 4]$.
    - Cannot visit Node $1$ yet; dispatch call to first child: Node $3$.
  - **Step 2: Arrive at Node 3:**
    - Children to explore: $[5, 6]$.
    - Cannot visit Node $3$ yet; dispatch call to first child of $3$: Node $5$.
  - **Step 3: Arrive at Node 5 (Leaf):**
    - Node $5$ has no children ($children = []$).
    - Child loop completes immediately.
    - Visit Node $5$:
      $$
      ans = [5]
      $$
    - Return to Node $3$.
  - **Step 4: Arrive at Node 6 (Leaf):**
    - Dispatch call to second child of $3$: Node $6$.
    - Node $6$ has no children.
    - Child loop completes immediately.
    - Visit Node $6$:
      $$
      ans = [5, \; 6]
      $$
    - Return to Node $3$.
  - **Step 5: Consolidate Subtree at Node 3:**
    - All children of Node $3$ ($5$ and $6$) have been fully processed.
    - Now visit Node $3$:
      $$
      ans = [5, \; 6, \; \mathbf{3}]
      $$
    - Return to Root Node $1$.
  - **Step 6: Arrive at Node 2 (Second child of Root):**
    - Dispatch call to second child of $1$: Node $2$.
    - Node $2$ has no children.
    - Visit Node $2$:
      $$
      ans = [5, \; 6, \; 3, \; \mathbf{2}]
      $$
    - Return to Root Node $1$.
  - **Step 7: Arrive at Node 4 (Third child of Root):**
    - Dispatch call to third child of $1$: Node $4$.
    - Node $4$ has no children.
    - Visit Node $4$:
      $$
      ans = [5, \; 6, \; 3, \; 2, \; \mathbf{4}]
      $$
    - Return to Root Node $1$.
  - **Step 8: Consolidate Root Node 1:**
    - All subtrees of Node $1$ ($[3, 2, 4]$) have completed.
    - Now visit Root Node $1$:
      $$
      ans = [5, \; 6, \; 3, \; 2, \; 4, \; \mathbf{1}]
      $$
  - Traversal terminates.
  - Final post-order sequence:
    $$
    \mathbf{[5, 6, 3, 2, 4, 1]}
    $$
- **Single Node Tree ($root = [1]$):**
  - No children $\implies$ visits root and returns $[1]$.
- **Empty Tree ($root = \text{null}$):**
  - Returns `[]`.

This instance demonstrates bottom-up post-order reduction over generalized trees, mathematically proves why post-order traversal yields topological subtree summaries where dependencies precede consumers, and derives $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of an $N$-ary tree:
Return the **post-order traversal** of its nodes' values.

```text
N-ary Tree:
        1
      / | \
     3  2  4
    / \
   5   6

Post-order: Visit Children left-to-right, then Root.
Subtree 3 -> [5, 6, 3]
Subtree 2 -> [2]
Subtree 4 -> [4]
Root 1    -> [1]

Sequence: 5 -> 6 -> 3 -> 2 -> 4 -> 1
```

### Post-Order Traversal Invariants in $N$-ary Trees
- A node cannot be processed until all subtrees rooted at its children have been completely evaluated.
- Useful for bottom-up aggregations (e.g. deleting tree nodes, computing subtree sizes, directory disk space calculation).

---

## 2. Conceptual Foundation & Invariants

### 1. The Recursive Formulation:
```text
dfs(node):
  if node is null:
    return
  for child in node.children:
    dfs(child)
  append node.val to ans
```

### 2. The Iterative Reversal Duality:
- A modified pre-order that visits `Root -> Right Child -> Left Child` produces:
  $$
  [1, 4, 2, 3, 6, 5]
  $$
- Notice that reversing this sequence produces the exact post-order:
  $$
  \text{reverse}([1, 4, 2, 3, 6, 5]) = [5, 6, 3, 2, 4, 1]
  $$
- This duality allows non-recursive implementations using a single stack followed by an array reversal!

> **Descendant Precedence Invariant.** For every node $u$ and every descendant $v$ of $u$, $v$ appears before $u$ in the post-order traversal sequence.

---

## 3. Step-by-Step Worked Execution

We trace the sample tree:

---

### Step 1: Subtree at 3
- Children are 5 and 6.
- Visit leaf 5: `[5]`.
- Visit leaf 6: `[5, 6]`.
- Visit parent 3: `[5, 6, 3]`.

---

### Step 2: Subtree at 2
- Leaf 2: `[5, 6, 3, 2]`.

---

### Step 3: Subtree at 4
- Leaf 4: `[5, 6, 3, 2, 4]`.

---

### Step 4: Visit Root 1
- All children done.
- Append 1:
  $$
  ans = \mathbf{[5, 6, 3, 2, 4, 1]}
  $$

---

## 4. Complete Execution Trace

| Recursion Event | Node Evaluated | Action Taken | Current $ans$ Accumulator |
|:---:|:---:|:---:|:---:|
| Leaf Arrival | Node $5$ | Append $5$ | `[5]` |
| Leaf Arrival | Node $6$ | Append $6$ | `[5, 6]` |
| Children Done | Node $3$ | Append $3$ | `[5, 6, 3]` |
| Leaf Arrival | Node $2$ | Append $2$ | `[5, 6, 3, 2]` |
| Leaf Arrival | Node $4$ | Append $4$ | `[5, 6, 3, 2, 4]` |
| Root Finished | Node $1$ | Append $1$ | **`[5, 6, 3, 2, 4, 1]`** |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = \text{null}$):** Returns `[]`.
- **Single Node Tree ($root = 1$):** Returns `[1]`.
- **Deep Linear Hierarchy ($1 \to 2 \to 3 \to 4$):** Deepest node 4 visited first, unwinding up to root $\implies [4, 3, 2, 1]$.
- **Broad Tree with Multiple Siblings:** Siblings evaluated strictly in left-to-right array index order.

---

## 6. Traps & Common Anti-Patterns

- **Appending Root Before Traversing Children:** Appending before children creates pre-order traversal. Post-order requires appending *after* the child loop.
- **Reversing Sibling Order:** Children must be processed left-to-right ($c_0, c_1, \dots$). Exploring children right-to-left inverts the horizontal order of the leaves.
- **Modifying Node Children List In-Place:** Popping children destructively alters the input data structure. Use standard index iteration.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Each node is visited twice (once on discovery, once on return from children).
  - Total operations: strictly linear $\mathcal{O}(N)$ for $N$ nodes.
  - For $N = 10^4$, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ call stack space proportional to maximum tree height ($H \le N$). In worst case of a skewed linear tree, $O(N)$.
