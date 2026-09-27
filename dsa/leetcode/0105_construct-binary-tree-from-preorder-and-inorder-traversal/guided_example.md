# Guided Example: Construct Binary Tree from Preorder and Inorder Traversal

We trace the step-by-step recursive divide-and-conquer tree reconstruction using hash map index lookups on representative traversal arrays:

- **Input:** $\text{preorder} = [3, 9, 20, 15, 7]$, $\text{inorder} = [9, 3, 15, 20, 7]$
- **Required output:** $[3, 9, 20, \text{null}, \text{null}, 15, 7]$
- **Single-Node Base:** $\text{preorder} = [1], \text{inorder} = [1] \implies [1]$

This instance demonstrates exploiting preorder root positioning ($\text{preorder}[\text{pre\_start}]$ is always the subtree root), partitioning inorder into left and right subtree spans, indexing with a precomputed hash map in $O(1)$ time, computing segment offsets, and avoiding array slicing in $O(N)$ linear time.

---

## 1. Instance & Teaching Goal

Given two integer arrays $\text{preorder}$ and $\text{inorder}$:
$$
\text{preorder} = [3, 9, 20, 15, 7], \quad \text{inorder} = [9, 3, 15, 20, 7]
$$
where each traversal describes the same binary tree with unique values, reconstruct and return the binary tree.

The properties of each traversal reveal tree topology:
1. **Preorder (Root $\to$ Left $\to$ Right):**
   The very first element is always the **Root** of the current subtree.
   Here, $\text{preorder}[0] = 3$ is the global tree root.
2. **Inorder (Left $\to$ Root $\to$ Right):**
   The root divides the sequence into elements in its left subtree and elements in its right subtree.
   Locating $3$ in $\text{inorder}$ at index $1$:
   - Left subtree values: $[9]$ (length $1$)
   - Right subtree values: $[15, 20, 7]$ (length $3$)

A naive approach calling `.index()` to find the root in `inorder` and slicing arrays incurs $O(N^2)$ time and $O(N^2)$ memory copying.
By building a hash map of value-to-index mappings for $\text{inorder}$ upfront and passing bounding pointers $(\text{pre\_start}, \text{pre\_end}, \text{in\_start}, \text{in\_end})$, construction runs in $O(N)$ time and $O(N)$ space.

---

## 2. Conceptual Foundation & Invariants

### Bounding Index Partitioning Protocol
Precompute $\text{in\_map} = \{v: i \text{ for } i, v \text{ in enumerate}(\text{inorder})\}$.
Define recursive helper $\text{build}(\text{pre\_start}, \text{pre\_end}, \text{in\_start}, \text{in\_end})$:

1. **Base Case:**
   If $\text{pre\_start} > \text{pre\_end}$ or $\text{in\_start} > \text{in\_end}$:
   $$
   \text{return } \emptyset
   $$
2. **Extract Root:**
   Root value is $V = \text{preorder}[\text{pre\_start}]$.
   Lookup root position in $\text{inorder}$: $k = \text{in\_map}[V]$.
   Calculate number of nodes in the left subtree:
   $$
   \text{left\_size} = k - \text{in\_start}
   $$
3. **Partition Intervals:**
   - **Left Subtree:**
     - Preorder bounds: $[\text{pre\_start} + 1, \; \text{pre\_start} + \text{left\_size}]$
     - Inorder bounds: $[\text{in\_start}, \; k - 1]$
   - **Right Subtree:**
     - Preorder bounds: $[\text{pre\_start} + \text{left\_size} + 1, \; \text{pre\_end}]$
     - Inorder bounds: $[k + 1, \; \text{in\_end}]$
4. **Construct Node:**
   $$
   \text{root} = \text{TreeNode}(V, \, \text{left} = \text{LeftSubtree}, \, \text{right} = \text{RightSubtree})
   $$

> **Invariant.** For any interval tuple $(\text{pre\_start}, \text{pre\_end}, \text{in\_start}, \text{in\_end})$, the two segments contain identical multisets of nodes spanning the exact subtree rooted at $\text{preorder}[\text{pre\_start}]$.

---

## 3. Step-by-Step Worked Execution

We trace $\text{preorder} = [3, 9, 20, 15, 7]$ and $\text{inorder} = [9, 3, 15, 20, 7]$:

### Upfront Inorder Index Map
$$
\text{in\_map} = \{9: 0, \, 3: 1, \, 15: 2, \, 20: 3, \, 7: 4\}
$$

---

### Step 1: Global Root (Bounds: $\text{pre}[0 \dots 4]$, $\text{in}[0 \dots 4]$)
- Root value: $V = \text{preorder}[0] = 3$.
- Inorder index of 3: $k = \text{in\_map}[3] = 1$.
- Left subtree size: $\text{left\_size} = 1 - 0 = 1$.
- Spawn subtrees:
  - Left: $\text{pre}[1 \dots 1]$, $\text{in}[0 \dots 0]$
  - Right: $\text{pre}[2 \dots 4]$, $\text{in}[2 \dots 4]$

