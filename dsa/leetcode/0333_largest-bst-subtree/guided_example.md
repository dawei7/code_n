# Guided Example: Largest BST Subtree

We trace the step-by-step bottom-up postorder validation, minimum and maximum boundary tuple propagation `(min_val, max_val, size)`, sentinel poison values `(-inf, inf, 0)` for ancestor invalidation, and maximum valid BST subtree size tracking on representative binary trees:

- **Input:** `root = [10, 5, 15, 1, 8, null, 7]`
- **Required output:** $3$
  - Subtree at node $5$ with children $1$ and $8$:
    - Left child $1 < 5$ and right child $8 > 5$
    - Valid BST of size $3$
  - Subtree at node $15$ with right child $7$:
    - $7 < 15$ violates BST right-child ordering condition ($15 < 7$ is false)
    - Subtree at $15$ is invalid
  - Root node $10$:
    - Right subtree is invalid, so tree at $10$ cannot be a BST
  - Maximum valid BST subtree size: $\mathbf{3}$
- **Entire Tree Valid BST:** `root = [2, 1, 3] \implies 3`
- **Single Node Tree:** `root = [1] \implies 1`
- **Empty Tree Base Case:** `root = [] \implies 0`

This instance demonstrates bottom-up postorder tree verification, proves why bubbling up `(-inf, inf, 0)` on violations automatically disqualifies all ancestor subtrees without extra traversal passes, and analyzes $O(N)$ linear time and $O(H)$ recursion stack space bounds.

---

## 1. Instance & Teaching Goal

Given a binary tree:
$$
\text{root} = [10, 5, 15, 1, 8, \text{null}, 7]
$$
Find the number of nodes in the largest subtree that is a valid **Binary Search Tree (BST)**:

```text
            10
          /    \
        5       15
       / \        \
      1   8        7  <-- BST VIOLATION (7 is right child of 15, but 7 < 15!)

Subtrees Analyzed:
- Leaf 1:       Valid BST, size 1
- Leaf 8:       Valid BST, size 1
- Leaf 7:       Valid BST, size 1
- Subtree at 5: Valid BST (1 < 5 < 8), size 3  (LARGEST BST SUBTREE!)
- Subtree at 15:INVALID (15 < 7 is false), size 0
- Root at 10:   INVALID (inherits invalid right subtree), size 0

Optimal BST Size: 3
```

### The BST Subtree Definition
A subtree consists of a node and **all of its descendants**:
- To be a valid BST, every node in its left subtree must be strictly less than the node's value, and every node in its right subtree must be strictly greater than the node's value.
- If we validate top-down, checking each node takes $O(N)$, resulting in an $O(N^2)$ algorithm.
- By validating **bottom-up (postorder)**, each node receives the minimum value, maximum value, and validity of its left and right subtrees in $O(1)$ time, achieving an optimal $O(N)$ runtime!

---

## 2. Conceptual Foundation & Invariants

### 1. Return Contract `dfs(root)`
Each recursive call returns a 3-tuple:
$$
(\text{min\_val}, \; \text{max\_val}, \; \text{size})
$$

### 2. Base Case: `root is None`
When a child pointer is absent:
$$
\text{return } (\infty, \; -\infty, \; 0)
$$
Why $\infty$ for minimum and $-\infty$ for maximum?
- For a left child, its maximum value must satisfy $\text{lmx} < \text{root.val}$. Since $-\infty < \text{root.val}$ is always true, an absent left child never triggers a false violation.
- For a right child, its minimum value must satisfy $\text{root.val} < \text{rmi}$. Since $\text{root.val} < \infty$ is always true, an absent right child never triggers a false violation.

### 3. Validity Condition & Cascading Invalidation:
Let left child return `(lmi, lmx, ln)` and right child return `(rmi, rmx, rn)`:
- **Condition:** $\text{lmx} < \text{root.val} < \text{rmi}$.
- If **True**:
  The subtree rooted at `root` is a valid BST!
  $$
  \text{size} = ln + rn + 1
  $$
  $$
  ans = \max(ans, \; \text{size})
  $$
  $$
  \text{return } (\min(\text{lmi}, \text{root.val}), \; \max(\text{rmx}, \text{root.val}), \; \text{size})
  $$
