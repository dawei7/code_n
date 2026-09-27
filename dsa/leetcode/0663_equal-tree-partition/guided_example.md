# Guided Example: Equal Tree Partition

We trace the step-by-step bottom-up post-order subtree summation ($S(u) = u.val + S(left) + S(right)$), total tree mass parity verification ($S_{total} \pmod 2 == 0$), target half-sum identification ($T = S_{total} / 2$), root-removal boundary exclusion (`seen.pop()`), and single-edge cut bipartition validation on representative binary tree graphs:

- **Input:**
  - Tree: $root = [5, 10, 10, \text{null}, \text{null}, 2, 3]$
  - Tree topology:
    ```text
            5
          /   \
        10     10
              /  \
             2    3
    ```
- **Required output:** `true`
  - Partition definition:
    - You must remove **exactly one edge** from the tree.
    - Removing one edge disconnects the tree into exactly two non-empty trees $T_1$ and $T_2$.
    - Return `true` if and only if:
      $$
      \text{sum}(T_1) = \text{sum}(T_2) = \frac{S_{total}}{2}
      $$
- **Edge Cut & Subtree Sum Equivalence Invariant:**
  - **The Subtree Cut Principle:**
    - Any edge in a tree connects a parent $p$ to a child $u$.
    - Cutting this edge $(p, u)$ detaches the entire subtree rooted at $u$ as $T_1$.
    - The sum of $T_1$ is simply the subtree sum $S(u)$.
    - The remaining component $T_2$ has sum:
      $$
      \text{sum}(T_2) = S_{total} - S(u)
      $$
    - The two components have equal sum if and only if:
      $$
      S(u) = S_{total} - S(u) \iff S(u) = \frac{S_{total}}{2}
      $$
  - **The Two Mandatory Filtering Gates:**
    1. **Parity Gate:** If the total tree sum $S_{total}$ is odd ($S_{total} \pmod 2 \ne 0$), dividing into two equal integer sums is mathematically impossible $\implies \mathbf{False}$.
    2. **Proper Edge Existence Gate (Root Exclusion):**
       - Cutting an edge requires an actual edge to cut.
       - The root node itself has no parent edge.
       - If $S_{total} = 0$, then $S_{total} / 2 = 0$. The root's subtree sum is 0, but you cannot "cut" above the root.
       - Therefore, the root's own sum must be **explicitly excluded** from the set of candidate cuts (`seen.pop()`).
- **Step-by-Step Worked Execution Trace on $[5, 10, 10, \text{null}, \text{null}, 2, 3]$:**
  - Nodes:
    - Root: Node 5
    - Left child: Node $10_L$
    - Right child: Node $10_R$
    - Left child of $10_R$: Node 2
    - Right child of $10_R$: Node 3
  - **Post-Order Subtree Summation:**
    - **Step 1: Leaf Node 2:**
      $$
      S(2) = 2 + 0 + 0 = \mathbf{2}
      $$
      - Register: `seen = [2]`.
    - **Step 2: Leaf Node 3:**
      $$
      S(3) = 3 + 0 + 0 = \mathbf{3}
      $$
      - Register: `seen = [2, 3]`.
    - **Step 3: Branch Node $10_R$:**
      $$
      S(10_R) = 10 + S(2) + S(3) = 10 + 2 + 3 = \mathbf{15}
      $$
      - Register: `seen = [2, 3, 15]`.
    - **Step 4: Leaf Node $10_L$:**
      $$
      S(10_L) = 10 + 0 + 0 = \mathbf{10}
      $$
      - Register: `seen = [2, 3, 15, 10]`.
    - **Step 5: Root Node 5:**
      $$
      S_{total} = S(5) = 5 + S(10_L) + S(10_R) = 5 + 10 + 15 = \mathbf{30}
      $$
      - Register: `seen = [2, 3, 15, 10, 30]`.
  - **Step 6: Parity and Target Calculation:**
    - Total sum: $S_{total} = 30$.
    - Check parity:
      $$
      30 \pmod 2 == 0 \implies \mathbf{Even\ (Passes\ Gate\ 1)}
      $$
    - Target half-sum:
      $$
      T = \frac{S_{total}}{2} = \frac{30}{2} = \mathbf{15}
      $$
  - **Step 7: Exclude Root and Query Proper Subtree Cuts:**
    - Remove total root sum from list:
      $$
      seen = [2, \; 3, \; \mathbf{15}, \; 10]
      $$
    - Does any proper subtree sum equal target $T = 15$?
      $$
      15 \in [2, \; 3, \; \mathbf{15}, \; 10] \implies \mathbf{True!}
      $$
    - The cut is achieved by severing the edge between Root 5 and Node $10_R$:
      - Component 1 (Subtree $10_R$): values $\{10, 2, 3\}$, sum $= 10 + 2 + 3 = \mathbf{15}$.
      - Component 2 (Rest of tree): values $\{5, 10\}$, sum $= 5 + 10 = \mathbf{15}$.
    - Both components have sum $15$. Equal partition confirmed!
    - Return **`true`**.
