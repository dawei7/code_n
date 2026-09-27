# Guided Example: Freedom Trail

We trace the step-by-step circular dial distance metric ($\min(|j - k|, n - |j - k|)$), multi-position occurrence tracking ($pos[c]$), dynamic programming state matrix ($f[i][j]$: minimum cost to spell prefix $key[0 \dots i]$ ending at ring index $j$), button-press cost addition ($+1$), and optimal final alignment selection on representative mechanical dial instances:

- **Input:**
  - Outer ring engraving: $ring = \text{"godding"}$
  - Target keyword: $key = \text{"gd"}$
- **Required output:** `4`
  - Ring length: $n = 7$
  - Key length: $m = 2$
  - Starting position: Index $0$ of $ring$ is aligned at 12:00.
  - Operation costs:
    - Rotate clockwise or counter-clockwise by 1 step: $1$ unit.
    - Press the center button to spell the aligned character: $1$ unit.
- **Character index distribution:**
  - Character `'g'`: indices $0, 6$ in $ring$
  - Character `'o'`: index $1$
  - Character `'d'`: indices $2, 3$
  - Character `'i'`: index $4$
  - Character `'n'`: index $5$
- **Dynamic programming execution trace:**
  - Let $f[i][j]$ be the minimum total cost to spell $key[0 \dots i]$ with $ring$ ending at index $j$.
  - Circular distance metric on ring of length $n = 7$:
    $$
    dist(j, k) = \min(|j - k|, \; 7 - |j - k|)
    $$
  - **Stage 0: Spell first letter $key[0] = \text{'g'}$ (Starting from index 0):**
    - Possible targets for `'g'`: indices $0$ and $6$.
    - **Target $j = 0$:**
      - Distance from start $0$: $dist(0, 0) = 0$.
      - Button press: $+1$.
      - $f[0][0] = 0 + 1 = \mathbf{1}$.
    - **Target $j = 6$:**
      - Distance from start $0$: $\min(|6 - 0|, 7 - 6) = \min(6, 1) = 1$ (1 step counter-clockwise).
      - Button press: $+1$.
      - $f[0][6] = 1 + 1 = \mathbf{2}$.
  - **Stage 1: Spell second letter $key[1] = \text{'d'}$:**
    - Possible targets for `'d'`: indices $2$ and $3$.
    - Previous candidates: $k \in \{0, 6\}$ with costs $f[0][0] = 1, f[0][6] = 2$.
    - **Evaluate Target $j = 2$:**
      - From $k = 0$:
        $$
        \text{cost} = f[0][0] + dist(0, 2) + 1 = 1 + 2 + 1 = \mathbf{4}
        $$
      - From $k = 6$:
        $$
        dist(6, 2) = \min(|6 - 2|, 7 - 4) = \min(4, 3) = 3
        $$
        $$
        \text{cost} = f[0][6] + dist(6, 2) + 1 = 2 + 3 + 1 = 6
        $$
      - Optimal transition:
        $$
        f[1][2] = \min(4, 6) = \mathbf{4}
        $$
    - **Evaluate Target $j = 3$:**
      - From $k = 0$:
        $$
        dist(0, 3) = \min(3, 4) = 3 \implies \text{cost} = 1 + 3 + 1 = \mathbf{5}
        $$
      - From $k = 6$:
        $$
        dist(6, 3) = \min(3, 4) = 3 \implies \text{cost} = 2 + 3 + 1 = 6
        $$
      - Optimal transition:
        $$
        f[1][3] = \min(5, 6) = \mathbf{5}
        $$
  - **Stage 2: Final Minimum Extraction:**
    - Target letters exhausted.
    - Global minimum across all valid terminal positions for $key[-1] = \text{'d'}$:
      $$
      \min(f[1][2], \; f[1][3]) = \min(4, 5) = \mathbf{4}
      $$
    - Optimal sequence:
      1. Press button at index 0 (spells `'g'`). Cost: $1$.
      2. Rotate clockwise by 2 steps to index 2 (aligns `'d'`). Cost: $2$.
      3. Press button at index 2 (spells `'d'`). Cost: $1$.
      4. Total cost: $1 + 2 + 1 = \mathbf{4}$.