- If **False**:
  This subtree violates the BST property!
  $$
  \text{return } (-\infty, \; \infty, \; 0)
  $$
  *(Returning $-\infty$ for minimum and $\infty$ for maximum poisons the parent check: any parent evaluating $\text{lmx} < \text{parent.val}$ or $\text{parent.val} < \text{rmi}$ will see $\infty < \text{parent.val}$ or $\text{parent.val} < -\infty$, both of which are false, immediately invalidating all ancestors!).*

> **Invariant.** A node confirms BST validity if and only if both child subtrees are valid BSTs and $\text{root.val}$ strictly separates the left subtree's maximum from the right subtree's minimum.

---

## 3. Step-by-Step Worked Execution

We trace the postorder traversal on `[10, 5, 15, 1, 8, null, 7]`:
Initialized: `ans = 0`.

---

### Step 1: Process Leaves in Left Subtree
1. **Node 1 (Left child of 5):**
   - Left child: `None` $\implies (\infty, -\infty, 0)$
   - Right child: `None` $\implies (\infty, -\infty, 0)$
   - Condition: $-\infty < 1 < \infty$ (**True**).
   - Valid BST! $size = 0 + 0 + 1 = 1$.
   - $ans = \max(0, 1) = \mathbf{1}$.
   - Return: $(\min(\infty, 1), \max(-\infty, 1), 1) = (1, 1, 1)$.
2. **Node 8 (Right child of 5):**
   - Leaf node $\implies$ condition $-\infty < 8 < \infty$ (**True**).
   - Valid BST! $size = 1$.
   - $ans = \max(1, 1) = 1$.
   - Return: $(8, 8, 1)$.

---

### Step 2: Process Node 5
- Left child (Node 1) returns: $(1, 1, 1) \implies \text{lmx} = 1, ln = 1$.
- Right child (Node 8) returns: $(8, 8, 1) \implies \text{rmi} = 8, rn = 1$.
- Check condition:
  $$
  \text{lmx} < 5 < \text{rmi} \iff 1 < 5 < 8 \quad (\mathbf{True!})
  $$
- Valid BST!
  $$
  \text{size} = 1 + 1 + 1 = \mathbf{3}
  $$
  $$
  ans = \max(1, 3) = \mathbf{3}
  $$
- Return tuple:
  $$
  (\min(1, 5), \; \max(8, 5), \; 3) = (1, 8, 3)
  $$

---

### Step 3: Process Right Subtree (Nodes 15 and 7)
1. **Node 7 (Right child of 15):**
   - Leaf node $\implies$ condition $-\infty < 7 < \infty$ (**True**).
   - Valid BST! $size = 1$.
   - $ans = \max(3, 1) = 3$.
   - Return: $(7, 7, 1)$.
2. **Node 15:**
   - Left child: `None` $\implies (\infty, -\infty, 0) \implies \text{lmx} = -\infty$.
   - Right child (Node 7) returns: $(7, 7, 1) \implies \text{rmi} = 7$.
   - Check condition:
     $$
     \text{lmx} < 15 < \text{rmi} \iff -\infty < 15 < 7 \quad (\mathbf{False!}, \; 15 \not< 7)
     $$
   - **BST Violation at Node 15!**
   - Return poisoned invalid tuple:
     $$
     (-\infty, \; \infty, \; 0)
     $$

---

### Step 4: Process Root Node 10
- Left child (Node 5) returns: $(1, 8, 3) \implies \text{lmx} = 8$.
- Right child (Node 15) returns: $(-\infty, \infty, 0) \implies \text{rmi} = -\infty$.
- Check condition:
  $$
  \text{lmx} < 10 < \text{rmi} \iff 8 < 10 < -\infty \quad (\mathbf{False!}, \; 10 \not< -\infty)
  $$
- Root node 10 cannot form a valid BST.
- Return: $(-\infty, \infty, 0)$.

---

### Step 5: Global Result
Maximum valid BST subtree size observed across all recursive calls:
$$
ans = \mathbf{3}
$$

