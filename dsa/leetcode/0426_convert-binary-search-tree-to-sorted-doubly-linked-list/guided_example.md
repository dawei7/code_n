# Guided Example: Convert Binary Search Tree to Sorted Doubly Linked List

We trace the step-by-step inorder traversal linear sequencing, in-place pointer stitching (`left` $\to$ predecessor, `right` $\to$ successor), first-node head preservation, and circular head-to-tail closure on representative binary search tree structures:

- **Input:** $root = [4, 2, 5, 1, 3]$
- **Required output:** Circular doubly linked list: $1 \rightleftharpoons 2 \rightleftharpoons 3 \rightleftharpoons 4 \rightleftharpoons 5 \rightleftharpoons 1$
  - Initial BST hierarchy:
    - Root $4$ has left child $2$ and right child $5$.
    - Node $2$ has left child $1$ and right child $3$.
  - Inorder traversal visits nodes in strictly ascending numerical order:
    - Visit Node $1$: `head` is unassigned $\implies head \leftarrow 1, \; prev \leftarrow 1$
    - Visit Node $2$: Link $prev.right \leftarrow 2, \; 2.left \leftarrow prev \implies 1 \rightleftharpoons 2$, update $prev \leftarrow 2$
    - Visit Node $3$: Link $2.right \leftarrow 3, \; 3.left \leftarrow 2 \implies 1 \rightleftharpoons 2 \rightleftharpoons 3$, update $prev \leftarrow 3$
    - Visit Node $4$: Link $3.right \leftarrow 4, \; 4.left \leftarrow 3 \implies 1 \rightleftharpoons 2 \rightleftharpoons 3 \rightleftharpoons 4$, update $prev \leftarrow 4$
    - Visit Node $5$: Link $4.right \leftarrow 5, \; 5.left \leftarrow 4 \implies 1 \rightleftharpoons 2 \rightleftharpoons 3 \rightleftharpoons 4 \rightleftharpoons 5$, update $prev \leftarrow 5$
  - Traversal completes:
    - First node: $head = 1$, Last node: $prev = 5$.
  - Circular ring closure:
    - Link $prev.right \leftarrow head$ ($5.right \leftarrow 1$)
    - Link $head.left \leftarrow prev$ ($1.left \leftarrow 5$)
  - Result: $1 \rightleftharpoons 2 \rightleftharpoons 3 \rightleftharpoons 4 \rightleftharpoons 5 \rightleftharpoons 1$. Return $head = 1$.
- **Single Node Instance:** $root = [7] \implies 7.left \leftarrow 7, \; 7.right \leftarrow 7 \implies 7 \rightleftharpoons 7$
- **Empty Tree Instance:** $root = [] \implies \text{None}$

This instance demonstrates in-place binary tree pointer rewiring without node reallocation, mathematically proves why inorder traversal guarantees sorted order, and derives $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary search tree $root = [4, 2, 5, 1, 3]$:
Convert the BST into a **sorted circular doubly linked list** in-place:
- The `left` pointer must act as the **predecessor** pointer.
- The `right` pointer must act as the **successor** pointer.
- The list must be **circular**: the `left` pointer of the smallest node (`head`) points to the largest node (`tail`), and the `right` pointer of the largest node points to the smallest node.

```text
Input Binary Search Tree:
        4
       / \
      2   5
     / \
    1   3

Inorder Sequence: 1 -> 2 -> 3 -> 4 -> 5

Output Circular Doubly Linked List:
  +---------------------------------------+
  |                                       |
  v                                       |
( 1 ) <===> ( 2 ) <===> ( 3 ) <===> ( 4 ) <===> ( 5 )
  |                                       ^
  |                                       |
  +---------------------------------------+
```

### The In-Place Transformation Invariant
Because we must transform the tree in-place without allocating new list nodes:
- We reuse the tree nodes themselves.
- The binary search tree property guarantees that an **inorder traversal** (Left $\to$ Root $\to$ Right) visits every node in strictly non-decreasing sorted order.
- As each node is visited, we rewire its `left` pointer to point to the previously visited node (`prev`), and rewire `prev.right` to point to the current node.

---

## 2. Conceptual Foundation & Invariants

### 1. The Global State Pointers:
- `head`: Points to the absolute first node visited during inorder traversal (the minimum value node in the BST).
- `prev`: Points to the most recently processed node in the inorder stream.

### 2. The Inorder Visitation Step at `curr`:
1. Recursively traverse left subtree: `dfs(curr.left)`.
2. Stitch links with `prev`:
   - If `prev` is `None`: `curr` is the very first node in the sorted sequence. Set `head = curr`.
   - If `prev` is not `None`:
     $$
     prev.right \leftarrow curr, \quad curr.left \leftarrow prev
     $$
   - Update predecessor pointer:
     $$
     prev \leftarrow curr
     $$
3. Recursively traverse right subtree: `dfs(curr.right)`.

### 3. Circular Ring Stitching:
After the DFS completes across the entire tree:
- `head` points to the smallest element.
- `prev` points to the largest element (the last node visited).
- Close the circular loop:
  $$
  prev.right \leftarrow head, \quad head.left \leftarrow prev
  $$

> **Invariant.** During the inorder walk, the sequence of nodes from `head` to `prev` forms a valid doubly linked list of the sorted prefix visited so far.

---

## 3. Step-by-Step Worked Execution

We trace $root = [4, 2, 5, 1, 3]$:
Initialize `head = None, prev = None`. Call `dfs(4)`.

---

### Step 1: Leftward Descent to Node 1
- `dfs(4)` calls `dfs(2)`.
- `dfs(2)` calls `dfs(1)`.
- `dfs(1)` calls `dfs(1.left)` (None $\implies$ returns).
- **Process Node 1:**
  - `prev` is `None` $\implies$ assign `head = 1`.
  - Update `prev = 1`.