- **Full Word Repeat Instance ($ring = \text{"godding"}, key = \text{"godding"}$):**
  - Evaluates transitions across all 7 letters $\implies \mathbf{13}$ total operations.
- **Single Character Match at Index 0 ($ring = \text{"abc"}, key = \text{"a"}$):**
  - Distance is 0, 1 button press $\implies \mathbf{1}$.

This instance demonstrates shortest path optimization on cyclic stage-graphs, mathematically proves why dynamic programming prevents greedy dead-ends on multi-occurrence letters, and derives $O(M \cdot N^2)$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $ring$ representing the engraved circular dial and a string $key$ representing the target keyword:
The ring begins with index 0 at the 12:00 position.
In each step, you can rotate the ring clockwise or counter-clockwise by 1 position (costs 1 step), or press the center button to spell the character currently at 12:00 (costs 1 step).
Find the **minimum number of steps** to spell all characters in $key$.

```text
Dial (ring = "godding"):
          [g] (idx 0, 12:00)
       g       o
     n           d
       i       d

Key = "gd":
  1. Spell 'g': Already at 12:00! Press button -> 1 step.
  2. Rotate to 'd':
     - Turn clockwise 2 steps to reach index 2 (costs 2 steps).
     - Or turn counter-clockwise 5 steps to reach index 2.
     Optimal turn = 2 steps.
  3. Spell 'd': Press button -> 1 step.

Total steps: 1 + 2 + 1 = 4
```

### Why a Greedy Choice Fails
- Characters in $ring$ often appear multiple times (e.g. `'g'` at indices $0$ and $6$; `'d'` at indices $2$ and $3$).
- Greedily rotating to the nearest copy of the next letter might place the dial in a disadvantageous position for subsequent letters in $key$.
- Because each letter in $key$ defines a new stage, and choices at stage $i$ only depend on the dial position at stage $i-1$, **Dynamic Programming** computes the globally optimal trajectory.

---

## 2. Conceptual Foundation & Invariants

### 1. The Cyclic Dial Distance Metric:
For two ring indices $j$ and $k$ on a ring of length $n$:
$$
dist(j, k) = \min(|j - k|, \; n - |j - k|)
$$
- $|j - k|$ represents the direct arc distance.
- $n - |j - k|$ represents the complementary arc distance wrapping around index 0.
- Taking the minimum selects the shorter rotation direction (clockwise vs counter-clockwise).

### 2. The Dynamic Programming State:
Let $f[i][j]$ be the minimum cost to spell the prefix $key[0 \dots i]$ such that the ring ends aligned at index $j \in pos[key[i]]$:
- **Base Case ($i = 0$):**
  For each index $j$ where $ring[j] == key[0]$:
  $$
  f[0][j] = dist(0, j) + 1
  $$
  ($+1$ accounts for pressing the button).
- **Recurrence ($i \ge 1$):**
  For each $j \in pos[key[i]]$:
  $$
  f[i][j] = \min_{k \in pos[key[i-1]]} \Big( f[i-1][k] + dist(k, j) + 1 \Big)
  $$
- **Final Result:**
  $$
  \min_{j \in pos[key[m-1]]} f[m-1][j]
  $$

> **Optimal Substructure Invariant.** The minimum cost to align $key[i]$ at dial position $j$ depends solely on the minimum costs of having aligned $key[i-1]$ at previous dial positions $k$ plus the shortest arc transition $dist(k, j) + 1$.

---

## 3. Step-by-Step Worked Execution

We trace $ring = \text{"godding"}$ ($n = 7$) and $key = \text{"gd"}$ ($m = 2$):

---

### Step 1: Precompute Character Indices
- `pos['g'] = [0, 6]`
- `pos['d'] = [2, 3]`

---

### Step 2: Base Stage ($i = 0$, $key[0] = \text{'g'}$)
Start at ring position $0$:
- Target $j = 0$:
  $$
  f[0][0] = dist(0, 0) + 1 = 0 + 1 = \mathbf{1}
  $$
