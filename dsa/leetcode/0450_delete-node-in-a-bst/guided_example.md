# Guided Example: Delete Node in a BST

We trace the step-by-step binary search descent, node removal case dispatch (0 children, 1 child, 2 children), in-order successor splicing, and subtree reattachment on representative binary search trees:

- **Input:**
  - Binary search tree:
    ```text
          5
         / \
        3   6
       / \   \
      2   4   7
    ```
  - `key = 3`
- **Required output:** Valid updated BST with node 3 excised:
  ```text
        5
       / \
      4   6
     /     \
    2       7
  ```
- **Execution trace:**
  - Start at root: $root.val = 5$. Compare with target $key = 3$:
    - $3 < 5 \implies$ Recurse into left subtree: $5.left = \text{deleteNode}(3, 3)$.
  - At target node: $root.val = 3 == key$:
    - Analyze child topology:
      - Left child exists: Node $2$
      - Right child exists: Node $4$
      - Node has **two children** (Case 3).
    - Locate in-order successor:
      - Step into right subtree: Node $4$.
      - Find the minimum (leftmost) node in the right subtree: Node $4$ has no left child, so Node $4$ is the in-order successor.
    - Splice left subtree under the in-order successor:
      - Attach original left child ($2$) to the left pointer of Node $4$:
        $$
        4.left \leftarrow 2
        $$
    - Replace node $3$ with its right child $4$:
      - Return Node $4$ up to the caller.
  - Reattach at root:
    - Root $5$'s left pointer is updated: $5.left \leftarrow 4$.
  - BST order property is fully preserved:
    - Left of 5 contains $\{4, 2\}$, where $2 < 4 < 5$.
    - Right of 5 contains $\{6, 7\}$, where $5 < 6 < 7$.
  - Return updated root: Node $5$.
- **Deleting a Leaf Node:** Node has no children $\implies$ simply return `None` to parent pointer.
- **Deleting Node with One Child:** Return the non-empty child directly to the parent pointer.
- **Key Not Found:** Search reaches `None` $\implies$ returns original tree unchanged.

This instance demonstrates in-place pointer surgery in binary search trees, mathematically proves why splicing under the in-order successor preserves the BST invariant ($left < root < right$), and derives $O(H)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a Binary Search Tree and a value $key = 3$:
Delete the node with value $key$ from the BST, returning the updated root.
The binary search tree invariant must be preserved after deletion:
For every node $u$, all values in $u$'s left subtree are strictly less than $u.val$, and all values in $u$'s right subtree are strictly greater than $u.val$.

```text
Original BST (Delete 3):              Resulting Valid BST:
          5                                     5
         / \                                   / \
       (3)  6                                 4   6
       / \   \                               /     \
      2   4   7                             2       7
```

### The Three Structural Cases of Node Deletion
1. **Case 1 (Leaf Node):** The target node has no children (`left == None` and `right == None`). Simply excise it by returning `None` to its parent.
2. **Case 2 (Single Child):** The target node has exactly one child (either `left == None` or `right == None`). Bypass the node by returning its sole child directly to its parent.
3. **Case 3 (Two Children):** The target node has both left and right children. We cannot simply promote one child without properly rehoming the other subtree.
   - **The In-Order Successor Property:** Every node in the target's left subtree is strictly smaller than every node in the target's right subtree.
   - Specifically, every node in $root.left$ is strictly smaller than the **minimum (leftmost) element** of $root.right$.
   - Therefore, we can safely attach the entire left subtree to the `left` pointer of the leftmost node in the right subtree!

---

## 2. Conceptual Foundation & Invariants

### 1. Binary Search Tree Traversal:
- If $key < root.val$: The target node resides strictly in the left subtree.
  $$
  root.left \leftarrow \text{deleteNode}(root.left, \; key)
  $$
- If $key > root.val$: The target node resides strictly in the right subtree.
  $$
  root.right \leftarrow \text{deleteNode}(root.right, \; key)
  $$
- If $key == root.val$: The current node is the target to be deleted.

### 2. Two-Children Splicing Logic:
When $root.val == key$ and both $root.left$ and $root.right$ are non-null:
1. Traverse to the in-order successor (the leftmost leaf of $root.right$):
   $$
   succ \leftarrow root.right
   $$
   $$
   \text{While } succ.left \ne \text{None}: \quad succ \leftarrow succ.left
   $$
2. Graft the target's left subtree onto the successor:
   $$
   succ.left \leftarrow root.left
   $$
3. Promote $root.right$ to replace $root$:
   $$
   \text{Return } root.right
   $$

