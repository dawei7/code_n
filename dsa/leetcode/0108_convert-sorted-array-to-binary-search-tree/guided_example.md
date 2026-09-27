# Guided Example: Convert Sorted Array to Binary Search Tree

We trace the step-by-step recursive midpoint divide-and-conquer BST construction on a representative sorted array:

- **Input:** $\text{nums} = [-10, -3, 0, 5, 9]$
- **Required output:** $[0, -10, 5, \text{null}, -3, \text{null}, 9]$ (or $[0, -3, 9, -10, \text{null}, 5]$)
- **Base Instance:** $\text{nums} = [1, 3] \implies [3, 1]$ or $[1, \text{null}, 3]$

This instance demonstrates selecting the median element $M = L + \lfloor (R - L) / 2 \rfloor$ as the root to guarantee height balance ($|H_L - H_R| \le 1$), recursive interval bisection without array slicing, and building a strictly valid BST in $O(N)$ linear time.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [-10, -3, 0, 5, 9]$ sorted in ascending order, convert it to a **height-balanced** Binary Search Tree (BST).
A height-balanced tree is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Any choice of root from a sorted array creates a valid BST, but choosing unbalanced roots (e.g. taking the first element repeatedly: $-10 \to -3 \to 0 \to 5 \to 9$) creates a degenerate linked-list tree of depth $5$.
To guarantee height balance:
- Always select the **median** element of the current interval as the root node.
- The median partitions the remaining elements into two sub-arrays whose counts differ by at most $1$.
- By structural induction, the heights of the resulting left and right subtrees differ by at most $1$ at every node.

Passing interval indices $(L, R)$ rather than copying array slices achieves $O(N)$ time and $O(\log N)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

### Midpoint Divide-and-Conquer Protocol
We define $\text{buildTree}(L, R)$:
1. **Base Case:**
   If $L > R$:
   The interval contains zero elements. Return $\emptyset$.
2. **Median Selection:**
   Compute the midpoint (rounding down):
   $$
   M = L + \left\lfloor \frac{R - L}{2} \right\rfloor
   $$
3. **Subtree Partitioning:**
   - The root takes the value $V = \text{nums}[M]$.
   - Elements strictly before $M$ form the left subtree:
     $$
     \text{left} = \text{buildTree}(L, M - 1)
     $$
   - Elements strictly after $M$ form the right subtree:
     $$
     \text{right} = \text{buildTree}(M + 1, R)
     $$
4. **Construct Node:**
   $$
   \text{return TreeNode}(V, \, \text{left}, \, \text{right})
   $$

> **Invariant.** For every interval $[L, R]$, the median choice partitions the range into sub-intervals whose sizes differ by at most 1, guaranteeing that every constructed subtree is both a valid BST and strictly height-balanced ($|H_L - H_R| \le 1$).

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [-10, -3, 0, 5, 9]$ ($N = 5$, indices $0 \dots 4$):

### Step 1: Global Root (Interval $[0, 4]$)
- Midpoint: $M = 0 + \lfloor (4 - 0) / 2 \rfloor = 2$.
- Root value: $\text{nums}[2] = 0$.
- Create root: $\text{Node}(0)$.
- Spawn left interval: $[0, 1]$ (values $[-10, -3]$).
- Spawn right interval: $[3, 4]$ (values $[5, 9]$).

---

### Step 2: Left Child of 0 (Interval $[0, 1]$)
- Midpoint: $M = 0 + \lfloor (1 - 0) / 2 \rfloor = 0$.
- Node value: $\text{nums}[0] = -10$.
- Create node: $\text{Node}(-10)$.
  - Left interval $[0, -1]$: empty $\implies \emptyset$.
  - Right interval $[1, 1]$:
    - $M = 1 \implies \text{nums}[1] = -3$.
    - Child bounds empty $\implies \text{Node}(-3)$ is a leaf.
- Subtree rooted at $-10$ has right child $-3$. Height $= 2$.

---

### Step 3: Right Child of 0 (Interval $[3, 4]$)
- Midpoint: $M = 3 + \lfloor (4 - 3) / 2 \rfloor = 3$.
- Node value: $\text{nums}[3] = 5$.
- Create node: $\text{Node}(5)$.
  - Left interval $[3, 2]$: empty $\implies \emptyset$.
  - Right interval $[4, 4]$:
    - $M = 4 \implies \text{nums}[4] = 9$.
    - Child bounds empty $\implies \text{Node}(9)$ is a leaf.
- Subtree rooted at $5$ has right child $9$. Height $= 2$.

---

### Tree Assembly
- Root $0$ connects:
  - Left child: $\text{Node}(-10)$ with right child $\text{Node}(-3)$.
  - Right child: $\text{Node}(5)$ with right child $\text{Node}(9)$.
- Subtree heights: $H_L = 2$, $H_R = 2 \implies |2 - 2| = 0 \le 1$.
- Total height is $3$, perfectly balanced.

**Balance audit for every constructed subtree.** Heights are counted as the number of nodes on the longest downward path from that root, so an empty interval has height $0$ and a leaf has height $1$. Every node's two subtree heights differ by at most one:

