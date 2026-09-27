# Guided Example: K-Similar Strings

We trace the step-by-step permutation cycle decomposition, shortest path breadth-first search in transposition Cayley graphs, canonical first-mismatch coordinate alignment ($s[i] \ne s_2[i]$), branch pruning on misaligned target characters ($s[j] == s_2[i] \land s[j] \ne s_2[j]$), and minimum swap distance derivation on representative string pairs:

- **Input:**
  $$
  s_1 = \text{"abc"}, \quad s_2 = \text{"bca"}
  $$
- **Required output:** `2`
  - $K$-similarity swap rules:
    - Two anagram strings $s_1$ and $s_2$ of length $n$ are $k$-similar if $s_1$ can be transformed into $s_2$ using at most $k$ swap operations.
    - Each operation swaps two characters at distinct indices $i$ and $j$.
    - Objective: Find the **minimum** number of swaps $k$ required to transform $s_1$ into $s_2$.
    - For $s_1 = \text{"abc"}$ and $s_2 = \text{"bca"}$:
      - Both strings are permutations of letters `'a'`, `'b'`, `'c'`.
      - Index 0 of $s_2$ requires character `'b'`. In $s_1$, `'b'` is at index 1.
      - Swap indices 0 and 1:
        $$
        \text{"abc"} \longrightarrow \text{"bac"} \quad (\text{Swap 1})
        $$
      - Now index 0 is correct (`'b' == 'b'`).
      - Index 1 of $s_2$ requires character `'c'`. In current string `"bac"`, `'c'` is at index 2.
      - Swap indices 1 and 2:
        $$
        \text{"bac"} \longrightarrow \text{"bca"} \quad (\text{Swap 2})
        $$
      - String matches $s_2$ exactly!
      - Minimum swaps: **`2`**.
- **Canonical Mismatch & Branch Pruning Invariant:**
  - **The First-Mismatch Alignment Theorem:**
    - To transform string $s$ to match $s_2$, every mismatched position must eventually be swapped.
    - Find the **first index $i$ where $s[i] \ne s_2[i]$**.
    - The character $s_2[i]$ belongs at index $i$.
    - In any optimal sequence of swaps, some swap must place $s_2[i]$ into position $i$.
    - By symmetry, we can **enforce this swap immediately without loss of generality**!
  - **Pruned Successor Branching:**
    - Scan for indices $j > i$ that can supply the needed character:
      1. $s[j] == s_2[i]$ (candidate character matches target).
      2. $s[j] \ne s_2[j]$ (position $j$ is currently misplaced; swapping away an already correctly placed character is strictly suboptimal).
    - For every qualifying index $j$:
      - Form successor state by swapping $s[i]$ and $s[j]$.
      - Successor now has position $i$ permanently matched:
        $$
        s' = s_2[:i+1] + s[i+1:j] + s[i] + s[j+1:]
        $$
    - Enqueue $s'$ in level-order BFS.
    - Fixing the lowest mismatched coordinate collapses the branching factor from $\mathcal{O}(N^2)$ to at most $\mathcal{O}(N)$ per step, enabling fast BFS convergence.
