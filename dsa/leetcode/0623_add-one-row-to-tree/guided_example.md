# Guided Example: Add One Row to Tree

We trace the step-by-step depth-controlled binary tree traversal ($d$), parent-level interception at target predecessor depth ($d == depth - 1$), bilateral synthetic child insertion (`left = Node(val, old_left, null)` and `right = Node(val, null, old_right)`), root-level insertion special case ($depth == 1 \implies \text{Node}(val, root, null)$), and tree rewiring on representative hierarchical structures:

- **Input:**
  - $root = [4, 2, 6, 3, 1, 5]$
  - $val = 1, \quad depth = 2$
  - Initial tree structure:
    ```text
          4         (Depth 1)
        /   \
       2     6      (Depth 2)
      / \   /
     3   1 5        (Depth 3)
    ```
- **Required output:**
  ```text
          4         (Depth 1)
        /   \
       1     1      (Depth 2 - New Row Inserted!)
      /       \
     2         6    (Depth 3 - Shifted)
    / \       /
   3   1     5      (Depth 4 - Shifted)
  ```
  - Serialization array: `[4, 1, 1, 2, null, null, 6, 3, 1, 5]`
  - Insertion specification:
    1. If $depth > 1$: Traverse to every non-null node $u$ at depth $depth - 1$.
       - Create a new left node with value $val$:
         $$
         u.left \leftarrow \text{Node}(val, \; \text{left}=u.left, \; \text{right}=\text{null})
         $$
       - Create a new right node with value $val$:
         $$
         u.right \leftarrow \text{Node}(val, \; \text{left}=\text{null}, \; \text{right}=u.right)
         $$
    2. If $depth == 1$:
       - Create a new root with value $val$, attach original $root$ as its **left child**, and set right child to `null`:
         $$
         new\_root = \text{Node}(val, \; \text{left}=root, \; \text{right}=\text{null})
         $$
- **Recursive Splitting & In-Place Splicing Mechanics:**
  - Notice the asymmetric subtree handoff:
    - The new **left** node inherits the original left subtree as its **left** child (its right child is `null`).
    - The new **right** node inherits the original right subtree as its **right** child (its left child is `null`).
  - This preserves the relative directional ordering of all existing descendant branches while inserting a clean horizontal row at depth $depth$.
- **Step-by-Step Worked Execution Trace:**
  - Input: $root$ (Node 4), $val = 1, depth = 2$.
  - Check root-level condition: $depth = 2 > 1 \implies$ Proceed with traversal from depth $d = 1$.
  - Target insertion parent level:
    $$
    d_{target} = depth - 1 = 2 - 1 = \mathbf{1}
    $$
  - **Examine Node 4 (Current depth $d = 1$):**
    - Condition $d == d_{target}$ ($1 == 1$) evaluates to $\mathbf{True!}$
    - Node 4 is a target parent node.
    - **Step 1: Save Original Children:**
      $$
      old\_left = \text{Node 2}
      $$
      $$
      old\_right = \text{Node 6}
      $$
    - **Step 2: Splice Left Intermediate Node:**
      - Create $new\_L = \text{Node}(1)$.
      - Attach original left subtree: $new\_L.left \leftarrow old\_left$ (Node 2).
      - Set right child: $new\_L.right \leftarrow \text{null}$.
      - Re-link parent: $root.left \leftarrow new\_L$.
    - **Step 3: Splice Right Intermediate Node:**
      - Create $new\_R = \text{Node}(1)$.
      - Set left child: $new\_R.left \leftarrow \text{null}$.
      - Attach original right subtree: $new\_R.right \leftarrow old\_right$ (Node 6).
      - Re-link parent: $root.right \leftarrow new\_R$.
    - **Step 4: Prune Further Traversal:**
      - Because the row has been successfully spliced at depth 2, recursion halts here and does not visit deeper levels!
  - **Inspection of Resulting Tree Topology:**
    - Root (Depth 1): Node 4.
    - Depth 2:
      - Left child of 4 is new Node 1.
      - Right child of 4 is new Node 1.
    - Depth 3:
      - Left child of left Node 1 is original Node 2.
      - Right child of right Node 1 is original Node 6.
    - Depth 4:
      - Node 2's children (3 and 1) remain untouched.
      - Node 6's child (5) remains untouched.
  - Return $root$ (Node 4).
- **Depth 1 Special Case ($root = [4, 2, 6], val = 1, depth = 1$):**
  - Target depth is 1 (replacing root).
  - Create new node: $\text{Node}(1, \; \text{left}=\text{Node 4}, \; \text{right}=\text{null})$.
  - Returns new root: Node 1 $\implies [1, 4, null, 2, 6]$.
