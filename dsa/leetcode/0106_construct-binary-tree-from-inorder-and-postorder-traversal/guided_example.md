# Guided Example: Construct Binary Tree from Inorder and Postorder Traversal

We trace the step-by-step recursive tree reconstruction using postorder root extraction and inorder index splitting on representative traversal arrays:

- **Input:** $\text{inorder} = [9, 3, 15, 20, 7]$, $\text{postorder} = [9, 15, 7, 20, 3]$
- **Required output:** $[3, 9, 20, \text{null}, \text{null}, 15, 7]$
- **Single-Node Base:** $\text{inorder} = [1], \text{postorder} = [1] \implies [1]$

This instance demonstrates exploiting the postorder root invariant ($\text{postorder}[\text{post\_end}]$ is always the subtree root), partitioning inorder into left and right subtree spans, index lookups with a precomputed hash map, calculating segment bounds, and contrasting right-first recursion vs explicit coordinate passing.

---

## 1. Instance & Teaching Goal

Given two integer arrays $\text{inorder}$ and $\text{postorder}$:
$$
\text{inorder} = [9, 3, 15, 20, 7], \quad \text{postorder} = [9, 15, 7, 20, 3]
$$
where each traversal describes the same binary tree with unique values, reconstruct and return the binary tree.

The roles of each traversal sequence:
1. **Postorder (Left $\to$ Right $\to$ Root):**
   The very **last** element in any postorder range is the root of that subtree.
   Here, $\text{postorder}[-1] = 3$ is the global root.
2. **Inorder (Left $\to$ Root $\to$ Right):**
   Locating the root value $3$ at index $1$ divides the tree:
   - Left subtree values: $[9]$ (length $1$)
   - Right subtree values: $[15, 20, 7]$ (length $3$)

Notice the contrast with LeetCode 105:
- In preorder, the root is at the front ($\text{start}$), and left subtrees precede right subtrees.
- In postorder, the root is at the back ($\text{end}$), and right subtrees immediately precede the root.

Using an upfront hash map for $\text{inorder}$ values eliminates linear searches, executing tree reconstruction in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### Bounding Index Partitioning Protocol
Precompute $\text{in\_map} = \{v: i \text{ for } i, v \text{ in enumerate}(\text{inorder})\}$.
Define recursive function $\text{build}(\text{in\_start}, \text{in\_end}, \text{post\_start}, \text{post\_end})$:

1. **Base Case:**
   If $\text{in\_start} > \text{in\_end}$ or $\text{post\_start} > \text{post\_end}$:
   $$
   \text{return } \emptyset
   $$
2. **Extract Subtree Root:**
   Root value is $V = \text{postorder}[\text{post\_end}]$.
   Locate root in inorder sequence: $k = \text{in\_map}[V]$.
   Subtree size counts:
   $$
   \text{left\_size} = k - \text{in\_start}
   $$
   $$
   \text{right\_size} = \text{in\_end} - k
   $$
3. **Partition Bounds:**
   - **Left Subtree:**
     - Inorder: $[\text{in\_start}, \; k - 1]$
     - Postorder: $[\text{post\_start}, \; \text{post\_start} + \text{left\_size} - 1]$
   - **Right Subtree:**
     - Inorder: $[k + 1, \; \text{in\_end}]$
     - Postorder: $[\text{post\_start} + \text{left\_size}, \; \text{post\_end} - 1]$
4. **Construct Node:**
   $$
   \text{root} = \text{TreeNode}(V, \, \text{left} = \text{LeftSubtree}, \, \text{right} = \text{RightSubtree})
   $$

### Pop-Based Variation
Because $\text{postorder}$ ends with the root, immediately preceded by the right subtree's elements, popping from the end of $\text{postorder}$ allows constructing the tree by recursing on `right` first, then `left`:
```text
root.right = build(k + 1, in_end)
root.left = build(in_start, k - 1)
```

> **Invariant.** The last element of $\text{postorder}[\text{post\_start} \dots \text{post\_end}]$ is the true root of the tree whose inorder traversal corresponds to $\text{inorder}[\text{in\_start} \dots \text{in\_end}]$.

---

## 3. Step-by-Step Worked Execution

We trace $\text{inorder} = [9, 3, 15, 20, 7]$ and $\text{postorder} = [9, 15, 7, 20, 3]$:

### Hash Map Setup
$$
\text{in\_map} = \{9: 0, \, 3: 1, \, 15: 2, \, 20: 3, \, 7: 4\}
$$

---

### Step 1: Global Root (Bounds: $\text{in}[0 \dots 4]$, $\text{post}[0 \dots 4]$)
- Root value: $V = \text{postorder}[4] = 3$.
- Inorder index of 3: $k = \text{in\_map}[3] = 1$.
- Left subtree size: $\text{left\_size} = 1 - 0 = 1$.
- Partition:
  - Left: $\text{in}[0 \dots 0]$, $\text{post}[0 \dots 0]$
  - Right: $\text{in}[2 \dots 4]$, $\text{post}[1 \dots 3]$