- Target $j = 6$:
  $$
  dist(0, 6) = \min(6, 7 - 6) = \min(6, 1) = 1
  $$
  $$
  f[0][6] = 1 + 1 = \mathbf{2}
  $$

---

### Step 3: Transition Stage ($i = 1$, $key[1] = \text{'d'}$)
Possible targets for `'d'`: $j \in \{2, 3\}$.
Prior positions: $k \in \{0, 6\}$.

1. **Calculate $f[1][2]$:**
   - Transition from $k = 0$:
     $$
     f[0][0] + dist(0, 2) + 1 = 1 + 2 + 1 = \mathbf{4}
     $$
   - Transition from $k = 6$:
     $$
     dist(6, 2) = \min(|6 - 2|, 7 - 4) = 3 \implies 2 + 3 + 1 = 6
     $$
   - Best: $f[1][2] = \min(4, 6) = \mathbf{4}$.

2. **Calculate $f[1][3]$:**
   - Transition from $k = 0$:
     $$
     dist(0, 3) = \min(3, 4) = 3 \implies 1 + 3 + 1 = \mathbf{5}
     $$
   - Transition from $k = 6$:
     $$
     dist(6, 3) = \min(3, 4) = 3 \implies 2 + 3 + 1 = 6
     $$
   - Best: $f[1][3] = \min(5, 6) = \mathbf{5}$.

---

### Step 4: Final Answer
$$
\min(f[1][2], \; f[1][3]) = \min(4, 5) = \mathbf{4}
$$

---

## 4. Complete Execution Trace

| Stage $i$ | Target Letter $key[i]$ | Dial Position $j$ | Best Previous Position $k$ | Rotation Steps $dist(k, j)$ | Button Press | Total Cost $f[i][j]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | `'g'` | $0$ | Start ($0$) | $0$ | $+1$ | **$1$** |
| **$0$** | `'g'` | $6$ | Start ($0$) | $1$ | $+1$ | **$2$** |
| **$1$** | `'d'` | $2$ | $0$ | $2$ | $+1$ | $1 + 2 + 1 = \mathbf{4}$ |
| **$1$** | `'d'` | $3$ | $0$ | $3$ | $+1$ | $1 + 3 + 1 = \mathbf{5}$ |
| **Result** | — | — | — | — | — | **$\min(4, 5) = \mathbf{4}$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Letter Key ($key = \text{"g"}$):** Returns base stage cost $\implies \mathbf{1}$.
- **All Identical Letters in Ring ($ring = \text{"aaaaa"}, key = \text{"aaaa"}$):** Dial never needs to rotate, only press button 4 times $\implies \mathbf{4}$.
- **Repeated Consecutive Letters in Key ($key = \text{"dd"}$):** After reaching `'d'`, the second `'d'` requires 0 rotations and 1 button press $\implies +1$.
- **Alternating Letters Across the Ring:** Circular wrap-around distance correctly bounds rotation cost by $n / 2$.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Choice at Each Step:** Choosing the nearest `'d'` might strand the ring far away from the next letter in $key$. Only full DP guarantees global optimality.
- **Linear Distance Instead of Modular Dial Distance:** Computing $|j - k|$ without comparing against $n - |j - k|$ misses shorter rotations across the 12:00 wrap-around boundary.
- **Forgetting Button Press Step:** Every spelled character requires an explicit button press ($+1$ step). The answer is strictly $\sum (\text{rotations}) + |key|$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Outer loop runs for each of the $M$ characters in $key$.
  - In each step, we iterate over all positions of $key[i]$ (at most $N$) and all positions of $key[i-1]$ (at most $N$).
  - Computing circular distance takes $O(1)$ arithmetic.
  - Total Time: $\mathcal{O}(M \cdot N^2)$. For $M, N \le 100$, $100 \times 10^4 = 10^6$ operations, completing in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ to store the DP table $f$, easily reducible to $O(N)$ space using rolling arrays.
