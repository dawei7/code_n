# Guided Example: Second Minimum Node in a Binary Tree

We trace the step-by-step tournament tree root property ($root.val = \min(\text{all descendants})$), post-order/pre-order recursive tree exploration, strict inequality threshold filtering ($node.val > root.val$), candidate subtree branch pruning, running second-minimum minimization ($ans = \min(ans, node.val)$), and uniform-value degenerate detection ($-1$) on representative tournament trees:

- **Input:**
  - Tree: $root = [2, 2, 5, \text{null}, \text{null}, 5, 7]$
  - Tree topology:
    ```text
            2
          /   \
         2     5
              / \
             5   7
    ```
- **Required output:** `5`
  - Special tournament tree property:
    - Every node has either $0$ or $2$ children.
    - If a node has $2$ children, its value is the minimum of its children:
      $$
      node.val = \min(node.left.val, \; node.right.val)
      $$
    - Mathematical consequence: The root node is guaranteed to hold the **absolute global minimum** of the entire tree:
      $$
      v = root.val = \min_{u \in \text{Tree}} u.val
      $$
    - Objective: Find the smallest node value that is **strictly greater** than the root value ($u.val > v$). If no such value exists (all nodes are equal), return $-1$.
- **Tournament Heap Monotonicity & Subtree Pruning Invariant:**
  - **The Subtree Lower Bound Property:**
    - By induction, for any node $u$, all nodes in the subtree rooted at $u$ have values $\ge u.val$:
      $$
      \forall w \in \text{subtree}(u): \quad w.val \ge u.val
      $$
    - Therefore, if we encounter a node $u$ with $u.val > v$:
      - Node $u$ is an immediate candidate for the second minimum ($ans \leftarrow \min(ans, \; u.val)$).
      - Crucially: **no node in the subtree of $u$ can ever be smaller than $u.val$**!
      - We can prune and halt traversal into the subtree of $u$ immediately.
    - If $u.val == v$:
      - Node $u$ matches the global minimum.
      - Its children could contain larger values that qualify as the second minimum, so we must explore both children.
- **Step-by-Step Worked Execution Trace on $[2, 2, 5, \text{null}, \text{null}, 5, 7]$:**
  - Global minimum recorded from root:
    $$
    v = root.val = \mathbf{2}
    $$
  - Initialize second minimum tracker:
    $$
    ans = -1
    $$
  - **Step 1: Inspect Root Node (value $2$):**
    - Value is $2 == v$.
    - Not strictly greater than $v$.
    - Recurse into left child (Node $2_L$) and right child (Node $5_R$).
  - **Step 2: Inspect Left Child (Node $2_L$):**
    - Value is $2 == v$.
    - Node $2_L$ has no children (leaf node).
    - Returns without finding any candidate $> 2$.
  - **Step 3: Inspect Right Child (Node $5_R$):**
    - Value is $5$.
    - Compare with global minimum:
      $$
      5 > v \quad (5 > 2) \implies \mathbf{Candidate\ Found!}
      $$
    - Update second minimum:
      $$
      ans = 5 \quad (\text{since } ans \text{ was } -1)
      $$
    - Subtree pruning: Because all descendants of Node $5_R$ must be $\ge 5$, examining children $5$ and $7$ cannot yield any value smaller than $5$.
    - (Even if child $7$ is visited, $\min(5, 7) = 5$, leaving $ans = 5$ unchanged).
    - Halt branch.
  - **Step 4: Conclude Traversal:**
    - All branches fully explored or pruned.
    - Smallest value strictly greater than $2$ found is:
      $$
      ans = \mathbf{5}
      $$
- **All Identical Values ($root = [2, 2, 2]$):**
  - Root: 2 ($v = 2$).
  - Left child: 2 ($== v$, leaf).
  - Right child: 2 ($== v$, leaf).
  - No node has value $> 2$.
  - $ans$ remains $-1 \implies$ Returns **`-1`**.
- **Deep Tree Propagation ($root = [1, 1, 3, 1, 2]$):**
  - Left subtree contains 1 with children 1 and 2.
  - Right subtree contains 3 ($3 > 1$).
  - Left traversal discovers candidate 2 ($2 > 1$).
  - Second minimum is $\min(3, 2) = \mathbf{2}$.

