# Guided Example: Recover Binary Search Tree

We trace the step-by-step detection and swap of two misplaced nodes via inorder traversal on representative corrupted binary search trees:

- **Input:** $\text{root} = [1, 3, \text{null}, \text{null}, 2]$
- **Required output:** $[3, 1, \text{null}, \text{null}, 2]$
- **Adjacent Swap Instance:** $\text{root} = [3, 1, 4, \text{null}, \text{null}, 2] \implies [2, 1, 4, \text{null}, \text{null}, 3]$

This instance demonstrates exploiting the strictly increasing property of BST inorder traversals, identifying the two inversion points ($\text{prev.val} > \text{cur.val}$), distinguishing non-adjacent vs adjacent swapped nodes, and repairing node values in $O(1)$ space using Morris traversal.

---

## 1. Instance & Teaching Goal

In a valid Binary Search Tree (BST), exactly two nodes have had their values swapped by mistake. Recover the tree without changing its structural links.

Given the tree $[1, 3, \text{null}, \text{null}, 2]$:
$$
\begin{gathered}
1 \\
\swarrow \\
3 \\
\quad \searrow \\
\qquad 2
\end{gathered}
$$
Performing an inorder traversal (Left $\to$ Root $\to$ Right):
$$
[3, \, 2, \, 1]
$$
A correct BST must yield a strictly increasing inorder sequence ($[1, 2, 3]$).
Here, two inversions occur:
1. $3 > 2$: Node $3$ is too large to precede $2$.
2. $2 > 1$: Node $1$ is too small to follow $2$.
The two swapped values are $3$ and $1$. Exchanging their values restores the valid BST.

A naive approach extracts all values into an array, sorts the array, and rewrites tree values in $O(N)$ auxiliary memory.
By tracking predecessors during an inorder traversal, the two misplaced nodes `first` and `second` can be identified directly and swapped in place in $O(1)$ space via Morris threading.

---

## 2. Conceptual Foundation & Invariants

### Inorder Inversion Detection Protocol
When traversing a sorted array where two elements have been swapped:
- **Case 1: Non-adjacent swap (e.g. $[1, \mathbf{5}, 3, 4, \mathbf{2}, 6]$ where $5$ and $2$ are swapped):**
  There are two distinct drops where $\text{prev} > \text{curr}$:
  - First drop ($5 > 3$): The misplaced larger element is the **first** element $\text{prev}$ ($5$).
  - Second drop ($4 > 2$): The misplaced smaller element is the **second** element $\text{curr}$ ($2$).
- **Case 2: Adjacent swap (e.g. $[1, 2, \mathbf{4}, \mathbf{3}, 5, 6]$ where $4$ and $3$ are swapped):**
  There is only one drop ($4 > 3$):
  - Misplaced elements are $\text{prev}$ ($4$) and $\text{curr}$ ($3$).

### Tracking Invariants
Maintain pointers `first`, `second`, and `prev` (initially `None`):
During inorder traversal:
- If $\text{prev}$ exists and $\text{prev.val} > \text{cur.val}$:
  - If `first` is null:
    $$
    \text{first} \leftarrow \text{prev}, \quad \text{second} \leftarrow \text{cur}
    $$
    *(Assigning `second = cur` handles the adjacent swap case in case a second drop never occurs)*.
  - Else (`first` is already found):
    $$
    \text{second} \leftarrow \text{cur}
    $$
- Advance predecessor: $\text{prev} \leftarrow \text{cur}$.

After completing the traversal:
$$
\text{first.val}, \, \text{second.val} \leftarrow \text{second.val}, \, \text{first.val}
$$

> **Invariant.** After the full traversal, `first` points to the node whose original value was swapped forward, and `second` points to the node whose original value was swapped backward.

---

## 3. Step-by-Step Worked Execution

We trace the inorder traversal on $\text{root} = [1, 3, \text{null}, \text{null}, 2]$:

### Traversal Order
The inorder path visits nodes in order:
1. Node with value 3 (leftmost leaf).
2. Node with value 2 (right child of 3).
3. Node with value 1 (root).

---

### Step 1: Visit Node 3
- `prev` is `None`.
- Update predecessor: $\text{prev} \leftarrow \text{Node}(3)$.

---

