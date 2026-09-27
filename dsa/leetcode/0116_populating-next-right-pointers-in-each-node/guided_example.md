# Guided Example: Populating Next Right Pointers in Each Node

We trace the step-by-step $O(1)$ space horizontal pointer stitching on a representative perfect binary tree:

- **Input:** $\text{root} = [1, 2, 3, 4, 5, 6, 7]$
- **Required output:** $[1, \text{\#}, 2, 3, \text{\#}, 4, 5, 6, 7, \text{\#}]$
- **Single-Node Base:** $\text{root} = [1] \implies [1, \text{\#}]$

This instance demonstrates connecting intra-parent siblings ($\text{curr.left.next} = \text{curr.right}$), bridging inter-parent cross-subtree gaps ($\text{curr.right.next} = \text{curr.next.left}$), using the established level $d$ horizontal chain to construct level $d+1$, and achieving strictly $O(1)$ extra space without queues or recursion.

---

## 1. Instance & Teaching Goal

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children:
$$
\begin{gathered}
1 \\
\swarrow \quad \searrow \\
2 \qquad\quad 3 \\
\swarrow \;\; \searrow \quad \swarrow \;\; \searrow \\
4 \quad\;\; 5 \quad 6 \quad\;\; 7
\end{gathered}
$$
Populate each node's `next` pointer to point to its immediate horizontal right neighbor. If no right neighbor exists, set `next` to `NULL`.

At completion, the tree forms linked lists at every horizontal tier:
- Level 0: $1 \to \text{NULL}$
- Level 1: $2 \to 3 \to \text{NULL}$
- Level 2: $4 \to 5 \to 6 \to 7 \to \text{NULL}$

A standard BFS queue requires $O(W) = O(N)$ auxiliary memory to store nodes of a level.
However, because parent nodes at depth $d$ already have their `next` pointers linked, we can traverse level $d$ horizontally like a linked list, establishing all `next` pointers of level $d+1$ before descending. This accomplishes full level-order stitching in $O(N)$ time and strictly $O(1)$ extra space.

---

## 2. Conceptual Foundation & Invariants

### Two Connection Types Under a Parent Node
At level $d$, let `curr` be a node whose children reside at level $d+1$:
1. **Intra-Parent Connection (Same Parent):**
   Connect `curr.left` to `curr.right`:
   $$
   \text{curr.left.next} \leftarrow \text{curr.right}
   $$
   *(Example: Node $4 \to 5$, Node $6 \to 7$)*.
2. **Inter-Parent Connection (Cross-Subtree Gap):**
   If `curr.next` exists, connect `curr.right` across the gap to the left child of `curr.next`:
   $$
   \text{curr.right.next} \leftarrow \text{curr.next.left}
   $$
   *(Example: Node $5 \to 6$ via parent link $2 \to 3$)*.

### Horizontal Level-by-Level March Protocol
- Maintain `leftmost = root`.
- While `leftmost.left` is not null (has a child level to stitch):
  - Set `curr = leftmost`.
  - While `curr` is not null:
    - $\text{curr.left.next} = \text{curr.right}$
    - If `curr.next`: $\text{curr.right.next} = \text{curr.next.left}$
    - Advance across active tier: $\text{curr} = \text{curr.next}$
  - Descend to next tier: $\text{leftmost} = \text{leftmost.left}$.

> **Invariant.** Before stitching level $d+1$, all nodes at level $d$ are already fully connected via valid `next` pointers, enabling a complete horizontal traversal across depth $d$.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $[1, 2, 3, 4, 5, 6, 7]$:

### Level $d = 0$ (`leftmost = Node(1)`)
- `curr = Node(1)`. `curr.next = NULL`.
- Stitch children at Level 1:
  - **Intra-Parent:** Connect $1.\text{left}$ to $1.\text{right}$:
    $$
    \text{Node}(2).\text{next} \leftarrow \text{Node}(3)
    $$
  - `curr.next` is NULL $\implies$ no cross-parent link.
- Advance: `curr = curr.next = NULL`.
- Descend: `leftmost = leftmost.left = Node(2)`.
- Level 1 is now fully stitched: $2 \to 3 \to \text{NULL}$.

---

### Level $d = 1$ (`leftmost = Node(2)`)
- We traverse the linked list $2 \to 3$ to stitch Level 2:

#### At `curr = Node(2)`:
- **Intra-Parent Link:** Connect $2.\text{left}$ to $2.\text{right}$:
  $$
  \text{Node}(4).\text{next} \leftarrow \text{Node}(5)
$$
- **Inter-Parent Link:** `curr.next` is $\text{Node}(3)$.
  Connect $2.\text{right}$ to $3.\text{left}$:
  $$
  \text{Node}(5).\text{next} \leftarrow \text{Node}(3).\text{left} = \text{Node}(6)
  $$
- Advance: `curr = curr.next = Node(3)`.

#### At `curr = Node(3)`:
- **Intra-Parent Link:** Connect $3.\text{left}$ to $3.\text{right}$:
  $$
  \text{Node}(6).\text{next} \leftarrow \text{Node}(7)
  $$
- **Inter-Parent Link:** `curr.next` is NULL $\implies$ Node 7's `next` remains NULL.
- Advance: `curr = curr.next = NULL`.

The whole march can be read as pointer state rather than as prose. Each row is one
execution of the inner loop body, and the two write columns record exactly which
pointers change during that iteration:

| Horizontal step | Level $d$ | `curr` | `curr.next` | Intra-parent write | Inter-parent write | Next `curr` |
|:---:|:---:|:---:|:---:|:---|:---|:---:|
| 1 | 0 | $\text{Node}(1)$ | $\text{NULL}$ | $2.\text{next} \leftarrow 3$ | skipped: `curr.next` is NULL | $\text{NULL}$ (level-0 pass ends) |
| 2 | 1 | $\text{Node}(2)$ | $\text{Node}(3)$ | $4.\text{next} \leftarrow 5$ | $5.\text{next} \leftarrow 6$ | $\text{Node}(3)$ |
| 3 | 1 | $\text{Node}(3)$ | $\text{NULL}$ | $6.\text{next} \leftarrow 7$ | skipped: `curr.next` is NULL | $\text{NULL}$ (level-1 pass ends) |

Only step 2 performs both writes; step 1 has no horizontal successor to bridge to,
and step 3 writes the last intra-parent link of the tier. The `curr.next` column is
what makes the bridge legal: it is never read before the previous pass has
finished writing it.

---

### Level $d = 2$ (`leftmost = Node(4)`)
- `leftmost.left` is NULL (leaf level reached).
- Outer while loop terminates.

Reconstruction complete!
Output levels:
$1 \to \text{NULL}$
$2 \to 3 \to \text{NULL}$
$4 \to 5 \to 6 \to 7 \to \text{NULL}$.

---

## 4. Complete Execution Trace

```text
Level 0:           1 -> NULL
                  / \
Level 1:         2 -> 3 -> NULL
                / \   / \
Level 2:       4-> 5->6-> 7 -> NULL
```

| Active Level | Parent Node `curr` | Child Link Established | Connection Type | Target Equation |
|:---:|:---:|:---:|:---:|:---|
| 0 | $\text{Node}(1)$ | $\text{Node}(2) \to \text{Node}(3)$ | Intra-Parent | $\text{curr.left.next} = \text{curr.right}$ |
| 1 | $\text{Node}(2)$ | $\text{Node}(4) \to \text{Node}(5)$ | Intra-Parent | $\text{curr.left.next} = \text{curr.right}$ |
| 1 | $\text{Node}(2)$ | $\text{Node}(5) \to \text{Node}(6)$ | **Inter-Parent Gap** | $\text{curr.right.next} = \text{curr.next.left}$ |
| 1 | $\text{Node}(3)$ | $\text{Node}(6) \to \text{Node}(7)$ | Intra-Parent | $\text{curr.left.next} = \text{curr.right}$ |
| 1 | $\text{Node}(3)$ | $\text{Node}(7) \to \text{NULL}$ | Boundary Sentinel | `curr.next` is NULL |
| 2 | $\text{Node}(4)$ | - | Leaf Level | `leftmost.left` is NULL $\implies$ Terminate |

---

## 5. Algorithmic Correctness

**Soundness.** Every node in a perfect binary tree (except the root) is either the left or right child of some parent. Left children are connected directly to their right siblings. Right children are connected to the left child of their parent's horizontal successor (`curr.next`). Because depth $d$ is verified connected before depth $d+1$ begins, `curr.next` is always valid.

**Completeness.** Traversal visits every parent from leftmost to rightmost across every level until leaves are reached. Every non-leaf node executes both connection rules, ensuring no child node is missed.

---

## 6. Traps This Instance Exposes

- **Crossing the Subtree Boundary ($5 \to 6$):** Connecting siblings with the same parent ($4 \to 5$) is straightforward, but bridging nodes with different parents ($5 \to 6$) requires accessing `curr.next.left`. If `curr.next` is not yet established, this pointer lookup is impossible.
- **Assuming Imperfect Trees:** This algorithm relies on the problem statement's guarantee that the tree is *perfect* (all levels filled). For arbitrary binary trees with missing children, see LeetCode 117.
- **Empty Tree:** Checking `if not root: return root` upfront prevents null pointer exceptions.

The instance also separates the plausible strategies by *space*, not by
correctness — all three below produce the same three chains for $[1,2,3,4,5,6,7]$:

| Strategy | Auxiliary memory | Mechanism | Behaviour on this instance |
|:---|:---|:---|:---|
| Level-order queue | $O(W)$ where $W$ is a tier's width | Hold one entire tier in a FIFO, then wire consecutive dequeued nodes | Peak frontier is the 4 leaf nodes, so $O(N)$ here and in general |
| Recursive tier stitching | $O(h)$ stack frames | Pass the previous node of a tier down the recursion | Depth 3 for this input, so $\Theta(\log N)$ rather than constant |
| Parent-chain stitching (used above) | $O(1)$ | Read the already-linked tier $d$ chain to write tier $d+1$ | Only two live pointers, `leftmost` and `curr`, regardless of depth |

The parent-chain row is the one that satisfies the problem's constant-space
requirement, and it is available only because the union of the two write rules
touches every child exactly once.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. Each node is visited once as `curr`, performing $O(1)$ pointer reassignments.
- **Auxiliary Space Complexity:** $O(1)$ extra space, using only two pointers (`leftmost` and `curr`), strictly satisfying the constant-space requirement.