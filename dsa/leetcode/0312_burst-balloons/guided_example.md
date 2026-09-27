# Guided Example: Burst Balloons

We trace the step-by-step reverse interval dynamic programming recurrence, padding with boundary ones, "last balloon burst" subproblem decoupling, and optimal coin collection on representative balloon arrays:

- **Input:** $\text{nums} = [3, 1, 5, 8]$
- **Required output:** $167$
  - Burst balloon $1$ (value 1): collects $3 \times 1 \times 5 = 15$ coins, remaining $[3, 5, 8]$
  - Burst balloon $2$ (value 5): collects $3 \times 5 \times 8 = 120$ coins, remaining $[3, 8]$
  - Burst balloon $0$ (value 3): collects $1 \times 3 \times 8 = 24$ coins, remaining $[8]$
  - Burst balloon $3$ (value 8): collects $1 \times 8 \times 1 = 8$ coins, remaining $[]$
  - Total maximum coins: $15 + 120 + 24 + 8 = \mathbf{167}$
- **Single Balloon Base Case:** $\text{nums} = [5] \implies 1 \times 5 \times 1 = 5$
- **Two Balloons Sequence:** $\text{nums} = [1, 5] \implies 1 \times 1 \times 5 + 1 \times 5 \times 1 = 5 + 5 = 10$
- **Zero Value Balloons:** Elements can be positive integers; boundary padding $1$ prevents zero collapse

This instance demonstrates reverse thinking in dynamic programming, mathematically proves why selecting the *last* balloon burst in an open interval $(i, j)$ decouples subproblems $(i, k)$ and $(k, j)$ with known static boundary neighbors ($arr[i]$ and $arr[j]$), contrasts $O(N^3)$ interval DP against $O(N!)$ brute-force permutations, and achieves $O(N^2)$ table space.

---

## 1. Instance & Teaching Goal

Given balloon values:
$$
\text{nums} = [3, 1, 5, 8] \quad (N = 4)
$$
Bursting a balloon at index $i$ yields $\text{nums}[i-1] \times \text{nums}[i] \times \text{nums}[i+1]$ coins (with virtual boundary balloons of value $1$ on the edges).
Find the bursting order that maximizes total coins.

```text
Forward Thinking Trap:
If you choose which balloon to burst FIRST:
Bursting balloon 1 (value 1) joins balloon 0 (value 3) and balloon 2 (value 5) as adjacent!
The remaining subproblems are dynamically coupled because future neighbors depend on past deletions.
Brute-force permutation search takes O(N!) = 4! = 24 paths (and explodes for N = 300).

Reverse Thinking Solution:
Ask: Which balloon k in (i, j) is burst LAST?
If balloon k is the VERY LAST to be burst in open interval (i, j):
All other balloons between i and j are ALREADY burst!
Therefore, the adjacent neighbors of balloon k at that final moment are GUARANTEED to be i and j!
Coins from bursting k last: arr[i] * arr[k] * arr[j].
The left subproblem (i, k) and right subproblem (k, j) become completely independent!
```

---

## 2. Conceptual Foundation & Invariants

### Array Boundary Padding
Augment the array with virtual boundary balloons:
$$
arr = [1] + \text{nums} + [1] = [1, \; 3, \; 1, \; 5, \; 8, \; 1] \quad (\text{Length } N + 2 = 6)
$$
Indices run from $0$ to $N + 1$.
- Any subarray of original balloons corresponds to an open interval $(i, j)$ where boundary balloons $i$ and $j$ remain unburst.

### The Interval DP Recurrence
Let $f[i][j]$ denote the maximum coins obtainable from bursting all balloons in the **strictly open interval** $(i, j)$:
- Base case: If $j \le i + 1$, the open interval $(i, j)$ is empty:
  $$
  f[i][j] = 0
  $$
- Recurrence: For every candidate balloon $k \in [i + 1, j - 1]$ chosen to burst **last**:
  $$
  f[i][j] = \max_{i < k < j} \Big( f[i][k] + f[k][j] + arr[i] \times arr[k] \times arr[j] \Big)
  $$
- Target: $f[0][N + 1]$ (bursting all balloons between virtual bounds $0$ and $N + 1$).

> **Invariant.** In open interval $(i, j)$, selecting balloon $k$ to burst last leaves $arr[i]$ and $arr[j]$ as its guaranteed immediate left and right neighbors, decoupling the interval into subproblems $f[i][k]$ and $f[k][j]$.

---

## 3. Step-by-Step Worked Execution

We trace the DP on $arr = [1, 3, 1, 5, 8, 1]$ ($N = 4$):
Interval length $L = j - i$ increases from $2$ to $5$.

