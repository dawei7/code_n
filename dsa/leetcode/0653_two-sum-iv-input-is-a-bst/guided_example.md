# Guided Example: Two Sum IV - Input is a BST

We trace the step-by-step complement set lookup ($k - root.val \in vis$), tree traversal node exploration (DFS / in-order), visited membership tracking ($vis.\text{add}(val)$), early pair match termination ($u + v == k$), and dual two-pointer in-order search equivalence on representative binary search trees:

- **Input:**
  - $root = [5, 3, 6, 2, 4, \text{null}, 7]$
  - Target sum: $k = 9$
  - Tree topology:
    ```text
            5
          /   \
         3     6
        / \     \
       2   4     7
    ```
- **Required output:** `true`
  - Problem objective: Determine whether there exist **two distinct nodes** in the binary search tree whose values sum to $k$:
    $$
    u.val + v.val = k \quad (u \ne v)
    $$
  - Notice that you cannot use the same node twice (e.g. if $k = 10$, you cannot pair Node 5 with itself).
- **Complement Lookup & Traversal Invariant:**
  - **The Complement Principle:**
    - For any active node with value $x$, its unique required pairing partner is:
      $$
      \text{target\_partner} = k - x
      $$
    - If $\text{target\_partner}$ has already been visited in earlier traversal steps, we have confirmed the existence of a valid pair $\{x, \; k - x\}$ and can terminate immediately with **`true`**!
    - Otherwise, add $x$ to the visited set $vis$ and continue searching.
  - **In-Order Monotonicity Alternative:**
    - Because the tree is a Binary Search Tree (BST), an in-order traversal ($\text{left} \to \text{root} \to \text{right}$) visits all node values in **strictly ascending sorted order**:
      $$
      [2, \; 3, \; 4, \; 5, \; 6, \; 7]
      $$
    - On this sorted array, standard bilateral two pointers ($left = 0, right = n - 1$) converge toward $k$ in linear time without extra hash structures.
- **Step-by-Step Worked Execution Trace on $[5, 3, 6, 2, 4, \text{null}, 7], k = 9$:**
  - Initialize empty visited set:
    $$
    vis = \emptyset
    $$
  - **Visit Node 5 (Root):**
    - Value $x = 5$.
    - Required complement:
      $$
      k - x = 9 - 5 = \mathbf{4}
      $$
    - Is $4 \in vis$? $vis = \emptyset \implies \mathbf{False}$.
    - Record node 5:
      $$
      vis \leftarrow \{5\}
      $$
    - Branch to left child (Node 3).
  - **Visit Node 3:**
    - Value $x = 3$.
    - Required complement:
      $$
      k - x = 9 - 3 = \mathbf{6}
      $$
    - Is $6 \in vis$? $\{5\} \implies \mathbf{False}$.
    - Record node 3:
      $$
      vis \leftarrow \{3, \; 5\}
      $$
    - Branch to left child (Node 2).
  - **Visit Node 2:**
    - Value $x = 2$.
    - Required complement:
      $$
      k - x = 9 - 2 = \mathbf{7}
      $$
    - Is $7 \in vis$? $\{3, 5\} \implies \mathbf{False}$.
    - Record node 2:
      $$
      vis \leftarrow \{2, \; 3, \; 5\}
      $$
    - Leaf reached; backtrack to Node 3 and branch to right child (Node 4).
  - **Visit Node 4:**
    - Value $x = 4$.
    - Required complement:
      $$
      k - x = 9 - 4 = \mathbf{5}
      $$
    - Check membership:
      $$
      5 \in vis \iff 5 \in \{2, \; 3, \; 5\} \implies \mathbf{True!}
      $$
    - Node 4 has found its previously recorded partner Node 5!
    - Sum check:
      $$
      4 + 5 = 9 == k
      $$
    - Pair confirmed: $\{4, 5\}$.
    - Immediate early exit: return **`true`**.
- **In-Order Two-Pointer Verification:**
  - In-order sorted list: $A = [2, 3, 4, 5, 6, 7]$.
  - $l = 0$ ($A[0] = 2$), $r = 5$ ($A[5] = 7$).
  - Sum $2 + 7 = 9 == k \implies$ Valid pair found on step 1!
- **Target Too Large ($k = 28$):**
  - Max possible sum of two nodes is $6 + 7 = 13 < 28$.
  - Entire tree visited $\implies vis = \{2, 3, 4, 5, 6, 7\}$.
  - 0 complements match $\implies$ Returns **`false`**.
