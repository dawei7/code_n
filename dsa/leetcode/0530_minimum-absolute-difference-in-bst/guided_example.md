# Guided Example: Minimum Absolute Difference in BST

We trace the step-by-step BST in-order monotonic property (sorted sequence generation), adjacent element difference minimization theorem ($v_{k} - v_{k-1}$), single-variable previous node tracking ($pre$), running minimum gap updating ($ans = \min(ans, root.val - pre)$), and array-free memory optimization on representative binary search trees:

- **Input:** $root = [4, 2, 6, 1, 3]$
  - Tree structure:
    - Root: $4$
    - Left subtree: $2$ (with children $1, 3$)
    - Right subtree: $6$
- **Required output:** `1`
  - Objective: Find the minimum absolute difference $|u - v|$ between any pair of distinct nodes in the BST.
- **BST In-Order Traversal Invariant:**
  - Standard in-order traversal ($Left \to Root \to Right$) visits nodes in **strictly ascending order**:
    $$
    [1, \; 2, \; 3, \; 4, \; 6]
    $$
  - In any sorted array $A_1 \le A_2 \le \dots \le A_n$, the minimum difference between any pair $(A_i, A_j)$ is guaranteed to occur between **adjacent elements**:
    $$
    \min_{i < j} (A_j - A_i) = \min_{1 \le k < n} (A_{k+1} - A_k)
    $$
  - Therefore, we only need to track the value of the **immediately preceding node** $pre$ during the traversal!
- **Traversal execution trace:**
  - State variables:
    - $pre = -\infty$: value of previously visited node
    - $ans = \infty$: minimum difference seen so far
  - **Node 1 ($val = 1$):**
    - $pre = -\infty \implies$ First node visited, no difference computed.
    - Update previous: $pre \leftarrow 1$.
  - **Node 2 ($val = 2$):**
    - Difference with predecessor:
      $$
      \Delta = root.val - pre = 2 - 1 = \mathbf{1}
      $$
    - Update minimum:
      $$
      ans \leftarrow \min(\infty, 1) = \mathbf{1}
      $$
    - Update previous: $pre \leftarrow 2$.
  - **Node 3 ($val = 3$):**
    - Difference with predecessor:
      $$
      \Delta = 3 - 2 = \mathbf{1}
      $$
    - Update minimum:
      $$
      ans \leftarrow \min(1, 1) = \mathbf{1}
      $$
    - Update previous: $pre \leftarrow 3$.
  - **Node 4 ($val = 4$, Root):**
    - Difference with predecessor:
      $$
      \Delta = 4 - 3 = \mathbf{1}
      $$
    - Update minimum:
      $$
      ans \leftarrow \min(1, 1) = \mathbf{1}
      $$
    - Update previous: $pre \leftarrow 4$.
  - **Node 5 ($val = 6$):**
    - Difference with predecessor:
      $$
      \Delta = 6 - 4 = \mathbf{2}
      $$
    - Update minimum:
      $$
      ans \leftarrow \min(1, 2) = \mathbf{1}
      $$
    - Update previous: $pre \leftarrow 6$.
  - Traversal finishes.
  - Final minimum difference: **`1`**.
- **Wide Subtree Minimum Instance ($root = [1, 0, 48, \text{null}, \text{null}, 12, 49]$):**
  - In-order sequence: $[0, 1, 12, 48, 49]$.
  - Gaps: $1 - 0 = 1, \; 12 - 1 = 11, \; 48 - 12 = 36, \; 49 - 48 = 1$.
  - Minimum gap: $\mathbf{1}$.
- **Two-Node Tree ($root = [1, \text{null}, 5]$):**
  - Only two nodes: gap is $5 - 1 = \mathbf{4}$.

This instance demonstrates in-order projection on binary search trees, mathematically proves why adjacent differences capture global minima in sorted topologies, and derives $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a Binary Search Tree (BST) with distinct values:
Find the **minimum absolute difference** between the values of any two different nodes in the tree.

```text
Tree:
        4
       / \
      2   6
     / \
    1   3

In-Order Traversal (L -> Node -> R):
  1  ->  2  ->  3  ->  4  ->  6

Adjacent Differences:
  2 - 1 = 1  <- Minimum!
  3 - 2 = 1
  4 - 3 = 1
  6 - 4 = 2

Minimum Absolute Difference = 1
```

### Adjacent Difference Invariant
- In an unsorted set of numbers, finding the minimum difference between any two numbers requires sorting first or comparing all $O(N^2)$ pairs.
- In a Binary Search Tree, an **in-order traversal** visits the nodes in strictly sorted order:
  $$
  x_1 < x_2 < x_3 < \dots < x_n
  $$
