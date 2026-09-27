# Guided Example: Minimum Distance Between BST Nodes

We trace the step-by-step Binary Search Tree (BST) in-order traversal projection ($Left \to Root \to Right$), strictly monotonic ascending sequence generation ($v_1 < v_2 < \dots < v_n$), adjacent predecessor difference tracking ($root.val - pre$), running minimum distance convergence ($\min(ans, \Delta)$), and global minimum gap extraction on representative hierarchical search trees:

- **Input:** $root = [4, 2, 6, 1, 3]$
- **Required output:** `1`
  - BST ordering & minimum gap criteria:
    - In a binary search tree, every node's value is strictly greater than all values in its left subtree, and strictly less than all values in its right subtree.
    - Objective: Find the **minimum absolute difference** between the values of any two distinct nodes:
      $$
      ans = \min_{u \ne v} |val(u) - val(v)|
      $$
    - For $[4, 2, 6, 1, 3]$:
      - The values present in the tree are $\{1, 2, 3, 4, 6\}$.
      - Pairwise differences:
        - $|2 - 1| = 1$
        - $|3 - 2| = 1$
        - $|4 - 3| = 1$
        - $|6 - 4| = 2$
      - Minimum difference across the entire tree is **1**.
- **In-Order Monotonicity & Adjacent Gap Invariant:**
  - **The Sorted Sequence Property:**
    - A symmetric in-order depth-first traversal ($L \to Root \to R$) visits the nodes of a BST in **strictly non-decreasing sorted order**:
      $$
      \text{InOrder}(root) = [v_1, \; v_2, \; v_3, \; \dots, \; v_n] \quad \text{where } v_1 < v_2 < \dots < v_n
      $$
  - **Adjacent Pair Optimality:**
    - On a linearly ordered 1D array of numbers $v_1 < v_2 < \dots < v_n$, the minimum distance between ANY pair $(v_i, v_j)$ with $i < j$ is guaranteed to be achieved by some **immediately adjacent pair**:
      $$
      \min_{i < j} (v_j - v_i) \equiv \min_{1 \le k < n} (v_{k + 1} - v_k)
      $$
      *(Because for any $j > i + 1$, $v_j - v_i = (v_j - v_{j-1}) + \dots + (v_{i+1} - v_i) \ge v_{i+1} - v_i$)*.
  - **Online State Maintenance ($pre, ans$):**
    - Maintain two scalar variables throughout the recursive traversal:
      - $pre$: The value of the node visited immediately prior in in-order sequence (initialized to $-\infty$).
      - $ans$: The running minimum adjacent difference (initialized to $\infty$).
    - At each visited node:
      $$
      ans \leftarrow \min(ans, \; root.val - pre)
      $$
      $$
      pre \leftarrow root.val
      $$
    - Eliminates the need to collect or store the full array of values!
- **Step-by-Step Worked Execution Trace on $root = [4, 2, 6, 1, 3]$:**
  - Tree topology:
    - Root: 4
    - Left child: 2 (with children 1, 3)
    - Right child: 6
  - Initialize: $pre = -\infty, ans = \infty$.
  - **Step 1: Traverse to Leftmost Leaf (Node 1):**
    - From 4, go left to 2, go left to 1.
    - Node 1 has no left child. Process Node 1 ($val = 1$):
      - Distance from initial state: $1 - (-\infty) = \infty$.
      - Update predecessor: $pre \leftarrow \mathbf{1}$.
      - No right child. Return to Node 2.
  - **Step 2: Process Node 2 ($val = 2$):**
    - Compute adjacent gap:
      $$
      \Delta = root.val - pre = 2 - 1 = \mathbf{1}
      $$
    - Update running minimum:
      $$
      ans \leftarrow \min(\infty, 1) = \mathbf{1}
      $$
    - Update predecessor: $pre \leftarrow \mathbf{2}$.
    - Traverse right child: Node 3.
  - **Step 3: Process Node 3 ($val = 3$):**
    - Node 3 has no left child.
    - Compute adjacent gap:
      $$
      \Delta = 3 - 2 = \mathbf{1}
      $$
    - Update running minimum:
      $$
      ans \leftarrow \min(1, 1) = \mathbf{1}
      $$
    - Update predecessor: $pre \leftarrow \mathbf{3}$.
    - Left subtree of root 4 is now completely finished! Return to Node 4.
  - **Step 4: Process Root Node 4 ($val = 4$):**
    - Compute adjacent gap:
      $$
      \Delta = 4 - 3 = \mathbf{1}
      $$
    - Update running minimum:
      $$
      ans \leftarrow \min(1, 1) = \mathbf{1}
      $$
    - Update predecessor: $pre \leftarrow \mathbf{4}$.
    - Traverse right child: Node 6.
  - **Step 5: Process Node 6 ($val = 6$):**
    - Node 6 has no left child.
    - Compute adjacent gap:
      $$
      \Delta = 6 - 4 = \mathbf{2}
      $$
    - Update running minimum:
      $$
      ans \leftarrow \min(1, 2) = \mathbf{1}
      $$
    - Update predecessor: $pre \leftarrow \mathbf{6}$.
  - **Traversal Complete:**
    - Final minimum adjacent difference:
      $$
      ans = \mathbf{1}
      $$
