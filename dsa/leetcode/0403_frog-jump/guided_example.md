# Guided Example: Frog Jump

We trace the step-by-step memoized depth-first search state machine ($dfs(i, k)$ where $i$ is the stone index and $k$ is the previous jump distance), dynamic jump fan-out ($j \in \{k-1, k, k+1\}$ with $j > 0$), position hash lookup ($stones[i] + j \in pos$), dead-end pruning, and terminal riverbank reachability on representative stone configurations:

- **Input:** $stones = [0, 1, 3, 5, 6, 8, 12, 17]$
- **Required output:** `true`
  - Position index mapping: $\{0:0, 1:1, 3:2, 5:3, 6:4, 8:5, 12:6, 17:7\}$
  - Successful trajectory trace:
    1. Start at stone $0$ ($pos = 0$): must jump $1$ unit $\implies$ lands on stone $1$ ($pos = 1, k = 1$)
    2. At stone $1$ ($k = 1$): test jump $2 \implies 1 + 2 = 3$ (stone $3$, $k = 2$)
    3. At stone $3$ ($k = 2$): test jump $2 \implies 3 + 2 = 5$ (stone $5$, $k = 2$)
    4. At stone $5$ ($k = 2$): test jump $3 \implies 5 + 3 = 8$ (stone $8$, $k = 3$)
    5. At stone $8$ ($k = 3$): test jump $4 \implies 8 + 4 = 12$ (stone $12$, $k = 4$)
    6. At stone $12$ ($k = 4$): test jump $5 \implies 12 + 5 = 17$ (stone $17$, $k = 5$)
  - Lands on the final stone $17$ ($i = n - 1$) $\implies$ Return `true`
- **Unreachable Riverbank:** $stones = [0, 1, 2, 3, 4, 8, 9, 11] \implies$ gap to $8$ and $11$ cannot be bridged $\implies \text{false}$
- **Initial Jump Failure:** $stones = [0, 2] \implies$ first jump must be $1$, but stone at $1$ is missing $\implies \text{false}$

This instance demonstrates modeling stateful mobility with 2D dynamic programming, mathematically proves why tracking the previous jump length $k$ captures the Markovian state without path history, and achieves $O(N^2)$ time and $O(N^2)$ space bounds.

---

## 1. Instance & Teaching Goal

A frog is crossing a river with stones at positions $stones = [0, 1, 3, 5, 6, 8, 12, 17]$:
- Initially at stone $0$. The first jump must be **exactly 1 unit**.
- If the frog's previous jump was $k$ units, the next jump must be **$k - 1$, $k$, or $k + 1$ units** (strictly forward, jump distance $j > 0$).
Determine whether the frog can reach the last stone:

```text
Stone Positions: 0    1    3    5    6    8         12        17
Index:           0    1    2    3    4    5          6         7

Optimal Jump Sequence:
  0 --(+1)--> 1 --(+2)--> 3 --(+2)--> 5 --(+3)--> 8 --(+4)--> 12 --(+5)--> 17
   k=1         k=2         k=2         k=3         k=4          k=5
```

### Why Position Alone Is Insufficient as a State
Landing on stone $5$ with previous jump $k = 1$ allows jumps $\{1, 2\}$ (reaching at most $5 + 2 = 7$).
Landing on stone $5$ with previous jump $k = 2$ allows jumps $\{1, 2, 3\}$ (reaching $5 + 3 = 8$).
The set of feasible future destinations depends entirely on the **magnitude of the previous jump $k$**.
Therefore, the state is the pair $(i, k)$.

---

## 2. Conceptual Foundation & Invariants

### 1. The State Space $(i, k)$:
- $i \in [0, n - 1]$: Current stone index.
- $k \in [0, n]$: Length of the jump that brought the frog to stone $i$.
- State function: $dfs(i, k) \to \text{bool}$ indicating whether the final stone $n - 1$ is reachable from state $(i, k)$.

