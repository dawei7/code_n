# Guided Example: Maximum Binary Tree

We trace the step-by-step array partition around the global maximum element ($\max(nums)$), Cartesian tree divide-and-conquer recursion, left-prefix subtree delegation ($nums[:i]$), right-suffix subtree delegation ($nums[i+1:]$), tree topology construction, and level-order serialization on representative permutation arrays:

- **Input:** $nums = [3, 2, 1, 6, 0, 5]$
- **Required output:** `[6, 3, 5, \text{null}, 2, 0, \text{null}, \text{null}, 1]`
  - Construction contract (Cartesian Tree):
    1. The root of the tree is the **maximum value** in the current array.
    2. The left child of the root is the Maximum Binary Tree built from all elements **strictly to the left** of the maximum.
    3. The right child of the root is the Maximum Binary Tree built from all elements **strictly to the right** of the maximum.
    4. Base case: An empty subarray returns `null`.
- **Cartesian Tree Divide-and-Conquer Architecture:**
  - In a Cartesian tree, the in-order traversal recovers the original array sequence $[3, 2, 1, 6, 0, 5]$, while every parent node is strictly greater than all of its descendants (max-heap property).
  - Let $construct(L, R)$ build the tree on subarray $nums[L \dots R]$:
    1. If $L > R$: Return `null`.
    2. Find index $m \in [L, R]$ such that $nums[m] = \max_{j=L}^R nums[j]$.
    3. Allocate node: $root = \text{Node}(nums[m])$.
    4. Recursively build left branch: $root.left \leftarrow construct(L, \; m - 1)$.
    5. Recursively build right branch: $root.right \leftarrow construct(m + 1, \; R)$.
    6. Return $root$.
- **Step-by-Step Worked Execution Trace on $[3, 2, 1, 6, 0, 5]$:**
  - Full array indices: $0 \dots 5$.
  - **Level 1 (Full Array $[3, 2, 1, 6, 0, 5]$):**
    - Find maximum:
      $$
      \max(3, 2, 1, 6, 0, 5) = \mathbf{6} \quad (\text{at index } 3)
      $$
    - Create Root Node with value $6$.
    - Partition into two subarrays:
      - Left partition: indices $0 \dots 2 \implies [3, 2, 1]$
      - Right partition: indices $4 \dots 5 \implies [0, 5]$
  - **Level 2: Build Left Subtree on $[3, 2, 1]$:**
    - Find maximum in $[3, 2, 1]$:
      $$
      \max(3, 2, 1) = \mathbf{3} \quad (\text{at index } 0)
      $$
    - Create Node with value $3$.
    - Attach as left child of 6: $6.left \leftarrow \text{Node } 3$.
    - Partition around index 0:
      - Left of 3: empty $[] \implies \mathbf{null}$.
      - Right of 3: $[2, 1]$ (indices $1 \dots 2$).
  - **Level 3: Build Right Subtree of 3 on $[2, 1]$:**
    - Find maximum in $[2, 1]$:
      $$
      \max(2, 1) = \mathbf{2} \quad (\text{at index } 1)
      $$
    - Create Node with value $2$.
    - Attach: $3.right \leftarrow \text{Node } 2$.
    - Partition around index 1:
      - Left of 2: empty $[] \implies \mathbf{null}$.
      - Right of 2: $[1]$ (index 2).
  - **Level 4: Build Right Subtree of 2 on $[1]$:**
    - Maximum is $1$.
    - Create Node with value $1$.
    - Attach: $2.right \leftarrow \text{Node } 1$.
    - Both left and right of 1 are empty $\implies$ Leaf node.
  - **Level 2: Build Right Subtree on $[0, 5]$:**
    - Return to root Node 6, process right partition $[0, 5]$:
    - Find maximum in $[0, 5]$:
      $$
      \max(0, 5) = \mathbf{5} \quad (\text{at index } 5)
      $$
    - Create Node with value $5$.
    - Attach as right child of 6: $6.right \leftarrow \text{Node } 5$.
    - Partition around index 5:
      - Left of 5: $[0]$ (index 4).
      - Right of 5: empty $[] \implies \mathbf{null}$.
  - **Level 3: Build Left Subtree of 5 on $[0]$:**
    - Maximum is $0$.
    - Create Node with value $0$.
    - Attach: $5.left \leftarrow \text{Node } 0$.
    - Leaf node (both children `null`).
  - **Step 7: Final Tree Assembly & Inspection:**
    ```text
            6
          /   \
         3     5
          \   /
           2 0
            \
             1
    ```
  - Level-Order Representation:
    - Level 0: `[6]`
    - Level 1: `[3, 5]`
    - Level 2: `[null, 2, 0, null]`
    - Level 3: `[null, 1]`
    - Array: `[6, 3, 5, null, 2, 0, null, null, 1]`.
- **Strictly Decreasing Input ($nums = [3, 2, 1]$):**
  - Maximum is 3 at index 0.
  - All other elements fall to the right:
    $$
    3 \to \text{right: } 2 \to \text{right: } 1
    $$
  - Produces a right-skewed tree: `[3, null, 2, null, 1]`.
- **Strictly Increasing Input ($nums = [1, 2, 3]$):**
  - Maximum is 3 at index 2.
  - All other elements fall to the left:
    $$
    3 \to \text{left: } 2 \to \text{left: } 1
    $$
  - Produces a left-skewed tree: `[3, 2, null, 1]`.

