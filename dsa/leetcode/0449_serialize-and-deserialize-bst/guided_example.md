# Guided Example: Serialize and Deserialize BST

We trace the step-by-step preorder traversal serialization (omitting all null markers), bounding-interval recursive reconstruction ($[mi, mx]$), BST range-pruning branch assignment, and compact string encoding on representative binary search trees:

- **Input:**
  - Binary search tree:
    ```text
        2
       / \
      1   3
    ```
- **Required output:** Reconstructed identical BST object
- **Execution trace:**
  - **Phase 1: Preorder Serialization:**
    - Visit root $2 \implies$ emit `"2"`
    - Traverse left child $1 \implies$ emit `"1"`
    - Traverse right child $3 \implies$ emit `"3"`
    - Serialized string (completely free of null delimiters):
      $$
      \text{"2 1 3"}
      $$
  - **Phase 2: Interval-Bounded Deserialization:**
    - Token array: $nums = [2, 1, 3]$, pointer $i = 0$
    - Frame 1: `dfs(-inf, +inf)`
      - Token $nums[0] = 2$ satisfies $-\infty \le 2 \le \infty$
      - Instantiate root node $\text{TreeNode}(2)$, advance $i \leftarrow 1$
      - **Left Subtree Call:** `dfs(-inf, 2)`
        - Token $nums[1] = 1$ satisfies $-\infty \le 1 \le 2$
        - Instantiate left child $\text{TreeNode}(1)$, advance $i \leftarrow 2$
        - Call `dfs(-inf, 1)`: Token $nums[2] = 3 \notin [-\infty, 1] \implies$ Returns `None`
        - Call `dfs(1, 2)`: Token $nums[2] = 3 \notin [1, 2] \implies$ Returns `None`
        - Node $1$ has `left = None, right = None`
      - **Right Subtree Call:** `dfs(2, +inf)`
        - Token $nums[2] = 3$ satisfies $2 \le 3 \le \infty$
        - Instantiate right child $\text{TreeNode}(3)$, advance $i \leftarrow 3$
        - Calls for children of $3$: pointer $i = 3 == \text{len}(nums) \implies$ Return `None`
        - Node $3$ has `left = None, right = None`
      - Root $2$ receives left child $1$ and right child $3$.
  - Reconstructed tree matches original input identically.
- **Null Delimiter Economy:** A generic binary tree of size $N$ requires $N + 1$ null markers (e.g. `"2,1,null,null,3,null,null"`). A BST requires strictly $N$ numbers without null markers.
- **Empty Tree Instance:** $root = \text{None} \implies$ Serialized: `""` $\implies$ Deserialized: `None`

This instance demonstrates how the binary search tree invariant ($val_{left} < val_{root} < val_{right}$) eliminates the need for structural null tokens, mathematically proves why preorder sequences uniquely determine BST topologies, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a Binary Search Tree (BST):
Design an algorithm to **serialize** the BST into a compact string and **deserialize** the string back into the original tree structure.
Make the serialized representation as compact as possible.

```text
Binary Search Tree:
        2
       / \
      1   3

Generic Tree Encoding (With Nulls):   "2,1,null,null,3,null,null"  (7 tokens)
BST Compact Encoding (No Nulls):      "2 1 3"                      (3 tokens)
```

### Why BSTs Require Zero Null Markers
- In a generic binary tree, the preorder sequence $[2, 1, 3]$ is ambiguous: does $3$ belong to the right of $2$, or to the right of $1$? Marking missing children with `null` is mandatory to resolve ambiguity.
- In a **Binary Search Tree**, all elements in the left subtree must be $< root$, and all elements in the right subtree must be $> root$.
- Therefore, in $[2, 1, 3]$:
  - Because $1 < 2$, $1$ must be in the left subtree.
  - Because $3 > 2$, $3$ cannot belong to the subtree of $1$ (which is restricted to $(-\infty, 2)$); it **must** belong to the right subtree of $2$!
- The numerical values themselves dictate parent-child relationships, rendering all null tokens completely redundant.

---

## 2. Conceptual Foundation & Invariants

### 1. Preorder Traversal Serialization:
A simple depth-first preorder traversal records each node's value upon first arrival:
$$
\text{Serialize}(root) = root.val \circ \text{Serialize}(root.left) \circ \text{Serialize}(root.right)
$$
Null nodes are skipped completely.

### 2. Range-Constrained Deserialization:
A recursive function `dfs(mi, mx)` reconstructs the tree using a global cursor $i$ in the token stream:
1. If $i == |nums|$ or the current number $nums[i]$ falls outside $[mi, mx]$:
   $$
   nums[i] < mi \quad \lor \quad nums[i] > mx
   $$
   Then $nums[i]$ cannot belong to this subtree. Return `None` without advancing $i$.
2. Otherwise, $nums[i]$ is the root of the current subtree:
   - Extract $x = nums[i]$ and advance $i \leftarrow i + 1$.
   - The left subtree must have values in range $[mi, x]$:
     $$
     node.left \leftarrow \text{dfs}(mi, \; x)
     $$
   - The right subtree must have values in range $[x, \; mx]$:
     $$
     node.right \leftarrow \text{dfs}(x, \; mx)
     $$
3. Return $node$.

> **Boundary Invariant.** The recursive interval $[mi, mx]$ strictly defines the valid numerical range for all descendants of the current tree node, ensuring every element attaches to its unique valid parent in $O(1)$ comparisons.

---

## 3. Step-by-Step Worked Execution

We trace $root = [2, 1, 3]$:

---