---

### Step 2: Construct Left Child of 3 (Bounds: $\text{in}[0 \dots 0]$, $\text{post}[0 \dots 0]$)
- Root value: $V = \text{postorder}[0] = 9$.
- Inorder index of 9: $k = 0$.
- Left size: $0 - 0 = 0$.
  - Child bounds empty $\implies \text{Node}(9)$ is a leaf.
- Left child of 3 is $\text{Node}(9)$.

---

### Step 3: Construct Right Child of 3 (Bounds: $\text{in}[2 \dots 4]$, $\text{post}[1 \dots 3]$)
- Root value: $V = \text{postorder}[3] = 20$.
- Inorder index of 20: $k = \text{in\_map}[20] = 3$.
- Subtree size: $\text{left\_size} = 3 - 2 = 1$.
- Partition:
  - Left of 20: $\text{in}[2 \dots 2]$, $\text{post}[1 \dots 1]$
  - Right of 20: $\text{in}[4 \dots 4]$, $\text{post}[2 \dots 2]$

---

### Step 4: Construct Left Child of 20 (Bounds: $\text{in}[2 \dots 2]$, $\text{post}[1 \dots 1]$)
- Root value: $V = \text{postorder}[1] = 15$.
- Inorder index: $k = 2$.
- Child bounds empty $\implies \text{Node}(15)$ is a leaf.

---

### Step 5: Construct Right Child of 20 (Bounds: $\text{in}[4 \dots 4]$, $\text{post}[2 \dots 2]$)
- Root value: $V = \text{postorder}[2] = 7$.
- Inorder index: $k = 4$.
- Child bounds empty $\implies \text{Node}(7)$ is a leaf.

Assembled Tree:
Node $20$ connects left $15$ and right $7$.
Node $3$ connects left $9$ and right $20$.
Final tree structure: $[3, 9, 20, \text{null}, \text{null}, 15, 7]$.

---

## 4. Complete Execution Trace

```text
       Root 3 (post[4], in[1])
       /                    \
  Node 9 (post[0], in[0])   Node 20 (post[3], in[3])
                           /                     \
                   Node 15 (post[1], in[2])   Node 7 (post[2], in[4])
```

| Recursion Frame | Target Subtree | Inorder Interval $[\text{in\_start}, \text{in\_end}]$ | Postorder Interval $[\text{post\_start}, \text{post\_end}]$ | Root Val $V$ | Root Inorder Idx $k$ | Left Subtree Size | Reconstructed Node |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | Global Root | $[0, 4]$ (`[9,3,15,20,7]`) | $[0, 4]$ (`[9,15,7,20,3]`) | 3 | 1 | 1 | $\text{Node}(3)$ |
| 1.1 | 3's Left | $[0, 0]$ (`[9]`) | $[0, 0]$ (`[9]`) | 9 | 0 | 0 | $\text{Node}(9)$ |
| 1.2 | 3's Right | $[2, 4]$ (`[15,20,7]`) | $[1, 3]$ (`[15,7,20]`) | 20 | 3 | 1 | $\text{Node}(20)$ |
| 1.2.1 | 20's Left | $[2, 2]$ (`[15]`) | $[1, 1]$ (`[15]`) | 15 | 2 | 0 | $\text{Node}(15)$ |
| 1.2.2 | 20's Right | $[4, 4]$ (`[7]`) | $[2, 2]$ (`[7]`) | 7 | 4 | 0 | $\text{Node}(7)$ |

### Interval Arithmetic on a Mixed Subtree Instance

Take $\text{inorder} = [4, 2, 5, 1, 3, 6]$ and $\text{postorder} = [4, 5, 2, 6, 3, 1]$. The root $1$ sits at inorder index $3$, so its left subtree holds three nodes while its right subtree holds two. The map is $\text{in\_map} = \{4: 0, 2: 1, 5: 2, 1: 3, 3: 4, 6: 5\}$.