- **Deeply Skewed Extremes Trace ($root = [1, 0, 48, \text{null}, \text{null}, 12, 49]$):**
  - In-order traversal sequence: `0, 1, 12, 48, 49`.
  - Gaps:
    - $1 - 0 = 1$
    - $12 - 1 = 11$
    - $48 - 12 = 36$
    - $49 - 48 = 1$
  - Minimum gap: $\min(1, 11, 36, 1) = \mathbf{1}$.
- **Two-Node Minimal Tree ($[4, 2]$):**
  - In-order: `2, 4`.
  - Gap: $4 - 2 = \mathbf{2}$.

This instance demonstrates symmetric binary tree projection into 1D sorted manifolds and telescoping sum gap minimization, mathematically proves why infimum search over pairwise differences reduces strictly to adjacent neighbors in the image of in-order functors, and derives $O(N)$ execution time and $O(H)$ recursion space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a Binary Search Tree (BST):
Find the **minimum difference** between any two different nodes in the tree.

```text
       4
     /   \
    2     6
   / \
  1   3

In-order traversal visits in strictly sorted order:
  [ 1, 2, 3, 4, 6 ]

Adjacent differences:
  2 - 1 = 1
  3 - 2 = 1
  4 - 3 = 1
  6 - 4 = 2

Minimum difference = 1
Result: 1
```

### The Invariant of In-Order Adjacent Differences
- The minimum difference in any set of numbers always occurs between **adjacent elements when sorted**.
- In-order traversal ($L \to Root \to R$) of a BST yields elements in strictly increasing order.
- Tracking the previous node's value $pre$ allows evaluating all adjacent differences online in $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### 1. In-Order Sorted Homomorphism:
$$
\text{InOrder}(root) = (v_1, v_2, \dots, v_n) \quad \text{with } v_k < v_{k + 1}
$$

### 2. Adjacent Telescoping Minimization:
$$
\min_{i \ne j} |v_i - v_j| \equiv \min_{1 \le k < n} (v_{k + 1} - v_k)
$$
$$
ans \leftarrow \min(ans, \; root.val - pre), \quad pre \leftarrow root.val
$$

> **Metric Convexity Invariant.** On the discrete real line with Euclidean metric $d(x, y) = |x - y|$, any non-adjacent pair $x < y < z$ satisfies the strict triangle equality $d(x, z) = d(x, y) + d(y, z) > \min(d(x, y), d(y, z))$, proving that the global metric minimum must be realized on an elementary adjacent interval.

---

## 3. Step-by-Step Worked Execution

We trace $root = [4, 2, 6, 1, 3]$:

---

### Step 1: Traverse Left
- Reach leaf 1 $\implies pre = 1$.

---

### Step 2: Node 2
- $\Delta = 2 - 1 = 1 \implies ans = 1, pre = 2$.

---

### Step 3: Node 3
- $\Delta = 3 - 2 = 1 \implies ans = 1, pre = 3$.

---

### Step 4: Node 4
- $\Delta = 4 - 3 = 1 \implies ans = 1, pre = 4$.

---

### Step 5: Node 6
- $\Delta = 6 - 4 = 2 \implies ans = \min(1, 2) = 1, pre = 6$.

---

### Step 6: Output
$$
\mathbf{1}
$$

---

## 4. Complete Execution Trace

| In-Order Step | Visited Node Value | Previous Node Value $pre$ | Current Difference $val - pre$ | Running Minimum $ans$ |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | $1$ | $-\infty$ | $\infty$ | $\infty$ |
| $2$ | $2$ | $1$ | $1$ | **$1$** |
| $3$ | $3$ | $2$ | $1$ | **$1$** |
| $4$ | $4$ | $3$ | $1$ | **$1$** |
| **$5$** | **$6$** | **$4$** | **$2$** | **`1`** |

---

## 5. Boundary Cases & Failure Modes

- **Minimum Two Nodes ($[1, 3]$):** Evaluates single pair $3 - 1 = 2$.
- **Large Values ($10^5$):** Initial $pre = -\infty$ and $ans = \infty$ prevent false comparisons on the first node.
- **Left-Skewed or Right-Skewed Trees:** In-order traversal visits all nodes in ascending order regardless of tree balance.
- **Repeated Values:** Problem guarantees all node values are distinct in a valid BST.

---

## 6. Traps & Common Anti-Patterns

- **Comparing Only Parent and Child Nodes:** The closest values in a BST are often in different subtrees (e.g. the maximum of the left subtree and the root, or adjacent leaves across sibling subtrees). Comparing only direct parent-child edges misses cross-tree pairs.
- **Collecting All Values into an Array ($O(N)$ Space):** Creating an array of all node values uses unnecessary auxiliary memory. Tracking scalar $pre$ and $ans$ during in-order traversal uses strictly $O(H)$ recursion stack space.
- **Pre-Order or Post-Order Traversal:** Only in-order traversal ($L \to Root \to R$) guarantees sorted values in a BST.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In-order traversal visits each of the $N$ nodes exactly once: $\mathcal{O}(N)$.
  - Constant-time scalar updates at each node: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 100$. Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ for the recursion call stack, where $H \le N$ is tree height ($\mathcal{O}(\log N)$ for balanced trees).