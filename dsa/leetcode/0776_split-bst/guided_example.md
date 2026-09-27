# Guided Example: Split BST

We trace the step-by-step Binary Search Tree (BST) partition property ($\le target$ versus $> target$), recursive sub-tree division ($dfs(root)$), directional branch selection ($root.val \le target$ vs $root.val > target$), subtree rewiring preserving ancestor-descendant relationships, and twin BST root pair assembly ($[root_{\le}, root_{>}]$) on representative hierarchical tree structures:

- **Input:**
  - Binary Search Tree: $root = [4, 2, 6, 1, 3, 5, 7]$
  - Split threshold: $target = 2$
- **Required output:**
  $$
  [[2, 1], \; [4, 3, 6, \text{null}, \text{null}, 5, 7]]
  $$
  - BST splitting specifications:
    - Split the given BST into **two valid BST subtrees**:
      1. Tree $T_{\le}$: Contains all nodes with values $\le target$.
      2. Tree $T_{>}$: Contains all nodes with values $> target$.
    - **Structural Preservation Invariant:** For any child $c$ with parent $p$ in the original tree, if both remain in the same partition, $c$ must maintain its child relationship with parent $p$.
    - For $root = 4, target = 2$:
      - Original tree contains nodes $\{1, 2, 3, 4, 5, 6, 7\}$.
      - Partition 1 ($\le 2$): Nodes $\{1, 2\}$.
        - Subtree rooted at $2$ with left child $1$.
      - Partition 2 ($> 2$): Nodes $\{3, 4, 5, 6, 7\}$.
        - Subtree rooted at $4$: right child is $6$ (with children $5, 7$), and left child is rewired to $3$.
      - Both resulting trees strictly satisfy the BST order invariant!
- **Recursive Branch Rewiring Invariant:**
  - **Divide-and-Conquer Case 1 ($root.val \le target$):**
    - The current $root$ and its **entire left subtree** are strictly $\le target$.
    - Therefore, $root$ belongs to the smaller partition $T_{\le}$, and its left child pointer is already correct!
    - However, its **right subtree** may contain a mixture of values $\le target$ and $> target$.
    - Recursively split the right subtree:
      $$
      [l, \; r] \leftarrow dfs(root.right)
      $$
    - Subtree $l$ contains values $\le target$ (which are also $> root.val$). It safely attaches as the new right child of $root$:
      $$
      root.right \leftarrow l
      $$
    - Subtree $r$ contains values $> target$.
    - Return pair: $[root, \; r]$.
  - **Divide-and-Conquer Case 2 ($root.val > target$):**
    - The current $root$ and its **entire right subtree** are strictly $> target$.
    - Therefore, $root$ belongs to the larger partition $T_{>}$, and its right child pointer is already correct!
    - Its **left subtree** may contain a mixture of values $\le target$ and $> target$.
    - Recursively split the left subtree:
      $$
      [l, \; r] \leftarrow dfs(root.left)
      $$
    - Subtree $r$ contains values $> target$ (which are also $< root.val$). It safely attaches as the new left child of $root$:
      $$
      root.left \leftarrow r
      $$
    - Subtree $l$ contains values $\le target$.
    - Return pair: $[l, \; root]$.
- **Step-by-Step Worked Execution Trace on $root = [4, 2, 6, 1, 3, 5, 7], target = 2$:**
  - **Call 1: `dfs(Node 4)` ($val = 4, target = 2$):**
    - Test: $4 > 2 \implies \mathbf{Case\ 2\ (Root\ in\ T_{>})}$.
    - Right subtree of 4 (node 6 with 5, 7) remains untouched in $T_{>}$.
    - Split left subtree: call `dfs(Node 2)`.
  - **Call 2: `dfs(Node 2)` ($val = 2, target = 2$):**
    - Test: $2 \le 2 \implies \mathbf{Case\ 1\ (Root\ in\ T_{\le})}$.
    - Left subtree of 2 (node 1) remains untouched in $T_{\le}$.
    - Split right subtree: call `dfs(Node 3)`.
  - **Call 3: `dfs(Node 3)` ($val = 3, target = 2$):**
    - Test: $3 > 2 \implies \mathbf{Case\ 2\ (Root\ in\ T_{>})}$.
    - Left subtree is `None`: `dfs(None)` returns `[None, None]`.
    - Rewire: $3.left \leftarrow None$.
    - Node 3 returns: $[None, \; \text{Node } 3]$.
  - **Unwind to Call 2 (`Node 2`):**
    - Received from right split: $l = None, \; r = \text{Node } 3$.
    - Rewire right child of 2:
      $$
      2.right \leftarrow l = None
      $$
    - Node 2 is now a complete tree containing $\{1, 2\}$ with $2.left = 1, 2.right = None$.
    - Node 2 returns: $[\text{Node } 2, \; \text{Node } 3]$.
  - **Unwind to Call 1 (`Node 4`):**
    - Received from left split: $l = \text{Node } 2, \; r = \text{Node } 3$.
    - Rewire left child of 4:
      $$
      4.left \leftarrow r = \text{Node } 3
      $$
    - Node 4 now has left child $3$ and right child $6$ (which has $5, 7$).
    - Node 4 returns:
      $$
      [\text{Node } 2, \; \text{Node } 4]
      $$
  - **Final Partition Trees:**
    - Tree $\le 2$: Root 2 with left child 1.
    - Tree $> 2$: Root 4 with left child 3, right child 6 (children 5, 7).
    - Serialized:
      $$
      ans = [[2, 1], \; [4, 3, 6, \text{null}, \text{null}, 5, 7]]
      $$