---

### Step 2: Construct Left Child of 3 (Bounds: $\text{pre}[1 \dots 1]$, $\text{in}[0 \dots 0]$)
- Root value: $V = \text{preorder}[1] = 9$.
- Inorder index of 9: $k = \text{in\_map}[9] = 0$.
- Left size: $0 - 0 = 0$.
  - Left child bounds: $\text{pre}[2 \dots 1] \implies \emptyset$.
  - Right child bounds: $\text{pre}[2 \dots 1] \implies \emptyset$.
- Returns leaf: $\text{Node}(9)$.

---

### Step 3: Construct Right Child of 3 (Bounds: $\text{pre}[2 \dots 4]$, $\text{in}[2 \dots 4]$)
- Root value: $V = \text{preorder}[2] = 20$.
- Inorder index of 20: $k = \text{in\_map}[20] = 3$.
- Left subtree size: $\text{left\_size} = 3 - 2 = 1$.
- Spawn subtrees:
  - Left of 20: $\text{pre}[3 \dots 3]$, $\text{in}[2 \dots 2]$
  - Right of 20: $\text{pre}[4 \dots 4]$, $\text{in}[4 \dots 4]$

---

### Step 4: Construct Left Child of 20 (Bounds: $\text{pre}[3 \dots 3]$, $\text{in}[2 \dots 2]$)
- Root value: $V = \text{preorder}[3] = 15$.
- Inorder index: $k = 2$.
- Both child bounds empty $\implies$ leaf $\text{Node}(15)$.

---

### Step 5: Construct Right Child of 20 (Bounds: $\text{pre}[4 \dots 4]$, $\text{in}[4 \dots 4]$)
- Root value: $V = \text{preorder}[4] = 7$.
- Inorder index: $k = 4$.
- Both child bounds empty $\implies$ leaf $\text{Node}(7)$.

Reconstruction complete:
Node $20$ links left $15$ and right $7$.
Node $3$ links left $9$ and right $20$.
Result: $[3, 9, 20, \text{null}, \text{null}, 15, 7]$.

---

## 4. Complete Execution Trace

```text
       Root 3 (pre[0], in[1])
       /                    \
  Node 9 (pre[1], in[0])   Node 20 (pre[2], in[3])
                           /                     \
                   Node 15 (pre[3], in[2])   Node 7 (pre[4], in[4])
```

| Recursion Call | Target Subtree | Preorder Range $[\text{pre\_start}, \text{pre\_end}]$ | Inorder Range $[\text{in\_start}, \text{in\_end}]$ | Subtree Root $V$ | Inorder Index $k$ | Left Subtree Size | Created Subtree |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | Global Root | $[0, 4]$ (`[3,9,20,15,7]`) | $[0, 4]$ (`[9,3,15,20,7]`) | 3 | 1 | 1 | $\text{Node}(3)$ |
| 1.1 | 3's Left | $[1, 1]$ (`[9]`) | $[0, 0]$ (`[9]`) | 9 | 0 | 0 | $\text{Node}(9)$ |
| 1.2 | 3's Right | $[2, 4]$ (`[20,15,7]`) | $[2, 4]$ (`[15,20,7]`) | 20 | 3 | 1 | $\text{Node}(20)$ |
| 1.2.1 | 20's Left | $[3, 3]$ (`[15]`) | $[2, 2]$ (`[15]`) | 15 | 2 | 0 | $\text{Node}(15)$ |
| 1.2.2 | 20's Right | $[4, 4]$ (`[7]`) | $[4, 4]$ (`[7]`) | 7 | 4 | 0 | $\text{Node}(7)$ |

### Interval Arithmetic on a Mixed Subtree Instance

Take $\text{preorder} = [1, 2, 4, 5, 3, 6]$ and $\text{inorder} = [4, 2, 5, 1, 3, 6]$. Here the root sits at inorder index $3$, so the left subtree is large and the two index systems drift apart immediately: the left subtree's preorder window and its inorder window no longer start at the same coordinate. The map is $\text{in\_map} = \{4: 0, 2: 1, 5: 2, 1: 3, 3: 4, 6: 5\}$.

