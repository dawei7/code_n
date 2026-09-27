# Guided Example: All Possible Full Binary Trees

We trace the step-by-step full binary tree parity proof ($n = 2k + 1$), Catalan partition branching, recursive subproblem memoization, Cartesian product tree construction, and structural enumeration on representative node budgets:

- **Input:**
  $$
  n = 7
  $$
- **Required output:** `5` distinct full binary trees
  - Full binary tree (FBT) rules:
    - A full binary tree is a binary tree in which every node has **either 0 or 2 children**.
    - All node values are set to $0$.
    - Return a list of all possible full binary trees with $n$ nodes in any order.
    - For $n = 7$:
      - The root consumes $1$ node.
      - The remaining $n - 1 = 6$ nodes must be split between the left and right subtrees.
      - Because each subtree must itself be an FBT, the node allocations $(i, j)$ must both be **odd positive integers**:
        - Allocation $(1, 5)$: Left has 1 node, Right has 5 nodes $\implies 1 \times 2 = 2$ trees.
        - Allocation $(3, 3)$: Left has 3 nodes, Right has 3 nodes $\implies 1 \times 1 = 1$ tree.
        - Allocation $(5, 1)$: Left has 5 nodes, Right has 1 node $\implies 2 \times 1 = 2$ trees.
      - Total trees generated: $2 + 1 + 2 = \mathbf{5}$ trees (the $3$rd Catalan number $C_3$).
- **The Parity & Cartesian Decomposition Invariant:**
  - **The Odd-Parity Invariant:**
    - A single leaf has $1$ node (odd).
    - Every internal node adds exactly $2$ children.
    - If a tree has $k$ internal nodes, the total number of nodes is:
      $$
      n = 1 + 2k
      $$
    - Therefore, **a full binary tree exists if and only if $n$ is odd**.
    - If $n$ is even, no full binary tree can ever be formed $\implies$ immediately return an empty list `[]`.
  - **Catalan Subtree Partitioning:**
    - For odd $n$, the root consumes $1$ node.
    - The remaining $n - 1$ nodes must be divided into:
      $$
      i \text{ nodes in left subtree} \quad \text{and} \quad j = n - 1 - i \text{ nodes in right subtree}
      $$
    - Both $i$ and $j$ must be odd: $i \in \{1, 3, 5, \dots, n - 2\}$.
    - For each valid partition $(i, j)$:
      - Let $L = \text{dfs}(i)$ be the set of all full binary trees with $i$ nodes.
      - Let $R = \text{dfs}(j)$ be the set of all full binary trees with $j$ nodes.
      - The Cartesian product $L \times R$ creates all combinations:
        $$
        \forall left \in L, \; \forall right \in R: \quad \text{Tree}(\text{root}=0, \; \text{left}, \; \text{right})
        $$
    - Memoizing subproblems avoids recomputing tree topologies for identical subtree sizes.

---

## 1. Instance & Teaching Goal

Given $n = 7$ nodes, demonstrate how recursive odd-integer partitions assemble the 5 Catalan trees.

```text
Node Budget n = 7 (Remaining for subtrees: 7 - 1 = 6):

Partition 1: Left = 1 node, Right = 5 nodes
  - Left has 1 tree:  (0)
  - Right has 2 trees: 5-node configurations
  -> Generates 1 * 2 = 2 trees

Partition 2: Left = 3 nodes, Right = 3 nodes
  - Left has 1 tree:  3-node balanced tree
  - Right has 1 tree: 3-node balanced tree
  -> Generates 1 * 1 = 1 tree

Partition 3: Left = 5 nodes, Right = 1 node
  - Left has 2 trees: 5-node configurations
  - Right has 1 tree: (0)
  -> Generates 2 * 1 = 2 trees

Total Catalan Trees = 2 + 1 + 2 = 5
```

The teaching goal is to demonstrate how structural recurrence on tree sizes reduces exhaustive tree generation to Catalan convolutions.

---

## 2. Conceptual Foundation & Invariants

### 1. Parity Filter:
$$
n \equiv 0 \pmod 2 \implies \text{return } []
$$

### 2. Catalan Convolution Recurrence:
$$
\text{dfs}(n) = \bigcup_{\substack{i \in \{1, 3, \dots, n-2\} \\ j = n - 1 - i}} \left\{ \text{Node}(0, left, right) \;\middle|\; left \in \text{dfs}(i), \; right \in \text{dfs}(j) \right\}
$$
Base case: $\text{dfs}(1) = [\text{Node}(0)]$.

---

## 3. Step-by-Step Worked Execution

We trace all subtree sizes from $1$ up to $7$:

---

### Step 1: Base Case $n = 1$
- Only $1$ node.
- A single leaf with value $0$ and no children:
  $$
  \text{dfs}(1) = [T_1] \quad (\text{Count} = 1)
  $$

---

### Step 2: Subproblem $n = 3$
- Budget remaining: $3 - 1 = 2$.
- Odd partitions: only $(i=1, j=1)$.
- Left subtrees: $\text{dfs}(1) = [T_1]$.
- Right subtrees: $\text{dfs}(1) = [T_1]$.
- Combine: $\text{Node}(0, T_1, T_1)$.
- Result:
  $$
  \text{dfs}(3) = [T_3] \quad (\text{Count} = 1 \times 1 = 1)
  $$

