# Guided Example: Find Leaves of Binary Tree

We trace the step-by-step bottom-up post-order DFS height computation ($h = \max(l, r)$), dynamic level bucket allocation (`len(ans) == h`), implicit leaf-peeling stratification, and final collection array assembly on representative binary trees:

- **Input:** `root = [1, 2, 3, 4, 5]`
- **Required output:** `[[4, 5, 3], [2], [1]]`
  - Visual tree structure:
    ```text
          1
         / \
        2   3
       / \
      4   5
    ```
  - Round 1 removal (Height 0 leaves):
    - Node 4: leaves $l=0, r=0 \implies h = 0$
    - Node 5: leaves $l=0, r=0 \implies h = 0$
    - Node 3: leaves $l=0, r=0 \implies h = 0$
    - Collected in Round 1: `[4, 5, 3]`
  - Round 2 removal (Height 1 nodes whose children were leaves):
    - Node 2: children had height 0 (returned 1) $\implies h = \max(1, 1) = 1$
    - Collected in Round 2: `[2]`
  - Round 3 removal (Height 2 root):
    - Node 1: left child height 1 (returned 2), right child height 0 (returned 1) $\implies h = \max(2, 1) = 2$
    - Collected in Round 3: `[1]`
  - Final leaf peel order: `[[4, 5, 3], [2], [1]]`
- **Single Node Tree:** `root = [1] \implies [[1]]`
- **Skewed Linear Tree:** `root = [1, 2, null, 3] \implies [[3], [2], [1]]`

This instance demonstrates bottom-up height classification in binary trees, mathematically proves why the round in which any node becomes a leaf equals its maximum distance to a descendant leaf, avoids explicit pointer modifications or tree mutation, and achieves $O(N)$ linear time and $O(H)$ recursion stack space.

---

## 1. Instance & Teaching Goal

Given a binary tree:
$$
\text{root} = [1, \; 2, \; 3, \; 4, \; 5]
$$
Collect and remove all leaf nodes repeatedly until the tree is completely empty. Return the leaves collected in each sequential wave:

```text
Initial Tree:
        1
       / \
      2   3
     / \
    4   5

Step 1: Collect current leaves {4, 5, 3} and remove them:
        1
       /
      2
Collected: [4, 5, 3]

Step 2: Collect new leaf {2} and remove it:
        1
Collected: [2]

Step 3: Collect root {1} and remove it:
        (Empty)
Collected: [1]

Final Output: [[4, 5, 3], [2], [1]]
```

### Eliminating Tree Mutation via Height Invariance
- Modifying tree pointers (`node.left = None`) and repeated scanning takes $O(N \cdot H)$ time.
- **The Height Principle:**
  A node is removed in round $h$ if and only if the longest path from the node down to any leaf in its subtree has length $h$!
  $$
  h(\text{node}) = \max\big(h(\text{node.left}), \; h(\text{node.right})\big)
  $$
  where $h(\text{None}) = 0$ (so a leaf has $l=0, r=0 \implies h = 0$).
- By performing a standard post-order traversal, each node can be placed directly into bucket `ans[h]` in a single $O(N)$ pass without mutating the tree!

---

## 2. Conceptual Foundation & Invariants

### 1. The Recursive Contract `dfs(node) -> int`
- **Base Case:**
  If `node is None`: return $0$.
- **Recursive Step:**
  Query children:
  $$
  l = dfs(\text{node.left}), \quad r = dfs(\text{node.right})
  $$
  Compute removal round:
  $$
  h = \max(l, \; r)
  $$
- **Bucket Allocation:**
  If $\text{len}(ans) == h$:
  $$
  ans.\text{append}([])
  $$
  Append value:
  $$
  ans[h].\text{append}(\text{node.val})
  $$
- **Return Height to Parent:**
  $$
  \text{return } h + 1
  $$

> **Invariant.** For every node $u$, $h = \max(dfs(u.left), dfs(u.right))$ is the exact number of leaf-peeling rounds that must precede the removal of $u$.

---

## 3. Step-by-Step Worked Execution

We trace `root = [1, 2, 3, 4, 5]`:
Post-order visits: Left $\to$ Right $\to$ Node.

---

### Step 1: Visit Node 4 (Left child of 2)
- Left child: `None \implies l = 0`.
- Right child: `None \implies r = 0`.
- Removal level: $h = \max(0, 0) = \mathbf{0}$.
- Since $\text{len}(ans) == 0$, create level: $ans = [[]]$.
- Append value: $ans[0].\text{append}(4) \implies ans = [[\mathbf{4}]]$.
- Return to parent: $h + 1 = \mathbf{1}$.

---

