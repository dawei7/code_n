# Guided Example: Maximum Width of Binary Tree

We trace the step-by-step complete binary tree positional indexing ($root \to 1$, $\text{left} \to 2i$, $\text{right} \to 2i + 1$), level-order BFS queue partitioning ($q = \text{deque}([(node, i)])$), boundary span difference calculation ($w = i_{right} - i_{left} + 1$), internal null-node gap counting, and maximum horizontal width evaluation on representative binary trees:

- **Input:**
  - Tree: $root = [1, 3, 2, 5, 3, \text{null}, 9]$
  - Tree topology:
    ```text
            1
          /   \
         3     2
        / \     \
       5   3     9
    ```
- **Required output:** `4`
  - Definition of level width:
    - The width of a level is the distance between its **leftmost non-null node** and its **rightmost non-null node**.
    - Any missing (null) nodes located between the two endpoints in a full complete binary tree are **explicitly included** in the width calculation.
    - Objective: Return the maximum width observed across all horizontal levels of the tree.
- **Complete Binary Tree Positional Indexing Invariant:**
  - **Heap Coordinate System:**
    - Assign the root node coordinate index $i = 1$.
    - For any node with coordinate $i$:
      - Its left child occupies coordinate:
        $$
        i_{left} = 2i
        $$
      - Its right child occupies coordinate:
        $$
        i_{right} = 2i + 1
        $$
    - This numbering scheme is identical to standard binary heap array indexing.
    - Notice that this formula automatically accounts for missing ancestors: whether intermediate nodes exist or not, the coordinate of any child strictly reflects its horizontal column position in a complete binary tree.
  - **Level Width Formula:**
    - At any level snapshot in a level-order BFS traversal, let the first node in the queue have index $i_{min}$, and the last node in the queue have index $i_{max}$.
    - The total number of positions spanned (including gaps) is:
      $$
      \text{Width} = i_{max} - i_{min} + 1
      $$
    - Update the running global maximum:
      $$
      ans \leftarrow \max(ans, \; i_{max} - i_{min} + 1)
      $$
- **Step-by-Step Worked Execution Trace on $[1, 3, 2, 5, 3, \text{null}, 9]$:**
  - Initialize BFS queue with root at coordinate $1$:
    $$
    q = [(\text{Node } 1, \; 1)], \quad ans = 0
    $$
  - **Level 0 Processing:**
    - Queue contains: `[(Node 1, 1)]`.
    - Leftmost index: $i_{min} = 1$.
    - Rightmost index: $i_{max} = 1$.
    - Level width:
      $$
      w = 1 - 1 + 1 = \mathbf{1}
      $$
    - Update maximum: $ans \leftarrow \max(0, 1) = \mathbf{1}$.
    - Enqueue children of Node 1 ($i = 1$):
      - Left child (Node 3): index $2(1) = \mathbf{2}$.
      - Right child (Node 2): index $2(1) + 1 = \mathbf{3}$.
  - **Level 1 Processing:**
    - Queue contains: `[(Node 3, 2), (Node 2, 3)]`.
    - Leftmost index: $i_{min} = 2$.
    - Rightmost index: $i_{max} = 3$.
    - Level width:
      $$
      w = 3 - 2 + 1 = \mathbf{2}
      $$
    - Update maximum: $ans \leftarrow \max(1, 2) = \mathbf{2}$.
    - Enqueue children:
      - From Node 3 ($i = 2$):
        - Left child (Node 5): index $2(2) = \mathbf{4}$.
        - Right child (Node 3): index $2(2) + 1 = \mathbf{5}$.
      - From Node 2 ($i = 3$):
        - Left child is null (slot $2(3) = 6$ is empty).
        - Right child (Node 9): index $2(3) + 1 = \mathbf{7}$.
  - **Level 2 Processing:**
    - Queue contains: `[(Node 5, 4), (Node 3, 5), (Node 9, 7)]`.
    - Leftmost index: $i_{min} = 4$ (Node 5).
    - Rightmost index: $i_{max} = 7$ (Node 9).
    - Physical layout at Level 2:
      ```text
      Slot 4: Node 5  [PRESENT]
      Slot 5: Node 3  [PRESENT]
      Slot 6: null    [GAP]
      Slot 7: Node 9  [PRESENT]
      ```
    - Level width calculation:
      $$
      w = i_{max} - i_{min} + 1 = 7 - 4 + 1 = \mathbf{4}
      $$
    - Update maximum:
      $$
      ans \leftarrow \max(2, \; 4) = \mathbf{4}
      $$
    - Nodes 5, 3, and 9 are all leaves; queue becomes empty.
  - **Step 4: Final Maximum Width:**
    $$
    ans = \mathbf{4}
    $$
