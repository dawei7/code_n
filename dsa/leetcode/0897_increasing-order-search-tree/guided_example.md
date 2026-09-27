# Guided Example: Increasing Order Search Tree

We trace the step-by-step in-order traversal of a binary search tree (BST), in-place pointer relinking using a sentinel dummy node, nullification of left-child pointers to prevent cyclic structures, and linear transformation into a strictly right-skewed tree:

- **Representative Input Tree:**
  $$
  \text{root} = [5, 3, 6, 2, 4, \text{null}, 8, 1, \text{null}, \text{null}, \text{null}, 7, 9]
  $$
- **Required Output:** A right-skewed binary tree whose root is $1$ and where every node has $\text{left} = \text{null}$ and $\text{right}$ pointing to the next node in ascending order:
  $$
  [1, \text{null}, 2, \text{null}, 3, \text{null}, 4, \text{null}, 5, \text{null}, 6, \text{null}, 7, \text{null}, 8, \text{null}, 9]
  $$
- **In-Order Relinking Mechanics:**
  - **BST In-Order Invariant:** An in-order depth-first traversal ($\text{Left} \to \text{Node} \to \text{Right}$) visits all nodes of a valid binary search tree in strictly non-decreasing sorted order:
    $$
    1 \longrightarrow 2 \longrightarrow 3 \longrightarrow 4 \longrightarrow 5 \longrightarrow 6 \longrightarrow 7 \longrightarrow 8 \longrightarrow 9
    $$
  - **Sentinel Alignment:** Initialize a sentinel node $\text{dummy}$ and maintain a moving cursor $prev$ initialized to $\text{dummy}$.
  - **Pointer Mutation Protocol:** For each visited node $curr$ during the in-order walk:
    1. Attach $curr$ as the right child of the predecessor: $prev.\text{right} \leftarrow curr$.
    2. Sever the former left subtree link: $curr.\text{left} \leftarrow \text{null}$.
    3. Advance the predecessor cursor: $prev \leftarrow curr$.
  - The reformed tree's head is $\text{dummy}.\text{right} = 1$.

---

## 1. Instance & Teaching Goal

Given the binary search tree:

```text
         5
       /   \
      3     6
     / \     \
    2   4     8
   /         / \
  1         7   9
```

The objective is to rearrange the tree in-place so that the deepest leftmost node ($1$) becomes the new root, and every node has no left child and exactly one right child (a rightward linked list using tree pointers):

```text
  1
   \
    2
     \
      3
       \
        4
         \
          5
           \
            6
             \
              7
               \
                8
                 \
                  9
```

The primary teaching goal is to demonstrate that no auxiliary node allocations are needed. By leveraging recursive in-order DFS, we process each node at the exact moment its left subtree has been fully traversed, allowing us to safely overwrite $prev.\text{right}$ and clear $curr.\text{left}$ without losing unvisited references.

---

## 2. Conceptual Foundation & Invariants

```mermaid
flowchart LR
    accTitle: In-Order Relinking Invariant
    accDescr: Diagram showing how prev.right connects to curr and curr.left is nullified
    D["Sentinel (dummy)"] -->|"right"| N1["Node (1)"]
    N1 -->|"right"| N2["Node (2)"]
    N2 -->|"right"| N3["Node (3)"]
    N3 -.->|"prev.right = curr"| NC["curr: Node (4)"]
    NC ---|"severed"| NL["left = null"]
```

### Core State Variables

| State Variable | Role & Definition | Initial State |
|---|---|---|
| `dummy` | Fixed sentinel node providing an immutable anchor to the transformed tree head | New tree node with `right = root` |
| `prev` | Running pointer pointing to the tail of the currently assembled right-skewed spine | Points to `dummy` |
| `curr` | The active node currently being visited at the in-order inflection point | First node visited ($1$) |

### Relinking Invariants

1. **Monotone Chain Invariant:** At any moment during traversal, the chain formed by $\text{dummy} \to \dots \to prev$ is strictly right-skewed, contains all nodes visited so far in sorted order, and satisfies $u.\text{left} = \text{null}$ for every node $u$ in the chain.
2. **Left-Severing Rule:** Because the left subtree of $curr$ has already been fully processed and attached to $prev$, setting $curr.\text{left} = \text{null}$ discards obsolete pointers and prevents cycles between parents and children.
3. **Right Subtree Preservation:** Because $curr.\text{right}$ is visited *after* $curr$, rewiring $prev.\text{right} = curr$ does not overwrite $curr.\text{right}$, which will be explored recursively in the subsequent DFS step.

---

## 3. Step-by-Step Worked Execution

We trace the chronological order of nodes visited and rewired during the in-order walk of the representative 9-node tree.