### Step 2: Visit Node 5 (Right child of 2)
- $l = 0, r = 0 \implies h = \mathbf{0}$.
- Level $0$ exists. Append value:
  $$
  ans[0].\text{append}(5) \implies ans = [[4, \; \mathbf{5}]]
  $$
- Return to parent: $h + 1 = \mathbf{1}$.

---

### Step 3: Visit Node 2 (Left child of 1)
- Left subtree returned $l = 1$, right subtree returned $r = 1$.
- Removal level: $h = \max(1, 1) = \mathbf{1}$.
- Since $\text{len}(ans) == 1$, create level: $ans = [[4, 5], \; []]$.
- Append value:
  $$
  ans[1].\text{append}(2) \implies ans = [[4, 5], \; [\mathbf{2}]]
  $$
- Return to parent: $h + 1 = \mathbf{2}$.

---

### Step 4: Visit Node 3 (Right child of 1)
- Left child: `None \implies l = 0`, Right child: `None \implies r = 0`.
- Removal level: $h = \max(0, 0) = \mathbf{0}$.
- Level 0 exists. Append value:
  $$
  ans[0].\text{append}(3) \implies ans = [[4, 5, \; \mathbf{3}], \; [2]]
  $$
- Return to parent: $h + 1 = \mathbf{1}$.

---

### Step 5: Visit Node 1 (Root)
- Left child (Node 2) returned $l = 2$.
- Right child (Node 3) returned $r = 1$.
- Removal level: $h = \max(2, 1) = \mathbf{2}$.
- Since $\text{len}(ans) == 2$, create level: $ans = [[4, 5, 3], [2], []]$.
- Append value:
  $$
  ans[2].\text{append}(1) \implies ans = [[4, 5, 3], \; [2], \; [\mathbf{1}]]
  $$
- Return: $h + 1 = 3$.

---

### Step 6: Traversal Complete
Post-order DFS finishes. Return collected levels:
$$
\mathbf{[[4, 5, 3], [2], [1]]}
$$

---

## 4. Complete Execution Trace

```text
Post-order Traversal Order:
1. dfs(4): l=0, r=0 -> h=0 -> ans[0].append(4) -> return 1
2. dfs(5): l=0, r=0 -> h=0 -> ans[0].append(5) -> return 1
3. dfs(2): l=1, r=1 -> h=1 -> ans[1].append(2) -> return 2
4. dfs(3): l=0, r=0 -> h=0 -> ans[0].append(3) -> return 1
5. dfs(1): l=2, r=1 -> h=2 -> ans[2].append(1) -> return 3

Result: [[4, 5, 3], [2], [1]]
```

| Traversal Step | Node Visited | Left Child Return $l$ | Right Child Return $r$ | Computed Level $h = \max(l, r)$ | Return to Parent $h + 1$ | State of Output Array `ans` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | Node 4 | 0 | 0 | 0 | 1 | `[[4]]` |
| 2 | Node 5 | 0 | 0 | 0 | 1 | `[[4, 5]]` |
| 3 | Node 2 | 1 | 1 | 1 | 2 | `[[4, 5], [2]]` |
| 4 | Node 3 | 0 | 0 | 0 | 1 | `[[4, 5, 3], [2]]` |
| **5** | **Node 1** | **2** | **1** | **2** | **3** | **`[[4, 5, 3], [2], [1]]`** |

---

## 5. Algorithmic Correctness

**Soundness.** A node becomes a leaf only when all its child nodes have already been removed. By induction, if child subtrees require $l$ and $r$ rounds respectively, the current node cannot be removed before round $\max(l, r)$. At round $\max(l, r)$, both children are gone, making this node a leaf. Assigning the node to bucket $h = \max(l, r)$ exactly replicates physical tree pruning.

**Completeness.** Every node in the binary tree is visited during the post-order DFS. Because `ans` expands dynamically whenever a new maximum height $h$ is discovered, every node value is appended to its exact height group.

---

## 6. Traps This Instance Exposes

- **Modifying Tree Nodes In-Place:** Physically unlinking child pointers (`node.left = None`) alters the tree structure and requires repeatedly walking the tree, incurring $O(N^2)$ worst-case time for skewed trees.
- **Top-Down Depth vs Bottom-Up Height:** A common misconception is grouping nodes by their depth from the root. Leaves can exist at multiple different depths (e.g. Node 3 is at depth 1, while Nodes 4 and 5 are at depth 2). The round of removal depends on bottom-up height, not top-down depth.
- **Order within Round:** Nodes removed in the same round can be listed in any valid left-to-right order. Post-order DFS naturally produces standard left-to-right order.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is visited exactly once during the post-order DFS.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the height of the binary tree ($O(\log N)$ average, $O(N)$ worst-case for skewed trees), representing the maximum call stack depth.
