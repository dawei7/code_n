# Guided Example: Pyramid Transition Matrix

We trace the step-by-step triangular block pyramid layer reduction ($N \to N-1 \to \dots \to 1$), transition dictionary mapping ($(u, v) \to \{w\}$), pairwise adjacent block constraint validation, Cartesian product next-layer branching ($\prod d[(s_i, s_{i+1})]$), depth-first search with state memoization ($@cache$), and apex termination ($|s| = 1$) on representative block configurations:

- **Input:**
  - Base layer: $bottom = \text{"BCD"}$
  - Allowed triples: $allowed = [\text{"BCC"}, \; \text{"CDE"}, \; \text{"CEA"}, \; \text{"FFF"}]$
- **Required output:** `true`
  - Pyramid assembly rules:
    - Each layer of the pyramid has one fewer block than the layer directly beneath it:
      $$
      \text{Layer } 1: N \text{ blocks} \implies \text{Layer } 2: N - 1 \text{ blocks} \implies \dots \implies \text{Apex}: 1 \text{ block}
      $$
    - A block of color $w$ can be placed directly on top of two adjacent blocks $u$ and $v$ (where $u$ is to the left of $v$) if and only if the pattern $uvw$ is listed in $allowed$.
    - Multiple colors may be valid for the same pair $(u, v)$.
    - Objective: Determine if there exists a valid sequence of layers that reaches the single-block apex ($|s| = 1$).
    - For $bottom = \text{"BCD"}$:
      - Layer 1: $\text{"BCD"}$ (3 blocks).
        - Adjacent pair 1: $\text{"BC"}$. In $allowed$, $\text{"BCC"} \implies$ top block must be `'C'`.
        - Adjacent pair 2: $\text{"CD"}$. In $allowed$, $\text{"CDE"} \implies$ top block must be `'E'`.
        - Resulting Layer 2: $\text{"CE"}$ (2 blocks).
      - Layer 2: $\text{"CE"}$ (2 blocks).
        - Adjacent pair: $\text{"CE"}$. In $allowed$, $\text{"CEA"} \implies$ top block must be `'A'`.
        - Resulting Layer 3: $\text{"A"}$ (1 block).
      - Layer 3 has length 1 (apex reached!).
      - Assembly is successful $\implies$ return **`true`**.
- **Context-Free Grammar Parsing & Memoized DFS Invariant:**
  - **The Adjacency Transition Dictionary ($d$):**
    - Group allowed rules by base pair:
      $$
      d[(u, v)] = \{ w \mid uvw \in allowed \}
      $$
  - **Layer Transition Operator:**
    - For a layer of blocks $s = s_0 s_1 \dots s_{m - 1}$ of length $m$:
      - For each adjacent pair $(s_i, s_{i + 1})$:
        - Query valid upper block candidates: $cs_i = d[(s_i, s_{i + 1})]$.
        - If any adjacent pair has no valid top block ($cs_i = \emptyset$), the current layer is a dead end $\implies$ fail immediately.
      - Next layer candidates correspond to the Cartesian product:
        $$
        \text{NextLayers}(s) = \prod_{i=0}^{m - 2} d[(s_i, s_{i + 1})]
        $$
  - **Memoized Recursive Descent:**
    - Define predicate $dfs(s)$: Can row $s$ build to the apex?
      - Base Case: If $|s| == 1$, apex reached $\implies$ return `true`.
      - Recursive Step:
        $$
        dfs(s) = \bigvee_{nxt \in \text{NextLayers}(s)} dfs(nxt)
        $$
    - Memoizing evaluated rows in a hash set prevents redundant re-exploration of identical intermediate rows produced by different branches.
- **Step-by-Step Worked Execution Trace on $bottom = \text{"BCD"}$:**
  - **Phase 0: Build Transition Mapping:**
    - Patterns:
      - $\text{"BCC"} \implies d[(\text{'B'}, \text{'C'})] = [\text{'C'}]$
      - $\text{"CDE"} \implies d[(\text{'C'}, \text{'D'})] = [\text{'E'}]$
      - $\text{"CEA"} \implies d[(\text{'C'}, \text{'E'})] = [\text{'A'}]$
      - $\text{"FFF"} \implies d[(\text{'F'}, \text{'F'})] = [\text{'F'}]$
  - **Level 1 (Base): $s = \text{"BCD"}$ (Length 3):**
    - Check length: $3 \ne 1$.
    - Pairwise inspection:
      - Pair $(s_0, s_1) = (\text{'B'}, \text{'C'})$:
        $$
        d[(\text{'B'}, \text{'C'})] = [\mathbf{\text{'C'}}]
        $$
      - Pair $(s_1, s_2) = (\text{'C'}, \text{'D'})$:
        $$
        d[(\text{'C'}, \text{'D'})] = [\mathbf{\text{'E'}}]
        $$
    - Cartesian product:
      $$
      [\text{'C'}] \times [\text{'E'}] = [\text{"CE"}]
      $$
    - Branch to next layer: `dfs("CE")`.
  - **Level 2: $s = \text{"CE"}$ (Length 2):**
    - Check length: $2 \ne 1$.
    - Pairwise inspection:
      - Pair $(s_0, s_1) = (\text{'C'}, \text{'E'})$:
        $$
        d[(\text{'C'}, \text{'E'})] = [\mathbf{\text{'A'}}]
        $$
    - Cartesian product:
      $$
      [\text{'A'}] = [\text{"A"}]
      $$
    - Branch to next layer: `dfs("A")`.
  - **Level 3 (Apex): $s = \text{"A"}$ (Length 1):**
    - Check length: $|s| = 1 \implies \mathbf{Apex\ Reached!}$
    - Return `true`.
  - **Unwind Search:**
    - `dfs("A")` returns `true` $\implies `dfs("CE")` returns `true` $\implies `dfs("BCD")` returns `true`.
    - Output:
      $$
      ans = \mathbf{true}
      $$
