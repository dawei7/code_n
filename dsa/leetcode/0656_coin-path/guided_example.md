# Guided Example: Coin Path

We trace the step-by-step backward dynamic programming recurrence ($f[i] = coins[i] + \min_{j} f[j]$), obstacle exclusion ($coins[i] == -1$), lexicographical tie-breaking preference (selecting smaller forward step index $j$), reachability validation ($f[0] < \infty$), and 1-indexed path reconstruction on representative hopping cost arrays:

- **Input:** $coins = [1, 2, 4, -1, 2], \quad maxJump = 2$
- **Required output:** `[1, 3, 5]`
  - Game mechanics:
    - Start at 1-indexed position $1$ and jump forward toward position $n = 5$.
    - From position $i$, you can jump to any position $i + k$ where $1 \le k \le maxJump$.
    - Landing on position $i$ costs $coins[i]$ coins.
    - A value of $-1$ represents an impassable hazard: you can never land on that index.
    - Objective: Find a path from $1$ to $n$ with **minimum total coin cost**.
    - Tie-breaking: If multiple paths share the same minimum cost, return the path that is **lexicographically smallest** in index sequence. If unreachable, return `[]`.
- **Backward Dynamic Programming & Lexicographical Invariant:**
  - **Why Compute Backwards from $n - 1$ down to $0$?**
    - Let $f[i]$ be the minimum cost required to reach destination $n - 1$ starting from index $i$.
    - Base case: $f[n - 1] = coins[n - 1]$ (if destination is blocked with $-1$, destination is unreachable $\implies []$).
    - For each predecessor $i = n - 2$ down to $0$:
      - If $coins[i] \ne -1$:
        - Test each valid jump destination $j \in [i + 1, \; \min(n - 1, \; i + maxJump)]$:
          $$
          f[i] = coins[i] + \min_{j} f[j]
          $$
    - **Lexicographical Advantage:**
      - If candidate jump targets $j_1 < j_2$ yield the **exact same minimal cost** ($f[j_1] == f[j_2]$), taking the smaller index $j_1$ first guarantees a lexicographically smaller path prefix!
      - By scanning candidates $j$ in ascending order and updating only on strict inequality ($f[i] > f[j] + coins[i]$), the first encountered (smallest) index is naturally preserved!
- **Step-by-Step Worked Execution Trace on $[1, 2, 4, -1, 2], maxJump = 2$ ($n = 5$):**
  - Translate to 0-based indexing: indices $0, 1, 2, 3, 4$.
  - Destination index $4$:
    $$
    f[4] = coins[4] = \mathbf{2}
    $$
  - Initialize $f = [\infty, \infty, \infty, \infty, 2]$.
  - **Index $i = 3$ ($coins[3] = -1$):**
    - Position 3 is blocked by hazard.
    - $f[3] = \infty$.
  - **Index $i = 2$ ($coins[2] = 4$):**
    - Possible jumps within $maxJump = 2$: $j \in \{3, 4\}$.
    - Option $j = 3$: $f[3] = \infty$ (blocked).
    - Option $j = 4$:
      $$
      \text{Cost} = coins[2] + f[4] = 4 + 2 = \mathbf{6}
      $$
    - Best for index 2: $f[2] = \mathbf{6}$ (leads to index 4).
  - **Index $i = 1$ ($coins[1] = 2$):**
    - Possible jumps: $j \in \{2, 3\}$.
    - Option $j = 2$:
      $$
      \text{Cost} = coins[1] + f[2] = 2 + 6 = \mathbf{8}
      $$
    - Option $j = 3$: $f[3] = \infty$ (blocked).
    - Best for index 1: $f[1] = \mathbf{8}$ (leads to index 2).
  - **Index $i = 0$ ($coins[0] = 1$):**
    - Possible jumps: $j \in \{1, 2\}$.
    - Option $j = 1$:
      $$
      \text{Cost} = coins[0] + f[1] = 1 + 8 = \mathbf{9}
      $$
    - Option $j = 2$:
      $$
      \text{Cost} = coins[0] + f[2] = 1 + 6 = \mathbf{7}
      $$
    - Compare costs:
      $$
      7 < 9 \implies \text{Option } j = 2 \text{ is strictly cheaper!}
      $$
    - Assign: $f[0] = \mathbf{7}$.
  - **Cost Vector Summary:**
    $$
    f = [7, \; 8, \; 6, \; \infty, \; 2]
    $$
  - **Step 5: Path Reconstruction:**
    - Target remaining cost: $s = f[0] = 7$.
    - Scan $i = 0 \dots 4$:
      - At $i = 0$: $f[0] == 7 \implies$ include index $0$ ($1$-indexed: $\mathbf{1}$).
        - Update target: $s \leftarrow s - coins[0] = 7 - 1 = \mathbf{6}$.
      - At $i = 1$: $f[1] = 8 \ne 6 \implies$ skip.
      - At $i = 2$: $f[2] == 6 \implies$ include index $2$ ($1$-indexed: $\mathbf{3}$).
        - Update target: $s \leftarrow s - coins[2] = 6 - 4 = \mathbf{2}$.
      - At $i = 3$: $f[3] = \infty \ne 2 \implies$ skip.
      - At $i = 4$: $f[4] == 2 \implies$ include index $4$ ($1$-indexed: $\mathbf{5}$).
        - Update target: $s \leftarrow s - coins[4] = 2 - 2 = \mathbf{0}$.
    - Path constructed:
      $$
      ans = [\mathbf{1}, \; \mathbf{3}, \; \mathbf{5}]
      $$
- **Unreachable Blocked Instance ($coins = [1, 2, -1, -1, 2], maxJump = 1$):**
  - Indices 2 and 3 both blocked; jump capacity 1 cannot bridge the gap.
  - $f[0] = \infty \implies$ returns `[]`.