This instance demonstrates recursive divide-and-conquer Cartesian tree induction, mathematically proves why partitioning along the global supremum preserves in-order projection while maintaining the max-heap property, and derives $O(N^2)$ worst-case / $O(N \log N)$ average runtime (or $O(N)$ with a monotonic stack) and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$ without duplicates:
Build the **Maximum Binary Tree**:
- Root is the maximum element.
- Left child is built from elements to the left of the maximum.
- Right child is built from elements to the right of the maximum.

```text
nums = [ 3, 2, 1, 6, 0, 5 ]

Step 1: Max is 6 (index 3) -> Root is 6
        Left slice:  [ 3, 2, 1 ]
        Right slice: [ 0, 5 ]

Step 2: On [ 3, 2, 1 ], max is 3 -> 6.left = 3
        Right slice of 3: [ 2, 1 ] -> 3.right = 2
        Right slice of 2: [ 1 ]    -> 2.right = 1

Step 3: On [ 0, 5 ], max is 5 -> 6.right = 5
        Left slice of 5: [ 0 ] -> 5.left = 0

Tree:
        6
      /   \
     3     5
      \   /
       2 0
        \
         1
```

### The Invariant of the Cartesian Tree
- In-order traversal: $[3, 2, 1, 6, 0, 5]$ (recovers original array order).
- Heap property: Every parent is strictly greater than its children ($6 > 3, 5$; $3 > 2$; $2 > 1$; $5 > 0$).

---

## 2. Conceptual Foundation & Invariants

### 1. The Recursive Divide-and-Conquer Protocol:
$$
construct(A) = \begin{cases} \text{null} & \text{if } A = \emptyset \\ \text{Node}(A[m], \; construct(A[:m]), \; construct(A[m+1:])) & \text{where } A[m] = \max(A) \end{cases}
$$

### 2. Monotonic Stack Equivalence ($O(N)$):
- A Cartesian tree can also be built in strictly linear $\mathcal{O}(N)$ time using a monotonic decreasing stack of nodes.
- Each incoming node pops smaller nodes and sets the last popped node as its left child; the node remaining on top of the stack adopts the incoming node as its right child.

> **Cartesian Duality Invariant.** A Cartesian tree uniquely encodes both the positional sequence of an array (via in-order tree projection) and its range maximum queries (via lowest common ancestor lookup: $\text{RMQ}(i, j) = \text{LCA}(i, j).val$).

---

## 3. Step-by-Step Worked Execution

We trace $nums = [3, 2, 1, 6, 0, 5]$:

---

### Step 1: Root Node
- Subarray $[3, 2, 1, 6, 0, 5]$.
- Max is 6 at index 3. Root is Node 6.

---

### Step 2: Left Child of 6
- Subarray $[3, 2, 1]$.
- Max is 3 at index 0.
- $6.left \leftarrow \text{Node } 3$.

---

### Step 3: Right Child of 3
- Subarray $[2, 1]$.
- Max is 2 at index 1.
- $3.right \leftarrow \text{Node } 2$.

---

### Step 4: Right Child of 2
- Subarray $[1]$.
- Max is 1 at index 2.
- $2.right \leftarrow \text{Node } 1$.

---

### Step 5: Right Child of 6
- Subarray $[0, 5]$.
- Max is 5 at index 5.
- $6.right \leftarrow \text{Node } 5$.
- Subarray to left of 5 is $[0] \implies 5.left \leftarrow \text{Node } 0$.

---

## 4. Complete Execution Trace

| Subarray Processed | Maximum Value | Index $m$ | Assigned Node Role | Left Child Range | Right Child Range |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $[3, 2, 1, 6, 0, 5]$ | **$6$** | $3$ | **Root** | $[3, 2, 1]$ | $[0, 5]$ |
| $[3, 2, 1]$ | **$3$** | $0$ | Left of 6 | $\emptyset$ (null) | $[2, 1]$ |
| $[2, 1]$ | **$2$** | $1$ | Right of 3 | $\emptyset$ (null) | $[1]$ |
| $[1]$ | **$1$** | $2$ | Right of 2 | $\emptyset$ (null) | $\emptyset$ (null) |
| $[0, 5]$ | **$5$** | $5$ | Right of 6 | $[0]$ | $\emptyset$ (null) |
| $[0]$ | **$0$** | $4$ | Left of 5 | $\emptyset$ (null) | $\emptyset$ (null) |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($[5]$):** Single root node returned.
- **Strictly Decreasing Array ($[5, 4, 3, 2, 1]$):** Forms a right-skewed tree of depth $N$.
- **Strictly Increasing Array ($[1, 2, 3, 4, 5]$):** Forms a left-skewed tree of depth $N$.
- **V-Shaped Array ($[5, 1, 6]$):** Root is 6; 5 and 1 both become descendants of 6.

---

## 6. Traps & Common Anti-Patterns

- **Slicing Arrays Directly ($O(N^2)$ Extra Memory):** Passing array slices `nums[:i]` creates new sub-lists. Passing index boundaries $(L, R)$ eliminates memory copying.
- **Off-by-One on Recursive Boundaries:** The left child must span $[L, m - 1]$, and the right child must span $[m + 1, R]$. Including $m$ leads to infinite recursion.
- **Assuming Balanced Tree Height:** In sorted or nearly sorted arrays, tree depth can degrade to $O(N)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Recursive search finds max in subarray of length $L$ in $\mathcal{O}(L)$ time.
  - Worst Case (sorted input, depth $N$): $\sum_{i=1}^N i = \mathcal{O}(N^2)$.
  - Average Case (random input, depth $\log N$): $\mathcal{O}(N \log N)$.
  - (Monotonic stack approach achieves strictly $\mathcal{O}(N)$).
  - For $N = 1000$, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ call stack depth in the worst case (skewed tree).