- **Wider Sparse Tree ($root = [1, 3, 2, 5, \text{null}, \text{null}, 9, 6, \text{null}, 7]$):**
  - Level 3 has Node 6 at index $2 \times 4 = 8$ (left of 5).
  - Node 7 is at index $2 \times 7 + 1 = 15$ (right of 9).
  - Width at Level 3: $15 - 8 + 1 = \mathbf{8}$.
- **Single Node Tree ($root = [1]$):**
  - Level 0 has 1 node at index 1 $\implies$ width is $1 - 1 + 1 = \mathbf{1}$.

This instance demonstrates complete binary tree coordinate labeling and level-order wavefront propagation, mathematically proves why dyadic coordinate difference measures horizontal span including intermediate null voids, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
Find the **maximum width** among all levels.
Width is the distance between the leftmost and rightmost non-null nodes, including null gaps between them.

```text
Tree:
        1          Level 0: [ 1 ]             -> width = 1
      /   \
     3     2        Level 1: [ 2, 3 ]          -> width = 3 - 2 + 1 = 2
    / \     \
   5   3     9      Level 2: [ 4, 5, _, 7 ]    -> width = 7 - 4 + 1 = 4

Max Width = 4
```

### The Invariant of Binary Heap Coordinate Indexing
- Root $= 1$.
- For node $i$: left $= 2i$, right $= 2i + 1$.
- At any level:
  $$
  width = \text{last\_index} - \text{first\_index} + 1
  $$
- The heap indices implicitly account for all intermediate missing subtrees without expanding null nodes into memory.

---

## 2. Conceptual Foundation & Invariants

### 1. The Dyadic Child Mapping:
$$
i_{left} = 2i, \quad i_{right} = 2i + 1
$$

### 2. Level Width Invariant:
For level queue $q = [(u_1, i_1), (u_2, i_2), \dots, (u_k, i_k)]$ sorted by index:
$$
\text{width}(q) = i_k - i_1 + 1
$$
$$
ans = \max_{\text{all levels}} \text{width}(q)
$$

> **Dyadic Heap Metric Invariant.** The index difference $i_{max} - i_{min} + 1$ under the canonical complete binary tree embedding is isomorphic to the length of the shortest contiguous word in $\{0, 1\}^d$ containing all active nodes at depth $d$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Level 0
- Queue: `[(1, 1)]`.
- Width: $1 - 1 + 1 = 1$. $ans = 1$.

---

### Step 2: Level 1
- Queue: `[(3, 2), (2, 3)]`.
- Width: $3 - 2 + 1 = 2$. $ans = 2$.

---

### Step 3: Level 2
- Node 3 pushes left (4) and right (5).
- Node 2 pushes right ($2 \times 3 + 1 = 7$).
- Queue: `[(5, 4), (3, 5), (9, 7)]`.
- Width: $7 - 4 + 1 = \mathbf{4}$.
- $ans = \max(2, 4) = \mathbf{4}$.

---

### Step 4: Halt
- Queue empty. Output is **`4`**.

---

## 4. Complete Execution Trace

| Level | Leftmost Node $(val, i)$ | Rightmost Node $(val, i)$ | Level Queue Elements | Calculated Width $i_{max} - i_{min} + 1$ | Running Max $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $(1, 1)$ | $(1, 1)$ | `[(1, 1)]` | $1 - 1 + 1 = 1$ | $1$ |
| $1$ | $(3, 2)$ | $(2, 3)$ | `[(3, 2), (2, 3)]` | $3 - 2 + 1 = 2$ | $2$ |
| **$2$** | **$(5, 4)$** | **$(9, 7)$** | **`[(5, 4), (3, 5), (9, 7)]`** | **$7 - 4 + 1 = \mathbf{4}$** | **`4`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node:** Width is $1$.
- **Linear Skewed Tree (Chain of left children):** Every level has exactly 1 node $\implies$ width is $1$.
- **Deep Tree ($depth = 100$):** In languages without arbitrary precision integers (like C++ or Java), $2^{100}$ overflows 64-bit integers. Subtracting $i_{min}$ from all indices at each level keeps numbers within standard 32-bit limits.
- **Null Subtrees Between Endpoints:** Captured mathematically without adding null nodes to the queue.

---

## 6. Traps & Common Anti-Patterns

- **Enqueueing Null Pointers in BFS:** Pushing null nodes into the queue exponentially doubles memory ($2^D$), causing Memory Limit Exceeded on deep sparse trees. Only enqueue non-null nodes with their heap index!
- **Integer Overflow in C++/Java:** For trees with depth $> 60$, $2 \cdot i$ overflows 64-bit integers. Normalize indices at each level by subtracting the first node's index: $i \leftarrow i - i_{min}$.
- **Counting Nodes Instead of Index Span:** Counting the number of non-null nodes gives $3$ on Level 2, but the width is $4$ due to the gap at position 6.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard BFS visits every node in the tree exactly once: $\mathcal{O}(N)$.
  - Slicing queue endpoints and arithmetic: $\mathcal{O}(1)$ per level.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 2$ ms for $N = 3000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the BFS queue.