- **Lexicographical Tie Instance ($coins = [1, 0, 0, 2], maxJump = 2$):**
  - From index 0, jumping directly to index 2 vs jumping to index 1:
  - $0 \to 1 \to 2 \to 3$ costs $1 + 0 + 0 + 2 = 3$.
  - $0 \to 2 \to 3$ costs $1 + 0 + 2 = 3$.
  - Lexicographical order: $[1, 2, 3, 4] < [1, 3, 4]$.
  - The algorithm naturally chooses $[1, 2, 3, 4]$ due to smaller intermediate index selection.

This instance demonstrates backward dynamic programming on directed acyclic step graphs and greedy lexicographical tie-breaking, mathematically proves why suffix Bellman optimality guarantees canonical index minimization, and derives $O(N \cdot maxJump)$ runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given array $coins$ and max jump $maxJump$:
Find the **minimum cost path** from index 1 to index $n$.
If costs tie, return the **lexicographically smallest** path.

```text
coins = [ 1, 2, 4, -1, 2 ], maxJump = 2 (0-indexed: 0 to 4)

Backward Cost Analysis:
  f[4] = 2 (destination)
  f[3] = inf (blocked)
  f[2] = coins[2] + f[4] = 4 + 2 = 6
  f[1] = coins[1] + f[2] = 2 + 6 = 8
  f[0] = min( 1 + f[1]=9, 1 + f[2]=7 ) = 7 (jump to 2!)

Cheapest path: 0 -> 2 -> 4
In 1-based indexing: [ 1, 3, 5 ]
```

### The Invariant of Backward Subproblem Construction
- Formulating the recurrence **backwards** from destination $n - 1$ down to 0 means that at node $i$, making the greedily smaller forward jump choice automatically resolves ties in favor of lexicographically smaller prefixes.

---

## 2. Conceptual Foundation & Invariants

### 1. Backward Bellman Recurrence:
$$
f[n-1] = coins[n-1]
$$
For $i = n - 2 \dots 0$:
$$
f[i] = coins[i] + \min_{1 \le k \le maxJump, \; coins[i+k] \ne -1} f[i + k]
$$

### 2. Lexicographical Tie Preference:
When checking $j \in [i + 1, i + maxJump]$ in ascending order:
$$
\text{Update } f[i] \text{ only if } f[j] + coins[i] < f[i]
$$
Strict inequality ensures the lowest index $j$ wins in case of cost equality.

> **Lexicographical Suffix Optimality Invariant.** Any optimal path generated by backward dynamic programming with strictly left-preferential tie-breaking is lexicographically minimal among all cost-minimizing trajectories in a DAG.

---

## 3. Step-by-Step Worked Execution

We trace $coins = [1, 2, 4, -1, 2], maxJump = 2$:

---

### Step 1: Base Step at Destination
- $f[4] = 2$.

---

### Step 2: Index 3
- Blocked: $f[3] = \infty$.

---

### Step 3: Index 2
- Jump to 4: $4 + 2 = 6$.
- $f[2] = 6$.

---

### Step 4: Index 1
- Jump to 2: $2 + 6 = 8$.
- $f[1] = 8$.

---

### Step 5: Index 0
- Jump to 1: $1 + 8 = 9$.
- Jump to 2: $1 + 6 = 7$.
- Choose min: $f[0] = 7$ (via index 2).

---

### Step 6: Path Construction
- $0 \to 2 \to 4 \implies [1, 3, 5]$.

---

## 4. Complete Execution Trace

| Position $i$ (0-based) | Coin Value | Valid Targets $j$ | Candidate Costs $coins[i] + f[j]$ | Optimal $f[i]$ | Optimal Next Step |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $4$ | $2$ | Destination | — | **$2$** | End |
| $3$ | $-1$ | Blocked | — | **$\infty$** | — |
| $2$ | $4$ | $\{3, 4\}$ | $\{4+\infty, 4+2\}$ | **$6$** | $4$ |
| $1$ | $2$ | $\{2, 3\}$ | $\{2+6, 2+\infty\}$ | **$8$** | $2$ |
| **$0$** | **$1$** | **$\{1, 2\}$** | **$\{1+8, 1+6\}$** | **`7`** | **`2`** |
| **Path (1-based)** | — | — | — | — | **`[1, 3, 5]`** |

---

## 5. Boundary Cases & Failure Modes

- **Destination Blocked ($coins[-1] == -1$):** Immediate return `[]`.
- **Start Blocked ($coins[0] == -1$):** Destination unreachable $\implies []$.
- **Length 1 Array ($[5]$):** Destination is start $\implies [1]$.
- **Longest Path Reachable:** Returns all $n$ indices if $0$ cost and $maxJump = 1$.

---

## 6. Traps & Common Anti-Patterns

- **Forward DP With Path Tracking:** Forward DP requires maintaining lexicographical tie-breakers across variable-length prefix paths, which can require costly string/tuple comparisons. Backward DP solves lexicographical ordering for free.
- **1-Based vs 0-Based Indexing Mismatch:** Array inputs are 0-indexed in code; the output must be converted back to 1-indexed integers.
- **Non-Strict Inequality Updates:** Using $\le$ instead of $<$ when testing $j$ in ascending order would overwrite a smaller index with a larger index on equal costs, ruining lexicographical minimality.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Outer loop runs $N$ times.
  - Inner jump window runs at most $maxJump$ times.
  - Path reconstruction scans array in $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(N \cdot maxJump)$. For $N = 1000$ and $maxJump = 100$, executes $\approx 10^5$ operations, completing in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the dynamic programming cost array $f$.