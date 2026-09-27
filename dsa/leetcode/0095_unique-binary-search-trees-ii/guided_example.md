# Guided Example: Unique Binary Search Trees II

We trace the step-by-step recursive Cartesian product generation of all structurally unique binary search trees on representative instances:

- **Input:** $n = 3$
- **Required output:** List of 5 unique BST roots ($C_3 = 5$)
- **Base Instance:** $n = 1 \implies [[1]]$ ($C_1 = 1$)

This instance demonstrates recursive divide-and-conquer interval partitioning ($[start, i-1]$ and $[i+1, end]$), evaluating every candidate root $i$, taking the Cartesian product of left and right subtree candidate lists, and generating all Catalan $C_n$ distinct BST topologies.

---

## 1. Instance & Teaching Goal

Given an integer $n = 3$, generate all structurally unique Binary Search Trees (BSTs) that store values $1 \dots n$.

The total number of structurally unique BSTs for $n$ nodes is given by the $n$-th Catalan number:
$$
C_n = \frac{1}{n + 1}\binom{2n}{n} \implies C_3 = \frac{1}{4}\binom{6}{3} = \frac{20}{4} = 5
$$

For $n = 3$, choosing each value $i \in \{1, 2, 3\}$ as the root divides the remaining values:
- **Root $i = 1$:** Left values $\emptyset$ (1 tree: null), Right values $\{2, 3\}$ (2 trees) $\implies 1 \times 2 = 2$ trees.
- **Root $i = 2$:** Left values $\{1\}$ (1 tree), Right values $\{3\}$ (1 tree) $\implies 1 \times 1 = 1$ tree.
- **Root $i = 3$:** Left values $\{1, 2\}$ (2 trees), Right values $\emptyset$ (1 tree: null) $\implies 2 \times 1 = 2$ trees.
Total trees: $2 + 1 + 2 = 5$.

A naive approach attempting to generate tree permutations and filter duplicates produces $O(n!)$ redundant checks.
The recursive interval approach $\text{build}(start, end)$ strictly constructs unique BSTs by construction without duplicate topologies.

---

## 2. Conceptual Foundation & Invariants

### Recursive Interval Cartesian Product
We define $\text{build}(start, end)$, returning a list of all unique BST roots formed by contiguous integers $[start, end]$:

1. **Base Case ($start > end$):**
   The interval is empty (representing an empty left or right child).
   Return `[None]`.
2. **Root Partitioning ($i \in [start, end]$):**
   For each integer $i$:
   - Recursively generate all valid left subtrees:
     $$
     \text{left\_trees} = \text{build}(start, i - 1)
     $$
   - Recursively generate all valid right subtrees:
     $$
     \text{right\_trees} = \text{build}(i + 1, end)
     $$
   - **Cartesian Product Pairing:**
     For every left subtree $L \in \text{left\_trees}$ and every right subtree $R \in \text{right\_trees}$:
     Construct a new root node:
     $$
     \text{root} = \text{TreeNode}(i, \, \text{left} = L, \, \text{right} = R)
     $$
     Append $\text{root}$ to the candidate list for $[start, end]$.

> **Invariant.** For any interval $[start, end]$, $\text{build}(start, end)$ returns exactly the complete set of valid, structurally distinct BSTs whose inorder traversal equals the sorted sequence $start \dots end$.

---

## 3. Step-by-Step Worked Execution

We trace the generation for $n = 3$ ($start = 1, end = 3$):

### Subproblem Caching / Base Evaluations
- Length 0 (e.g. $[2, 1]$, $[4, 3]$): returns `[None]`.
- Length 1 (e.g. $[1, 1]$, $[2, 2]$, $[3, 3]$):
  - $[1, 1] \implies \text{Node}(1, \text{None}, \text{None})$.
  - $[2, 2] \implies \text{Node}(2, \text{None}, \text{None})$.
  - $[3, 3] \implies \text{Node}(3, \text{None}, \text{None})$.

---

### Root Choice $i = 1$ ($start = 1, end = 3$)
- Left subtrees from $[1, 0]$: `[None]`.
- Right subtrees from $[2, 3]$:
  - Sub-root 2: left `None`, right `Node(3)` $\implies 2 \to (\emptyset, 3)$.
  - Sub-root 3: left `Node(2)`, right `None` $\implies 3 \to (2, \emptyset)$.
  - Right candidates list: $[T_{2 \to 3}, \, T_{3 \to 2}]$.
- Combine with root 1 ($1 \times 2 = 2$ trees):
  - **Tree 1:** $\text{Node}(1, \text{left}=\emptyset, \text{right}=T_{2 \to 3})$:
    $$
    1 \longrightarrow \emptyset, \; 2 \longrightarrow (\emptyset, 3)
    $$
  - **Tree 2:** $\text{Node}(1, \text{left}=\emptyset, \text{right}=T_{3 \to 2})$:
    $$
    1 \longrightarrow \emptyset, \; 3 \longrightarrow (2, \emptyset)
    $$