### Step 2: Visit Node 2
- Check condition: $\text{prev.val} = 3 > \text{cur.val} = 2$ ($3 > 2$).
- **First Inversion Detected!**
  - Record: $\text{first} \leftarrow \text{Node}(3)$.
  - Record: $\text{second} \leftarrow \text{Node}(2)$ (tentative).
- Update predecessor: $\text{prev} \leftarrow \text{Node}(2)$.

---

### Step 3: Visit Node 1
- Check condition: $\text{prev.val} = 2 > \text{cur.val} = 1$ ($2 > 1$).
- **Second Inversion Detected!**
  - `first` is already set to $\text{Node}(3)$.
  - Update: $\text{second} \leftarrow \text{Node}(1)$.
- Update predecessor: $\text{prev} \leftarrow \text{Node}(1)$.

---

### Value Recovery
- Swapped nodes identified:
  - $\text{first} = \text{Node}(3)$
  - $\text{second} = \text{Node}(1)$
- Swap values:
  $$
  \text{Node}(3).\text{val} \leftarrow 1, \quad \text{Node}(1).\text{val} \leftarrow 3
  $$
- Recovered inorder sequence: $[1, 2, 3]$.

Tree successfully repaired.

---

### The Same Traversal with Morris Threads

The detection above needs only `first`, `second`, and `prev`, so the $O(1)$ version weaves temporary right-pointers instead of pushing a stack. For this tree the predecessor of the root is the rightmost node of its left subtree: starting at node $3$, the walk follows right pointers as far as possible, and $3$'s right child is node $2$, which has no right child of its own.

| Visit | Active `cur` | `cur.left` | Predecessor found | Thread action | Emitted value | Inorder so far |
|:---:|:---:|:---:|:---|:---|:---:|:---|
| 1 | $\text{Node}(1)$ | $\text{Node}(3)$ | $\text{Node}(2)$ | Set `2.right = 1` | none | `[]` |
| 2 | $\text{Node}(3)$ | `None` | Not needed | None | `3` | `[3]` |
| 3 | $\text{Node}(2)$ | `None` | Not needed | None | `2` | `[3, 2]` |
| 4 | $\text{Node}(1)$ | $\text{Node}(3)$ | $\text{Node}(2)$, reached through the thread | Restore `2.right = None` | `1` | `[3, 2, 1]` |
| 5 | `None` | — | Not needed | None | Halt | `[3, 2, 1]` |

Visits 2 and 3 are the two comparisons that raise the drops, and visit 4 both undoes the thread and completes the traversal. The tree is structurally identical at the end of visit 4, and the two misplaced nodes are then exchanged in place, so no link is ever rewritten permanently.

---

## 4. Complete Execution Trace

### Non-Adjacent Swap Trace ($[1, 3, \text{null}, \text{null}, 2]$)

| Step | Visited Node $\text{cur}$ | Previous Node $\text{prev}$ | Inversion Check ($\text{prev.val} > \text{cur.val}$) | First Candidate | Second Candidate | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $\text{Node}(3)$ | `None` | - | `None` | `None` | Set $\text{prev} = \text{Node}(3)$ |
| 2 | $\text{Node}(2)$ | $\text{Node}(3)$ | $3 > 2$ (Inversion 1) | $\text{Node}(3)$ | $\text{Node}(2)$ | First drop: record both |
| 3 | $\text{Node}(1)$ | $\text{Node}(2)$ | $2 > 1$ (Inversion 2) | $\text{Node}(3)$ | $\text{Node}(1)$ | Second drop: update second |
| Post | - | - | - | $\text{Node}(3)$ | $\text{Node}(1)$ | **Swap values: $3 \leftrightarrow 1$** |

### Adjacent Swap Comparison ($[3, 1, 4, \text{null}, \text{null}, 2] \implies \text{Inorder: } [1, \mathbf{3}, \mathbf{2}, 4]$)
- At $3 > 2$: First drop sets $\text{first} = \text{Node}(3), \text{second} = \text{Node}(2)$.
- Next step: $2 < 4$ (no second drop).
- Result: Swaps $\text{Node}(3)$ and $\text{Node}(2)$, correctly handling adjacent inversions.

---

## 5. Algorithmic Correctness

**Soundness.** Swapping two elements in a strictly increasing sequence creates either two inversions (if non-adjacent) or one inversion (if adjacent). In both cases, the first inversion's leading element is the misplaced large value, and the last inversion's trailing element is the misplaced small value. Exchanging their values restores the strictly increasing inorder sequence required of a BST.

