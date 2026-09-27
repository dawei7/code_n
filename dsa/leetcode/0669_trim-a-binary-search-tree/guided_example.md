# Guided Example: Trim a Binary Search Tree

We trace the step-by-step recursive range filtering ($[low, high]$), binary search tree directional pruning (pruning entire right subtrees when $val > high$, pruning entire left subtrees when $val < low$), valid root preservation, child pointer rewiring, and resulting trimmed BST topology synthesis on representative tree instances:

- **Input:**
  - Tree: $root = [3, 0, 4, \text{null}, 2, \text{null}, \text{null}, 1]$
  - Interval: $[low, high] = [1, 3]$
  - Original tree topology:
    ```text
            3
          /   \
         0     4
          \
           2
          /
         1
    ```
- **Required output:** `[3, 2, \text{null}, 1]`
  - Output tree topology:
    ```text
          3
         /
        2
       /
      1
    ```
  - Trimming rules:
    - Retain every node whose value $x$ satisfies $low \le x \le high$.
    - Completely remove any node whose value $x < low$ or $x > high$.
    - Preserve the ancestor-descendant relationships of all surviving nodes: the resulting tree must remain a valid Binary Search Tree.
- **BST Subtree Pruning Invariants:**
  - **Case 1: $root.val > high$ (Overshoot Pruning):**
    - In a BST, all nodes in the right subtree of $root$ have values strictly greater than $root.val$:
      $$
      \forall u \in \text{right}(root): \quad u.val > root.val > high
      $$
    - Therefore, the current node and its **entire right subtree** are invalid and must be discarded.
    - However, nodes in its left subtree are smaller than $root.val$ and may fall within $[low, high]$.
    - Action: Bypass $root$ and return the trimmed left subtree:
      $$
      \text{trim}(root) \leftarrow \text{trim}(root.left)
      $$
  - **Case 2: $root.val < low$ (Undershoot Pruning):**
    - All nodes in the left subtree have values strictly less than $root.val$:
      $$
      \forall u \in \text{left}(root): \quad u.val < root.val < low
      $$
    - The current node and its **entire left subtree** are invalid and must be discarded.
    - Action: Bypass $root$ and return the trimmed right subtree:
      $$
      \text{trim}(root) \leftarrow \text{trim}(root.right)
      $$
  - **Case 3: $low \le root.val \le high$ (Admissible Node):**
    - The current node is within bounds and must be retained.
    - Recursively trim its left child: $root.left \leftarrow \text{trim}(root.left)$.
    - Recursively trim its right child: $root.right \leftarrow \text{trim}(root.right)$.
    - Return $root$.
- **Step-by-Step Worked Execution Trace on $[3, 0, 4, \text{null}, 2, \text{null}, \text{null}, 1]$:**
  - Range: $[low, high] = [1, 3]$.
  - **Visit Root Node 3:**
    - Value $3 \in [1, 3] \implies \mathbf{Admissible\ (Case\ 3)}$.
    - Node 3 is preserved as the trimmed tree's root.
    - Now recursively trim left child (Node 0) and right child (Node 4).
  - **Trim Right Branch of 3 (Node 4):**
    - Inspect value:
      $$
      4 > high \quad (4 > 3) \implies \mathbf{Case\ 1\ (Overshoot)}
      $$
    - Node 4 is too large. Discard Node 4 and its non-existent right subtree.
    - Delegate to its left child:
      $$
      \text{trim}(4) = \text{trim}(4.left) = \text{trim}(\text{null}) = \mathbf{null}
      $$
    - Rewire right child of 3:
      $$
      3.right \leftarrow \mathbf{null}
      $$
  - **Trim Left Branch of 3 (Node 0):**
    - Inspect value:
      $$
      0 < low \quad (0 < 1) \implies \mathbf{Case\ 2\ (Undershoot)}
      $$
    - Node 0 is too small. Discard Node 0 and its left subtree.
    - Some nodes in its right subtree (values $> 0$) might be valid!
    - Delegate directly to its right child (Node 2):
      $$
      \text{trim}(0) = \text{trim}(0.right) = \text{trim}(\text{Node } 2)
      $$
  - **Trim Node 2 (Subtree under 0):**
    - Inspect value:
      $$
      2 \in [1, 3] \implies \mathbf{Case\ 3\ (Admissible)}
      $$
    - Node 2 is retained.
    - Trim left child of 2 (Node 1):
      - Inspect value: $1 \in [1, 3] \implies \mathbf{Admissible}$.
      - Node 1 has no children $\implies 1.left = \text{null}, 1.right = \text{null}$.
      - Returns Node 1.
    - Trim right child of 2:
      - $2.right$ is null $\implies \text{null}$.
    - Node 2 now has left child Node 1 and right child null.
    - Returns Node 2.
  - **Rewire Left Child of Root 3:**
    - The recursive call $\text{trim}(0)$ returned Node 2.
    - Rewire pointer:
      $$
      3.left \leftarrow \text{Node } 2
      $$
  - **Step 6: Final Trimmed Tree:**
    - Root: Node 3
    - Left of 3: Node 2
    - Left of 2: Node 1
    - Topology:
      ```text
            3
           /
          2
         /
        1
      ```
    - Level-order serialization: `[3, 2, null, 1]`.
    - Return root Node 3.
