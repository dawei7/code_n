# Guided Example: N-ary Tree Preorder Traversal

We trace the step-by-step top-down pre-order visit sequence ($\text{root} \to \text{children}$), recursive depth-first stack activation, left-to-right sibling ordering, empty tree base case handling, and node value accumulation on representative $N$-ary tree structures:

- **Input:**
  - $N$-ary tree with root $1$:
    - Node $1$ has three children: Node $3$, Node $2$, and Node $4$.
    - Node $3$ has two children: Node $5$ and Node $6$.
    - Nodes $5, 6, 2, 4$ are leaf nodes (empty child lists).
- **Required output:** `[1, 3, 5, 6, 2, 4]`
  - Traversal invariant: In a **pre-order** traversal, a parent node is visited **strictly before** any of its children, and children are explored sequentially from left to right.
- **Recursive Depth-First Preorder Trace:**
  - Traversal rule $dfs(u)$:
    1. If $u$ is `null`, return.
    2. Record current node's value: $\text{visit}(u)$.
    3. Iterate through children: $dfs(c_1), dfs(c_2), \dots, dfs(c_k)$.
  - **Step 1: Start at Root Node 1:**
    - Visit Node $1$ first:
      $$
      ans = [1]
      $$
    - Node $1$ has children: $[3, 2, 4]$.
    - Dispatch call to first child: Node $3$.
  - **Step 2: Recurse on Node 3:**
    - Visit Node $3$ immediately:
      $$
      ans = [1, \; 3]
      $$
    - Node $3$ has children: $[5, 6]$.
    - Dispatch call to first child of $3$: Node $5$.
  - **Step 3: Recurse on Node 5 (Leaf):**
    - Visit Node $5$:
      $$
      ans = [1, \; 3, \; 5]
      $$
    - Node $5$ has no children ($children = []$).
    - Traversal of Node $5$ finishes $\implies$ return to Node $3$.
  - **Step 4: Recurse on Node 6 (Leaf):**
    - Dispatch call to second child of $3$: Node $6$.
    - Visit Node $6$:
      $$
      ans = [1, \; 3, \; 5, \; 6]
      $$
    - Node $6$ has no children.
    - Traversal of Node $6$ finishes $\implies$ return to Node $3$.
  - Traversal of Node $3$'s subtree is fully complete $\implies$ return to Root Node $1$.
  - **Step 5: Recurse on Node 2 (Second child of Root):**
    - Dispatch call to second child of $1$: Node $2$.
    - Visit Node $2$:
      $$
      ans = [1, \; 3, \; 5, \; 6, \; 2]
      $$
    - Node $2$ has no children.
    - Traversal of Node $2$ finishes $\implies$ return to Root Node $1$.
  - **Step 6: Recurse on Node 4 (Third child of Root):**
    - Dispatch call to third child of $1$: Node $4$.
    - Visit Node $4$:
      $$
      ans = [1, \; 3, \; 5, \; 6, \; 2, \; 4]
      $$
    - Node $4$ has no children.
    - Traversal of Node $4$ finishes $\implies$ return to Root Node $1$.
  - All children of Root Node $1$ exhausted.
  - Final pre-order sequence:
    $$
    \mathbf{[1, 3, 5, 6, 2, 4]}
    $$
- **Single Node Tree ($root = [1]$):**
  - Visits root $1$ and terminates $\implies [1]$.
- **Empty Tree ($root = \text{null}$):**
  - Base case triggers immediately $\implies []$.

This instance demonstrates recursive and stack-based pre-order scheduling over multi-way trees, mathematically proves why root-first processing yields a unique topological sequence preserving ancestral dominance, and derives $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of an $N$-ary tree:
Return the **pre-order traversal** of its nodes' values.

```text
N-ary Tree:
        1
      / | \
     3  2  4
    / \
   5   6

Pre-order: Visit Root, then Children left-to-right.
Sequence: 1 -> 3 -> 5 -> 6 -> 2 -> 4
```