---

### Step 1: Interval Length $L = 2$ (Single Balloon in $(i, i+2)$)
- $(0, 2)$: Only $k = 1$ ($arr[1] = 3$).
  $$
  f[0][2] = 0 + 0 + arr[0] \times arr[1] \times arr[2] = 1 \times 3 \times 1 = \mathbf{3}
  $$
- $(1, 3)$: Only $k = 2$ ($arr[2] = 1$).
  $$
  f[1][3] = 0 + 0 + arr[1] \times arr[2] \times arr[3] = 3 \times 1 \times 5 = \mathbf{15}
  $$
- $(2, 4)$: Only $k = 3$ ($arr[3] = 5$).
  $$
  f[2][4] = 0 + 0 + arr[2] \times arr[3] \times arr[4] = 1 \times 5 \times 8 = \mathbf{40}
  $$
- $(3, 5)$: Only $k = 4$ ($arr[4] = 8$).
  $$
  f[3][5] = 0 + 0 + arr[3] \times arr[4] \times arr[5] = 5 \times 8 \times 1 = \mathbf{40}
  $$

---

### Step 2: Interval Length $L = 3$ (Two Balloons in $(i, i+3)$)
- **Interval $(0, 3)$ (Balloons $\{1, 2\}$):**
  - $k = 1$: $f[0][1] + f[1][3] + 1 \times 3 \times 5 = 0 + 15 + 15 = 30$.
  - $k = 2$: $f[0][2] + f[2][3] + 1 \times 1 \times 5 = 3 + 0 + 5 = 8$.
  - $f[0][3] = \max(30, 8) = \mathbf{30}$.
- **Interval $(1, 4)$ (Balloons $\{2, 3\}$):**
  - $k = 2$: $f[1][2] + f[2][4] + 3 \times 1 \times 8 = 0 + 40 + 24 = 64$.
  - $k = 3$: $f[1][3] + f[3][4] + 3 \times 5 \times 8 = 15 + 0 + 120 = 135$.
  - $f[1][4] = \max(64, 135) = \mathbf{135}$.
- **Interval $(2, 5)$ (Balloons $\{3, 4\}$):**
  - $k = 3$: $f[2][3] + f[3][5] + 1 \times 5 \times 1 = 0 + 40 + 5 = 45$.
  - $k = 4$: $f[2][4] + f[4][5] + 1 \times 8 \times 1 = 40 + 0 + 8 = 48$.
  - $f[2][5] = \max(45, 48) = \mathbf{48}$.

---

### Step 3: Interval Length $L = 4$ (Three Balloons in $(i, i+4)$)
- **Interval $(0, 4)$ (Balloons $\{1, 2, 3\}$):**
  - $k = 1$: $f[0][1] + f[1][4] + 1 \times 3 \times 8 = 0 + 135 + 24 = 159$.
  - $k = 2$: $f[0][2] + f[2][4] + 1 \times 1 \times 8 = 3 + 40 + 8 = 51$.
  - $k = 3$: $f[0][3] + f[3][4] + 1 \times 5 \times 8 = 30 + 0 + 40 = 70$.
  - $f[0][4] = \max(159, 51, 70) = \mathbf{159}$.
- **Interval $(1, 5)$ (Balloons $\{2, 3, 4\}$):**
  - $k = 2$: $f[1][2] + f[2][5] + 3 \times 1 \times 1 = 0 + 48 + 3 = 51$.
  - $k = 3$: $f[1][3] + f[3][5] + 3 \times 5 \times 1 = 15 + 40 + 15 = 70$.
  - $k = 4$: $f[1][4] + f[4][5] + 3 \times 8 \times 1 = 135 + 0 + 24 = 159$.
  - $f[1][5] = \max(51, 70, 159) = \mathbf{159}$.

---

### Step 4: Interval Length $L = 5$ (All 4 Balloons in $(0, 5)$)
Evaluate all candidate last balloons $k \in \{1, 2, 3, 4\}$:
- **$k = 1$:** $f[0][1] + f[1][5] + arr[0] \times arr[1] \times arr[5] = 0 + 159 + (1 \times 3 \times 1) = 162$.
- **$k = 2$:** $f[0][2] + f[2][5] + arr[0] \times arr[2] \times arr[5] = 3 + 48 + (1 \times 1 \times 1) = 52$.
- **$k = 3$:** $f[0][3] + f[3][5] + arr[0] \times arr[3] \times arr[5] = 30 + 40 + (1 \times 5 \times 1) = 75$.
- **$k = 4$ (Optimal!):**
  $$
  f[0][4] + f[4][5] + arr[0] \times arr[4] \times arr[5] = 159 + 0 + (1 \times 8 \times 1) = 159 + 8 = \mathbf{167}
  $$

