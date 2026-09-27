# Guided Example: Binary Tree Upside Down

We trace the step-by-step left-spine pointer rotation and sibling-parent rewiring on representative binary tree instances:

- **Input:** $\text{root} = [1, 2, 3, 4, 5]$
- **Required output:** $[4, 5, 2, \text{null}, \text{null}, 3, 1]$ (Node 4 becomes new root, with 5 as left child and 2 as right child)
- **Base Instances:** $\text{root} = [] \implies [], \quad \text{root} = [1] \implies [1]$

This instance demonstrates in-place structural tree inversion (original left child becomes parent, original right child becomes left child, and original parent becomes right child), models the transformation as left-spine linked list reversal with sibling preservation, and achieves $O(N)$ linear time with strictly $O(1)$ auxiliary memory.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree with the structural guarantee that every node has either 0 or 2 children, and all right nodes are leaf nodes:
$$
\begin{gathered}
1 \\
\swarrow \quad \searrow \\
2 \qquad\quad 3 \\
\swarrow \;\; \searrow \qquad\qquad \\
4 \quad\;\; 5 \qquad\qquad
\end{gathered}
$$
Turn the binary tree upside down such that:
1. The original **left child** becomes the new **root**.
2. The original **right child** becomes the new **left child**.
3. The original **root** becomes the new **right child**.

Applying the rules to the subsegments:
- For node 2 with children 4 and 5: 4 becomes root, 5 becomes 4's left child, and 2 becomes 4's right child.
- For node 1 with child 2 and right sibling 3: 3 becomes 2's left child, and 1 becomes 2's right child.
- Node 1 becomes a leaf with both children set to null.
The resulting inverted tree:
$$
\begin{gathered}
4 \\
\swarrow \quad \searrow \\
5 \qquad\quad 2 \\
\qquad\qquad \swarrow \;\; \searrow \\
\qquad\qquad 3 \quad\;\; 1
\end{gathered}
$$
Level-order output: $[4, 5, 2, \text{null}, \text{null}, 3, 1]$.

A top-down recursive solution uses $O(H)$ stack frames.
The transformation can be understood as an iterative single-linked list reversal along the left spine: as we descend down the left children ($1 \to 2 \to 4$), we reverse the spine pointers while wiring the right siblings into left positions in $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### Iterative Left-Spine Reversal Protocol
Maintain three tracking pointers:
- `curr`: current node along the left spine (starts at `root`).
- `prev`: original parent of `curr` (starts as $\emptyset$).
- `prev_right`: original right sibling of `curr` (starts as $\emptyset$).

While `curr` is not null:
1. **Cache Descendants:**
   $$
   \text{next\_node} = \text{curr.left}
   $$
   $$
   \text{next\_right} = \text{curr.right}
   $$
2. **Rewire Current Node:**
   - Attach original sibling as new left child:
     $$
     \text{curr.left} \leftarrow \text{prev\_right}
     $$
   - Attach original parent as new right child:
     $$
     \text{curr.right} \leftarrow \text{prev}
     $$
3. **Advance Pointers Down Left Spine:**
   $$
   \text{prev} \leftarrow \text{curr}
   $$
   $$
   \text{prev\_right} \leftarrow \text{next\_right}
   $$
   $$
   \text{curr} \leftarrow \text{next\_node}
   $$

When `curr` becomes null, `prev` holds the new root of the upside-down tree.

> **Invariant.** Before processing `curr`, the subtree rooted at `prev` is already completely inverted, and `prev_right` holds the sibling waiting to attach to `curr`.

---

## 3. Step-by-Step Worked Execution

We trace the iterative rewiring on $\text{root} = [1, 2, 3, 4, 5]$:
Initial: `curr = Node(1), prev = null, prev_right = null`.

---

### Step 1: Process Node 1
- Cache forward links:
  - $\text{next\_node} = \text{Node}(1).\text{left} = \text{Node}(2)$.
  - $\text{next\_right} = \text{Node}(1).\text{right} = \text{Node}(3)$.
- Rewire Node 1:
  - $\text{Node}(1).\text{left} = \text{prev\_right} = \text{null}$.
  - $\text{Node}(1).\text{right} = \text{prev} = \text{null}$.
  - *(Node 1 is now a leaf!)*
