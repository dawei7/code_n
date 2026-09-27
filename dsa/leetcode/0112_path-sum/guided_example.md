# Guided Example: Path Sum

We trace the step-by-step root-to-leaf target reduction and leaf-terminal verification on a representative binary tree:

- **Input:** $\text{root} = [5, 4, 8, 11, \text{null}, 13, 4, 7, 2, \text{null}, \text{null}, \text{null}, 1]$, $\text{targetSum} = 22$
- **Required output:** $\text{True}$ (Path $5 \to 4 \to 11 \to 2 = 22$)
- **Internal Node Sum Trap:** $\text{root} = [1, 2], \text{targetSum} = 1 \implies \text{False}$ (Root 1 is not a leaf)

This instance demonstrates recursive subtraction of node values along search paths ($\text{rem} \leftarrow \text{rem} - \text{node.val}$), enforcing that paths strictly terminate at true leaf nodes ($\text{left} = \text{right} = \emptyset$), short-circuiting on the first valid leaf, and handling empty root trees in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
$$
\begin{gathered}
5 \\
\swarrow \qquad \searrow \\
4 \qquad\qquad\quad 8 \\
\swarrow \qquad\qquad \swarrow \quad \searrow \\
11 \qquad\qquad\quad 13 \qquad\quad 4 \\
\swarrow \quad \searrow \qquad\qquad\qquad\qquad \searrow \\
7 \qquad\quad 2 \qquad\qquad\qquad\qquad\quad 1
\end{gathered}
$$
and $\text{targetSum} = 22$, determine if there exists a **root-to-leaf path** whose sum equals $22$.

Consider the path candidates:
1. $5 \to 4 \to 11 \to 7 = 27 \ne 22$
2. $5 \to 4 \to 11 \to 2 = 22$ (Leaf node $2$: $22 == 22$, **Valid!**)
3. $5 \to 8 \to 13 = 26 \ne 22$
4. $5 \to 8 \to 4 \to 1 = 18 \ne 22$

Notice the crucial constraint: **the path must end at a leaf node**.
In the tree $[1, 2]$ with $\text{targetSum} = 1$, the root node has value $1$, but it has a child ($2$) and is therefore **not** a leaf. The only root-to-leaf path is $1 \to 2 = 3 \ne 1$, so the answer is `False`.

Subtracting values downward transforms the problem into testing if any leaf node has value equal to the remaining target.

---

## 2. Conceptual Foundation & Invariants

### Subtractive Leaf DFS Protocol
We define $\text{hasPathSum}(\text{node}, \text{rem})$:

1. **Empty Node Base Case:**
   If $\text{node} == \emptyset$: return $\text{False}$.
2. **Leaf Node Verification:**
   If $\text{node.left} == \emptyset$ and $\text{node.right} == \emptyset$:
   - The path has reached a true leaf.
   - Return $\text{True}$ if and only if $\text{node.val} == \text{rem}$:
     $$
     \text{return } (\text{node.val} == \text{rem})
     $$
3. **Internal Node Branching:**
   Subtract the current node's value and recurse on both subtrees:
   $$
   \text{hasPathSum}(\text{node.left}, \, \text{rem} - \text{node.val}) \lor \text{hasPathSum}(\text{node.right}, \, \text{rem} - \text{node.val})
   $$

> **Invariant.** At any node $u$ at depth $d$, $\text{rem}$ equals $\text{targetSum} - \sum_{v \in \text{ancestors}(u)} v.\text{val}$. The problem reduces to finding whether any leaf in $u$'s subtree sums to $\text{rem}$.

---

## 3. Step-by-Step Worked Execution

We trace the target reduction on the successful path $5 \to 4 \to 11 \to 2$ with $\text{targetSum} = 22$:

### Step 1: Root Node 5
- `node.val = 5`, `rem = 22`.
- Not a leaf (has children 4 and 8).
- Update remaining target for children:
  $$
  \text{rem}' = 22 - 5 = 17
  $$
- Recurse left: $\text{hasPathSum}(\text{Node}(4), 17)$.

---

