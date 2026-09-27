# Guided Example: Insert into a Binary Search Tree

We trace the step-by-step binary search tree leaf-attachment navigation ($root.val > val \implies \text{left}$, $root.val < val \implies \text{right}$), null pointer attachment base condition ($root == \text{null} \implies \text{Node}(val)$), parent-child link reconstruction ($root.left = \dots$ / $root.right = \dots$), BST ordering preservation, and resulting topology synthesis on representative tree insertion events:

- **Input:**
  - Original tree: $root = [4, 2, 7, 1, 3]$
  - Insertion value: $val = 5$
  - Initial tree topology:
    ```text
            4
          /   \
         2     7
        / \
       1   3
    ```
- **Required output:** $[4, 2, 7, 1, 3, 5]$
  - Output tree topology:
    ```text
            4
          /   \
         2     7
        / \   /
       1   3 5
    ```
  - Problem objective:
    - Insert the new value $val = 5$ into the Binary Search Tree such that all BST ordering invariants remain valid.
    - It is guaranteed that $val$ does not already exist in the tree.
    - The canonical, simplest, and universally accepted method is to descend the tree following BST comparison rules until finding an empty null link, where the new node is attached as a **new leaf**.
- **BST Invariant & Leaf-Attachment Recurrence:**
  - **The BST Invariant:**
    - For every node $u$:
      $$
      \text{All values in } u.left < u.val < \text{All values in } u.right
      $$
  - **The Leaf Insertion Rule:**
    - At current node $u$:
      1. If $u == \text{null}$:
         - We have found the unique empty leaf position where $val$ belongs.
         - Allocate and return a new node holding $val$:
           $$
           \text{return } \text{TreeNode}(val)
           $$
      2. If $u.val > val$:
         - The new value is smaller than $u$, so it must be placed into $u$'s left subtree:
           $$
           u.left \leftarrow \text{insert}(u.left, \; val)
           $$
      3. If $u.val < val$:
         - The new value is larger than $u$, so it must be placed into $u$'s right subtree:
           $$
           u.right \leftarrow \text{insert}(u.right, \; val)
           $$
      4. Return the unmodified current node pointer $u$ to preserve the tree structure above.
- **Step-by-Step Worked Execution Trace for $val = 5$:**
  - **Step 1: Inspect Root Node 4:**
    - Current node value: $4$.
    - Compare with new value:
      $$
      4 < 5 \implies \mathbf{New\ Value\ is\ Larger}
      $$
    - The new node belongs in the right subtree of 4.
    - Recurse into right child:
      $$
      4.right \leftarrow \text{insert}(7, \; 5)
      $$
  - **Step 2: Inspect Node 7 (Right Child of 4):**
    - Current node value: $7$.
    - Compare with new value:
      $$
      7 > 5 \implies \mathbf{New\ Value\ is\ Smaller}
      $$
    - The new node belongs in the left subtree of 7.
    - Recurse into left child:
      $$
      7.left \leftarrow \text{insert}(\text{null}, \; 5)
      $$
  - **Step 3: Reach Null Child ($\text{Node } 7.left$ is $\text{null}$):**
    - Current node is $\text{null}$.
    - Instantiate new leaf node:
      $$
      \text{newNode} = \text{TreeNode}(5)
      $$
    - Return $\text{newNode}$ upward to caller.
  - **Step 4: Rewire Pointers on Return:**
    - At Node 7:
      $$
      7.left \leftarrow \text{newNode}(5)
      $$
      Node 7 now points to left child 5. Returns Node 7.
    - At Root 4:
      $$
      4.right \leftarrow \text{Node } 7
      $$
      Returns Root 4.
  - **Step 5: Insertion Complete:**
    - Root 4 returned intact.
    - In-order traversal of final tree:
      $$
      [1, \; 2, \; 3, \; 4, \; \mathbf{5}, \; 7]
      $$
    - The in-order traversal is strictly monotonically increasing, proving BST validity.
- **Empty Tree Insertion Trace ($root = \text{null}, val = 5$):**
  - Root is null $\implies$ returns $\text{TreeNode}(5)$ as the new root of the tree.
- **Insert New Global Minimum ($root = [4, 2, 7], val = 1$):**
  - Path: $4 \to 2 \to 2.left (\text{null})$.
  - Attaches 1 as the left child of 2.
  - In-order: $[1, 2, 4, 7]$.