- Advance:
  - $\text{prev} = \text{Node}(1)$.
  - $\text{prev\_right} = \text{Node}(3)$.
  - $\text{curr} = \text{Node}(2)$.

---

### Step 2: Process Node 2
- Cache forward links:
  - $\text{next\_node} = \text{Node}(2).\text{left} = \text{Node}(4)$.
  - $\text{next\_right} = \text{Node}(2).\text{right} = \text{Node}(5)$.
- Rewire Node 2:
  - $\text{Node}(2).\text{left} = \text{prev\_right} = \mathbf{\text{Node}(3)}$.
  - $\text{Node}(2).\text{right} = \text{prev} = \mathbf{\text{Node}(1)}$.
  - *(Node 2 now has children 3 and 1!)*
- Advance:
  - $\text{prev} = \text{Node}(2)$.
  - $\text{prev\_right} = \text{Node}(5)$.
  - $\text{curr} = \text{Node}(4)$.

---

### Step 3: Process Node 4
- Cache forward links:
  - $\text{next\_node} = \text{Node}(4).\text{left} = \text{null}$.
  - $\text{next\_right} = \text{Node}(4).\text{right} = \text{null}$.
- Rewire Node 4:
  - $\text{Node}(4).\text{left} = \text{prev\_right} = \mathbf{\text{Node}(5)}$.
  - $\text{Node}(4).\text{right} = \text{prev} = \mathbf{\text{Node}(2)}$.
  - *(Node 4 now has children 5 and 2!)*
- Advance:
  - $\text{prev} = \text{Node}(4)$.
  - $\text{prev\_right} = \text{null}$.
  - $\text{curr} = \text{null}$.

---

### Termination
- `curr` is null.
- Return `prev = Node(4)` as the new root.

Final structure verified:
- $\text{Node}(4): \text{left}=5, \text{right}=2$.
- $\text{Node}(2): \text{left}=3, \text{right}=1$.
- $\text{Node}(5), \text{Node}(3), \text{Node}(1)$: all children are null.
Result: $[4, 5, 2, \text{null}, \text{null}, 3, 1]$.

---

## 4. Complete Execution Trace

```text
Initial Tree:                         Inverted Tree:
     1                                     4
    / \                                   / \
   2   3                                 5   2
  / \                                       / \
 4   5                                     3   1
```

| Step | Active Node `curr` | Cached Next Left | Cached Next Right | Reassigned Left (`curr.left`) | Reassigned Right (`curr.right`) | Advance `prev` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $\text{Node}(1)$ | $\text{Node}(2)$ | $\text{Node}(3)$ | $\text{null}$ | $\text{null}$ | $\text{Node}(1)$ |
| 2 | $\text{Node}(2)$ | $\text{Node}(4)$ | $\text{Node}(5)$ | **$\text{Node}(3)$** | **$\text{Node}(1)$** | $\text{Node}(2)$ |
| **3** | **$\text{Node}(4)$** | **$\text{null}$** | **$\text{null}$** | **$\text{Node}(5)$** | **$\text{Node}(2)$** | **$\text{Node}(4)$ (New Root)** |
| End | $\emptyset$ | - | - | - | - | **Return $\text{Node}(4)$** |

---

## 5. Algorithmic Correctness

**Soundness.** At each level along the left spine, the algorithm explicitly assigns the right sibling to `curr.left` and the parent to `curr.right`. Because the problem guarantees all right nodes are childless leaves, attaching them as left children cannot create cycles or overwrite non-empty subtrees.

**Completeness.** Since every non-leaf node along the spine is visited until the deepest left node is reached, all nodes in the original tree are rewired into the new tree structure without omitting any subtree.

---

## 6. Traps This Instance Exposes

- **Overwriting Child References Before Caching:** Attempting to assign `curr.left = prev_right` before saving `curr.left` destroys the pointer to the rest of the left spine! Caching both `next_node` and `next_right` before reassignment is mandatory.
- **Original Root Children:** The original root (Node 1) must have both `left` and `right` set to null; failing to nullify them creates a cycle ($1 \to 2$ and $2 \to 1$).
- **Single Node or Empty Tree:** If `root is None` or `root.left is None`, the loop terminates immediately and returns `root` unchanged.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(H) = O(N)$ time, where $H$ is the height of the left spine (which is bounded by $N/2$ nodes). Each step performs $O(1)$ pointer swaps.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory, using only scalar pointer references without recursion or heap allocations.