- **Target Above All Nodes Trace ($root = [2, 1, 3], target = 5$):**
  - All nodes are $\le 5$.
  - Rightmost traversal reaches `None`, returning `[None, None]`.
  - Entire original tree returned as $T_{\le}$, with $T_{>} = None$.
  - Output: `[[2, 1, 3], []]`.
- **Target Below All Nodes Trace ($root = [2, 1, 3], target = 0$):**
  - All nodes are $> 0$.
  - Leftmost traversal reaches `None`.
  - Entire original tree returned as $T_{>}$, with $T_{\le} = None$.
  - Output: `[[], [2, 1, 3]]`.

This instance demonstrates recursive treap/BST split operations and pointer rewiring under total order cuts, mathematically proves why in-order sub-segment preservation guarantees valid search tree geometry in both partitioned components, and derives $O(H)$ execution time and $O(H)$ recursion space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a BST and an integer $target$:
Split the tree into two BSTs:
1. $T_{\le}$: all nodes with value $\le target$.
2. $T_{>}$: all nodes with value $> target$.
Preserve existing parent-child relationships where possible.

```text
       4
     /   \
    2     6      target = 2
   / \   / \
  1   3 5   7

Split at 2:
  Tree <= 2:     2
                /
               1

  Tree > 2:      4
                / \
               3   6
                  / \
                 5   7
Result: [ [2, 1], [4, 3, 6, null, null, 5, 7] ]
```

### The Invariant of the Single Branch Split
- If $root.val \le target$: $root$ and its left subtree are fully $\le target$. Only the right subtree needs splitting: $root.right = dfs(root.right)[0]$.
- If $root.val > target$: $root$ and its right subtree are fully $> target$. Only the left subtree needs splitting: $root.left = dfs(root.left)[1]$.

---

## 2. Conceptual Foundation & Invariants

### 1. Directional Recurrence:
$$
\text{if } root.val \le target \implies [l, r] = dfs(root.right), \; root.right = l \implies \text{return } [root, r]
$$
$$
\text{if } root.val > target \implies [l, r] = dfs(root.left), \; root.left = r \implies \text{return } [l, root]
$$

### 2. Base Case:
$$
dfs(None) = [None, None]
$$

> **BST Dedekind Cut Invariant.** The cut $(-\infty, target] \cup (target, \infty)$ partitions the in-order traversal of the BST into two contiguous segments. The recursive split algorithm preserves the relative order topology, producing two valid search trees in time proportional to tree height $H$.

---

## 3. Step-by-Step Worked Execution

We trace $root = [4, 2, 6, 1, 3, 5, 7], target = 2$:

---

### Step 1: At Node 4 ($4 > 2$)
- Recurse left on 2.

---

### Step 2: At Node 2 ($2 \le 2$)
- Recurse right on 3.

---

### Step 3: At Node 3 ($3 > 2$)
- Left is None $\implies$ returns $[None, 3]$.

---

### Step 4: Reconnect
- Node 2 connects right to None $\implies$ returns $[2, 3]$.
- Node 4 connects left to 3 $\implies$ returns $[2, 4]$.

---

### Step 5: Output
$$
[[2, 1], \; [4, 3, 6, \text{null}, \text{null}, 5, 7]]
$$

---

## 4. Complete Execution Trace

| Call Depth | Evaluated Node | Node Value vs Target | Branch Recursion | Child Split Returned $[l, r]$ | Rewired Edge | Returned Pair |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $3$ | Node $3$ | $3 > 2$ | Left (`None`) | `[None, None]` | $3.left = None$ | `[None, 3]` |
| $2$ | Node $2$ | $2 \le 2$ | Right (Node $3$) | `[None, 3]` | $2.right = None$ | `[2, 3]` |
| **$1$ (Root)** | **Node $4$** | **$4 > 2$** | **Left (Node $2$)** | **`[2, 3]`** | **$4.left = 3$** | **`[2, 4]`** |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($None$):** Returns `[None, None]`.
- **Target Greater Than All Nodes ($target = 10$):** Traverses right spine to end $\implies$ returns `[root, None]`.
- **Target Less Than All Nodes ($target = 0$):** Traverses left spine to end $\implies$ returns `[None, root]`.
- **Single Node ($[1], target = 1$):** Returns `[[1], None]`.

---

## 6. Traps & Common Anti-Patterns

- **Rebuilding the Trees from Scratch ($O(N \log N)$):** Extracting all values and inserting them into new trees violates the problem requirement to preserve original parent-child edges. Direct pointer rewiring in $O(H)$ preserves maximum original tree structure.
- **Swapping Return Pointers:** In Case 1 ($root.val \le target$), the returned pair is $[root, r]$, attaching $l$ to $root.right$. In Case 2 ($root.val > target$), the returned pair is $[l, root]$, attaching $r$ to $root.left$. Mixing them up reverses the trees.
- **Losing One Side of the Split:** The recursive call returns a 2-element list $[l, r]$. Both $l$ and $r$ must be accounted for (one reattached, the other passed upward).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The recursion visits only nodes along the search path for $target$.
  - Depth of recursion is bounded by tree height $H$.
  - Total Time: $\mathcal{O}(H)$ where $H = \mathcal{O}(\log N)$ for balanced trees and $\mathcal{O}(N)$ for skewed trees ($N \le 50$). Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ space for the recursion call stack.