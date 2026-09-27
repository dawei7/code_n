# Guided Example: Flatten Binary Tree to Linked List

We trace the step-by-step in-place binary tree flattening using Morris predecessor splicing and reverse post-order recursion on a representative tree:

- **Input:** $\text{root} = [1, 2, 5, 3, 4, \text{null}, 6]$
- **Required output:** $[1, \text{null}, 2, \text{null}, 3, \text{null}, 4, \text{null}, 5, \text{null}, 6]$
- **Base Instance:** $\text{root} = [] \implies \emptyset, \quad \text{root} = [0] \implies [0]$

This instance demonstrates in-place structural tree transformation to match preorder sequence, locating the inorder predecessor's rightmost leaf, splicing original right subtrees onto left tails, nullifying left pointers, and contrasting $O(1)$-space Morris flattening against reverse post-order recursion.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
$$
\begin{gathered}
1 \\
\swarrow \quad \searrow \\
2 \qquad\quad 5 \\
\swarrow \;\; \searrow \qquad\quad \searrow \\
3 \quad\;\; 4 \qquad\qquad 6
\end{gathered}
$$
flatten the tree into a "linked list" in place:
1. The linked list must use the same `TreeNode` class where the `right` child pointer points to the next node and the `left` child pointer is always `None`.
2. The nodes must appear in the exact order of a **pre-order traversal** ($1 \to 2 \to 3 \to 4 \to 5 \to 6$).

A naive approach traverses the tree, collects node references into a list, and rewires pointers in a second pass in $O(N)$ auxiliary memory.
Using Morris predecessor splicing, we rewire pointers strictly in-place: for each node with a left child, its original right subtree is attached to the rightmost leaf of its left subtree, eliminating left branches in $O(N)$ time and strictly $O(1)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

### Method 1: Morris Predecessor Splicing ($O(1)$ Space)
Maintain a pointer `cur = root`.
While `cur` is not null:
1. **Left Child Check:**
   If `cur.left` exists:
   - Find the rightmost node of `cur.left` (the predecessor that will immediately precede `cur.right` in preorder):
     $$
     \text{pred} = \text{cur.left}
     $$
     $$
     \text{while pred.right:} \quad \text{pred} = \text{pred.right}
     $$
   - Splice `cur.right` onto `pred.right`:
     $$
     \text{pred.right} \leftarrow \text{cur.right}
     $$
   - Move the entire left subtree to `cur.right`:
     $$
     \text{cur.right} \leftarrow \text{cur.left}
     $$
     $$
     \text{cur.left} \leftarrow \emptyset
     $$
2. **Advance Spine:**
   $$
   \text{cur} \leftarrow \text{cur.right}
   $$

### Method 2: Reverse Post-Order Recursion
Traverse in reverse preorder (Right $\to$ Left $\to$ Root) while maintaining a global reference `prev = None`:
- $\text{flatten}(\text{node.right})$
- $\text{flatten}(\text{node.left})$
- $\text{node.right} = \text{prev}$
- $\text{node.left} = \emptyset$
- $\text{prev} = \text{node}$

> **Invariant.** Under Morris splicing, every node preceding `cur` on the right spine has `left = None` and its `right` pointer correctly references its immediate preorder successor.

---

## 3. Step-by-Step Worked Execution

We trace Morris Splicing on $\text{root} = [1, 2, 5, 3, 4, \text{null}, 6]$:

### Step 1: At `cur = Node(1)`
- `cur.left` exists ($\text{Node}(2)$).
- Find rightmost descendant of $\text{Node}(2)$:
  - $\text{Node}(2).\text{right} = \text{Node}(4)$.
  - $\text{Node}(4).\text{right} = \emptyset \implies \text{pred} = \text{Node}(4)$.
- **Splice Operations:**
  1. Attach 1's right subtree to 4: $\text{Node}(4).\text{right} \leftarrow \text{Node}(5)$.
  2. Shift left subtree to right: $\text{Node}(1).\text{right} \leftarrow \text{Node}(2)$.
  3. Clear left pointer: $\text{Node}(1).\text{left} \leftarrow \emptyset$.
- Tree structure:
  $$
  1 \longrightarrow 2 \longrightarrow (3, \; 4 \longrightarrow 5 \longrightarrow 6)
  $$
- Advance: $\text{cur} \leftarrow \text{Node}(2)$.

---