This instance demonstrates tournament tree minimum selection and branch-and-bound subtree pruning, mathematically proves why monotonicity allows early termination at the first strict upper bound on any path, and derives $O(N)$ worst-case / $O(K)$ pruned runtime and $O(H)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a special binary tree where $node.val = \min(left.val, right.val)$:
Find the **second minimum value** in the tree.
If all nodes have the same value, return $-1$.

```text
Tree:
        2   (Root is ALWAYS the global minimum: 2)
      /   \
     2     5  <-- 5 > 2: Candidate for second minimum!
          / \
         5   7

Candidates strictly greater than 2: [ 5, 7 ]
Second Minimum = min(5, 7) = 5
```

### The Invariant of the Tournament Root
- The root holds the minimum of the entire tree ($v = root.val$).
- Any node with value $> v$ is a candidate for the second minimum.
- Any node with value $== v$ must be explored deeper to find divergent branches.

---

## 2. Conceptual Foundation & Invariants

### 1. The Second Minimum Search Invariant:
For any node $u$:
- If $u.val > v$:
  $$
  ans \leftarrow \begin{cases} u.val & \text{if } ans == -1 \\ \min(ans, \; u.val) & \text{otherwise} \end{cases}
  $$
  (Prune subtree of $u$ because all its descendants are $\ge u.val$).
- If $u.val == v$:
  - Recurse on both $u.left$ and $u.right$.

### 2. Degenerate Condition:
If all nodes in the tree equal $v$, $ans$ remains $-1$.

> **Tournament Monotone Convexity Invariant.** Under the operation $u.val = \min(u.left.val, u.right.val)$, the values along any path from the root to any leaf form a non-decreasing sequence, guaranteeing that the first value strictly exceeding $root.val$ on any branch is minimal for that branch.

---

## 3. Step-by-Step Worked Execution

We trace $root = [2, 2, 5, \text{null}, \text{null}, 5, 7]$:

---

### Step 1: Initialize
- $v = 2$.
- $ans = -1$.

---

### Step 2: Visit Left (Node $2_L$)
- $2 == 2$: Not greater than $v$.
- Leaf node $\implies$ no children.

---

### Step 3: Visit Right (Node $5_R$)
- $5 > 2$: Candidate!
- $ans \leftarrow 5$.
- Prune children of 5.

---

### Step 4: Output
- $ans = \mathbf{5}$.

---

## 4. Complete Execution Trace

| Node Evaluated | Node Value | Root Minimum $v$ | Value $> v$? | Subtree Action | Second Minimum Candidate $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Root | $2$ | $2$ | No ($2 = 2$) | Explore left and right | $-1$ |
| Left Child | $2$ | $2$ | No ($2 = 2$) | Leaf reached | $-1$ |
| **Right Child** | **`5`** | **`2`** | **Yes (`5 > 2`)** | **Prune Subtree** | **`5`** |
| Subtree Children | $5, 7$ | $2$ | $\ge 5$ | Skipped by pruning | $5$ |
| **Conclusion** | — | — | — | — | **`5`** |

---

## 5. Boundary Cases & Failure Modes

- **All Nodes Identical ($[2, 2, 2]$):** No candidate $> 2$ found $\implies -1$.
- **Single Node Tree:** Zero children $\implies -1$.
- **Two Levels ($[1, 1, 2]$):** Right child is 2 $\implies 2$.
- **Large Values ($val = 2^{31} - 1$):** Handled cleanly using $-1$ as the empty sentinel rather than $\infty$.

---

## 6. Traps & Common Anti-Patterns

- **Searching Subtrees of Elements $> v$:** If a node has value 5, all its descendants are $\ge 5$. Exploring below 5 can never find a value smaller than 5. Pruning at 5 saves exponential work.
- **Using 32-Bit Max as Sentinel:** If the second minimum itself is $2^{31} - 1$, initializing $ans = 2^{31} - 1$ makes it impossible to distinguish between finding $2^{31} - 1$ and finding nothing. Use $-1$ as the empty state flag.
- **Collecting All Values in a Set ($O(N \log N)$):** Dumping all tree values into a set and sorting takes extra space and time. Direct recursive search with pruning runs in $O(N)$ or better.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In the worst case (all nodes equal), visits all $N$ nodes: $\mathcal{O}(N)$.
  - With branch pruning, skips all descendants of nodes with $val > v$, running in $\mathcal{O}(K)$ where $K$ is the number of nodes with value equal to root.
  - Total Time: $\mathcal{O}(N)$. Completes in $< 1$ ms for $N = 1000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ auxiliary space for the recursion call stack, where $H$ is the tree height.