| Subtree Root $V$ | Interval $[L, R]$ | Size $K$ | Left Size | Right Size | $H_L$ | $H_R$ | $\lvert H_L - H_R \rvert$ | Balanced? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $[0, 4]$ | 5 | 2 | 2 | 2 | 2 | 0 | Yes |
| $-10$ | $[0, 1]$ | 2 | 0 | 1 | 0 | 1 | 1 | Yes |
| $-3$ | $[1, 1]$ | 1 | 0 | 0 | 0 | 0 | 0 | Yes |
| $5$ | $[3, 4]$ | 2 | 0 | 1 | 0 | 1 | 1 | Yes |
| $9$ | $[4, 4]$ | 1 | 0 | 0 | 0 | 0 | 0 | Yes |

The two interval sizes at every node differ by at most one because bisection splits $K$ elements into $\lfloor (K-1)/2 \rfloor$ and $\lceil (K-1)/2 \rceil$; because the recursion is identical on both sides, that size parity propagates into the height difference recorded above.

---

## 4. Complete Execution Trace

```text
               Root 0 (index 2)
              /                \
     Node -10 (index 0)       Node 5 (index 3)
           \                        \
        Node -3 (index 1)         Node 9 (index 4)
```

| Recursion Step | Active Range $[L, R]$ | Midpoint $M$ | Selected Value $\text{nums}[M]$ | Left Child Range | Right Child Range | Resulting Subtree |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $[0, 4]$ | 2 | 0 | $[0, 1]$ | $[3, 4]$ | $\text{Node}(0)$ |
| 1.1 | $[0, 1]$ | 0 | -10 | $[0, -1]$ ($\emptyset$) | $[1, 1]$ | $\text{Node}(-10)$ |
| 1.1.1 | $[0, -1]$ | - | - | - | - | $\emptyset$ |
| 1.1.2 | $[1, 1]$ | 1 | -3 | $[1, 0]$ ($\emptyset$) | $[2, 1]$ ($\emptyset$) | $\text{Node}(-3)$ (Leaf) |
| 1.2 | $[3, 4]$ | 3 | 5 | $[3, 2]$ ($\emptyset$) | $[4, 4]$ | $\text{Node}(5)$ |
| 1.2.1 | $[3, 2]$ | - | - | - | - | $\emptyset$ |
| 1.2.2 | $[4, 4]$ | 4 | 9 | $[4, 3]$ ($\emptyset$) | $[5, 4]$ ($\emptyset$) | $\text{Node}(9)$ (Leaf) |

---

## 5. Algorithmic Correctness

**Soundness.** Because the input array is strictly sorted in ascending order, all elements to the left of the midpoint $M$ are $< \text{nums}[M]$, and all elements to the right are $> \text{nums}[M]$. Therefore, every constructed node strictly satisfies the Binary Search Tree property.

**Completeness.** Bisection divides an interval of length $K$ into sub-intervals of sizes $\lfloor (K-1)/2 \rfloor$ and $\lceil (K-1)/2 \rceil$. The difference between sub-interval lengths is at most 1, guaranteeing by mathematical induction that the maximum path length across left and right subtrees differs by at most 1 at every node.

---

## 6. Traps This Instance Exposes

- **Integer Overflow in Midpoint Calculation:** In languages with fixed-width integers, writing `(L + R) // 2` can overflow when $L + R > 2^{31} - 1$. The form $L + (R - L) // 2$ prevents overflow.
- **Multiple Valid BST Topologies:** For an even number of elements (such as $[0, 1]$), choosing the lower median ($\lfloor (L+R)/2 \rfloor$) or the upper median ($\lceil (L+R)/2 \rceil$) both produce valid height-balanced BSTs. Both choices are accepted by the judge.

**Boundary instances and what the midpoint rule does with each.**

| Scenario | Input | Midpoint decision | Serialized result | Why it remains a correct balanced BST |
|:---|:---|:---|:---|:---|
| Empty input | $\text{nums} = [\,]$ | $\text{buildTree}(0, -1)$ has $L > R$ | $[\,]$ | The empty interval admits exactly one tree, so returning $\emptyset$ without selecting a root is forced rather than special-cased. |
| Single element | $\text{nums} = [5]$ | $M = 0$ | $[5]$ | Both child intervals $[0, -1]$ and $[1, 0]$ are empty, so the lone node is a leaf with $H_L = H_R = 0$. |
| Two elements | $\text{nums} = [1, 3]$ | $M = 0 + \lfloor 1/2 \rfloor = 0$ | $[1, \text{null}, 3]$ | The lower-median rule keeps the smaller value as root and pushes the remaining element right, preserving $1 < 3$ and giving heights $0$ and $1$. |
| Odd count, seven values | $\text{nums} = [-5, -3, -1, 0, 2, 4, 8]$ | $M = 0 + \lfloor 6/2 \rfloor = 3$ | $[0, -3, 4, -5, -1, 2, 8]$ | The split is exactly $3$ and $3$ elements, so both subtrees have height $2$ and the difference is $0$. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |\text{nums}|$. Exactly $N$ tree nodes are created, each taking $O(1)$ operations to determine midpoint and link pointers.
- **Auxiliary Space Complexity:** $O(\log N)$ stack frames. Because the tree is strictly balanced, the maximum depth of the recursion tree is $\lceil \log_2(N + 1) \rceil$.