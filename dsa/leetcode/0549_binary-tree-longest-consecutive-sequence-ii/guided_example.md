# Guided Example: Binary Tree Longest Consecutive Sequence II

We trace the step-by-step bidirectional consecutive sequence definition ($|u - v| = 1$), bottom-up post-order DFS returning dual monotonic branch lengths ($[incr, decr]$), parent-child step validation ($child.val \pm 1 == root.val$), apex turning path synthesis ($incr + decr - 1$), and global maximum path tracking on representative binary trees:

- **Input:** $root = [2, 1, 3]$
  - Tree structure:
    - Root: Node $2$
    - Left child: Node $1$
    - Right child: Node $3$
- **Required output:** `3`
  - Consecutive path definition: A simple path where values of consecutive nodes differ by exactly $1$ (either continuously increasing or continuously decreasing).
  - Flexibility: The path can travel downwards, upwards, or turn through a parent node (e.g. $1 \to 2 \to 3$).
- **Dual-Metric Depth-First Search Formulation:**
  - For each subtree, let $dfs(node)$ return a tuple:
    $$
    [incr, \; decr]
    $$
    - $incr$: Length of the longest path starting at $node$ and descending into its subtree where node values decrease downwards (meaning traversing upwards into $node$ **increases** by 1: $child.val + 1 == node.val$).
    - $decr$: Length of the longest path starting at $node$ and descending into its subtree where node values increase downwards (traversing upwards into $node$ **decreases** by 1: $child.val - 1 == node.val$).
  - When $node$ acts as the apex connecting an upward-increasing path from one child and a downward-increasing path to another child, the total path length is:
    $$
    \text{total path} = incr + decr - 1
    $$
    *(subtracting 1 because $node$ is counted in both branches)*.
- **Bottom-up execution trace on $root = [2, 1, 3]$:**
  - **Leaf Node 1 (Left Child):**
    - Both children are `None`.
    - No children to extend from $\implies incr = 1, \; decr = 1$.
    - Apex path: $1 + 1 - 1 = \mathbf{1}$.
    - Return to parent: $[1, 1]$.
  - **Leaf Node 3 (Right Child):**
    - Both children are `None` $\implies incr = 1, \; decr = 1$.
    - Apex path: $1 + 1 - 1 = \mathbf{1}$.
    - Return to parent: $[1, 1]$.
  - **Apex Node 2 (Root):**
    - Initialize: $incr = 1, \; decr = 1$.
    - Receives from left (Node 1): $i_1 = 1, \; d_1 = 1$.
    - Receives from right (Node 3): $i_2 = 1, \; d_2 = 1$.
    - **Inspect Left Child (Node 1):**
      - $node.left.val + 1 = 1 + 1 = 2 == node.val$ (**Match!**)
        - Climbing from Node 1 to Node 2 increases value ($1 \to 2$).
        - $incr \leftarrow i_1 + 1 = 1 + 1 = \mathbf{2}$.
      - $node.left.val - 1 = 1 - 1 = 0 \ne 2$ (No match).
    - **Inspect Right Child (Node 3):**
      - $node.right.val + 1 = 3 + 1 = 4 \ne 2$ (No match).
      - $node.right.val - 1 = 3 - 1 = 2 == node.val$ (**Match!**)
        - Descending from Node 2 to Node 3 increases value ($2 \to 3$).
        - $decr \leftarrow \max(decr, \; d_2 + 1) = \max(1, 1 + 1) = \mathbf{2}$.
    - **Evaluate Apex Turning Path at Node 2:**
      $$
      \text{path} = incr + decr - 1 = 2 + 2 - 1 = \mathbf{3}
      $$
      *(The unified continuous path is $1 \to 2 \to 3$, containing 3 nodes!)*
    - Update global maximum:
      $$
      ans \leftarrow \max(0, 3) = \mathbf{3}
      $$
    - Return vector: $[incr, decr] = [2, 2]$.
  - Traversal completes.
  - Final longest consecutive path: **`3`**.
- **No Turning Path Instance ($root = [1, 2, 3]$):**
  - Left child 2: $2 - 1 == 1 \implies decr = 2$.
  - Right child 3: does not differ by 1 from 1.
  - $incr = 1, decr = 2 \implies 1 + 2 - 1 = \mathbf{2}$ (path $1 \to 2$).
- **Single Node Tree ($root = [10]$):**
  - $incr = 1, decr = 1 \implies 1 + 1 - 1 = \mathbf{1}$.

This instance demonstrates bidirectional path synthesis via dual-metric dynamic programming over tree topologies, mathematically proves why tracking upward-increasing and upward-decreasing paths allows $O(1)$ apex path fusion, and derives $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
Return the length of the **longest consecutive path** in the tree.
The path:
1. Can be increasing or decreasing ($|v_{i+1} - v_i| == 1$).
2. Can travel child-to-parent, parent-to-child, or turn at an ancestor (child1 $\to$ parent $\to$ child2).
3. Path length is measured by the **number of nodes** in the path.

```text
Tree:
        2
       / \
      1   3

Consecutive Path:
  1 -> 2 -> 3  (Values: 1, 2, 3 consecutive!)
Length = 3 nodes
```