### 2. Transition Recurrence:
From state $(i, k)$:
1. **Base Case:**
   If $i == n - 1$, return **`True`**.
2. **Explore Valid Next Jumps:**
   For $j \in [k - 1, k + 1]$:
   - Must be forward: $j > 0$.
   - Next stone position: $target = stones[i] + j$.
   - If $target \in pos$ (where $pos$ maps stone position $\to$ stone index):
     If $dfs(pos[target], \; j)$ is True, return **`True`**.
3. **Dead End:**
   If none of the transitions reach the final stone, return **`False`**.

> **Invariant.** The maximum possible jump after $i$ hops is at most $i + 1$. Thus, $k \le n$ always holds, bounding the number of reachable states to at most $O(N^2)$.

---

## 3. Step-by-Step Worked Execution

We trace $stones = [0, 1, 3, 5, 6, 8, 12, 17]$ ($n = 8$):
$pos = \{0:0, 1:1, 3:2, 5:3, 6:4, 8:5, 12:6, 17:7\}$.

---

### Step 1: Start at Stone 0: `dfs(0, 0)`
- $i = 0, k = 0$.
- Feasible jumps: $j \in \{-1, 0, 1\}$. Filtering for $j > 0 \implies j = 1$.
- Target: $stones[0] + 1 = 0 + 1 = 1 \in pos$ (Index 1).
- Recurse: `dfs(1, 1)`.

---

### Step 2: At Stone 1: `dfs(1, 1)`
- $i = 1, k = 1$.
- Feasible jumps: $j \in \{0, 1, 2\} \implies j \in \{1, 2\}$.
  - $j = 1 \implies 1 + 1 = 2 \notin pos$.
  - $j = 2 \implies 1 + 2 = 3 \in pos$ (Index 2).
- Recurse: `dfs(2, 2)`.

---

### Step 3: At Stone 3: `dfs(2, 2)`
- $i = 2, k = 2$.
- Feasible jumps: $j \in \{1, 2, 3\}$.
  - $j = 1 \implies 3 + 1 = 4 \notin pos$.
  - $j = 2 \implies 3 + 2 = 5 \in pos$ (Index 3).
- Recurse: `dfs(3, 2)`.

---

### Step 4: At Stone 5: `dfs(3, 2)`
- $i = 3, k = 2$.
- Feasible jumps: $j \in \{1, 2, 3\}$.
  - Branch $j = 1$: $5 + 1 = 6 \in pos$ (Index 4).
    - `dfs(4, 1)` at stone 6: tries jumps $\{1, 2\} \implies 6 + 1 = 7 \notin pos, 6 + 2 = 8 \in pos$ (Index 5).
    - At stone 8 ($k = 2$): tries jumps $\{1, 2, 3\} \implies 8 + 1 = 9, 8 + 2 = 10, 8 + 3 = 11$ (None in $pos$). Backtracks!
  - Branch $j = 2$: $5 + 2 = 7 \notin pos$.
  - Branch $j = 3$: $5 + 3 = 8 \in pos$ (Index 5).
- Recurse: `dfs(5, 3)`.

---

### Step 5: At Stone 8: `dfs(5, 3)`
- $i = 5, k = 3$.
- Feasible jumps: $j \in \{2, 3, 4\}$.
  - $j = 2 \implies 8 + 2 = 10 \notin pos$.
  - $j = 3 \implies 8 + 3 = 11 \notin pos$.
  - $j = 4 \implies 8 + 4 = 12 \in pos$ (Index 6).
- Recurse: `dfs(6, 4)`.

---

### Step 6: At Stone 12: `dfs(6, 4)`
- $i = 6, k = 4$.
- Feasible jumps: $j \in \{3, 4, 5\}$.
  - $j = 3 \implies 12 + 3 = 15 \notin pos$.
  - $j = 4 \implies 12 + 4 = 16 \notin pos$.
  - $j = 5 \implies 12 + 5 = 17 \in pos$ (Index 7).