- `dfs(1)` calls `dfs(1.right)` (None $\implies$ returns).
- Frame for Node 1 finishes. Return to Node 2.

---

### Step 2: Process Node 2
- **Process Node 2:**
  - `prev` is Node 1.
  - Wire links:
    $$
    1.right \leftarrow 2, \quad 2.left \leftarrow 1
    $$
  - Sublist: $1 \rightleftharpoons 2$.
  - Update `prev = 2`.
- `dfs(2)` calls `dfs(2.right)` $\to$ Node 3.

---

### Step 3: Process Node 3
- `dfs(3.left)` returns None.
- **Process Node 3:**
  - `prev` is Node 2.
  - Wire links:
    $$
    2.right \leftarrow 3, \quad 3.left \leftarrow 2
    $$
  - Sublist: $1 \rightleftharpoons 2 \rightleftharpoons 3$.
  - Update `prev = 3`.
- `dfs(3.right)` returns None.
- Frame for Node 2 finishes. Return to Root Node 4.

---

### Step 4: Process Root Node 4
- **Process Node 4:**
  - `prev` is Node 3.
  - Wire links:
    $$
    3.right \leftarrow 4, \quad 4.left \leftarrow 3
    $$
  - Sublist: $1 \rightleftharpoons 2 \rightleftharpoons 3 \rightleftharpoons 4$.
  - Update `prev = 4`.
- `dfs(4)` calls `dfs(4.right)` $\to$ Node 5.

---

### Step 5: Process Node 5
- `dfs(5.left)` returns None.
- **Process Node 5:**
  - `prev` is Node 4.
  - Wire links:
    $$
    4.right \leftarrow 5, \quad 5.left \leftarrow 4
    $$
  - Sublist: $1 \rightleftharpoons 2 \rightleftharpoons 3 \rightleftharpoons 4 \rightleftharpoons 5$.
  - Update `prev = 5`.
- `dfs(5.right)` returns None.
- Entire traversal finishes!

---

### Step 6: Close the Circular Ring
- `head = 1`, `prev = 5`.
- Establish circular boundary links:
  $$
  5.right \leftarrow 1, \quad 1.left \leftarrow 5
  $$
- Return `head = 1`.

---

## 4. Complete Execution Trace

| Step | Visited Node | `prev` Before Step | Action Taken | Sublist Formed | `prev` After Step | `head` Reference |
|:---:|:---:|:---:|:---|:---|:---:|:---:|
| **Init** | — | `None` | Traversal begins | Empty | `None` | `None` |
| **1** | **$1$** | `None` | First node: assign `head` | $(1)$ | **$1$** | **$1$** |
| **2** | **$2$** | $1$ | Stitch $1 \rightleftharpoons 2$ | $1 \rightleftharpoons 2$ | **$2$** | $1$ |
| **3** | **$3$** | $2$ | Stitch $2 \rightleftharpoons 3$ | $1 \rightleftharpoons 2 \rightleftharpoons 3$ | **$3$** | $1$ |
| **4** | **$4$** | $3$ | Stitch $3 \rightleftharpoons 4$ | $1 \rightleftharpoons 2 \rightleftharpoons 3 \rightleftharpoons 4$ | **$4$** | $1$ |
| **5** | **$5$** | $4$ | Stitch $4 \rightleftharpoons 5$ | $1 \rightleftharpoons 2 \rightleftharpoons 3 \rightleftharpoons 4 \rightleftharpoons 5$ | **$5$** | $1$ |
| **Final** | — | $5$ | Stitch $5.right \leftarrow 1, \; 1.left \leftarrow 5$ | **Circular: $1 \rightleftharpoons \dots \rightleftharpoons 5 \rightleftharpoons 1$** | $5$ | **$1$** |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = \text{None}$):** Returns `None` immediately without null pointer exceptions.
- **Single Node Tree ($root = [7]$):** `head = 7, prev = 7`. Stitching $7.right \leftarrow 7, 7.left \leftarrow 7$ forms a valid 1-node circular loop pointing to itself.
- **Left-Skewed Tree ($3 \to 2 \to 1$):** Recursion descends to bottom leaf 1 first. Correctly chains $1 \rightleftharpoons 2 \rightleftharpoons 3 \rightleftharpoons 1$.
- **Right-Skewed Tree ($1 \to 2 \to 3$):** Traversal visits root 1, stitches 2, stitches 3, and loops $3 \leftrightarrow 1$.

---

## 6. Traps & Common Anti-Patterns

- **Overwriting Subtree Pointers Before Traversing Them:** If a node's `right` pointer is modified *before* recursing into its right child, the reference to the right subtree is lost. Calling `dfs(curr.left)` first, then stitching `curr`, and only then calling `dfs(curr.right)` ensures pointers are safely modified only after their original references are no longer needed.
- **Forgetting Circular Closure:** Omitting $prev.right = head$ and $head.left = prev$ leaves the list open-ended (linear doubly linked list instead of circular).
- **Allocating Auxiliary Nodes:** Creating new `Node` objects wastes memory and violates the strict in-place pointer transformation requirement.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard inorder DFS visits each of the $N$ nodes exactly once.
  - Pointer rewiring at each node takes $O(1)$ time.
  - Circular ring closure takes $O(1)$ time.
  - Total Time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ where $H$ is the height of the binary search tree, representing the recursion call stack depth.
  - For balanced trees, $H = O(\log N)$; for degenerate skewed trees, $H = O(N)$.
  - No auxiliary heap memory is allocated.