### Step 2: Node 4 (Left child of 5)
- `node.val = 4`, `rem = 17`.
- Not a leaf (has child 11).
- Update remaining target:
  $$
  \text{rem}' = 17 - 4 = 13
  $$
- Recurse left: $\text{hasPathSum}(\text{Node}(11), 13)$.

---

### Step 3: Node 11 (Left child of 4)
- `node.val = 11`, `rem = 13`.
- Not a leaf (has children 7 and 2).
- Update remaining target:
  $$
  \text{rem}' = 13 - 11 = 2
  $$
- Probe left child: $\text{hasPathSum}(\text{Node}(7), 2)$.
  - Node 7 is a leaf ($\text{left} = \text{right} = \emptyset$).
  - Value check: $7 == 2 \implies \text{False}$.
- Probe right child: $\text{hasPathSum}(\text{Node}(2), 2)$.

---

### Step 4: Node 2 (Right child of 11)
- `node.val = 2`, `rem = 2`.
- Inspect children: $\text{left} == \emptyset$ and $\text{right} == \emptyset$.
- **Leaf Detected!**
- Evaluate leaf condition:
  $$
  \text{node.val} == \text{rem} \implies 2 == 2 \quad (\textbf{True})
  $$
- **Match Found!** Returns $\text{True}$.

The boolean `True` propagates up the call stack, short-circuiting remaining branches.

---

## 4. Complete Execution Trace

```text
                     (5, rem=22)
                     /         \
              (4, rem=17)     (8, rem=17)
               /               /         \
        (11, rem=13)     (13, rem=9)   (4, rem=9)
         /        \          |             \
    (7, rem=2)  (2, rem=2) (Leaf 13!=9)   (1, rem=5)
   (Leaf 7!=2)  (Leaf 2==2)               (Leaf 1!=5)
      [F]          [T] -> SUCCESS
```

| Traversal Frame | Node Visited | Node Value | Incoming $\text{rem}$ | Is Leaf? | Action / Evaluation | Subtree Return |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | $\text{Node}(5)$ | 5 | 22 | No | Recurse left with $\text{rem} = 17$ | Pending |
| 1.1 | $\text{Node}(4)$ | 4 | 17 | No | Recurse left with $\text{rem} = 13$ | Pending |
| 1.1.1 | $\text{Node}(11)$ | 11 | 13 | No | Recurse children with $\text{rem} = 2$ | Pending |
| 1.1.1.1 | $\text{Node}(7)$ | 7 | 2 | **Yes** | Compare $7 == 2$ | **False** |
| **1.1.1.2** | **$\text{Node}(2)$** | **2** | **2** | **Yes** | **Compare $2 == 2$** | **True (Target Met)** |
| Return | - | - | - | - | Short-circuit $\lor$ to root | **True** |

---

## 5. Algorithmic Correctness

**Soundness.** Subtracting values along the path ensures that when reaching any leaf, $\text{node.val} == \text{rem}$ holds if and only if the sum of all nodes from the root down to that leaf equals $\text{targetSum}$. Testing `not node.left and not node.right` strictly enforces that matches are accepted only at true tree leaves.

**Completeness.** Preorder DFS searches all root-to-leaf paths. If any valid path exists, it evaluates to `True`. If no path sums to `targetSum`, all leaf checks return `False`, correctly concluding `False`.

---

## 6. Traps This Instance Exposes

- **Terminating on Non-Leaf Zero Remainder:** If a node has value equal to $\text{rem}$ but has children (e.g. $[1, 2]$ with target 1), it is not a leaf. Checking `not node.left and not node.right` prevents premature termination.
- **Empty Tree Root:** An empty tree $\text{root} = \emptyset$ has no leaves and no paths, returning `False` for any `targetSum` (including $\text{targetSum} = 0$).
- **Negative Node Values:** Tree node values can be negative (e.g. $-10 \dots 1000$). Never prune branches based on `rem < 0`, because adding negative descendants can restore the sum.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. In the worst case (no path matches), every node is visited once in $O(1)$ time.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the tree height, for the recursion call stack ($O(\log N)$ average, $O(N)$ worst case).