| Subproblem | Preorder window | Inorder window | Root $V$ | $k$ | $\text{left\_size} = k - \text{in\_start}$ | Left child windows (pre / in) | Right child windows (pre / in) |
|:---|:---|:---|:---:|:---:|:---:|:---|:---|
| Root | `pre[0..5]` = `[1, 2, 4, 5, 3, 6]` | `in[0..5]` = `[4, 2, 5, 1, 3, 6]` | 1 | 3 | $3 - 0 = 3$ | `pre[1..3]` / `in[0..2]` | `pre[4..5]` / `in[4..5]` |
| $1$'s left | `pre[1..3]` = `[2, 4, 5]` | `in[0..2]` = `[4, 2, 5]` | 2 | 1 | $1 - 0 = 1$ | `pre[2..2]` / `in[0..0]` | `pre[3..3]` / `in[2..2]` |
| $1$'s left-left | `pre[2..2]` = `[4]` | `in[0..0]` = `[4]` | 4 | 0 | $0 - 0 = 0$ | empty | empty |
| $1$'s left-right | `pre[3..3]` = `[5]` | `in[2..2]` = `[5]` | 5 | 2 | $2 - 2 = 0$ | empty | empty |
| $1$'s right | `pre[4..5]` = `[3, 6]` | `in[4..5]` = `[3, 6]` | 3 | 4 | $4 - 4 = 0$ | empty | `pre[5..5]` / `in[5..5]` |
| $1$'s right-right | `pre[5..5]` = `[6]` | `in[5..5]` = `[6]` | 6 | 5 | $5 - 5 = 0$ | empty | empty |

Row two is the offset trap made concrete. Node $2$ has $k + 1 = 2$, but its right subtree actually begins at preorder index $1 + 1 + 1 = 3$. Using $k + 1$ as the preorder offset would hand node $4$ — a left-subtree node — to the right subtree, and every value below it would be misplaced. The correct formula, $\text{pre\_start} + \text{left\_size} + 1$, is derived from the preorder layout, not from the inorder index.

The reconstructed tree is $[1, 2, 3, 4, 5, \text{null}, 6]$: node $1$ keeps both children, node $2$ keeps both children, and node $3$ has only a right child, which is why its left slot appears as a null in the level-order output.

---

## 5. Algorithmic Correctness

**Soundness.** Preorder traversal guarantees that the first element in any contiguous subtree range is the root. Inorder traversal guarantees that all elements preceding the root belong to its left subtree, and all elements succeeding it belong to its right subtree. Because values in the tree are strictly unique, locating the root in the hash map partitions both arrays unambiguously.

**Completeness.** Every node index appears in `preorder` and is processed as the root of some subproblem. The divide-and-conquer base case cleanly terminates leaves when interval lengths reach zero, ensuring every node is correctly positioned in the tree.

---

## 6. Traps This Instance Exposes

- **Array Slicing Complexity ($O(N^2)$ Trap):** Writing `build(preorder[1:left_size+1], inorder[:k])` creates new array slices at every recursive step, degrading runtime to $O(N^2)$. Passing scalar index boundaries avoids any array allocation.
- **Index Offsets in Preorder:** The right subtree in `preorder` does not begin at $k+1$; it begins at $\text{pre\_start} + \text{left\_size} + 1$, because preorder groups left subtree nodes contiguously.
- **Duplicate Value Preconditions:** This algorithm requires tree values to be unique. If duplicate values exist, inorder root lookups would be ambiguous without additional structural hints.

### Construction Strategies Compared

| Strategy | How the root position is found | Time | Auxiliary space | When it fails or costs more |
|:---|:---|:---:|:---:|:---|
| Inorder hash map plus scalar bounds (used here) | One dictionary lookup per subproblem | $O(N)$ | $O(N)$ for the map plus $O(H)$ stack | Needs the unique-value guarantee; the map alone is $N$ entries regardless of tree shape |
| Direct-address table over the value domain | An array slot per admissible value, shifted by the lower bound $-3000$ | $O(N)$ | $O(6001)$ table plus $O(H)$ stack | Exploits the constraint $-3000 \le \text{inorder}[i] \le 3000$; it is invalid for values outside that fixed window, and wastes 6001 slots even for $N = 5$ |
| Slice-based recursion with a linear root search | Scan the inorder slice for the root value | $O(N^2)$ | $O(N^2)$ transient copies | Correct for the two-node and six-node instances but degrades sharply near $N = 3000$, where each level copies a large slice |
| Iterative monotonic stack over preorder | Walk an inorder cursor and compare it with the stack top instead of mapping values | $O(N)$ | $O(H)$ | Removes recursion but still requires unique values and both traversals; the stack must be popped whenever its top matches the next unconsumed inorder value, and an off-by-one in that cursor silently misplaces right children |

The absolute-bounds method is preferred here because it is the only one whose cost is independent of both the value range and the tree shape: it pays exactly one map entry per node and one stack frame per open subtree.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. Building the hash map takes $O(N)$ time. Each recursive step performs $O(1)$ dictionary lookups and arithmetic, executing exactly $N$ times.
- **Auxiliary Space Complexity:** $O(N)$ to store the hash map of size $N$ and $O(H)$ recursion stack depth ($O(\log N)$ average, $O(N)$ worst case).