---

### Root Choice $i = 2$ ($start = 1, end = 3$)
- Left subtrees from $[1, 1]$: `[Node(1)]`.
- Right subtrees from $[3, 3]$: `[Node(3)]`.
- Combine with root 2 ($1 \times 1 = 1$ tree):
  - **Tree 3:** $\text{Node}(2, \text{left}=\text{Node}(1), \text{right}=\text{Node}(3))$ (Balanced Tree):
    $$
    2 \longrightarrow (1, 3)
    $$

---

### Root Choice $i = 3$ ($start = 1, end = 3$)
- Left subtrees from $[1, 2]$:
  - Sub-root 1: left `None`, right `Node(2)` $\implies 1 \to (\emptyset, 2)$.
  - Sub-root 2: left `Node(1)`, right `None` $\implies 2 \to (1, \emptyset)$.
  - Left candidates list: $[T_{1 \to 2}, \, T_{2 \to 1}]$.
- Right subtrees from $[4, 3]$: `[None]`.
- Combine with root 3 ($2 \times 1 = 2$ trees):
  - **Tree 4:** $\text{Node}(3, \text{left}=T_{1 \to 2}, \text{right}=\emptyset)$:
    $$
    3 \longrightarrow (1 \to (\emptyset, 2), \; \emptyset)
    $$
  - **Tree 5:** $\text{Node}(3, \text{left}=T_{2 \to 1}, \text{right}=\emptyset)$:
    $$
    3 \longrightarrow (2 \to (1, \emptyset), \; \emptyset)
    $$

All 5 trees constructed.

---

## 4. Complete Execution Trace

```text
Tree 1:        Tree 2:        Tree 3:        Tree 4:        Tree 5:
   1              1              2              3              3
    \              \            / \            /              /
     2              3          1   3          1              2
      \            /                           \            /
       3          2                             2          1
```

| Root $i$ | Left Range | Left Subtrees Count | Right Range | Right Subtrees Count | Cartesian Pairs ($\lvert L \rvert \times \lvert R \rvert$) | Tree Root Representations |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $[1, 0]$ ($\emptyset$) | 1 (`[None]`) | $[2, 3]$ | 2 | $1 \times 2 = 2$ | `[1, null, 2, null, 3]`, `[1, null, 3, 2]` |
| 2 | $[1, 1]$ ($\{1\}$) | 1 (`[Node(1)]`) | $[3, 3]$ ($\{3\}$) | 1 (`[Node(3)]`) | $1 \times 1 = 1$ | `[2, 1, 3]` |
| 3 | $[1, 2]$ | 2 | $[4, 3]$ ($\emptyset$) | 1 (`[None]`) | $2 \times 1 = 2$ | `[3, 1, null, null, 2]`, `[3, 2, null, 1]` |
| Total | - | - | - | - | **$C_3 = 5$** | **5 Distinct Trees** |

---

## 5. Algorithmic Correctness

**Soundness.** For any chosen root $i$, every node in the left subtree has value $\le i - 1 < i$, and every node in the right subtree has value $\ge i + 1 > i$. Because both subtrees are recursively valid BSTs, the assembled tree satisfies the strict Binary Search Tree ordering invariant everywhere.

**Completeness.** Any unique BST containing values $1 \dots n$ must have some root $i \in [1, n]$, and its left and right children must be valid BSTs over the subsets $[1, i-1]$ and $[i+1, n]$. Because all possible roots $i$ and all possible subtrees $L$ and $R$ are paired via the Cartesian product, every valid BST is generated.

---

## 6. Traps This Instance Exposes

- **Base Case Returning Empty List Instead of `[None]`:** If $\text{build}(start, end)$ returns `[]` when $start > end$, the nested loops for $L$ in `left_trees` and $R$ in `right_trees` will execute 0 times, creating zero parent trees! The empty tree must be represented by a list containing one element: `[None]`.
- **Node Sharing vs Deep Copy:** Reusing subtree references across multiple trees is valid in functional and memory-efficient Python implementations, as trees are read-only. If callers mutate nodes, deep copies are required.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \cdot C_n) = O\left(\frac{4^n}{\sqrt{n}}\right)$, where $C_n$ is the $n$-th Catalan number. Generating and copying references for each of the $C_n$ trees with $n$ nodes takes time proportional to $n C_n$.
- **Auxiliary Space Complexity:** $O(n \cdot C_n)$ to store all nodes across the generated trees, with $O(n)$ recursion call stack depth.