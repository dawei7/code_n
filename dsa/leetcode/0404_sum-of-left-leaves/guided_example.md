# Guided Example: Sum of Left Leaves

We trace the step-by-step binary tree structural inspection, parent-perspective left-leaf identification (`root.left.left == root.left.right == None`), recursive subtree decomposition, and accumulator aggregation on representative tree instances:

- **Input:** $root = [3, 9, 20, \text{null}, \text{null}, 15, 7]$
- **Required output:** `24`
  - Tree diagram:
    ```text
            3
           / \
         [9]  20
             /  \
           [15]  7
    ```
  - Step 1 (Inspect root $3$):
    - Recurse right: evaluate subtree at node $20$
  - Step 2 (Inspect node $20$):
    - Recurse right: node $7$ has no left child $\implies$ returns $0$
    - Inspect left child $15$:
      - Node $15$ has `left == None` and `right == None` $\implies$ Leaf node!
      - Because it is the left child of $20$, it is a **left leaf**
      - Contribution: $+15$
    - Node $20$ subtotal: $0 + 15 = 15$
  - Step 3 (Back at root $3$, inspect left child $9$):
    - Node $9$ has `left == None` and `right == None` $\implies$ Leaf node!
    - Because it is the left child of $3$, it is a **left leaf**
    - Contribution: $+9$
  - Total sum: $15 + 9 = \mathbf{24}$
- **Single Node Tree:** $root = [1] \implies$ node $1$ is a root leaf, but has no parent to make it a *left* leaf $\implies \mathbf{0}$
- **Right-Leaning Chain:** $[1, \text{null}, 2, \text{null}, 3] \implies$ zero left children $\implies \mathbf{0}$

This instance demonstrates distinguishing directional structural relationships in hierarchical trees from the parent's perspective, mathematically proves why leaf verification requires nullity on both children, and achieves $O(N)$ time and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree $root = [3, 9, 20, \text{null}, \text{null}, 15, 7]$:
Compute the sum of all **left leaves**:

```text
Definitions:
1. Leaf Node: A node with no children (node.left is None and node.right is None).
2. Left Leaf: A leaf node that is specifically the LEFT child of its parent.

Tree:
        3
       / \
     (9)  20
         /  \
       (15)  7

Node Classifications:
  Node 3:  Root (Not a leaf)
  Node 9:  Left child of 3, has no children -> LEFT LEAF (Value: 9)
  Node 20: Right child of 3 (Not a leaf)
  Node 15: Left child of 20, has no children -> LEFT LEAF (Value: 15)
  Node 7:  Right child of 20, has no children -> Right Leaf (Ignored)

Sum = 9 + 15 = 24
```

### Why the Parent Must Classify Left Leaves
A node in a standard binary tree has pointers to its children, but no pointer to its parent.
Once the traversal enters a node, the node cannot know whether it is a left or right child of its caller.
Inspecting `root.left` from `root` solves this cleanly:
- If `root.left` exists and both `root.left.left` and `root.left.right` are `None`:
  Then `root.left` is provably a **left leaf**!
- If `root.left` is not a leaf, recurse into `root.left`.

---

## 2. Conceptual Foundation & Invariants

### 1. The Recursive Function Contract:
Let $f(\text{node})$ compute the sum of all left leaves in the subtree rooted at $\text{node}$:
1. **Base Case:**
   If $\text{node}$ is `None`:
   $$
   f(\text{node}) = 0
   $$
2. **Right Subtree Contribution:**
   The right child cannot be a left leaf itself, but its subtree may contain left leaves:
   $$
   ans = f(\text{node.right})
   $$
3. **Left Child Inspection:**
   If $\text{node.left}$ exists:
   - **Leaf Test:** If $\text{node.left.left} == \text{node.left.right} == \text{None}$:
     $\text{node.left}$ is a left leaf!
     $$
     ans \leftarrow ans + \text{node.left.val}
     $$
   - **Internal Node:** If $\text{node.left}$ has children:
     $$
     ans \leftarrow ans + f(\text{node.left})
     $$