### Phase 1: Serialization Walk
- Visit 2: write `"2"`.
- Left to 1: write `"1"`.
- Right to 3: write `"3"`.
- Serialized result: `"2 1 3"`.

---

### Phase 2: Deserialization Walk
Tokens: $nums = [2, 1, 3]$. Stream index $i = 0$.
Call `dfs(-inf, +inf)`:

#### Step 1: Root Construction
- Current token: $nums[0] = 2$.
- Range check: $-\infty \le 2 \le +\infty$ (**Valid**).
- Allocate $\text{TreeNode}(2)$. Advance $i \leftarrow 1$.

#### Step 2: Left Child of 2
- Call `dfs(-inf, 2)`:
  - Current token: $nums[1] = 1$.
  - Range check: $-\infty \le 1 \le 2$ (**Valid**).
  - Allocate $\text{TreeNode}(1)$. Advance $i \leftarrow 2$.
  - Call `dfs(-inf, 1)`:
    - Current token: $nums[2] = 3$.
    - Range check: $3 \le 1$ (False! $3 > 1$).
    - Returns `None`. Cursor stays $i = 2$.
  - Call `dfs(1, 2)`:
    - Current token: $nums[2] = 3$.
    - Range check: $3 \le 2$ (False! $3 > 2$).
    - Returns `None`. Cursor stays $i = 2$.
  - Subtree for Node 1 completes: `TreeNode(1, left=None, right=None)`.
  - Attach: $2.left = 1$.

#### Step 3: Right Child of 2
- Call `dfs(2, +inf)`:
  - Current token: $nums[2] = 3$.
  - Range check: $2 \le 3 \le +\infty$ (**Valid**).
  - Allocate $\text{TreeNode}(3)$. Advance $i \leftarrow 3$.
  - Call `dfs(2, 3)`:
    - $i = 3 == |nums|$ (End of tokens). Returns `None`.
  - Call `dfs(3, +inf)`:
    - $i = 3 == |nums|$. Returns `None`.
  - Subtree for Node 3 completes: `TreeNode(3, left=None, right=None)`.
  - Attach: $2.right = 3$.

#### Step 4: Root Completion
- Node 2 has `left = 1, right = 3`.
- Returns root $\text{TreeNode}(2)$.

---

## 4. Complete Execution Trace

| Call Frame | Active Interval $[mi, mx]$ | Scanned Token $nums[i]$ | In Range? | Action Taken | Cursor $i$ | Resulting Subtree |
|:---:|:---:|:---:|:---:|:---|:---:|:---|
| **Root** | $[-\infty, +\infty]$ | $2$ | **Yes** | Create Node $2$ | $0 \to 1$ | — |
| $\to$ **$2.left$** | $[-\infty, 2]$ | $1$ | **Yes** | Create Node $1$ | $1 \to 2$ | — |
| $\to\to$ **$1.left$** | $[-\infty, 1]$ | $3$ | No ($3 > 1$) | Return `None` | $2$ | `None` |
| $\to\to$ **$1.right$** | $[1, 2]$ | $3$ | No ($3 > 2$) | Return `None` | $2$ | `None` |
| $\to$ Complete | — | — | — | Node 1 finished | $2$ | $(1)$ |
| $\to$ **$2.right$** | $[2, +\infty]$ | $3$ | **Yes** | Create Node $3$ | $2 \to 3$ | — |
| $\to\to$ **$3.left$** | $[2, 3]$ | EOF | EOF | Return `None` | $3$ | `None` |
| $\to\to$ **$3.right$** | $[3, +\infty]$ | EOF | EOF | Return `None` | $3$ | `None` |
| $\to$ Complete | — | — | — | Node 3 finished | $3$ | $(3)$ |
| **Final** | — | — | — | Root finished | $3$ | **$2 \to (1, 3)$** |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = \text{None}$):** Emits `""`. Deserializer parses empty token list and immediately returns `None`.
- **Single Node Tree ($root = [5]$):** Emits `"5"`. Deserializer allocates Node 5, child calls detect EOF $\implies \text{Node}(5)$.
- **Degenerate Left-Skewed Tree ($3 \to 2 \to 1$):** Preorder sequence is `"3 2 1"`. Each node enters the left branch with tightened upper bounds: $[-\infty, 3] \to [-\infty, 2] \to [-\infty, 1]$. Reconstructs linear left spine correctly.
- **Degenerate Right-Skewed Tree ($1 \to 2 \to 3$):** Preorder sequence is `"1 2 3"`. Lower bounds increase: $[1, \infty] \to [2, \infty] \to [3, \infty]$. Reconstructs linear right spine.

---

## 6. Traps & Common Anti-Patterns

- **Using Quadratic Partitioning ($O(N^2)$):** Searching linearly for the first element greater than the root to split left and right subarrays takes $O(N^2)$ time on skewed trees. Using the global cursor with $[mi, mx]$ intervals processes each element in guaranteed $O(1)$ amortized time.
- **Including Null Tokens in Serialized Output:** Serializing with `null` works correctly but wastes memory and fails the problem requirement to optimize compactness.
- **Splitting and Popping from Arrays:** Calling `list.pop(0)` takes $O(N)$ per element. Using an integer index pointer `i` guarantees $O(1)$ token access.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **Serialization:** Preorder DFS visits each of the $N$ nodes once in $O(N)$ time.
  - **Deserialization:** Each token is examined at most a constant number of times (at its valid allocation frame and by immediate parent boundaries). Total time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ recursion stack depth, where $H \le N$ is the tree height ($O(\log N)$ for balanced trees, $O(N)$ for skewed trees).
  - The token list stores $N$ integers.