---

### Step 3: Subproblem $n = 5$
- Budget remaining: $5 - 1 = 4$.
- Odd partitions: $(1, 3)$ and $(3, 1)$.
- **Partition $(i=1, j=3)$:**
  - $left \in \text{dfs}(1) \implies T_1$
  - $right \in \text{dfs}(3) \implies T_3$
  - Yields tree $T_{5A} = \text{Node}(0, T_1, T_3)$.
- **Partition $(i=3, j=1)$:**
  - $left \in \text{dfs}(3) \implies T_3$
  - $right \in \text{dfs}(1) \implies T_1$
  - Yields tree $T_{5B} = \text{Node}(0, T_3, T_1)$.
- Result:
  $$
  \text{dfs}(5) = [T_{5A}, T_{5B}] \quad (\text{Count} = 1 + 1 = 2)
  $$

---

### Step 4: Target Problem $n = 7$
- Budget remaining: $7 - 1 = 6$.
- Odd partitions: $(1, 5)$, $(3, 3)$, and $(5, 1)$.

---

#### Allocation A: $(i=1, j=5)$
- $left \in \text{dfs}(1)$: $1$ tree ($T_1$).
- $right \in \text{dfs}(5)$: $2$ trees ($T_{5A}, T_{5B}$).
- Combinations:
  1. $\text{Node}(0, T_1, T_{5A})$
  2. $\text{Node}(0, T_1, T_{5B})$
- Count $= 1 \times 2 = \mathbf{2}$.

---

#### Allocation B: $(i=3, j=3)$
- $left \in \text{dfs}(3)$: $1$ tree ($T_3$).
- $right \in \text{dfs}(3)$: $1$ tree ($T_3$).
- Combination:
  3. $\text{Node}(0, T_3, T_3)$
- Count $= 1 \times 1 = \mathbf{1}$.

---

#### Allocation C: $(i=5, j=1)$
- $left \in \text{dfs}(5)$: $2$ trees ($T_{5A}, T_{5B}$).
- $right \in \text{dfs}(1)$: $1$ tree ($T_1$).
- Combinations:
  4. $\text{Node}(0, T_{5A}, T_1)$
  5. $\text{Node}(0, T_{5B}, T_1)$
- Count $= 2 \times 1 = \mathbf{2}$.

---

### Total Output:
$$
\text{Total Trees} = 2 + 1 + 2 = \mathbf{5}
$$

---

## 4. Complete Execution Trace

| Partition $(i, j)$ | Left Subtree Count $\lvert \text{dfs}(i) \rvert$ | Right Subtree Count $\lvert \text{dfs}(j) \rvert$ | Product $(\lvert \text{dfs}(i) \rvert \times \lvert \text{dfs}(j) \rvert)$ | Resulting Topologies | Running Total |
|:---:|:---:|:---:|:---:|:---|:---:|
| $(1, 5)$ | $1$ ($T_1$) | $2$ ($T_{5A}, T_{5B}$) | $1 \times 2 = 2$ | Left leaf, Right deep (2 forms) | $2$ |
| $(3, 3)$ | $1$ ($T_3$) | $1$ ($T_3$) | $1 \times 1 = 1$ | Perfectly symmetric balanced tree | $3$ |
| **$(5, 1)$** | **$2$ ($T_{5A}, T_{5B}$)** | **$1$ ($T_1$)** | **$2 \times 1 = 2$** | **Left deep (2 forms), Right leaf** | **`5`** |

---

## 5. Boundary Cases & Failure Modes

- **Even $n$ (e.g. $n = 2, 4, 6$):** Impossible to construct an FBT $\implies$ loop produces no odd partitions, returns empty list `[]`.
- **$n = 1$:** Single node without children $\implies$ `[TreeNode(0)]`.
- **Maximum $n = 19$:** The number of trees is given by the 9th Catalan number $C_9 = 4862$. Memoization ensures each subproblem size is evaluated once.

---

## 6. Traps & Common Anti-Patterns

- **Attempting Partitions on Even Sizes:** Testing even $i$ leads to empty sets $|\text{dfs}(i)| = 0$, wasting function calls. Stepping $i \in 1, 3, \dots, n-2$ skips all invalid partitions.
- **Node Object Mutation:** Reusing the same mutable node instance across different trees causes cross-tree corruption if node pointers are subsequently altered. Constructing new parent `TreeNode(0, left, right)` instances preserves topology integrity.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The number of full binary trees with $n = 2k + 1$ nodes is given by the $k$-th Catalan number:
    $$
    C_k = \frac{1}{k+1}\binom{2k}{k} = \mathcal{O}\left(\frac{4^k}{k^{3/2}}\right)
    $$
  - Generating all trees takes time proportional to the total number of created nodes: $\mathcal{O}(n \cdot C_{(n-1)/2})$.
  - For $n = 7$, $k = 3 \implies C_3 = 5$, executing in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - Memoization cache storing subtree references: $\mathcal{O}(n \cdot C_{(n-1)/2})$ space.
