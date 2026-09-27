# Guided Example: Path Sum IV

We trace the step-by-step three-digit coordinate unpacking ($\text{hundreds} \to d, \; \text{tens} \to p, \; \text{units} \to v$), hash-map coordinate registration ($mp[10d + p] = v$), parent-child binary relationship derivation ($left = 10(d+1) + (2p - 1), \; right = left + 1$), depth-first cumulative path sum propagation ($t \leftarrow t + v$), leaf node identification ($left \notin mp \land right \notin mp$), and total root-to-leaf path aggregation on representative encoded tree arrays:

- **Input:** $nums = [113, 215, 221]$
- **Required output:** `12`
  - Encoding protocol:
    - Each 3-digit integer represents a tree node:
      - Hundreds digit: Depth $d$ of the node ($1$-indexed, $1 \le d \le 4$).
      - Tens digit: Position $p$ within depth $d$ ($1$-indexed, $1 \le p \le 2^{d-1}$).
      - Units digit: Node value $v$ ($0 \le v \le 9$).
    - Objective: Calculate the **sum of all path values from the root to every leaf**.
- **Coordinate Geometry & Binary Child Invariant:**
  - **Child Coordinate Mapping:**
    - In a 1-indexed complete binary tree, a node at depth $d$ and position $p$ has:
      - Left child at depth $d + 1$, position:
        $$
        p_{left} = 2p - 1
        $$
        Key code:
        $$
        k_{left} = 10(d + 1) + (2p - 1)
        $$
      - Right child at depth $d + 1$, position:
        $$
        p_{right} = 2p
        $$
        Key code:
        $$
        k_{right} = 10(d + 1) + 2p = k_{left} + 1
        $$
  - **The Leaf Condition:**
    - A node is a **leaf** if and only if **neither** its left child nor its right child exists in the dictionary:
      $$
      k_{left} \notin mp \quad \land \quad k_{right} \notin mp
      $$
    - When a leaf is reached, the cumulative path sum $t$ is added directly to global answer:
      $$
      ans \leftarrow ans + t
      $$
- **Step-by-Step Worked Execution Trace on $[113, 215, 221]$:**
  - **Step 1: Unpack Numbers into Coordinate Map $mp$:**
    - $113 \implies d = 1, p = 1, v = 3 \implies mp[11] = 3$ (Root)
    - $215 \implies d = 2, p = 1, v = 5 \implies mp[21] = 5$
    - $221 \implies d = 2, p = 2, v = 1 \implies mp[22] = 1$
    - Physical tree structure:
      ```text
              (11): 3
             /       \
         (21): 5    (22): 1
      ```
  - **Step 2: Start DFS from Root $(11)$ with Initial Sum $t = 0$:**
    - Current node: $11$.
    - Add node value:
      $$
      t \leftarrow 0 + mp[11] = 0 + 3 = \mathbf{3}
      $$
    - Compute child coordinates:
      - $d = 1, \; p = 1$.
      - Left child key:
        $$
        10(1 + 1) + (2(1) - 1) = 20 + 1 = \mathbf{21}
        $$
      - Right child key:
        $$
        21 + 1 = \mathbf{22}
        $$
    - Are both children missing? No, both $21$ and $22$ exist in $mp$!
    - Branch to left child $21$, then right child $22$.
  - **Step 3: DFS Traverse Left Child $(21)$:**
    - Current node: $21$.
    - Add node value:
      $$
      t \leftarrow 3 + mp[21] = 3 + 5 = \mathbf{8}
      $$
    - Compute child coordinates ($d = 2, p = 1$):
      - Left child key: $10(3) + (2(1) - 1) = 31$.
      - Right child key: $31 + 1 = 32$.
    - Check membership:
      $$
      31 \notin mp \quad \land \quad 32 \notin mp \implies \mathbf{Leaf\ Node\ Reached!}
      $$
    - Path 1: Root $\to$ Node 21 has sum $\mathbf{8}$.
    - Add to global answer:
      $$
      ans \leftarrow ans + 8 = \mathbf{8}
      $$
  - **Step 4: DFS Traverse Right Child $(22)$:**
    - Current node: $22$.
    - Add node value:
      $$
      t \leftarrow 3 + mp[22] = 3 + 1 = \mathbf{4}
      $$
    - Compute child coordinates ($d = 2, p = 2$):
      - Left child key: $10(3) + (2(2) - 1) = 33$.
      - Right child key: $33 + 1 = 34$.
    - Check membership:
      $$
      33 \notin mp \quad \land \quad 34 \notin mp \implies \mathbf{Leaf\ Node\ Reached!}
      $$
    - Path 2: Root $\to$ Node 22 has sum $\mathbf{4}$.
    - Add to global answer:
      $$
      ans \leftarrow 8 + 4 = \mathbf{12}
      $$
  - **Step 5: Output:**
    $$
    ans = \mathbf{12}
    $$
- **Sparse Tree with Missing Left Branch ($nums = [113, 221]$):**
  - Root $11$ (val 3). Left child $21$ is missing. Right child $22$ (val 1) is present.
  - Root 11 has a right child, so 11 is **not** a leaf.
  - Path traverses only to 22:
    $$
    t = 3 + 1 = \mathbf{4}
    $$
  - Output is **`4`**.