- **Step-by-Step Worked Execution Trace on $s_1 = \text{"abc"}, s_2 = \text{"bca"}$ ($n = 3$):**
  - Target: $s_2 = \text{"bca"}$.
  - Initialize queue: $q = [\text{"abc"}]$, visited set: $vis = \{\text{"abc"}\}$, distance: $ans = 0$.
  - **Level 0 ($ans = 0$):**
    - Pop $s = \text{"abc"}$.
    - Target check: $\text{"abc"} \ne \text{"bca"}$.
    - **Find First Mismatch Index $i$:**
      - At index 0: $s[0] = \text{'a'}, s_2[0] = \text{'b'} \implies \mathbf{First\ Mismatch\ at\ } i = 0$.
      - Required character at index 0 is $s_2[0] = \mathbf{\text{'b'}}$.
    - **Find Valid Donors $j > 0$ with $s[j] == \text{'b'}$:**
      - $j = 1$: $s[1] = \text{'b'} == s_2[0]$ and $s[1] \ne s_2[1]$ ('b' $\ne$ 'c') $\implies \mathbf{Valid\ Donor!}$
      - $j = 2$: $s[2] = \text{'c'} \ne \text{'b'}$.
    - **Generate Successor State:**
      - Swap indices 0 and 1:
        $$
        nxt = \text{swap}(\text{"abc"}, 0, 1) = \mathbf{\text{"bac"}}
        $$
      - Add to queue: $q.\text{append}(\text{"bac"})$, $vis.\text{add}(\text{"bac"})$.
    - Level 0 finished. Increment distance: $ans \leftarrow 0 + 1 = \mathbf{1}$.
  - **Level 1 ($ans = 1$):**
    - Pop $s = \text{"bac"}$.
    - Target check: $\text{"bac"} \ne \text{"bca"}$.
    - **Find First Mismatch Index $i$:**
      - Index 0: $s[0] = \text{'b'} == s_2[0]$ (matched!).
      - Index 1: $s[1] = \text{'a'}, s_2[1] = \text{'c'} \implies \mathbf{First\ Mismatch\ at\ } i = 1$.
      - Required character at index 1 is $s_2[1] = \mathbf{\text{'c'}}$.
    - **Find Valid Donors $j > 1$ with $s[j] == \text{'c'}$:**
      - $j = 2$: $s[2] = \text{'c'} == s_2[1]$ and $s[2] \ne s_2[2]$ ('c' $\ne$ 'a') $\implies \mathbf{Valid\ Donor!}$
    - **Generate Successor State:**
      - Swap indices 1 and 2:
        $$
        nxt = \text{swap}(\text{"bac"}, 1, 2) = \mathbf{\text{"bca"}}
        $$
      - Add to queue: $q.\text{append}(\text{"bca"})$, $vis.\text{add}(\text{"bca"})$.
    - Level 1 finished. Increment distance: $ans \leftarrow 1 + 1 = \mathbf{2}$.
  - **Level 2 ($ans = 2$):**
    - Pop $s = \text{"bca"}$.
    - Target check:
      $$
      s == s_2 \iff \text{"bca"} == \text{"bca"} \implies \mathbf{Target\ Reached!}
      $$
    - Return current distance:
      $$
      ans = \mathbf{2}
      $$
- **Single Swap Trace ($s_1 = \text{"ab"}, s_2 = \text{"ba"}$):**
  - Mismatch at 0; donor at 1.
  - Swap yields `"ba"` at level 1 $\implies ans = \mathbf{1}$.
- **Identical Strings Trace ($s_1 = \text{"abc"}, s_2 = \text{"abc"}$):**
  - Checked at level 0: $s_1 == s_2 \implies ans = \mathbf{0}$.

This instance demonstrates geodesic distance computation in permutation symmetric groups $S_n$ generated by transpositions, mathematically proves why canonical prefix fixing eliminates factorial state permutations without distorting the shortest path metric, and derives $O(V + E)$ pruned BFS runtime and $O(V)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given two anagram strings $s_1$ and $s_2$:
Find the **minimum number of swaps** to turn $s_1$ into $s_2$.

```text
s1 = "abc", s2 = "bca"

Mismatch at index 0: s1[0]='a', s2[0]='b'
Swap with 'b' at index 1:
  "abc" -> "bac"  (1 swap)

Mismatch at index 1: s1[1]='a', s2[1]='c'
Swap with 'c' at index 2:
  "bac" -> "bca"  (2 swaps)

Matches s2!
Result: 2
```

