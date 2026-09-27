# Guided Example: Binary Tree Vertical Order Traversal

We trace the step-by-step 2D coordinate assignment $(\text{depth}, \text{offset})$, left-to-right column grouping, depth-based vertical ordering, stable tie-breaking, and column aggregation on representative binary tree instances:

- **Input:** Binary tree $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7]$
- **Required output:** `[[9], [3, 15], [20], [7]]`
  - Column $-1$: Node $9$ (row 1) $\implies [9]$
  - Column $0$: Node $3$ (row 0), Node $15$ (row 2) $\implies [3, 15]$
  - Column $1$: Node $20$ (row 1) $\implies [20]$
  - Column $2$: Node $7$ (row 2) $\implies [7]$
- **Overlapping Same Row/Col Instance:** When two nodes share both row and column, the left-to-right visitation order is strictly preserved
- **Empty Tree Base Case:** $\text{root} = \text{null} \implies []$
- **Single Node Tree:** $\text{root} = [1] \implies [[1]]$
- **Linear Skewed Tree:** Left-skewed tree shifts columns monotonically: $0, -1, -2, \dots$

This instance demonstrates vertical spatial partitioning on tree graphs, formalizes the geometric coordinate mapping $(\text{left} \to \text{col}-1, \; \text{right} \to \text{col}+1)$, explains why vertical columns must be ordered from leftmost to rightmost while nodes within each column proceed from top to bottom, and analyzes time and auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a binary tree:
```text
        3
       / \
      9   20
         /  \
        15   7
```
Compute the **vertical order traversal**:
- Columns are ordered from **left to right** (minimum column index to maximum column index).
- Within each column, nodes are ordered from **top to bottom** (increasing depth/row).
- If two nodes share the same row and column, order them from **left to right**.

```text
2D Coordinate Mapping:
Root 3:  depth = 0, col = 0
Node 9:  depth = 1, col = -1
Node 20: depth = 1, col = +1
Node 15: depth = 2, col = 0
Node 7:  depth = 2, col = +2

Grouping by Column:
Col -1: [9]
Col  0: [3, 15]   (depth 0 before depth 2)
Col +1: [20]
Col +2: [7]

Output: [[9], [3, 15], [20], [7]]
```

---

## 2. Conceptual Foundation & Invariants

### 2D Coordinate System
Assign every node a 2D coordinate $(\text{depth}, \text{offset})$:
- The root is placed at origin $(0, 0)$.
- For a node at $(\text{depth}, \text{offset})$:
  - Its left child is at $(\text{depth} + 1, \; \text{offset} - 1)$.
  - Its right child is at $(\text{depth} + 1, \; \text{offset} + 1)$.

### Multi-Key Sorting Invariants:
1. **Primary Key (Column `offset`):** Columns must be processed in strictly ascending order:
   $$
   \text{col}_{\text{min}} \le \dots \le \text{col}_{\text{max}}
   $$
2. **Secondary Key (Depth `row`):** Within each column list, elements must appear in strictly ascending depth order (top-down).
3. **Tertiary Key (Left-to-Right Insertion Order):** If two nodes share both column and depth, they must be ordered as they appear from left to right. Performing a preorder traversal (visiting `node.left` before `node.right`) combined with stable sorting (`v.sort(key=lambda x: x[0])`) guarantees this invariant.

> **Invariant.** For every column bucket $d[c]$, all entries $(depth, val)$ preserve the topological top-to-bottom and left-to-right order of the tree hierarchy.

---

## 3. Step-by-Step Worked Execution

We trace the coordinate collection on tree $[3, 9, 20, \text{null}, \text{null}, 15, 7]$:
Hash map `d = defaultdict(list)` to store `(depth, val)` pairs.

---

### Step 1: Traverse Root (Node 3)
- Position: $\text{depth} = 0, \; \text{offset} = 0$.
- Record: `d[0].append((0, 3))`.
- Left branch: Node 9 at $(\text{depth}=1, \text{offset}=-1)$.
- Right branch: Node 20 at $(\text{depth}=1, \text{offset}=1)$.

---

### Step 2: Traverse Left Subtree (Node 9)
- Position: $\text{depth} = 1, \; \text{offset} = -1$.
- Record: `d[-1].append((1, 9))`.
- Left child is `None`.
- Right child is `None`.
- Subtree completed.

---