### Pre-Order Traversal Invariants in $N$-ary Trees
- Unlike binary trees which have only left and right children, an $N$-ary tree node can have $0, 1, 2, \dots, K$ children.
- The pre-order contract is universal:
  1. Process the **current node first**.
  2. Recursively process **each child in the order of the `children` list**.

---

## 2. Conceptual Foundation & Invariants

### 1. The Recursive Formulation:
```text
dfs(node):
  if node is null:
    return
  append node.val to ans
  for child in node.children:
    dfs(child)
```

### 2. Iterative Simulation with a Stack:
- Push `root` to a LIFO stack.
- While stack is not empty:
  - Pop `curr`.
  - Append `curr.val` to `ans`.
  - Push `curr.children` onto the stack in **reverse order** (so the leftmost child ends on top and is processed next).

> **Ancestral Precedence Invariant.** For every node $u$ and every descendant $v$ of $u$, $u$ appears before $v$ in the pre-order traversal sequence.

---

## 3. Step-by-Step Worked Execution

We trace the sample tree:

---

### Step 1: Visit Root
- Visit Node 1: `ans = [1]`.
- Children: $[3, 2, 4]$.

---

### Step 2: Traverse Child 3
- Visit Node 3: `ans = [1, 3]`.
- Children of 3: $[5, 6]$.
- Visit Node 5: `ans = [1, 3, 5]`.
- Visit Node 6: `ans = [1, 3, 5, 6]`.

---

### Step 3: Traverse Child 2
- Visit Node 2: `ans = [1, 3, 5, 6, 2]`.
- No children.

---

### Step 4: Traverse Child 4
- Visit Node 4: `ans = [1, 3, 5, 6, 2, 4]`.
- No children.

---

### Step 5: Emit Output
$$
ans = \mathbf{[1, 3, 5, 6, 2, 4]}
$$

---

## 4. Complete Execution Trace

| Step | Call Stack | Node Visited | Children Queued | Output List $ans$ |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | `[1]` | **$1$** | `[3, 2, 4]` | `[1]` |
| $2$ | `[1, 3]` | **$3$** | `[5, 6]` | `[1, 3]` |
| $3$ | `[1, 3, 5]` | **$5$** | `[]` | `[1, 3, 5]` |
| $4$ | `[1, 3, 6]` | **$6$** | `[]` | `[1, 3, 5, 6]` |
| $5$ | `[1, 2]` | **$2$** | `[]` | `[1, 3, 5, 6, 2]` |
| $6$ | `[1, 4]` | **$4$** | `[]` | **`[1, 3, 5, 6, 2, 4]`** |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = \text{null}$):** Returns empty list `[]`.
- **Single Node Tree ($root = 1$, no children):** Returns `[1]`.
- **Linear Chain ($1 \to 2 \to 3 \to 4$):** Traverses down the chain returning `[1, 2, 3, 4]`.
- **Wide Tree (Root with 1000 leaf children):** Visits root, then all leaves in left-to-right order.

---

## 6. Traps & Common Anti-Patterns

- **Visiting Children Before Appending Root:** Appending the root after recursing on children produces post-order traversal instead of pre-order. Pre-order requires visiting the root *before* the child loop.
- **Pushing Children Left-to-Right in Iterative Stack:** In an explicit stack, pushing child 0 then child 1 leaves child 1 on top, causing the right branch to be explored first. Children must be pushed in reverse order (`reversed(node.children)`).
- **Not Handling `None` Root:** Omitting the base case `if root is None: return []` throws an attribute error when accessing `root.val`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Every node is visited exactly once during the DFS traversal.
  - For $N$ nodes, total operations: $\mathcal{O}(N)$.
  - For $N = 10^4$, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ stack space proportional to the maximum height of the tree ($H \le N$). In the worst case of a degenerate linked list, $O(N)$.