> **BST Preservation Invariant.** Because all keys in $root.left$ are strictly smaller than $root.val$, and $succ$ is the smallest key in $root.right$ ($root.val < succ.val$), every key in $root.left$ is strictly smaller than $succ.val$, maintaining the BST invariant when attached to $succ.left$.

---

## 3. Step-by-Step Worked Execution

We trace $root = [5, 3, 6, 2, 4, \text{null}, 7]$ with $key = 3$:

---

### Step 1: Call Frame 1 at Root Node 5
- Compare $key = 3$ with $root.val = 5$:
  $$
  3 < 5
  $$
- Recurse left:
  $$
  5.left \leftarrow \text{deleteNode}(5.left, \; 3)
  $$

---

### Step 2: Call Frame 2 at Target Node 3
- Compare $key = 3$ with $root.val = 3$:
  $$
  3 == 3 \quad (\text{Target Located!})
  $$
- Check children:
  - $root.left = \text{Node}(2)$ (Exists)
  - $root.right = \text{Node}(4)$ (Exists)
  - Both children exist $\implies$ Trigger Two-Children Splicing.

---

### Step 3: Successor Discovery & Splicing
- Inspect right child: $succ = root.right = \text{Node}(4)$.
- Find leftmost node of $succ$:
  - Node $4$ has `left == None`.
  - Therefore, $succ = \text{Node}(4)$ is the in-order successor.
- Wire left subtree to successor:
  $$
  4.left \leftarrow root.left \implies 4.left \leftarrow \text{Node}(2)
  $$
- Promote right subtree:
  - The new root of this subsegment is Node $4$.
  - Return Node $4$ to Frame 1.

---

### Step 4: Reattachment at Root Node 5
- Frame 1 receives Node $4$:
  $$
  5.left \leftarrow \text{Node}(4)
  $$
- Root Node 5 remains unchanged.
- Return Node 5.

---

### Final Reconstructed Tree:
Root 5:
- Left child: 4 (with left child 2).
- Right child: 6 (with right child 7).
BST valid throughout.

---

## 4. Complete Execution Trace

| Call Depth | Inspected Node | Value | Comparison with $key = 3$ | Branch Chosen | Splicing Action | Return Value to Parent |
|:---:|:---:|:---:|:---:|:---|:---|:---:|
| **1** | Root | $5$ | $3 < 5$ | Left child | Awaits return for $5.left$ | Node $5$ |
| **2** | Left Child | $3$ | $3 == 3$ | **Target Found** | Find successor $4$<br>Attach $4.left \leftarrow 2$ | **Node $4$** |
| **1** | Root | $5$ | — | Reconnect | $5.left \leftarrow 4$ | **Node $5$** |

---

## 5. Boundary Cases & Failure Modes

- **Key is at Root ($key = 5$):** The root itself has two children (3 and 6). Finds successor 6 (or leftmost in 6), splices 3 under it, and returns 6 as the new global root.
- **Key Does Not Exist ($key = 10$):** Searches through $5 \to 6 \to 7 \to \text{None}$. Returns `None` at the base case, leaving all parent pointers identical.
- **Deleting Node with Only Left Child ($3$ has child $2$, right is `None`):** Condition `if root.right is None: return root.left` triggers immediately, bypassing node 3 in $O(1)$ operations.
- **Empty Tree ($root = \text{None}$):** Returns `None` immediately.

---

## 6. Traps & Common Anti-Patterns

- **Swapping Values Instead of Rewiring Pointers:** Copying values between nodes can be slow or problematic in real-world systems where nodes contain heavy data payloads or external pointers. Pure pointer surgery preserves node identities.
- **Tree Deepening from Successor Splicing:** Splicing the left subtree under the leftmost leaf of the right subtree can increase the height of that specific branch. An alternative balanced approach swaps with the immediate successor and deletes that leaf, maintaining tree balance.
- **Losing References to Unprocessed Subtrees:** Overwriting `root.right` before attaching `root.left` to the successor orphans the left subtree. Splicing `succ.left = root.left` *before* returning `root.right` preserves list connectivity.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding the node takes $O(H)$ time, where $H$ is tree height.
  - Finding the in-order successor in the right subtree takes at most $O(H)$ steps.
  - Total Time: $\mathcal{O}(H)$. For a balanced tree, $H = O(\log N)$; for a degenerate skewed tree, $H = O(N)$. For $N = 10^4$, executes in under 2 ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ for the recursion call stack.
  - Zero auxiliary heap nodes are allocated.