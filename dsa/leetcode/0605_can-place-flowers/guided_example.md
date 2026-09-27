# Guided Example: Can Place Flowers

We trace the step-by-step zero-padded sentinel boundary framing ($[0] + flowerbed + [0]$), 3-plot vacant window detection ($flowerbed[i-1] == 0 \land flowerbed[i] == 0 \land flowerbed[i+1] == 0$), greedy immediate planting ($flowerbed[i] \leftarrow 1$), quota reduction ($n \leftarrow n - 1$), and non-adjacent feasibility testing on representative planting beds:

- **Input:** $flowerbed = [1, 0, 0, 0, 1], \quad n = 1$
- **Required output:** `true`
  - Planting constraints:
    - Flowers cannot be planted in **adjacent plots** (no two $1$s may be adjacent).
    - Given an array where $1$ is planted and $0$ is empty, determine if at least $n$ new flowers can be added without violating adjacency.
- **Greedy Earliest Placement & Zero Sentinel Framing:**
  - **Greedy Choice Property:**
    - Scanning from left to right, whenever we encounter a legal planting opportunity, planting a flower as early as possible is always globally optimal. It never reduces the capacity to plant future flowers compared to delaying the planting.
  - **The 3-Consecutive Zero Condition:**
    - A flower can be safely placed at plot $i$ if and only if:
      $$
      flowerbed[i - 1] == 0 \quad \land \quad flowerbed[i] == 0 \quad \land \quad flowerbed[i + 1] == 0
      $$
  - **Sentinel Boundary Padding:**
    - To eliminate boundary edge-case logic for plot $0$ and plot $m - 1$, prepend $0$ and append $0$ to the array:
      $$
      padded = [0] + flowerbed + [0]
      $$
    - The original indices $0 \dots m - 1$ now cleanly map to indices $1 \dots m$, where every plot has well-defined left and right neighbors.
- **Step-by-Step Worked Execution Trace:**
  - Original array: $flowerbed = [1, 0, 0, 0, 1]$, length $m = 5$, target $n = 1$.
  - Pad boundaries with $0$:
    $$
    padded = [\mathbf{0}, \; 1, \; 0, \; 0, \; 0, \; 1, \; \mathbf{0}] \quad (\text{length } 7)
    $$
  - **Scan indices $i = 1 \dots 5$:**
    - **Plot $i = 1$ (Original plot 0, value $1$):**
      - Window $padded[0 \dots 2] = [0, 1, 0]$.
      - Current plot is already planted ($1 \ne 0$) $\implies$ Skip.
    - **Plot $i = 2$ (Original plot 1, value $0$):**
      - Window $padded[1 \dots 3] = [1, 0, 0]$.
      - Left neighbor is $1$ (planted) $\implies$ Cannot plant. Skip.
    - **Plot $i = 3$ (Original plot 2, value $0$):**
      - Window $padded[2 \dots 4] = [0, 0, 0]$.
      - Check sum:
        $$
        0 + 0 + 0 = 0 \implies \mathbf{Legal\ to\ plant!}
        $$
      - Plant flower at index 3:
        $$
        padded[3] \leftarrow 1
        $$
      - Decrement quota:
        $$
        n \leftarrow 1 - 1 = \mathbf{0}
        $$
      - Updated array: $[0, 1, 0, \mathbf{1}, 0, 1, 0]$.
    - **Plot $i = 4$ (Original plot 3, value $0$):**
      - Window $padded[3 \dots 5] = [1, 0, 1]$.
      - Left neighbor is now $1$ (the newly planted flower!) $\implies$ Cannot plant. Skip.
    - **Plot $i = 5$ (Original plot 4, value $1$):**
      - Current plot is $1 \implies$ Skip.
  - **Termination & Quota Check:**
    - Quota remaining:
      $$
      n = 0 \le 0 \implies \mathbf{True!}
      $$
    - Return **`true`**.
- **Insufficient Space Instance ($flowerbed = [1, 0, 0, 0, 1], n = 2$):**
  - Only 1 flower can fit into the middle plot.
  - Final remaining quota: $n = 2 - 1 = 1 > 0 \implies \mathbf{false}$.
- **Empty Flowerbed Instance ($flowerbed = [0, 0, 0, 0, 0], n = 3$):**
  - Padded: $[0, 0, 0, 0, 0, 0, 0]$.
  - Plants at plots $1, 3, 5$ (original indices $0, 2, 4$).
  - Total planted = $3 \implies \mathbf{true}$.
- **Zero Target Quota ($n = 0$):**
  - Trivially achievable without any planting $\implies \mathbf{true}$.