This instance demonstrates binary search tree leaf placement and structural pointer preservation, mathematically proves why in-order monotonicity is preserved under empty-slot leaf attachment, and derives $O(H)$ runtime and $O(1)$ iterative / $O(H)$ recursive space bounds.

---

## 1. Instance & Teaching Goal

Given a BST and a new value $val$:
Insert $val$ into the tree while maintaining the **Binary Search Tree invariant**.
Return the root of the modified tree.

```text
Original BST:
        4
      /   \
     2     7   <- Target to insert: 5
    / \
   1   3

Search descent:
  4 < 5 -> go RIGHT to 7
  7 > 5 -> go LEFT of 7 (currently null)

Attach 5 at 7.left:
        4
      /   \
     2     7
    / \   /
   1   3 5

Result: [ 4, 2, 7, 1, 3, 5 ]
```

### The Invariant of Leaf-Level Insertion
- A new key can always be inserted as a **new leaf** at the exact null pointer where a standard search for that key would terminate.
- Re-assigning child pointers `root.left = insert(...)` seamlessly links the new leaf while returning the root unmodified.

---

## 2. Conceptual Foundation & Invariants

### 1. Pointer Reconstruction Recurrence:
$$
\text{insert}(u, val) = \begin{cases} \text{TreeNode}(val) & \text{if } u = \text{null} \\ u.left = \text{insert}(u.left, val) & \text{if } u.val > val \\ u.right = \text{insert}(u.right, val) & \text{if } u.val < val \end{cases}
$$
Always return $u$ after updating children.

### 2. In-Order Invariance:
Let $I(T)$ be the in-order sequence of tree $T$.
$$
I(T_{new}) = \text{insert\_sorted}(I(T_{old}), \; val)
$$

> **Convex Partition Attachment Invariant.** In any binary search tree, the topological frontier formed by the collection of null pointers decomposes the real line into disjoint open intervals; inserting $x$ into the unique null frontier corresponding to $x$'s interval preserves the global total order without modifying existing internal node keys.

---

## 3. Step-by-Step Worked Execution

We trace $root = [4, 2, 7, 1, 3], val = 5$:

---

### Step 1: Root Node 4
- $4 < 5 \implies$ Recurse on right child: $4.right = \text{insert}(7, 5)$.

---

### Step 2: Node 7
- $7 > 5 \implies$ Recurse on left child: $7.left = \text{insert}(\text{null}, 5)$.

---

### Step 3: Base Case
- Node is $\text{null} \implies$ create new node $\text{Node}(5)$.
- Return $\text{Node}(5)$.

---

### Step 4: Link Rewiring
- $7.left \leftarrow \text{Node}(5)$.
- $4.right \leftarrow \text{Node}(7)$.
- Return Root 4.

---

## 4. Complete Execution Trace

| Recursion Depth | Current Node $u$ | Comparison with $val = 5$ | Action Taken | Returned Node | Pointer Reassigned |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | Root $4$ | $4 < 5$ | Descend Right | Root $4$ | $4.right \leftarrow \text{Node } 7$ |
| $1$ | Node $7$ | $7 > 5$ | Descend Left | Node $7$ | $7.left \leftarrow \text{Node } 5$ |
| **$2$** | **`null`** | — | **Create Leaf** | **`Node(5)`** | — |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = \text{null}$):** Returns new single-node tree `TreeNode(val)`.
- **Insert New Minimum ($val < \min$):** Descends all the way down left branches, attaches to leftmost leaf.
- **Insert New Maximum ($val > \max$):** Descends all the way down right branches, attaches to rightmost leaf.
- **Deep Skewed Tree ($N = 10^4$):** Iterative implementation avoids recursion stack limit.

---

## 6. Traps & Common Anti-Patterns

- **Rotations / Rebalancing:** The problem does **not** ask for a self-balancing AVL or Red-Black tree. Rebalancing is completely unnecessary and adds pointless complexity.
- **Losing Parent Connection:** Forgetting to assign `root.left = ...` or `root.right = ...` leaves the new node unattached to the tree.
- **Handling Duplicate Values:** Problem guarantees $val$ does not exist in the original tree.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Traverses a single path from root to leaf: at most tree height $H$.
  - Balanced Tree: $\mathcal{O}(\log N)$.
  - Skewed Tree: $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(H)$. Completes in $< 0.1$ ms for $N = 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ auxiliary space for recursive stack, or $\mathcal{O}(1)$ space using an iterative pointer traversal.