### The Invariant of Dual Monotonic Branches
- At any turning node $u$:
  - If we want to form a path $c_1 \to u \to c_2$:
  - One side must lead into $u$ with values **strictly increasing** by 1.
  - The other side must lead out of $u$ with values **strictly increasing** by 1 (or decreasing).
- If both sides were increasing into $u$, the sequence would increase then decrease ($1 \to 2 \leftarrow 1$), which is NOT consecutive!
- Therefore, each node must compute two separate metrics:
  1. $incr$: Length of consecutive path where values increase towards $u$.
  2. $decr$: Length of consecutive path where values decrease towards $u$.
- Combining them at apex $u$:
  $$
  L = incr + decr - 1
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. Depth-First Search Return Contract:
Function $dfs(node) \to [incr, decr]$:
- If $node$ is `None`: return $[0, 0]$.
- Initialize $incr = 1, \; decr = 1$.
- Recursively resolve left child: $[i_1, d_1] = dfs(node.left)$.
- Recursively resolve right child: $[i_2, d_2] = dfs(node.right)$.

### 2. Parent-Child Transition Rules:
- **For Left Child:**
  - If $left.val + 1 == node.val$: $incr = i_1 + 1$.
  - If $left.val - 1 == node.val$: $decr = d_1 + 1$.
- **For Right Child:**
  - If $right.val + 1 == node.val$: $incr = \max(incr, \; i_2 + 1)$.
  - If $right.val - 1 == node.val$: $decr = \max(decr, \; d_2 + 1)$.

### 3. Apex Path Update:
$$
ans \leftarrow \max(ans, \; incr + decr - 1)
$$
Return $[incr, decr]$ to parent.

> **Parity Compatibility Invariant.** Because $incr$ and $decr$ enforce opposite monotonic directions relative to $node$, concatenating them at $node$ forms a strictly monotonic sequence along the composite path.

---

## 3. Step-by-Step Worked Execution

We trace $root = [2, 1, 3]$:

---

### Step 1: Initialize
- $ans = 0$.

---

### Step 2: Post-Order DFS Leaves
- Node 1 (left):
  - No children $\implies incr = 1, decr = 1$.
  - $ans = \max(0, 1 + 1 - 1) = 1$.
  - Return $[1, 1]$.
- Node 3 (right):
  - No children $\implies incr = 1, decr = 1$.
  - $ans = \max(1, 1) = 1$.
  - Return $[1, 1]$.

---

### Step 3: Apex Node 2 (Root)
- Initial: $incr = 1, decr = 1$.
- **From Left (Node 1):**
  - $1 + 1 = 2 == root.val \implies incr = 1 + 1 = \mathbf{2}$.
- **From Right (Node 3):**
  - $3 - 1 = 2 == root.val \implies decr = \max(1, 1 + 1) = \mathbf{2}$.
- **Calculate Total Path at Apex Node 2:**
  $$
  L = incr + decr - 1 = 2 + 2 - 1 = \mathbf{3}
  $$
- Update global max:
  $$
  ans \leftarrow \max(1, 3) = \mathbf{3}
  $$
- Return $[2, 2]$.

---

### Step 4: Final Output
$$
ans = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Node Visited | Left Child Match | Right Child Match | Node $incr$ | Node $decr$ | Apex Path $incr + decr - 1$ | Running $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Node 1 | None | None | $1$ | $1$ | $1 + 1 - 1 = 1$ | $1$ |
| Node 3 | None | None | $1$ | $1$ | $1 + 1 - 1 = 1$ | $1$ |
| **Node 2** | $1+1=2$ ($incr$) | $3-1=2$ ($decr$) | **$2$** | **$2$** | $2 + 2 - 1 = \mathbf{3}$ | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node Tree ($[1]$):** $incr = 1, decr = 1 \implies ans = 1$.
- **Two Nodes ($[1, 2]$):** Node 2 has $child.val - 1 = 1 \implies decr = 2 \implies ans = 2$.
- **Non-Consecutive Values ($[1, 5, 9]$):** Neither child matches $val \pm 1 \implies$ each node reports $incr = 1, decr = 1 \implies ans = 1$.
- **Deep Zig-Zag Paths:** Can travel across any inverted V-shaped subtree.

---

## 6. Traps & Common Anti-Patterns

- **Measuring Edges Instead of Nodes:** Unlike Problem 543 (Diameter of Binary Tree), which counts *edges*, this problem measures path length by the *number of nodes*. A single node has length 1.
- **Allowing Both Branches to Increase (or Both Decrease):** If left child is 1 and right child is 1 for root 2, combining them would give sequence $[1, 2, 1]$, which is NOT consecutive. By pairing $incr$ from one side with $decr$ from the other, direction consistency is mathematically preserved.
- **Overwriting $incr$ and $decr$ Without `max`:** When evaluating the right child, using `incr = i2 + 1` instead of `max(incr, i2 + 1)` overwrites a valid longer left branch.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Post-order DFS visits each node in the tree exactly once.
  - At each node, constant arithmetic evaluations and comparisons occur.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ call stack space where $H$ is the tree height ($O(\log N)$ average, $O(N)$ worst-case).