| Step | Visited Node $curr$ | Previous Node $prev$ | Operation 1: $prev.\text{right} \leftarrow curr$ | Operation 2: $curr.\text{left} \leftarrow \text{null}$ | New Tail $prev$ | Accumulated Right-Spine |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Init | — | `dummy` | — | — | `dummy` | `[dummy]` |
| 1 | **1** | `dummy` | `dummy.right = 1` | `1.left = null` | **1** | `dummy -> 1` |
| 2 | **2** | **1** | `1.right = 2` | `2.left = null` | **2** | `dummy -> 1 -> 2` |
| 3 | **3** | **2** | `2.right = 3` | `3.left = null` | **3** | `dummy -> 1 -> 2 -> 3` |
| 4 | **4** | **3** | `3.right = 4` | `4.left = null` | **4** | `dummy -> 1 -> 2 -> 3 -> 4` |
| 5 | **5** | **4** | `4.right = 5` | `5.left = null` | **5** | `dummy -> 1 -> ... -> 5` |
| 6 | **6** | **5** | `5.right = 6` | `6.left = null` | **6** | `dummy -> 1 -> ... -> 6` |
| 7 | **7** | **6** | `6.right = 7` | `7.left = null` | **7** | `dummy -> 1 -> ... -> 7` |
| 8 | **8** | **7** | `7.right = 8` | `8.left = null` | **8** | `dummy -> 1 -> ... -> 8` |
| 9 | **9** | **8** | `8.right = 9` | `9.left = null` | **9** | `dummy -> 1 -> ... -> 9` |

### Post-Processing Extraction

When the recursive in-order traversal finishes:
- All 9 nodes have been chained in strictly increasing numerical order.
- Every node's left child is explicitly set to `null`.
- The final result returned is $\text{dummy}.\text{right} = \mathbf{1}$.

---

## 4. Why Setting Left to Null is Essential

Consider what happens if $curr.\text{left} = \text{null}$ is omitted:

1. When node $2$ is processed, its original left child was $1$.
2. In step 1, node $1$ had its right child set to $2$ ($1.\text{right} = 2$).
3. If $2.\text{left}$ is left pointing to $1$, we create a cycle:
   $$
   1 \xrightarrow{\text{right}} 2 \xrightarrow{\text{left}} 1
   $$
4. Furthermore, the problem specification requires *every* node to have no left child. Setting $curr.\text{left} = \text{null}$ simultaneously fulfills the output contract and destroys bidirectional loops.

---

## 5. Algorithmic Correctness

### Mathematical Induction on In-Order Sequence

Let the sorted in-order sequence of the BST be $S = \langle v_1, v_2, \dots, v_n \rangle$.

- **Base Case ($k = 1$):**
  The first node visited is $v_1$ (the minimum element). $\text{dummy}.\text{right}$ is set to $v_1$, $v_1.\text{left}$ is set to $\text{null}$, and $prev$ becomes $v_1$. The invariant holds for length 1.
- **Inductive Step ($k \to k+1$):**
  Assume the chain $\text{dummy} \to v_1 \to \dots \to v_k$ is right-skewed with all left pointers nullified. The next node visited by in-order traversal is $v_{k+1}$.
  By BST properties, $v_k < v_{k+1}$.
  Setting $prev.\text{right} = v_{k+1}$ extends the right spine.
  Setting $v_{k+1}.\text{left} = \text{null}$ ensures $v_{k+1}$ has no left child.
  Setting $prev = v_{k+1}$ restores the invariant for length $k+1$.
- By induction, upon completion, the tree consists of a single right-skewed path containing all $n$ nodes in strictly increasing order.

---

## 6. Edge Cases & Traps

| Edge Case | Input Tree | Traversal Behavior | Trapped Risk |
|---|---|---|---|
| Single Node | `root = [7]` | Visits node $7$ immediately. $\text{dummy}.\text{right} = 7$, $7.\text{left} = \text{null}$. | None; returns node $7$ unchanged. |
| Already Right-Skewed | `[1, null, 2, null, 3]` | In-order visits $1 \to 2 \to 3$. Pointers are redundantly confirmed. | Pointers already conform; no cycle formed. |
| Completely Left-Skewed | `[3, 2, null, 1]` | Recursion goes straight to $1$, unwinds to $2$, then to $3$, inverting tree completely. | Deepest node becomes root; stack depth reaches $n$. |
| Unbalanced Root | Root has only right subtree | Left subtree call returns immediately; root is processed as first node. | Correctly handled by sentinel initialization. |

---

## 7. Complexity Derivation

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the number of nodes in the tree. Each node is visited exactly once by the in-order depth-first traversal, and the pointer mutations take $\mathcal{O}(1)$ time per node.
- **Auxiliary Space:** $\mathcal{O}(h)$, where $h$ is the height of the binary search tree. This corresponds to the memory consumed by the recursive call stack:
  - Best/Balanced case: $h = \mathcal{O}(\log n)$.
  - Worst case (skewed tree): $h = \mathcal{O}(n)$.
  - No new tree nodes are allocated beyond the single $\mathcal{O}(1)$ sentinel dummy node.