- **The Zero-Sum Trap ($root = [0]$):**
  - Only one node with value 0.
  - Total sum $S_{total} = 0$, target $T = 0 / 2 = 0$.
  - Subtree sums: `[0]`.
  - Popping root sum leaves `seen = []`.
  - $0 \in [] \implies \mathbf{False}$!
  - Correctly avoids falsely declaring that a single isolated node can be cut.
- **Asymmetric Tree Without Valid Cut ($root = [1, 2, 10, \dots]$):**
  - Total sum $S_{total} = 35$.
  - $35$ is odd $\implies$ Returns **`false`** immediately.

This instance demonstrates edge-contraction bipartition on tree metrics and post-order recursive accumulation, mathematically proves why root-boundary exclusion enforces proper non-empty graph decomposition, and derives $O(N)$ runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
Determine if you can **remove exactly one edge** to split the tree into two components with **equal sums**.

```text
Tree:
        5
      /   \
    10     10  <-- CUT THIS EDGE!
          /  \
         2    3

Subtree at right 10: 10 + 2 + 3 = 15
Rest of tree:        5 + 10     = 15

Both sides sum to 15! Return true.
```

### The Invariant of the Single Edge Cut
- Every edge in a tree is the parent edge of some non-root node $u$.
- Severing the edge above $u$ isolates the subtree rooted at $u$ with sum $S(u)$.
- The cut produces equal partitions if and only if:
  $$
  S(u) = \frac{S_{total}}{2} \quad \text{for some non-root node } u
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. Post-Order Subtree Sum:
$$
S(u) = u.val + S(u.left) + S(u.right)
$$

### 2. The Two Validation Gates:
1. $S_{total} \pmod 2 == 0$ (Total sum must be even).
2. $\frac{S_{total}}{2} \in \{S(u) \mid u \ne root\}$ (Target must appear in a proper subtree).

> **Fundamental Tree Bipartition Invariant.** Any tree edge $e \in E$ defines a fundamental cut $(V_1, V_2)$ where $V_1$ is isomorphic to the descendant closure of some proper node $u$, establishing an exact equivalence between edge cuts and subtree sums.

---

## 3. Step-by-Step Worked Execution

We trace $root = [5, 10, 10, \text{null}, \text{null}, 2, 3]$:

---

### Step 1: Compute Subtree Sums
- $S(2) = 2$.
- $S(3) = 3$.
- $S(10_R) = 10 + 2 + 3 = 15$.
- $S(10_L) = 10$.
- $S_{total} = S(5) = 5 + 10 + 15 = 30$.

---

### Step 2: Check Even Parity
- $30 \pmod 2 == 0 \implies$ Even.
- Target $T = 30 / 2 = 15$.

---

### Step 3: Check Candidate Subtrees
- Subtree sums: $\{2, 3, \mathbf{15}, 10\}$.
- $15$ exists in proper subtrees!
- Return **`true`**.

---

## 4. Complete Execution Trace

| Node Evaluated | Left Subtree Sum | Right Subtree Sum | Node Value | Subtree Sum $S(u)$ | Candidate for Cut? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Node 2 | $0$ | $0$ | $2$ | $2$ | Yes ($2 \ne 15$) |
| Node 3 | $0$ | $0$ | $3$ | $3$ | Yes ($3 \ne 15$) |
| **Node $10_R$** | **$2$** | **$3$** | **$10$** | **`15`** | **MATCH! ($15 == T$)** |
| Node $10_L$ | $0$ | $0$ | $10$ | $10$ | Yes ($10 \ne 15$) |
| Root 5 | $10$ | $15$ | $5$ | $30$ | **No (Root cannot be cut)** |
| **Conclusion** | — | — | — | — | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node ($root = [0]$):** $S = 0, T = 0$. But no edge exists to cut $\implies$ returns `false` (via `seen.pop()`).
- **Two Nodes ($root = [1, 1]$):** $S = 2, T = 1$. Child has sum 1 $\implies$ returns `true`.
- **Negative Values ($root = [0, -1, 1]$):** Handled transparently by algebra.
- **Odd Total Sum:** Returns `false` immediately without searching.

---

## 6. Traps & Common Anti-Patterns

- **Forgetting to Exclude the Root:** If $S_{total} = 0$, $T = 0$. The root's sum is 0. If you don't remove the root's sum from candidates, you return `true` on $root = [0]$, which is wrong because there are 0 edges in the tree!
- **Floating Point Division:** In Python, `s / 2` creates a float (e.g. `15.0`). Use integer division `s // 2` to match integer subtree sums.
- **Cutting Multiple Edges:** The problem allows cutting **exactly one** edge, not two.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single post-order DFS traversal computes all subtree sums: $\mathcal{O}(N)$.
  - Set lookup for target $S_{total} // 2$: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 2$ ms for $N = 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store subtree sums in an array/set and for the recursion call stack.