- **Duplicate Element Prevention ($k = 6$, Tree contains single 3):**
  - At Node 3: complement is $6 - 3 = 3$.
  - Since $3 \notin vis$ prior to inserting Node 3, the node is not paired with itself.
  - Node 3 is added to $vis$. Unless a second distinct node with value 3 exists, self-matching is safely avoided.

This instance demonstrates complement set intersection over tree-structured key-value domains, mathematically proves why pre-insertion queries prevent self-referential collision errors, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a Binary Search Tree and target $k$:
Determine if there exist **two distinct nodes** whose values sum to $k$.

```text
Tree:
        5
      /   \
     3     6
    / \     \
   2   4     7

Target k = 9:
  Visit 5: need 4 -> not seen yet -> vis = {5}
  Visit 3: need 6 -> not seen yet -> vis = {3, 5}
  Visit 2: need 7 -> not seen yet -> vis = {2, 3, 5}
  Visit 4: need 5 -> 5 IS IN VISITED SET! -> MATCH!

Pair (4, 5) sums to 9. Return true.
```

### The Invariant of Pre-Insert Complement Checking
- Testing `k - root.val in vis` **before** adding `root.val` to `vis` guarantees that a single node cannot pair with itself when $k = 2 \cdot root.val$.
- Early return halts traversal the moment the first valid pair is discovered.

---

## 2. Conceptual Foundation & Invariants

### 1. The Complement Test:
For node $u$:
$$
k - u.val \in vis \implies \text{return true}
$$
$$
vis \leftarrow vis \cup \{u.val\}
$$

### 2. Dual Two-Pointer Alternative:
In-order traversal produces sorted list $L$.
Initialize $l = 0, r = |L| - 1$.
While $l < r$:
- $s = L[l] + L[r]$
- If $s == k \implies \text{return true}$
- If $s < k \implies l \leftarrow l + 1$
- If $s > k \implies r \leftarrow r - 1$
Return `false`.

> **Orthogonal Complement Invariant.** The algebraic involution $\tau(x) = k - x$ maps any target sum representation into a point reflection across $k/2$, enabling constant-time hash set collision detection.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Visit 5
- Need $9 - 5 = 4$. $4 \notin vis$.
- $vis = \{5\}$.

---

### Step 2: Visit 3
- Need $9 - 3 = 6$. $6 \notin vis$.
- $vis = \{3, 5\}$.

---

### Step 3: Visit 2
- Need $9 - 2 = 7$. $7 \notin vis$.
- $vis = \{2, 3, 5\}$.

---

### Step 4: Visit 4
- Need $9 - 4 = 5$.
- $5 \in vis$ is **True**!
- Pair $(4, 5)$ satisfies $4 + 5 = 9$.
- Return **`true`**.

---

## 4. Complete Execution Trace

| Traversed Node | Value $x$ | Complement $k - x$ | In Visited Set? | Action | Visited Set After |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Node 5 | $5$ | $4$ | No | Insert 5 | $\{5\}$ |
| Node 3 | $3$ | $6$ | No | Insert 3 | $\{3, 5\}$ |
| Node 2 | $2$ | $7$ | No | Insert 2 | $\{2, 3, 5\}$ |
| **Node 4** | **$4$** | **$5$** | **Yes** | **Match Found** | Terminated |
| **Result** | — | — | — | — | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node Tree ($root = [1], k = 2$):** $2 - 1 = 1$, but 1 not in set $\implies$ returns `false` (cannot reuse same node).
- **Target Not Reachable:** Traverses all nodes, returns `false`.
- **Negative Values ($[-2, -1, 3], k = 1$):** $-2 + 3 = 1 \implies$ returns `true`.
- **Large BST ($10^4$ nodes):** Set lookups execute in $O(1)$ amortized time.

---

## 6. Traps & Common Anti-Patterns

- **Adding Node to Set Before Complement Check:** Writing `vis.add(root.val)` before `if k - root.val in vis` causes a node with value $3$ to falsely match itself when $k = 6$. Check complement first!
- **Searching the BST for Every Node ($O(N \log N)$):** Searching the BST for $k - x$ for each node takes $O(N \log N)$ (or $O(N^2)$ for unbalanced trees). A hash set or sorted two-pointer pass runs in strictly linear $O(N)$ time.
- **Tree Modification:** Modifying node pointers is unnecessary and destroys tree structure.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Traversal visits each node at most once: $\mathcal{O}(N)$.
  - Hash set membership test and insertion: $\mathcal{O}(1)$ average time.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the hash set $vis$ and recursion call stack.