- **Insertion Below Leaf Nodes:**
  - If a parent node at $depth - 1$ has no children ($u.left = \text{null}, u.right = \text{null}$):
  - Both new intermediate nodes are still created with value $val$, and both inherit `null` as their respective child subtrees.

This instance demonstrates recursive depth-bounded graph surgery and structural grafting, mathematically proves why intercepting traversal at depth $d - 1$ performs constant-time local pointer rewiring per level node, and derives $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a binary tree, an integer `val`, and a target `depth`:
Insert an entire horizontal row of nodes with value `val` at depth `depth`.
Original subtrees at `depth` shift down by 1 level.

```text
Original (depth = 2, val = 1):
      4 (depth 1)
     / \
    2   6 (depth 2)

After Insertion at Depth 2:
      4 (depth 1)
     / \
    1   1 (depth 2 - NEW ROW!)
   /     \
  2       6 (depth 3 - original children shifted)
```

### The Invariant of Predecessor Interception
- Attempting to insert nodes from the perspective of the node *at* depth $depth$ is awkward because you must re-link the parent.
- Instead, stop traversal at depth **$depth - 1$** (the parent level).
- The parent directly creates the new intermediate nodes and attaches its old left and right children to them.

---

## 2. Conceptual Foundation & Invariants

### 1. The Rewiring Protocol at Depth $d == depth - 1$:
$$
u.left \leftarrow \text{Node}(val, \; \text{left}=u.left, \; \text{right}=\text{null})
$$
$$
u.right \leftarrow \text{Node}(val, \; \text{left}=\text{null}, \; \text{right}=u.right)
$$

### 2. The $depth = 1$ Base Case:
When inserting at depth 1, the new node becomes the **root of the entire tree**:
$$
new\_root = \text{Node}(val, \; \text{left}=root, \; \text{right}=\text{null})
$$

> **Chiral Attachment Invariant.** The new left child strictly attaches the old left subtree to its own left pointer; the new right child strictly attaches the old right subtree to its own right pointer, preserving in-order projection.

---

## 3. Step-by-Step Worked Execution

We trace $root = [4, 2, 6], val = 1, depth = 2$:

---

### Step 1: Start Traversal
- Root is Node 4 at depth $d = 1$.
- Target parent level is $depth - 1 = 1$.
- Condition $d == 1$ is satisfied!

---

### Step 2: Splice Left Child
- $old\_left = 2$.
- Create new node with value 1.
- Set its left pointer to 2.
- Set Node 4's left pointer to the new node.

---

### Step 3: Splice Right Child
- $old\_right = 6$.
- Create new node with value 1.
- Set its right pointer to 6.
- Set Node 4's right pointer to the new node.

---

### Step 4: Halt Deeper Recursion
- Splicing complete at depth 1; return root.

---

## 4. Complete Execution Trace

| Traversed Node | Current Depth $d$ | Target Parent $depth - 1$? | Spliced Left Child | Spliced Right Child |
|:---:|:---:|:---:|:---:|:---:|
| **Node 4** | $1$ | **Yes ($1 == 1$)** | $\text{Node}(1, 2, \text{null})$ | $\text{Node}(1, \text{null}, 6)$ |
| Node 2 | — | Skipped | — | — |
| Node 6 | — | Skipped | — | — |
| **Result** | — | — | **`[4, 1, 1, 2, null, null, 6]`** | — |

---

## 5. Boundary Cases & Failure Modes

- **$depth = 1$:** Replaces tree root; original root becomes left child of new node.
- **$depth = \text{height} + 1$:** Adds new leaf row beneath current leaves.
- **Node Has Only One Child:** The absent child position still receives a new node with value $val$ and `null` child pointer.
- **Empty Subtrees (`null`):** Handled transparently by pointer assignment.

---

## 6. Traps & Common Anti-Patterns

- **Missing the $depth = 1$ Special Case:** At $depth = 1$, there is no parent at depth 0. Forgetting `if depth == 1: return TreeNode(val, root)` fails this common test case.
- **Cross-Linking Children:** Attaching the old left child to the new node's right pointer inverts the binary search property and violates problem rules.
- **Continuing Traversal After Splicing:** Once nodes are spliced at $d == depth - 1$, continuing DFS will traverse into the newly created nodes and corrupt deeper levels. Return immediately.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Traversal visits only nodes down to depth $depth - 1$.
  - At most $\mathcal{O}(N)$ nodes visited in the worst case.
  - Rewiring pointers takes $\mathcal{O}(1)$ time per target node.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 3$ ms for $N \le 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ call stack depth proportional to tree height ($H \le N$).