| Subproblem | Inorder window | Postorder window | Root $V$ | $k$ | $\text{left\_size}$ | $\text{right\_size}$ | Left child windows (in / post) | Right child windows (in / post) |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---|:---|
| Root | `in[0..5]` = `[4, 2, 5, 1, 3, 6]` | `post[0..5]` = `[4, 5, 2, 6, 3, 1]` | 1 | 3 | $3 - 0 = 3$ | $5 - 3 = 2$ | `in[0..2]` / `post[0..2]` | `in[4..5]` / `post[3..4]` |
| $1$'s left | `in[0..2]` = `[4, 2, 5]` | `post[0..2]` = `[4, 5, 2]` | 2 | 1 | $1 - 0 = 1$ | $2 - 1 = 1$ | `in[0..0]` / `post[0..0]` | `in[2..2]` / `post[1..1]` |
| $1$'s left-left | `in[0..0]` = `[4]` | `post[0..0]` = `[4]` | 4 | 0 | 0 | 0 | empty | empty |
| $1$'s left-right | `in[2..2]` = `[5]` | `post[1..1]` = `[5]` | 5 | 2 | 0 | 0 | empty | empty |
| $1$'s right | `in[4..5]` = `[3, 6]` | `post[3..4]` = `[6, 3]` | 3 | 4 | $4 - 4 = 0$ | $5 - 4 = 1$ | empty | `in[5..5]` / `post[3..3]` |
| $1$'s right-right | `in[5..5]` = `[6]` | `post[3..3]` = `[6]` | 6 | 5 | 0 | 0 | empty | empty |

Two window facts are visible in this table. First, the root of every window is always its last postorder slot: node $2$ is at `post[2]`, node $3$ at `post[4]`, node $6$ at `post[3]`. Second, the right child's postorder window starts at $\text{post\_start} + \text{left\_size}$ and ends at $\text{post\_end} - 1$, not at $k + 1$: for node $2$ that start is $0 + 1 = 1$, and for node $3$ it is $3 + 0 = 3$ with end $4 - 1 = 3$, giving the window `post[3..3]`. Using $k + 1$ as a postorder index would read `post[2] = 2` as the root of node $2$'s right subtree, which is node $2$ itself.

The reconstructed tree is $[1, 2, 3, 4, 5, \text{null}, 6]$: nodes $1$ and $2$ keep both children, while node $3$ keeps only its right child $6$.

---

## 5. Algorithmic Correctness

**Soundness.** Postorder traversal strictly finishes processing a subtree at its root node; hence $\text{postorder}[\text{post\_end}]$ is guaranteed to be the subtree root. Inorder traversal places all left subtree nodes strictly before the root index $k$ and all right subtree nodes strictly after $k$. The hash map allows exact partitioning into non-overlapping spans.

**Completeness.** Every element in `postorder` is consumed as a root node. The base case $\text{start} > \text{end}$ cleanly terminates when no children exist, constructing the complete binary tree without omissions.

---

## 6. Traps This Instance Exposes

- **Right-First Recursion Requirement When Popping:** If using `postorder.pop()`, you **must** build the right subtree before the left subtree (`root.right = build(...)` then `root.left = build(...)`). Because postorder traversal is `Left -> Right -> Root`, reading backwards encounters `Root`, then `Right`, then `Left`.
- **Calculating Postorder Range Endpoints:** The right subtree's postorder span ends at $\text{post\_end} - 1$ (excluding the root), and starts at $\text{post\_start} + \text{left\_size}$. Mixing up endpoints will associate wrong nodes with subtrees.

### Authored Instances and Their Deciding Feature

| Instance | Inorder | Postorder | Root $V$ | $k$ | $\text{left\_size}$ / $\text{right\_size}$ | Level-order result | What it tests |
|:---|:---|:---|:---:|:---:|:---:|:---|:---|
| Single node | `[1]` | `[1]` | 1 | 0 | 0 / 0 | `[1]` | Both windows collapse to one slot; the base case must still build the node |
| Left child only | `[1, 2]` | `[1, 2]` | 2 | 1 | 1 / 0 | `[2, 1]` | The root is the last postorder element, so $2$ is the parent even though it appears second in inorder |
| Right child only | `[1, 2]` | `[2, 1]` | 1 | 0 | 0 / 1 | `[1, null, 2]` | A zero left size leaves the left slot null while the right window still holds one node |
| Mixed six nodes | `[4, 2, 5, 1, 3, 6]` | `[4, 5, 2, 6, 3, 1]` | 1 | 3 | 3 / 2 | `[1, 2, 3, 4, 5, null, 6]` | Both subtrees are non-empty and of different sizes, so both postorder offsets must be computed independently |
| Three-level sample | `[9, 3, 15, 20, 7]` | `[9, 15, 7, 20, 3]` | 3 | 1 | 1 / 3 | `[3, 9, 20, null, null, 15, 7]` | A right subtree of three nodes whose root sits at postorder index $3$, immediately before the global root |

The left-child-only and right-child-only rows are the pair to keep straight: the two inputs differ only by swapping the postorder entries, yet one produces a left child and the other a right child. Each instance consumes exactly $N$ recursion frames that create a node, plus one terminating frame for every empty window.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Building the hash map takes $O(N)$ time. The recursive function runs $N$ times, with each call executing in $O(1)$ operations.
- **Auxiliary Space Complexity:** $O(N)$ to store the hash map and $O(H)$ recursion stack depth ($O(\log N)$ average, $O(N)$ worst case).