### The Invariant of Canonical Position Fixing
- Find the **first mismatch index $i$** where $s[i] \ne s_2[i]$.
- Swap $s[i]$ only with indices $j > i$ where $s[j] == s_2[i]$ and $s[j] \ne s_2[j]$.
- Fixing one misplaced character at a time eliminates redundant permutations and guarantees minimal search depth in BFS.

---

## 2. Conceptual Foundation & Invariants

### 1. Cayley Graph Geodesic Metric:
$$
d(s_1, s_2) = \min \{ k \mid s_1 \cdot \tau_1 \cdots \tau_k = s_2, \; \tau_r \in \text{Transpositions} \}
$$

### 2. Canonical Successor Operator:
For first mismatch $i = \min \{ k \mid s[k] \ne s_2[k] \}$:
$$
\text{succ}(s) = \{ \text{swap}(s, i, j) \mid j > i \;\land\; s[j] = s_2[i] \;\land\; s[j] \ne s_2[j] \}
$$

> **Prefix Canonicalization Invariant.** The permutation action decomposes into a product of disjoint cycles. Restricting state transitions to align the minimal uncorrected index preserves the cycle partition deficit $\text{dist}(s, s_2) = n - c(s^{-1} s_2)$ while bounding the out-degree of each BFS node by $|\Sigma|$.

---

## 3. Step-by-Step Worked Execution

We trace $s_1 = \text{"abc"}, s_2 = \text{"bca"}$:

---

### Step 1: Initial State
- $s = \text{"abc"}$. $ans = 0$.

---

### Step 2: Level 0
- First mismatch at $i = 0$. Needs `'b'`.
- Found at $j = 1$. Swap $(0, 1) \implies \text{"bac"}$.
- Enqueue `"bac"`.

---

### Step 3: Level 1
- Pop `"bac"`. First mismatch at $i = 1$. Needs `'c'`.
- Found at $j = 2$. Swap $(1, 2) \implies \text{"bca"}$.
- Enqueue `"bca"`.

---

### Step 4: Level 2
- Pop `"bca" == s_2`. Match!
- Return $\mathbf{2}$.

---

## 4. Complete Execution Trace

| BFS Level ($ans$) | Current State $s$ | Mismatch Position $i$ | Needed Character $s_2[i]$ | Donor Index $j$ | Generated State | Target Reached? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `"abc"` | $0$ | `'b'` | $1$ | `"bac"` | No |
| $1$ | `"bac"` | $1$ | `'c'` | $2$ | `"bca"` | No |
| **$2$** | **`"bca"`** | — | — | — | — | **`Yes (Return 2)`** |

---

## 5. Boundary Cases & Failure Modes

- **Already Equal ($s_1 == s_2$):** Exits at level 0 $\implies 0$.
- **Pure Two-Cycle Transposition ($s_1 = "ab", s_2 = "ba"$):** Resolves in 1 swap.
- **Multiple Duplicate Letters ($"abac", "bcaa"$):** Branching considers all valid donor positions $j$.
- **Maximum Length ($N \le 20$):** Canonical mismatch pruning prevents exponential state explosion.

---

## 6. Traps & Common Anti-Patterns

- **Generating All $\binom{N}{2}$ Swaps Every Step:** Swapping every pair generates massive state duplication and times out. Only swap the first mismatched index $i$ with valid donors $j$.
- **Swapping Away Already Correct Characters:** Never pick a donor $j$ where $s[j] == s_2[j]$; that character is already in place.
- **DFS Without Pruning:** Standard DFS without cycle heuristics visits deep suboptimal paths. BFS guarantees the first time $s_2$ is visited is the minimal swap count.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N \le 20$ and alphabet size $|\Sigma| \le 6$.
  - Canonical prefix fixing limits the branch factor per state to at most $|\Sigma| \le 6$.
  - Total Time: bounded by number of reachable states $\mathcal{O}(|\Sigma|^K \cdot N)$. Completes in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\text{States} \cdot N)$ memory for the BFS queue and visited set.