### Step 3: Traverse Right Subtree (Node 20)
- Position: $\text{depth} = 1, \; \text{offset} = 1$.
- Record: `d[1].append((1, 20))`.
- Left branch: Node 15 at $(\text{depth} = 1 + 1 = 2, \; \text{offset} = 1 - 1 = 0)$.
- Right branch: Node 7 at $(\text{depth} = 1 + 1 = 2, \; \text{offset} = 1 + 1 = 2)$.

---

### Step 4: Traverse Children of Node 20
1. **Node 15:**
   - Position: $\text{depth} = 2, \; \text{offset} = 0$.
   - Record: `d[0].append((2, 15))`.
   - Children are `None`.
2. **Node 7:**
   - Position: $\text{depth} = 2, \; \text{offset} = 2$.
   - Record: `d[2].append((2, 7))`.
   - Children are `None`.

---

### Step 5: Column Sorting & Output Construction
Columns present in dictionary: $\{-1, 0, 1, 2\}$.
Sort columns in ascending order:

1. **Column $-1$:**
   - Entries: `[(1, 9)]`.
   - Values: `[9]`.
2. **Column $0$:**
   - Entries: `[(0, 3), (2, 15)]`.
   - Sorted by depth: `(0, 3)` then `(2, 15)`.
   - Values: `[3, 15]`.
3. **Column $1$:**
   - Entries: `[(1, 20)]`.
   - Values: `[20]`.
4. **Column $2$:**
   - Entries: `[(2, 7)]`.
   - Values: `[7]`.

Final output:
$$
\mathbf{[[9], [3, 15], [20], [7]]}
$$

---

## 4. Complete Execution Trace

```text
Tree:
      3 (0, 0)
     / \
(1,-1)9 20 (1, 1)
       /  \
(2, 0)15   7 (2, 2)

Collected Map:
  -1: [(1, 9)]
   0: [(0, 3), (2, 15)]
   1: [(1, 20)]
   2: [(2, 7)]

Output by Column:
  Col -1 -> [9]
  Col  0 -> [3, 15]
  Col  1 -> [20]
  Col  2 -> [7]

Result: [[9], [3, 15], [20], [7]]
```

| Traversed Node | Value | Depth ($\text{row}$) | Offset ($\text{column}$) | Bucket Updated | Entries in Bucket After Step |
|:---:|:---:|:---:|:---:|:---:|:---|
| Root | 3 | 0 | 0 | `d[0]` | `[(0, 3)]` |
| Left | 9 | 1 | -1 | `d[-1]` | `[(1, 9)]` |
| Right | 20 | 1 | +1 | `d[1]` | `[(1, 20)]` |
| Right $\to$ Left | 15 | 2 | 0 | `d[0]` | `[(0, 3), (2, 15)]` |
| Right $\to$ Right | 7 | 2 | +2 | `d[2]` | `[(2, 7)]` |

---

## 5. Algorithmic Correctness

**Soundness.** Every node's horizontal position is strictly determined by the path from the root, where going left subtracts 1 and going right adds 1. Depth increases by 1 at each level. Sorting the dictionary keys orders columns from leftmost to rightmost, and stable-sorting each column bucket by depth ensures upper nodes precede lower nodes.

**Completeness.** The DFS traversal visits every node in the binary tree exactly once. Because no node is skipped, all node values are assigned to their appropriate column lists, producing an exhaustive vertical partition.

---

## 6. Traps This Instance Exposes

- **Vertical Order Traversal I vs II:** In LeetCode 314 (Vertical Order Traversal), if two nodes share the same row and column, they must be ordered from **left to right** (the order they are visited in tree traversal). In LeetCode 987 (Vertical Order Traversal of a Binary Tree), same-row/same-col nodes must be sorted by **numerical value**. Confusing the two problems causes wrong answers.
- **Pure DFS without Depth Tracking:** If nodes are added directly to `d[offset]` during DFS without recording depth, a deep left node in a right branch might be appended before an earlier shallow node, violating the top-to-bottom vertical requirement.
- **Empty Tree:** Passing `None` must return `[]` without raising attribute errors.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$ or $O(N)$ with BFS. The DFS visits $N$ nodes in $O(N)$ time. Sorting the $C$ column keys takes $O(C \log C)$ (where $C \le N$). Sorting the entries inside columns takes $\sum O(K_c \log K_c) \le O(N \log N)$ total. If implemented with BFS and tracked minimum/maximum column bounds, runtime is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store all tree nodes and coordinates in hash table `d`.