- **Branch Failure Trace ($bottom = \text{"AAAA"}, allowed = [\text{"AAB"}, \text{"AAC"}, \text{"BCD"}, \text{"BBE"}, \text{"DEF"}]$):**
  - Layer 1: `"AAAA"`.
    - Adjacent pairs: `AA`, `AA`, `AA`.
    - Each `AA` produces `['B', 'C']`.
    - Generates $2 \times 2 \times 2 = 8$ possible second layers: `"BBB"`, `"BBC"`, `"BCB"`, `"BCC"`, etc.
  - Testing branch `"BBB"`:
    - Pairs: `BB`, `BB`.
    - `BB` produces `['E']` $\implies$ Layer 3: `"EE"`.
    - Testing `"EE"`: No rule exists for `EE` in $allowed$ $\implies d[(\text{'E'}, \text{'E'})] = \emptyset \implies$ Dead end!
  - All 8 branches lead to invalid pairs at Layer 3 or Layer 4.
  - Returns **`false`**.

This instance demonstrates constrained 2D shape assembly and CYK-style inverted context-free parsing, mathematically proves why memoization over layer strings bounds branching factor combinatorial explosion, and derives $O(A^N)$ worst-case runtime and $O(N^2)$ recursion stack bounds.

---

## 1. Instance & Teaching Goal

Given a $bottom$ row of colored blocks and a list of $allowed$ rules $uvw$ ($u$ and $v$ support $w$):
Determine if you can build a pyramid all the way to a single-block apex ($N \to N-1 \to \dots \to 1$).

```text
bottom = "BCD"
allowed = [ "BCC", "CDE", "CEA", "FFF" ]

Layer 1: B C D
  B C -> C
  C D -> E
Layer 2:  C E
  C E -> A
Layer 3:   A  (Apex reached!)

Result: true
```

### The Invariant of the Layer-Wise Cartesian Product
- Each layer $s$ of length $m$ generates next layer candidates from the Cartesian product of allowed colors for its $m - 1$ adjacent pairs: $\prod d[(s_i, s_{i+1})]$.
- If any adjacent pair has no valid transitions, that branch terminates immediately.
- Memoizing evaluated rows prevents duplicate exploration of identical sub-pyramids.

---

## 2. Conceptual Foundation & Invariants

### 1. Grammar Rule Dictionary:
$$
d[(u, v)] = \{ w \mid uvw \in allowed \}
$$

### 2. State Transition:
$$
dfs(s): \quad \text{if } |s| == 1 \implies \text{return true}
$$
$$
dfs(s) = \bigvee_{nxt \in \prod_{i=0}^{|s|-2} d[(s_i, s_{i+1})]} dfs(nxt)
$$

> **Inverted CYK Hierarchy Invariant.** The pyramid construction problem is the dual derivation problem of a Chomsky Normal Form grammar $W \to U V$, whose parse tree existence over root length 1 is decidable by memoized depth-first search over the layer word lattice.

---

## 3. Step-by-Step Worked Execution

We trace $bottom = \text{"BCD"}$:

---

### Step 1: Base Row `"BCD"`
- Pair `BC` $\to$ `C`.
- Pair `CD` $\to$ `E`.
- Candidate row: `"CE"`.

---

### Step 2: Row `"CE"`
- Pair `CE` $\to$ `A`.
- Candidate row: `"A"`.

---

### Step 3: Apex `"A"`
- Length 1 $\implies$ Apex reached!
- Returns `true`.

---

### Step 4: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| Pyramid Layer Level | Layer String $s$ | Adjacent Pairs Evaluated | Allowed Top Colors for Pairs | Candidate Next Layer | Apex Reached? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ (Base) | `"BCD"` (len 3) | `(B, C)`, `(C, D)` | `[C]`, `[E]` | `"CE"` | No |
| $2$ | `"CE"` (len 2) | `(C, E)` | `[A]` | `"A"` | No |
| **$3$ (Top)** | **`"A"` (len 1)** | **None** | **—** | **—** | **Yes (Return `true`)** |

---

## 5. Boundary Cases & Failure Modes

- **Missing Transition:** If any adjacent pair has $d[(u, v)] = \emptyset$, that row cannot produce any layer above $\implies$ returns `false`.
- **Branch Explosion:** Multiple allowed colors for each pair multiply the number of candidate next rows; memoization `@cache` prunes duplicate layer evaluations.
- **Base Already Length 1:** $bottom$ of length 1 is already at the apex $\implies$ returns `true`.
- **All Branches Dead End:** If all combinations fail to reach apex $\implies$ returns `false`.

---

## 6. Traps & Common Anti-Patterns

- **Building Next Row Character by Character without Caching Entire Rows:** Generating every block sequentially without memoizing complete row strings causes massive redundant re-computation of subtrees.
- **Order of Left and Right Blocks:** Rule $uvw$ requires $u$ on the left and $v$ on the right. Transition $(v, u)$ is distinct from $(u, v)$.
- **Modifying Input Strings:** Always construct new strings for subsequent layers rather than mutating previous layer state.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Base length $N \le 6$.
  - Number of distinct possible row strings of length $k$ over an alphabet of size $|\Sigma| \le 7$ is bounded by $|\Sigma|^k \le 7^k$.
  - With memoization, each unique layer is expanded at most once: $\mathcal{O}(|\Sigma|^N)$ worst case. For $N \le 6$, completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ recursion depth stack, and $\mathcal{O}(|\Sigma|^N)$ cache memory for memoized layer states.