Global maximum coins:
$$
f[0][5] = \mathbf{167}
$$

---

## 4. Complete Execution Trace

```text
arr = [1, 3, 1, 5, 8, 1]

L = 2:
  f[0][2] = 3, f[1][3] = 15, f[2][4] = 40, f[3][5] = 40
L = 3:
  f[0][3] = max(k=1: 30,  k=2: 8)         = 30
  f[1][4] = max(k=2: 64,  k=3: 135)       = 135
  f[2][5] = max(k=3: 45,  k=4: 48)        = 48
L = 4:
  f[0][4] = max(k=1: 159, k=2: 51, k=3: 70) = 159
  f[1][5] = max(k=2: 51,  k=3: 70, k=4: 159)= 159
L = 5:
  f[0][5] = max(k=1: 162, k=2: 52, k=3: 75, k=4: 167) = 167

Result: 167
```

| Interval $(i, j)$ | Interval Length | Choice $k$ Evaluated | Left $f[i][k]$ | Right $f[k][j]$ | Burst Coins $arr[i] \cdot arr[k] \cdot arr[j]$ | Total for $k$ | Optimal $f[i][j]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 2)$ | 2 | $k = 1$ | 0 | 0 | $1 \times 3 \times 1 = 3$ | 3 | **3** |
| $(1, 3)$ | 2 | $k = 2$ | 0 | 0 | $3 \times 1 \times 5 = 15$ | 15 | **15** |
| $(2, 4)$ | 2 | $k = 3$ | 0 | 0 | $1 \times 5 \times 8 = 40$ | 40 | **40** |
| $(3, 5)$ | 2 | $k = 4$ | 0 | 0 | $5 \times 8 \times 1 = 40$ | 40 | **40** |
| $(0, 3)$ | 3 | $k = 1$ | 0 | 15 | $1 \times 3 \times 5 = 15$ | 30 | **30** |
| $(1, 4)$ | 3 | $k = 3$ | 15 | 0 | $3 \times 5 \times 8 = 120$ | 135 | **135** |
| $(0, 4)$ | 4 | $k = 1$ | 0 | 135 | $1 \times 3 \times 8 = 24$ | 159 | **159** |
| **$(0, 5)$** | **5** | **$k = 4$** | **159** | **0** | **$1 \times 8 \times 1 = 8$** | **167** | **$\mathbf{167}$** |

---

## 5. Algorithmic Correctness

**Soundness.** Every step evaluates bursting balloon $k$ as the last balloon in the open interval $(i, j)$. Because $k$ is burst last, all balloons between $i$ and $k$ and between $k$ and $j$ have already been removed, ensuring that $arr[i]$ and $arr[j]$ are indeed the adjacent neighbors of $arr[k]$. The subproblems $f[i][k]$ and $f[k][j]$ are strictly independent and leave $i$ and $k$ (resp. $k$ and $j$) unburst as their own external boundaries.

**Completeness.** Any optimal bursting sequence must have some balloon that is burst last among all balloons in $(0, N+1)$. The recurrence tests every possible candidate $k \in [1, N]$ for this role and maximizes over all possibilities. By induction on interval length $L$, the global optimal bursting schedule is guaranteed to be found.

---

## 6. Traps This Instance Exposes

- **Greedy Bursting Lowest Values First:** Greedily popping the smallest balloon does not guarantee the optimum. In this instance, bursting $1$ first yields optimal results, but on `[3, 5, 8]`, popping $5$ before $3$ and $8$ yields $120$ coins, whereas popping $3$ first would yield only $24$.
- **Thinking Forward Instead of Backward:** Trying to decide the *first* balloon to burst causes future neighbors to depend on the deletion, coupling subproblems and preventing dynamic programming. Selecting the *last* balloon guarantees static boundary neighbors.
- **Topological Evaluation Order:** Subproblems must be computed in order of increasing interval length $L = j - i$, or equivalently by iterating $i$ downwards from $N - 1$ to $0$ and $j$ upwards from $i + 2$ to $N + 1$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^3)$, where $N$ is the number of balloons in `nums`. There are $O(N^2)$ interval pairs $(i, j)$. For each interval, $k$ ranges over at most $N$ values. Evaluating $f[i][j]$ takes $O(1)$ operations per $k$, giving $O(N^3)$ total time. For $N = 300$, $N^3 / 6 \approx 4.5 \times 10^6$ operations, executing in under 0.1 seconds.
- **Auxiliary Space Complexity:** $O(N^2)$ auxiliary memory to store the $(N + 2) \times (N + 2)$ DP table $f$.