- **Single Node Tree ($nums = [115]$):**
  - Root has no children $\implies$ leaf.
  - Output: **`5`**.

This instance demonstrates decimal-encoded binary tree coordinate parsing and path sum accumulation, mathematically proves why positional arithmetic $2p - 1$ and $2p$ preserves full-binary index topology under arbitrary sparsity, and derives $O(N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of 3-digit integers `[d p v]` where:
- $d$ is depth ($1 \dots 4$).
- $p$ is position at depth $d$ ($1 \dots 8$).
- $v$ is node value.
Find the **sum of all root-to-leaf paths**.

```text
nums = [ 113, 215, 221 ]

Tree:
         (depth 1, pos 1): val = 3
        /                         \
  (depth 2, pos 1): val = 5    (depth 2, pos 2): val = 1

Paths:
  Path 1: 3 -> 5 = 8
  Path 2: 3 -> 1 = 4

Total Sum = 8 + 4 = 12
```

### The Invariant of Positional Child Numbering
- For node at depth $d$ and position $p$:
  - Left child is at $(d + 1, \; 2p - 1)$.
  - Right child is at $(d + 1, \; 2p)$.
- A node is a leaf if and only if **neither** child exists in the coordinate table.

---

## 2. Conceptual Foundation & Invariants

### 1. The Key Hash Function:
For each element `num`:
$$
key = \lfloor num / 10 \rfloor = 10d + p, \quad value = num \pmod{10} = v
$$

### 2. Child Lookup Keys:
Given parent key $node = 10d + p$:
$$
k_{left} = 10(d + 1) + 2p - 1
$$
$$
k_{right} = k_{left} + 1
$$

### 3. Leaf Aggregation:
$$
k_{left} \notin mp \quad \land \quad k_{right} \notin mp \implies ans \leftarrow ans + t
$$

> **Positional Dyadic Embedding Invariant.** The encoding $(d, p)$ embeds the tree into a binary trie over prefix words $\{0, 1\}^{d-1}$, where left and right step transitions correspond strictly to bit-shifts $p \to 2p - 1$ and $p \to 2p$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [113, 215, 221]$:

---

### Step 1: Map Construction
- $mp = \{11: 3, \; 21: 5, \; 22: 1\}$.

---

### Step 2: Root (11)
- $t = 3$.
- Children keys: $21$ and $22$.
- Both exist $\implies$ not a leaf.

---

### Step 3: Node 21
- $t = 3 + 5 = 8$.
- Children keys: $31$ and $32$ (neither in $mp$).
- Leaf! $ans \leftarrow 0 + 8 = 8$.

---

### Step 4: Node 22
- $t = 3 + 1 = 4$.
- Children keys: $33$ and $34$ (neither in $mp$).
- Leaf! $ans \leftarrow 8 + 4 = 12$.

---

### Step 5: Output
$$
\mathbf{12}
$$

---

## 4. Complete Execution Trace

| Traversed Key $(d, p)$ | Node Value $v$ | Path Sum $t$ | Left Child Key | Right Child Key | Is Leaf? | Contribution to $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $11$ ($1, 1$) | $3$ | $3$ | $21$ (Present) | $22$ (Present) | No | $0$ |
| **$21$ ($2, 1$)** | **$5$** | **$8$** | $31$ (Absent) | $32$ (Absent) | **Yes** | **$+8$** |
| **$22$ ($2, 2$)** | **$1$** | **$4$** | $33$ (Absent) | $34$ (Absent) | **Yes** | **$+4$** |
| **Total** | — | — | — | — | — | **`12`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node ($[119]$):** Root is itself a leaf $\implies 9$.
- **Only Right Child Present ($[113, 221]$):** Root is not a leaf; only path $3 \to 1$ sums to 4.
- **Maximum Depth 4 Tree:** Max 15 nodes; coordinates like $41 \dots 48$ computed flawlessly.
- **Deep Single Path ($[111, 212, 313, 414]$):** Sums $1 + 2 + 3 + 4 = 10$.

---

## 6. Traps & Common Anti-Patterns

- **Treating Nodes with Only One Child as Leaves:** If node 11 has only child 22, node 11 is NOT a leaf. A node is a leaf only if **both** children are absent (`l not in mp and r not in mp`).
- **Incorrect Left Child Formula:** Using $2p$ for left and $2p + 1$ for right causes 1-indexed offset bugs. For 1-indexing, left is $2p - 1$ and right is $2p$.
- **Rebuilding Full Tree Pointers ($O(N)$ Extra Classes):** Constructing pointer-based tree nodes is unnecessary overhead. Dictionary key lookups run in $O(1)$ directly.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Building map from $N$ numbers: $\mathcal{O}(N)$.
  - DFS visits each node at most once: $\mathcal{O}(N)$.
  - Since depth is $\le 4$, $N \le 15$.
  - Total Time: $\mathcal{O}(N)$, completing in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the coordinate dictionary and recursion stack ($depth \le 4$).