### Step 2: At `cur = Node(2)`
- `cur.left` exists ($\text{Node}(3)$).
- Find rightmost descendant of $\text{Node}(3)$:
  - $\text{Node}(3).\text{right} = \emptyset \implies \text{pred} = \text{Node}(3)$.
- **Splice Operations:**
  1. Attach 2's right subtree to 3: $\text{Node}(3).\text{right} \leftarrow \text{Node}(4)$.
  2. Shift left subtree to right: $\text{Node}(2).\text{right} \leftarrow \text{Node}(3)$.
  3. Clear left pointer: $\text{Node}(2).\text{left} \leftarrow \emptyset$.
- Tree structure:
  $$
  1 \longrightarrow 2 \longrightarrow 3 \longrightarrow 4 \longrightarrow 5 \longrightarrow 6
  $$
- Advance: $\text{cur} \leftarrow \text{Node}(3)$.

---

### Step 3: At `cur = Node(3)` through `Node(6)`
- `cur.left` is $\emptyset$ for all remaining nodes $3, 4, 5, 6$.
- Pointer simply advances along the right spine:
  - $\text{Node}(3) \to \text{Node}(4) \to \text{Node}(5) \to \text{Node}(6) \to \emptyset$.
- Loop terminates.

Final tree: $1 \to 2 \to 3 \to 4 \to 5 \to 6$ (all `left` pointers are null).

---

## 4. Complete Execution Trace

```text
Initial Tree:               After Step 1 (cur=1):        After Step 2 (cur=2):
      1                           1                            1
     / \                           \                            \
    2   5                           2                            2
   / \   \                         / \                            \
  3   4   6                       3   4                            3
                                       \                            \
                                        5                            4
                                         \                            \
                                          6                            5
                                                                        \
                                                                         6
```

| Step | Active Node `cur` | Left Child Exists? | Predecessor Leaf `pred` | Splicing Action (`pred.right = cur.right`) | Subtree Shift |
|:---:|:---:|:---:|:---:|:---|:---|
| 1 | $\text{Node}(1)$ | Yes ($\text{Node}(2)$) | $\text{Node}(4)$ | $\text{Node}(4).\text{right} \to \text{Node}(5)$ | $1.\text{right} \to 2, 1.\text{left} \to \emptyset$ |
| 2 | $\text{Node}(2)$ | Yes ($\text{Node}(3)$) | $\text{Node}(3)$ | $\text{Node}(3).\text{right} \to \text{Node}(4)$ | $2.\text{right} \to 3, 2.\text{left} \to \emptyset$ |
| 3 | $\text{Node}(3)$ | No | - | Advance `cur` | None |
| 4 | $\text{Node}(4)$ | No | - | Advance `cur` | None |
| 5 | $\text{Node}(5)$ | No | - | Advance `cur` | None |
| 6 | $\text{Node}(6)$ | No | - | Advance `cur` | None |
| Exit | $\emptyset$ | - | - | Complete linear chain | **$1 \to 2 \to 3 \to 4 \to 5 \to 6$** |

---

## 5. Algorithmic Correctness

**Soundness.** In a preorder traversal ($R \to L \to \text{Right}$), all nodes in the left subtree are visited before any node in the right subtree. The very last node visited in the left subtree is the rightmost node of that subtree. Splicing `cur.right` onto this rightmost leaf guarantees that when traversal leaves the left branch, it transitions immediately to the original right branch.

**Completeness.** Moving `cur.left` to `cur.right` and clearing `cur.left` guarantees that all left children are eliminated and converted into a single right spine. Since `cur` advances along the right pointers, every node in the tree is processed.

---

## 6. Traps This Instance Exposes

- **Forgetting to Nullify Left Pointers:** Leaving `node.left` pointing to the old child causes test case rejections because LeetCode verifies that all `left` references are strictly `None`.
- **Finding Predecessor on Empty Left Child:** Only find `pred` when `cur.left` is non-null. If `cur.left` is null, advance directly to `cur.right`.
- **Predecessor Traversal Boundary:** When searching for `pred`, only advance right: `while pred.right: pred = pred.right`. Do not advance left.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Although there is a nested while loop to find predecessors, each edge in the tree is traversed at most twice (once to find the predecessor and once when `cur` visits it).
- **Auxiliary Space Complexity:** $O(1)$ constant memory for Morris splicing, modifying existing tree pointers in place without recursion stack or heap allocations.