- **Simple Child Removal ($root = [1, 0, 2], [low, high] = [1, 2]$):**
  - Node 1: valid. Left child 0 is discarded ($0 < 1$). Right child 2 is retained.
  - Trimmed tree: `[1, null, 2]`.
- **Entire Tree Pruned Away ($root = [5, 3, 6], [low, high] = [10, 20]$):**
  - All nodes are $< 10 \implies$ returns `null`.

This instance demonstrates recursive structural pruning on ordered binary search trees, mathematically proves why monotonicity preserves validity during branch bypass splicing, and derives $O(N)$ execution time and $O(H)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a BST and range $[low, high]$:
Trim the tree so that **only values in $[low, high]$ remain**.
Preserve relative BST descendant relationships.

```text
Tree:
        3            [low, high] = [1, 3]
      /   \
     0     4  <-- 4 > 3: Discard 4 and its right subtree!
      \
       2      <-- 0 < 1: Discard 0, promote right child 2!
      /
     1

Result:
      3
     /
    2
   /
  1
```

### The Invariant of the BST Monotonic Split
- If $node.val > high$: neither the node nor its right subtree can ever be valid. Only the left subtree can contain valid elements.
- If $node.val < low$: neither the node nor its left subtree can ever be valid. Only the right subtree can contain valid elements.
- If $low \le node.val \le high$: the node survives, and both children are trimmed recursively.

---

## 2. Conceptual Foundation & Invariants

### 1. The Recursive Trimming Mapping:
$$
\text{trim}(u) = \begin{cases} \text{null} & \text{if } u = \text{null} \\ \text{trim}(u.left) & \text{if } u.val > high \\ \text{trim}(u.right) & \text{if } u.val < low \\ \text{Node}(u.val, \; \text{trim}(u.left), \; \text{trim}(u.right)) & \text{otherwise} \end{cases}
$$

### 2. Relative Order Preservation:
Because we only bypass pruned nodes and never swap child orientations, any surviving node remains a descendant of its original surviving ancestors.

> **Order-Convex BST Restriction Invariant.** The preimage of any interval $[low, high]$ under a binary search tree embedding forms a connected sub-forest whose connected components can be contracted into a single valid BST by removing boundary-violating ancestor paths.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Root 3
- $3 \in [1, 3]$: Keep Node 3.
- Recurse on left (0) and right (4).

---

### Step 2: Right Child 4
- $4 > 3$: Discard 4.
- Return $\text{trim}(4.left) = \text{null}$.
- $3.right \leftarrow \text{null}$.

---

### Step 3: Left Child 0
- $0 < 1$: Discard 0.
- Return $\text{trim}(0.right) = \text{trim}(2)$.

---

### Step 4: Node 2
- $2 \in [1, 3]$: Keep Node 2.
- Left child 1 is in $[1, 3] \implies$ Keep Node 1.
- Return Node 2.

---

### Step 5: Splicing
- $3.left \leftarrow \text{Node } 2$.
- Return Node 3.

---

## 4. Complete Execution Trace

| Node Evaluated | Value | Condition | Action Taken | Subtree Returned | Attached To |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Node 3 | $3$ | $1 \le 3 \le 3$ | Retain Node 3 | Root of result | Output root |
| Node 4 | $4$ | $4 > 3$ | Discard 4 | $\text{trim}(4.left) = \text{null}$ | $3.right$ |
| Node 0 | $0$ | $0 < 1$ | Discard 0 | $\text{trim}(0.right) = \text{Node } 2$ | $3.left$ |
| Node 2 | $2$ | $1 \le 2 \le 3$ | Retain Node 2 | Node 2 (with child 1) | Replaces 0 under 3 |
| Node 1 | $1$ | $1 \le 1 \le 3$ | Retain Node 1 | Node 1 (leaf) | $2.left$ |

---

## 5. Boundary Cases & Failure Modes

- **Root Itself is Pruned ($root = [0], [1, 2]$):** Discards 0, returns `null`.
- **No Pruning Needed ($root = [2, 1, 3], [0, 4]$):** Returns original tree unchanged.
- **Leftmost Branch Trimmed ($low$ cuts off small leaves):** Smoothly clips bottom leaves without affecting upper structure.
- **Deep Skewed Tree ($N = 10^4$):** DFS recursion reaches depth $N$; executes within standard stack bounds.

---

## 6. Traps & Common Anti-Patterns

- **Searching Both Children When Out of Bounds:** If $root.val > high$, searching the right child is completely redundant since all right descendants are strictly greater than $high$. Only the left child can contain valid nodes.
- **Deleting Children Without Splicing:** In languages like C++, remember to free or orphan pruned nodes cleanly without breaking pointers to valid promoted grandchildren.
- **Rebuilding from Values ($O(N \log N)$):** Re-inserting values into a new tree takes extra memory and time. Splicing pointers in-place takes strictly $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Every node in the BST is visited at most once: $\mathcal{O}(N)$.
  - Each visit executes $\mathcal{O}(1)$ pointer operations.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 1$ ms for $N = 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ auxiliary space for the recursion call stack, where $H$ is the tree height ($\mathcal{O}(\log N)$ for balanced trees, $\mathcal{O}(N)$ in the worst-case skewed tree).