---

## 4. Complete Execution Trace

```text
Tree:
        10
       /  \
      5    15
     / \     \
    1   8     7

dfs(1):  lmx=-inf, rmi=inf -> 1 < 1 < inf  -> VALID -> (1, 1, 1), ans = 1
dfs(8):  lmx=-inf, rmi=inf -> 8 < 8 < inf  -> VALID -> (8, 8, 1), ans = 1
dfs(5):  lmx=1, rmi=8      -> 1 < 5 < 8    -> VALID -> (1, 8, 3), ans = 3 (MAX!)
dfs(7):  leaf              -> VALID        -> (7, 7, 1), ans = 3
dfs(15): lmx=-inf, rmi=7   -> 15 < 7 FALSE -> INVALID -> (-inf, inf, 0)
dfs(10): lmx=8, rmi=-inf   -> 10 < -inf F  -> INVALID -> (-inf, inf, 0)

Result: ans = 3
```

| Traversal Node | Node Value | Left Subtree `(min, max, n)` | Right Subtree `(min, max, n)` | Condition $\text{lmx} < \text{val} < \text{rmi}$ | BST Valid? | Subtree Size | Updated Max `ans` | Return Tuple |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 | $(\infty, -\infty, 0)$ | $(\infty, -\infty, 0)$ | $-\infty < 1 < \infty$ | Yes | 1 | 1 | $(1, 1, 1)$ |
| 8 | 8 | $(\infty, -\infty, 0)$ | $(\infty, -\infty, 0)$ | $-\infty < 8 < \infty$ | Yes | 1 | 1 | $(8, 8, 1)$ |
| **5** | **5** | **$(1, 1, 1)$** | **$(8, 8, 1)$** | **$1 < 5 < 8$** | **Yes** | **3** | **3** | **$(1, 8, 3)$** |
| 7 | 7 | $(\infty, -\infty, 0)$ | $(\infty, -\infty, 0)$ | $-\infty < 7 < \infty$ | Yes | 1 | 3 | $(7, 7, 1)$ |
| 15 | 15 | $(\infty, -\infty, 0)$ | $(7, 7, 1)$ | $-\infty < 15 < 7$ (False) | **No** | 0 | 3 | $(-\infty, \infty, 0)$ |
| 10 | 10 | $(1, 8, 3)$ | $(-\infty, \infty, 0)$ | $8 < 10 < -\infty$ (False) | **No** | 0 | 3 | $(-\infty, \infty, 0)$ |

---

## 5. Algorithmic Correctness

**Soundness.** A binary tree is a BST if and only if for every node, its value is strictly greater than the maximum value in its left subtree and strictly less than the minimum value in its right subtree. Because the recursion executes in postorder (children before parent), the minimum and maximum boundaries accurately reflect the entire left and right subtrees. If a condition is violated, returning $(-\infty, \infty, 0)$ guarantees that no ancestor node can mistakenly qualify as a BST.

**Completeness.** Every node in the binary tree is evaluated as a potential root of a BST subtree. The global maximum size `ans` is updated whenever a valid BST configuration is confirmed. Since all subtrees are visited, the maximum possible BST subtree size is guaranteed to be captured.

---

## 6. Traps This Instance Exposes

- **Local vs Global BST Violations:** Checking only immediate child values (`left.val < root.val < right.val`) fails when a deep descendant violates the ancestor boundary (e.g. a right child's left descendant is smaller than the root). Passing subtree min/max values solves this completely.
- **Top-Down Quadratic Slowness:** Running an independent `isBST` check on each node requires $O(N)$ work per node, totaling $O(N^2)$. Bottom-up postorder validation evaluates each node in $O(1)$ time.
- **Poison Return Values:** Setting `(-inf, inf, 0)` for an invalid subtree cleanly propagates the failure upward without requiring additional boolean flags.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is visited once during postorder traversal, and combinations execute in $O(1)$ arithmetic steps.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the height of the binary tree ($O(\log N)$ for balanced trees, $O(N)$ for skewed chains), representing the maximum call stack depth.