- Recurse: `dfs(7, 5)`.

---

### Step 7: At Final Stone 17: `dfs(7, 5)`
- Index $i = 7 == n - 1$.
- Terminal goal reached!
- Returns:
  $$
  \mathbf{\text{True}}
  $$

---

## 4. Complete Execution Trace

```text
dfs(0, 0)
  j = 1 -> target = 1 -> dfs(1, 1)
    j = 2 -> target = 3 -> dfs(2, 2)
      j = 2 -> target = 5 -> dfs(3, 2)
        j = 1 -> target = 6 -> dfs(4, 1) -> ... dead end (backtracks)
        j = 3 -> target = 8 -> dfs(5, 3)
          j = 4 -> target = 12 -> dfs(6, 4)
            j = 5 -> target = 17 -> dfs(7, 5) -> REACHED! (True)

Output: true
```

| Step | Stone Position $stones[i]$ | Stone Index $i$ | Previous Jump $k$ | Tested Next Jump $j$ | Target Position $stones[i] + j$ | Target in $pos$? | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 0 | 0 | 1 | 1 | Yes (Idx 1) | Call `dfs(1, 1)` |
| 2 | 1 | 1 | 1 | 2 | 3 | Yes (Idx 2) | Call `dfs(2, 2)` |
| 3 | 3 | 2 | 2 | 2 | 5 | Yes (Idx 3) | Call `dfs(3, 2)` |
| 4 | 5 | 3 | 2 | 1 | 6 | Yes (Idx 4) | Dead end $\to$ backtrack |
| 5 | 5 | 3 | 2 | 3 | 8 | Yes (Idx 5) | Call `dfs(5, 3)` |
| 6 | 8 | 5 | 3 | 4 | 12 | Yes (Idx 6) | Call `dfs(6, 4)` |
| 7 | 12 | 6 | 4 | 5 | 17 | Yes (Idx 7) | Call `dfs(7, 5)` |
| **8** | **17** | **7** | **5** | - | - | - | **$i == n - 1 \implies \text{True}$** |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly enforces the problem's physics: $j \in [k - 1, k + 1]$ and $j > 0$. The hash map $pos$ guarantees that the frog only lands on actual stones in the river. Because all transitions obey the allowed speed variations, any path reaching $n - 1$ represents a physically legal crossing.

**Completeness.** Memoization caches results for each unique state $(i, k)$. Since there are at most $N$ stones and at most $N$ possible jump lengths, all reachable states in the discrete DAG are explored at most once, guaranteeing that if any valid sequence of jumps exists, the search will discover it.

---

## 6. Traps This Instance Exposes

- **State Space Collapse Without $k$:** Remembering only the stone index $i$ without the jump speed $k$ fails because reaching stone $i$ with a larger $k$ unlocks longer future jumps.
- **First Jump Constraint:** The first jump must be exactly 1 unit ($stones[1] == 1$). If $stones[1] > 1$, the frog can never leave stone 0, and the function returns `False`.
- **Backward Jumps ($j \le 0$):** If $k = 1$, $k - 1 = 0$. A jump of 0 units means staying in place, which would cause an infinite loop. The condition `j > 0` prevents stationary or negative jumps.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N = \text{len}(stones)$.
  - The number of stones is $N$.
  - At stone $i$, the maximum jump length cannot exceed $i + 1 \le N$.
  - Total distinct states $(i, k)$ is at most $N \times N = O(N^2)$.
  - Each state evaluates at most 3 transitions ($k - 1, k, k + 1$), taking $O(1)$ time with hash lookup.
  - Overall time is bounded by $O(N^2)$, running in under 50 ms for $N = 2000$.
- **Auxiliary Space Complexity:** $O(N^2)$ auxiliary space for the memoization cache and position map $pos$.