This instance demonstrates greedy independent set placement on linear path graphs, mathematically proves why local 3-zero windows maximize non-adjacent packing, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a flowerbed array of 0s (empty) and 1s (planted), and an integer $n$:
Can we plant $n$ new flowers such that no two flowers are in adjacent plots?

```text
flowerbed: [ 1,  0,  0,  0,  1 ],  n = 1

Padded: [0,  1,  0,  0,  0,  1,  0]
                 ^   ^   ^
                 Window [0, 0, 0] at index 3!

Plant at index 3 -> [0, 1, 0, 1, 0, 1, 0]
Planted = 1 flower. Quota satisfied!
Result: true
```

### The Sentinel Boundary Pattern
- The edge plots ($i = 0$ and $i = m - 1$) only have one neighbor.
- A flower can be planted at index 0 if index 0 is empty and index 1 is empty.
- Instead of writing separate boundary condition `if` statements, prepending and appending a virtual `0` uniformly allows every plot to check the identical 3-element condition:
  $$
  \text{sum}(padded[i-1 \dots i+1]) == 0
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. The Greedy Strategy:
- Whenever a plot is empty and both its left and right plots are empty:
  Plant a flower immediately (`flowerbed[i] = 1`) and decrement $n$.
- This greedy choice is optimal: delaying a planting never creates more future opportunities than planting at the earliest possible slot.

### 2. Padded Formulation:
```text
padded = [0] + flowerbed + [0]
for i from 1 to len(flowerbed):
    if padded[i-1] == 0 and padded[i] == 0 and padded[i+1] == 0:
        padded[i] = 1
        n -= 1
return n <= 0
```

> **Greedy Dominance Invariant.** Planting at the earliest legal position $i$ minimizes the blocking range on future indices $j > i$, leaving maximal remaining slots for subsequent flowers.

---

## 3. Step-by-Step Worked Execution

We trace $flowerbed = [1, 0, 0, 0, 1], n = 1$:

---

### Step 1: Pad Bed
$$
padded = [0, \; 1, \; 0, \; 0, \; 0, \; 1, \; 0]
$$

---

### Step 2: Iterate Across Plots
- $i = 1$: current is 1 $\implies$ skip.
- $i = 2$: window is `[1, 0, 0]` $\implies$ sum is 1, skip.
- $i = 3$: window is `[0, 0, 0]` $\implies$ sum is 0!
  - Plant: $padded[3] \leftarrow 1$.
  - $n \leftarrow 1 - 1 = 0$.
- $i = 4$: window is `[1, 0, 1]` $\implies$ skip.
- $i = 5$: current is 1 $\implies$ skip.

---

### Step 3: Check Quota
$$
n = 0 \le 0 \implies \mathbf{True}
$$

---

## 4. Complete Execution Trace

| Index $i$ | Padded Window $[i-1, i, i+1]$ | Window Sum | Legal to Plant? | Flowerbed Action | Quota $n$ After |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $[0, 1, 0]$ | $1$ | No | Skip | $1$ |
| $2$ | $[1, 0, 0]$ | $1$ | No | Skip | $1$ |
| **$3$** | **$[0, 0, 0]$** | **$0$** | **Yes** | **Plant $1$** | **$0$** |
| $4$ | $[1, 0, 1]$ | $2$ | No | Skip | $0$ |
| $5$ | $[0, 1, 0]$ | $1$ | No | Skip | $0$ |
| **Final** | — | — | — | **Quota met** | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 0$:** Already satisfied $\implies$ returns `true` immediately.
- **Single Plot Empty ($[0], n = 1$):** Padded is `[0, 0, 0]` $\implies$ plants at 0 $\implies$ returns `true`.
- **Single Plot Occupied ($[1], n = 1$):** Cannot plant $\implies$ returns `false`.
- **Alternating Plots ($[1, 0, 1, 0, 1]$):** No 3 consecutive zeros $\implies$ 0 flowers can be planted.

---

## 6. Traps & Common Anti-Patterns

- **Not Mutating the Array Upon Planting:** If you do not set $padded[i] = 1$, the next index $i + 1$ might also see 3 zeros and plant an adjacent flower, violating the no-adjacent-flowers rule.
- **Mathematical Division Shortcuts Without Accounting for Ends:** Trying to count consecutive zeros via division formulas requires complex edge adjustments for ends. The greedy linear scan is bug-free.
- **Continuing Scan After $n \le 0$:** Once $n \le 0$, the algorithm can terminate early.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single linear pass through the array of length $N$: $\mathcal{O}(N)$ operations.
  - Can terminate early as soon as $n \le 0$.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 2 \times 10^4$, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to create the padded array (or $\mathcal{O}(1)$ with inline boundary checks).
