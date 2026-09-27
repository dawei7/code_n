# Guided Example: Invert Binary Tree

We trace the step-by-step mirror reflection pointer swaps, recursive post-order subtree inversion, and iterative BFS level-order pointer mutation on representative binary trees:

- **Input:** $\text{root} = [4, 2, 7, 1, 3, 6, 9]$
- **Required output:** $[4, 7, 2, 9, 6, 3, 1]$ (Every node's left and right child pointers are swapped)
- **Three Node Instance:** $\text{root} = [2, 1, 3] \implies [2, 3, 1]$
- **Single Node Instance:** $\text{root} = [1] \implies [1]$
- **Empty Tree Instance:** $\text{root} = [] \implies []$

This instance demonstrates in-place pointer transposition on directed binary tree topologies, proves the equivalence of recursive DFS and iterative BFS queue traversals, explains why simultaneous tuple assignment (`node.left, node.right = node.right, node.left`) eliminates temporary pointer variables, and runs in strictly $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
```text
        4
       / \
      2   7
     / \ / \
    1  3 6  9
```
Invert the tree so that every left child becomes a right child and vice versa (producing a mirror reflection):
```text
        4
       / \
      7   2
     / \ / \
    9  6 3  1
```

### The Geometric Reflection Invariant
A mirror reflection of a tree requires:
1. Swapping the root's left and right subtrees.
2. Recursively inverting the left subtree.
3. Recursively inverting the right subtree.
Whether executed top-down (pre-order), bottom-up (post-order), or level-by-level (BFS queue), every single node in the tree must have its `left` and `right` pointers swapped exactly once.

---

## 2. Conceptual Foundation & Invariants

### Method A: Recursive Inversion (DFS)
Define `invertTree(node)`:
1. **Base Case:** If `node is None`, return `None`.
2. **Recursive Subtree Inversion:**
   $$
   \text{inverted\_left} = \text{invertTree}(\text{node.left})
   $$
   $$
   \text{inverted\_right} = \text{invertTree}(\text{node.right})
   $$
3. **Pointer Transposition:**
   Attach the inverted subtrees to opposite child references:
   $$
   \text{node.left} \leftarrow \text{inverted\_right}, \quad \text{node.right} \leftarrow \text{inverted\_left}
   $$
4. Return `node`.

### Method B: Iterative Queue Traversal (BFS)
Maintain a queue $Q = \text{deque}([\text{root}])$:
While $Q$ is not empty:
- Pop `curr = Q.popleft()`.
- Swap child pointers:
  $$
  \text{curr.left}, \text{curr.right} = \text{curr.right}, \text{curr.left}
  $$
- Enqueue any non-null children:
  If `curr.left`: $Q.\text{append}(\text{curr.left})$.
  If `curr.right`: $Q.\text{append}(\text{curr.right})$.
Return `root`.

> **Invariant.** For every node $u$ in the tree, after the algorithm visits $u$, the left pointer of $u$ references what was originally in the right subtree of $u$, and the right pointer references what was originally in the left subtree.

---

## 3. Step-by-Step Worked Execution

We trace the recursive bottom-up inversion on $\text{root} = [4, 2, 7, 1, 3, 6, 9]$:

### Step 1: Invert Leaves (Depth 2)
- Node 1: `left = None, right = None` $\implies$ Swapping leaves it unchanged. Returns Node 1.
- Node 3: `left = None, right = None` $\implies$ Returns Node 3.
- Node 6: `left = None, right = None` $\implies$ Returns Node 6.
- Node 9: `left = None, right = None` $\implies$ Returns Node 9.

---

### Step 2: Invert Left Subtree at Node 2 (Depth 1)
- Original children: `node.left = Node 1`, `node.right = Node 3`.
- Swap pointers:
  $$
  \text{Node 2.left} \leftarrow \text{Node 3}, \quad \text{Node 2.right} \leftarrow \text{Node 1}
  $$
- Inverted subtree at 2:
  ```text
      2
     / \
    3   1
  ```
- Returns Node 2.

---

### Step 3: Invert Right Subtree at Node 7 (Depth 1)
- Original children: `node.left = Node 6`, `node.right = Node 9`.
- Swap pointers:
  $$
  \text{Node 7.left} \leftarrow \text{Node 9}, \quad \text{Node 7.right} \leftarrow \text{Node 6}
  $$
- Inverted subtree at 7:
  ```text
      7
     / \
    9   6
  ```
- Returns Node 7.

---

### Step 4: Invert Root Node 4 (Depth 0)
- Original children: `node.left = Node 2`, `node.right = Node 7`.
- Swap pointers:
  $$
  \text{Node 4.left} \leftarrow \text{Node 7}, \quad \text{Node 4.right} \leftarrow \text{Node 2}
  $$
- Full inverted tree:
  ```text
          4
         / \
        7   2
       / \ / \
      9  6 3  1
  ```
- Level-order serialization: $[4, 7, 2, 9, 6, 3, 1]$.

---

## 4. Complete Execution Trace

```text
Original Tree:
        4
       / \
      2   7
     / \ / \
    1  3 6  9

Node 2: swap children (1, 3) -> (3, 1)
Node 7: swap children (6, 9) -> (9, 6)
Node 4: swap children (Subtree 2, Subtree 7) -> (Subtree 7, Subtree 2)

Resulting Tree:
        4
       / \
      7   2
     / \ / \
    9  6 3  1

Output: [4, 7, 2, 9, 6, 3, 1]
```

| Traversal Step | Node Evaluated | Left Child Before Swap | Right Child Before Swap | Pointers After Swap | Subtree Mirror Status |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Node 1 | `None` | `None` | `None, None` | Mirror leaf |
| 2 | Node 3 | `None` | `None` | `None, None` | Mirror leaf |
| **3** | **Node 2** | **Node 1** | **Node 3** | **`left: 3, right: 1`** | **Inverted** |
| 4 | Node 6 | `None` | `None` | `None, None` | Mirror leaf |
| 5 | Node 9 | `None` | `None` | `None, None` | Mirror leaf |
| **6** | **Node 7** | **Node 6** | **Node 9** | **`left: 9, right: 6`** | **Inverted** |
| **7** | **Node 4 (Root)** | **Node 2** | **Node 7** | **`left: 7, right: 2`** | **Complete Tree Inverted** |

---

## 5. Algorithmic Correctness

**Soundness.** Swapping `node.left` and `node.right` mirrors the child structure at that specific node. Applying this swap across every single node inductively inverts every horizontal relationship across all levels of the tree.

**Completeness.** Every reachable node in the binary tree is visited exactly once. No node is skipped, ensuring the entire tree topology is mirrored.

---

## 6. Traps This Instance Exposes

- **Sequential Overwrite Without Swap:** In languages without simultaneous tuple assignment, writing `root.left = invertTree(root.right)` overwrites `root.left` before it is passed to the right subtree! A temporary variable `temp = root.left` is required, or Python tuple unpacking `root.left, root.right = root.right, root.left`.
- **Empty Tree:** When `root is None`, immediately returning `None` guards against null-pointer dereferencing.
- **Asymmetric / Skewed Trees:** A node with only one child (e.g. `left = Node(2), right = None`) correctly swaps to `left = None, right = Node(2)`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the total number of nodes in the binary tree. Each node is visited once and its child pointers are swapped in $O(1)$ time.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the height of the tree.
  - In a balanced tree, $H = O(\log N)$ call stack frames.
  - In a completely skewed tree, $H = O(N)$ call stack frames.
  - Using BFS queue, space is $O(W) = O(N)$ where $W$ is maximum level width.