**Completeness.** Inorder traversal visits every node in the binary tree. Since exactly two nodes were swapped, all other pairs remain strictly monotonic, guaranteeing that the search logic isolates precisely the two corrupted nodes.

---

## 6. Traps This Instance Exposes

Two elements are out of place, so the inorder sequence differs from sorted order in a very specific way. Each row below states the sequence that is actually observed, the drops it contains, and the pair the algorithm selects:

| Scenario | Observed inorder sequence | Inversions detected | `first` / `second` | Repair performed |
|:---|:---|:---|:---|:---|
| Traced non-adjacent instance | $[3, 2, 1]$ | $3 > 2$, then $2 > 1$ | node holding $3$ / node holding $1$ | Exchange $3 \leftrightarrow 1$, giving $[1, 2, 3]$. |
| Adjacent instance `[3, 1, 4, null, null, 2]` | $[1, 3, 2, 4]$ | one drop, $3 > 2$ | node holding $3$ / node holding $2$, assigned at that same drop | Exchange $3 \leftrightarrow 2$, giving $[1, 2, 3, 4]$ and the serialization `[2, 1, 4, null, null, 3]`. |
| Root children exchanged `[2, 3, 1]` | $[3, 2, 1]$ | $3 > 2$, then $2 > 1$ | node holding $3$ / node holding $1$ | Exchange $3 \leftrightarrow 1$; the root keeps its value and the serialization becomes `[2, 1, 3]`. |
| Smallest legal tree `[1, 2]` | $[2, 1]$ | one drop, $2 > 1$ | node holding $2$ / node holding $1$ | Exchange $2 \leftrightarrow 1$, giving the serialization `[2, 1]`; the minimum size of $2$ nodes is handled by the same rule. |
| Extreme stored values | A strictly increasing run interrupted at exactly one or two places | detected by direct comparison only | whichever nodes hold the two extreme values | Safe over the whole range $-2^{31} \le \text{val} \le 2^{31} - 1$, because the test compares two stored values and never forms their difference. |

The single-drop row is the trap: if the second node were only recorded on a *second* drop, an adjacent swap would leave `second` unset and no repair would happen.

- **Adjacent Inversion Trap:** If the two swapped nodes are adjacent in inorder traversal (e.g. $[1, 3, 2, 4]$), only a single inversion occurs ($3 > 2$). Initializing $\text{second} = \text{cur}$ at the first inversion ensures that adjacent swaps are resolved even when no second drop occurs.
- **Modifying Pointers vs Values:** The problem requires fixing the tree without altering its topology (i.e. keep node links identical and swap only the `val` attributes).
- **Constant Memory Guarantee:** Using recursion or an explicit stack takes $O(H)$ auxiliary memory. To satisfy the optimal $O(1)$ memory requirement, Morris Inorder Traversal can be used to weave and unweave temporary threads without call-stack overhead.

---

## 7. Complexity Derivation

Every strategy below finds the same two nodes; only the memory they spend to do it changes:

| Strategy | Auxiliary space | How the two nodes surface | Failure mode to guard against |
|:---|:---|:---|:---|
| Copy values, sort, write back | $O(N)$ for the copied list | The sorted list is compared position by position with a second inorder pass, and the positions that differ are the two corrupted nodes | Correct and simple, but it needs a second full traversal to push the sorted values back and it violates the constant-space follow-up. |
| Recursive inorder | $O(H)$ call frames | Each recursive visit compares its value with the value recorded by the previous visit | The depth tracks the tree height, so a chain of $1000$ nodes consumes $1000$ frames. |
| Explicit stack inorder | $O(H)$ stack entries | Each popped node is compared with the last value emitted | On a fully skewed tree $H = N$, so this is no better than the copied list. |
| Morris inorder | $O(1)$ | The same predecessor comparison, evaluated while the temporary threads are woven and unwoven | A thread left in place on the second visit corrupts the tree that the caller still owns — here it would also break the validation pass that serializes the repaired root. |

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. Each node is visited at most twice during Morris traversal (or once during standard inorder recursion).
- **Auxiliary Space Complexity:** $O(1)$ when implemented with Morris traversal, or $O(H)$ when using stack/recursive traversal.