4. Return $ans$.

> **Invariant.** A node's value is added to the total if and only if it is a child reached via `root.left` and has zero descendants.

---

## 3. Step-by-Step Worked Execution

We trace $root = [3, 9, 20, \text{null}, \text{null}, 15, 7]$:

---

### Step 1: Call $f(\text{Node } 3)$
- Node 3 is not None.
- Recurse right: call $f(\text{Node } 20)$.

---

### Step 2: Call $f(\text{Node } 20)$
- Node 20 is not None.
- Recurse right: call $f(\text{Node } 7)$.
  - At Node 7:
    - `node.right` is None $\implies f(\text{None}) = 0$.
    - `node.left` is None.
    - Returns: $0$.
  - Node 20 receives $ans = 0$.
- Inspect left child of Node 20: $\text{Node } 15$:
  - $\text{Node } 15.\text{left} = \text{None}$
  - $\text{Node } 15.\text{right} = \text{None}$
  - Both children are None $\implies \text{Node } 15$ is a **leaf**!
  - Add value:
    $$
    ans = 0 + 15 = \mathbf{15}
    $$
- Return 15 to Node 3.

---

### Step 3: Back at Node 3
- Current accumulator: $ans = 15$ (from right subtree).
- Inspect left child of Node 3: $\text{Node } 9$:
  - $\text{Node } 9.\text{left} = \text{None}$
  - $\text{Node } 9.\text{right} = \text{None}$
  - Both children are None $\implies \text{Node } 9$ is a **leaf**!
  - Add value:
    $$
    ans = 15 + 9 = \mathbf{24}
    $$

---

### Step 4: Termination
All subtrees processed. Return:
$$
\mathbf{24}
$$

---

## 4. Complete Execution Trace

```text
f(Node 3)
  ans = f(Node 20)
    ans = f(Node 7) -> 0
    left child is Node 15 (leaf) -> ans += 15 -> returns 15
  ans = 15
  left child is Node 9 (leaf) -> ans += 9 -> returns 24

Final Output: 24
```

| Traversal Frame | Target Node | Action Evaluated | Child Inspected | Is Left Leaf? | Subtree Return Value | Running Total |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | Node 3 | Recurse right | Node 20 | - | - | 0 |
| 2 | Node 20 | Recurse right | Node 7 | - | - | 0 |
| 3 | Node 7 | Terminal leaf | None | No (Right child) | 0 | 0 |
| 4 | Node 20 | Inspect left | Node 15 | **Yes (Left + Leaf)** | $0 + 15 = 15$ | 15 |
| **5** | **Node 3** | **Inspect left** | **Node 9** | **Yes (Left + Leaf)** | **$15 + 9 = 24$** | **`24` (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** For any node $u$, $u$ is included in the sum if and only if $u$ was accessed as the left pointer of some ancestor $p$ and $u.\text{left} == u.\text{right} == \text{None}$. This matches the definition of a left leaf. Nodes accessed via right pointers (such as node 7) are never added to the sum directly, only their subtrees are searched.

**Completeness.** Tree traversal visits every node in the binary tree exactly once. Any left leaf that exists must be the left child of some unique internal node, which will inspect it and accumulate its value.

---

## 6. Traps This Instance Exposes

- **Single Node Tree ($root = [1]$):** A single root node has no parent. Even though it is a leaf, it is not a *left* leaf, so the answer must be 0. Top-down inspection from the parent handles this naturally because the root has no parent.
- **Right Leaf Nodes:** A right child with no children (e.g. node 7) is a leaf, but NOT a left leaf. It must not be counted.
- **Pythonic Leaf Check:** Checking `node.left.left == node.left.right` works because `None == None` is True. However, if a node has two different non-None children with different values, they are unequal objects, correctly identifying non-leaves.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the total number of nodes in the binary tree. Each node is visited at most once.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the height of the tree, representing the recursion stack depth ($O(\log N)$ for balanced trees, $O(N)$ for degenerate skewed chains).