- In any sorted array:
  $$
  x_j - x_i = (x_j - x_{j-1}) + \dots + (x_{i+1} - x_i) \ge x_{k+1} - x_k
  $$
  for some adjacent pair $(x_k, x_{k+1})$.
- Hence, the global minimum difference is guaranteed to be the difference between two **consecutively visited nodes** in in-order sequence!

---

## 2. Conceptual Foundation & Invariants

### 1. In-Order DFS State Tracking:
Maintain:
- $pre$: the value of the most recently visited node (initialized to $-\infty$).
- $ans$: the minimum difference observed so far (initialized to $\infty$).
At each node during in-order traversal:
1. Recurse left: $dfs(root.left)$.
2. Evaluate difference with previous node:
   $$
   ans \leftarrow \min(ans, \; root.val - pre)
   $$
3. Update previous pointer:
   $$
   pre \leftarrow root.val
   $$
4. Recurse right: $dfs(root.right)$.

> **Sorting Invariant.** Because in-order DFS guarantees $root.val > pre$, the difference $root.val - pre$ is always strictly positive, eliminating the need for absolute value operations.

---

## 3. Step-by-Step Worked Execution

We trace $root = [4, 2, 6, 1, 3]$:

---

### Step 1: Initialize
- $pre = -\infty$
- $ans = \infty$

---

### Step 2: Visit Nodes in In-Order Sequence

1. **Visit Node 1:**
   - First node reached (leftmost).
   - $1 - (-\infty) = \infty$.
   - $pre \leftarrow 1$.

2. **Visit Node 2:**
   - $\Delta = 2 - 1 = \mathbf{1}$.
   - $ans \leftarrow \min(\infty, 1) = \mathbf{1}$.
   - $pre \leftarrow 2$.

3. **Visit Node 3:**
   - $\Delta = 3 - 2 = \mathbf{1}$.
   - $ans \leftarrow \min(1, 1) = \mathbf{1}$.
   - $pre \leftarrow 3$.

4. **Visit Node 4 (Root):**
   - $\Delta = 4 - 3 = \mathbf{1}$.
   - $ans \leftarrow \min(1, 1) = \mathbf{1}$.
   - $pre \leftarrow 4$.

5. **Visit Node 6:**
   - $\Delta = 6 - 4 = \mathbf{2}$.
   - $ans \leftarrow \min(1, 2) = \mathbf{1}$.
   - $pre \leftarrow 6$.

---

### Step 3: Traversal Terminated
Output:
$$
ans = \mathbf{1}
$$

---

## 4. Complete Execution Trace

| In-Order Sequence Step | Node Visited $root.val$ | Preceding Node $pre$ | Difference $root.val - pre$ | New Minimum $ans$ | Next $pre$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init** | — | $-\infty$ | — | $\infty$ | — |
| **Node 1** | $1$ | $-\infty$ | $\infty$ | $\infty$ | $1$ |
| **Node 2** | $2$ | $1$ | **$1$** | **$1$** | $2$ |
| **Node 3** | $3$ | $2$ | **$1$** | **$1$** | $3$ |
| **Node 4** | $4$ | $3$ | **$1$** | **$1$** | $4$ |
| **Node 5** | $6$ | $4$ | $2$ | **$1$** | $6$ |
| **Result** | — | — | — | — | **`1`** |

---

## 5. Boundary Cases & Failure Modes

- **Minimum Two Nodes ($root = [1, null, 3]$):** Sequence $[1, 3] \implies 3 - 1 = \mathbf{2}$.
- **Node Values with Large Values ($10^5$):** Floating-point or integer subtraction does not overflow.
- **Root Value Matches Predecessor Delta:** Whether the closest pair is across parent-child or cousins across different subtrees (e.g. leaf in left subtree and root), in-order sequence captures them consecutively.

---

## 6. Traps & Common Anti-Patterns

- **Storing All Nodes in an Explicit List:** Appending every node value to a Python `list` takes $O(N)$ extra memory. Comparing in-place with a single scalar $pre$ takes $O(1)$ extra space (excluding call stack).
- **Comparing Only Parent and Children:** The closest pair does not necessarily share a direct parent-child edge. For example, in $[1, 0, 48, null, null, 12, 49]$, the closest pair is $48$ and $49$, where $48$ is the parent of $49$, but $0$ and $1$ are parent and left child. In general, a right child's leftmost descendant can be closer to the root than the root's direct children. In-order traversal visits them in exact sorted order regardless of tree shape.
- **Initializing $pre = 0$:** If the tree contains node values $\le 0$, initializing $pre = 0$ creates false differences with the first positive or zero node. $pre$ must be initialized to $-\infty$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard in-order DFS visits each node exactly once.
  - At each node, computing the difference and updating scalars takes $O(1)$ time.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ where $H$ is the tree height to store the recursion call stack ($O(\log N)$ average, $O(N)$ worst-case). Zero additional array allocation.