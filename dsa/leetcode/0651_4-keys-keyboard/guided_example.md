# Guided Example: 4 Keys Keyboard

We trace the step-by-step 4-key operational taxonomy (typing `'A'` vs `Select All` + `Copy` + repeated `Paste`), keystroke overhead analysis ($2$ setup steps for `Ctrl-A` and `Ctrl-C`), multiplicative scaling factor derivation ($(i - k - 1) \times dp[k]$), dynamic programming recurrence ($dp[i] = \max dp[j-1] \cdot (i - j)$), and screen character maximization on representative keypress budgets:

- **Input:** $n = 7$
- **Required output:** `9`
  - Available keyboard actions:
    1. Key 1 (`A`): Types one `'A'` on screen ($+1$ character).
    2. Key 2 (`Ctrl-A`): Selects all characters currently on screen ($0$ new characters).
    3. Key 3 (`Ctrl-C`): Copies the selected text to clipboard ($0$ new characters).
    4. Key 4 (`Ctrl-V`): Appends the clipboard text to the screen ($+\text{clipboard}$ characters).
  - Objective: Maximize the total number of `'A'`s on screen using **at most $n$ keypresses**.
- **Setup Overhead & Multiplicative Paste Model:**
  - **Direct Typing Baseline:**
    - If you only press Key 1 (`A`), after $i$ keypresses you produce exactly $i$ characters:
      $$
      dp[i] \ge i
      $$
    - For small $n \le 6$, direct typing or simple single pastes dominate.
  - **Copy-Paste Multiplier Mechanics:**
    - To duplicate the screen contents present at step $k$:
      - Step $k + 1$: Press `Ctrl-A` (Select All) — $1$ keypress.
      - Step $k + 2$: Press `Ctrl-C` (Copy) — $1$ keypress.
      - Note: These two steps cost $2$ keypresses without producing any new characters on screen!
    - From step $k + 3$ onwards, every subsequent keypress can be `Ctrl-V` (Paste):
      - Step $k + 3$ (1st paste): Screen now has $dp[k] + dp[k] = 2 \cdot dp[k]$.
      - Step $k + 4$ (2nd paste): Screen now has $dp[k] + 2 \cdot dp[k] = 3 \cdot dp[k]$.
      - In general, at step $i$ (where $i \ge k + 3$):
        - Number of paste operations executed:
          $$
          \text{Pastes} = i - (k + 2)
          $$
        - Total screen count:
          $$
          \text{Count} = dp[k] \times (1 + \text{Pastes}) = dp[k] \times (i - k - 1)
          $$
  - **Dynamic Programming Recurrence:**
    - Let $dp[i]$ be the maximum characters producible with $i$ keypresses.
    - Base state: $dp[i] = i$.
    - For each candidate anchor step $k$ (where $k \le i - 3$):
      $$
      dp[i] = \max(dp[i], \; dp[k] \times (i - k - 1))
      $$
- **Step-by-Step Worked Execution Trace for $n = 7$:**
  - Initialize $dp$ array for $i = 0 \dots 7$:
    $$
    dp = [0, 1, 2, 3, 4, 5, 6, 7]
    $$
  - **Steps $i = 1 \dots 5$:**
    - For $i \le 5$, setup cost of $2$ keypresses means copy-pasting cannot beat direct typing (e.g. at $i = 5$, copy-pasting after $k = 2$ gives $dp[2] \times (5 - 2 - 1) = 2 \times 2 = 4 < 5$).
    - $dp[1] = 1, \; dp[2] = 2, \; dp[3] = 3, \; dp[4] = 4, \; dp[5] = 5$.
  - **Step $i = 6$:**
    - Direct typing: $6$.
    - Anchor $k = 3$ (copy after 3 'A's):
      - Cost: 3 typing + 1 `Ctrl-A` + 1 `Ctrl-C` + 1 `Ctrl-V` = 6 keypresses.
      - Pastes: $6 - 3 - 2 = 1$.
      - Screen count: $dp[3] \times (1 + 1) = 3 \times 2 = \mathbf{6}$.
    - Best: $dp[6] = 6$.
  - **Step $i = 7$:**
    - Direct typing: $7$.
    - Test anchor $k = 1$: $dp[1] \times (7 - 1 - 1) = 1 \times 5 = 5$.
    - Test anchor $k = 2$: $dp[2] \times (7 - 2 - 1) = 2 \times 4 = 8$.
    - Test anchor $k = 3$:
      - Sequence:
        - Keys $1, 2, 3$: Type `'A'`, `'A'`, `'A'` ($dp[3] = 3$)
        - Key $4$: `Ctrl-A` (Select all 3)
        - Key $5$: `Ctrl-C` (Copy 3 into clipboard)
        - Key $6$: `Ctrl-V` (Paste 3 $\implies$ Screen has $3 + 3 = 6$)
        - Key $7$: `Ctrl-V` (Paste 3 $\implies$ Screen has $6 + 3 = 9$)
      - Formula:
        $$
        dp[3] \times (7 - 3 - 1) = 3 \times 3 = \mathbf{9}
        $$
    - Test anchor $k = 4$: $dp[4] \times (7 - 4 - 1) = 4 \times 2 = 8$.
    - Maximize:
      $$
      dp[7] = \max(7, 5, 8, \mathbf{9}, 8) = \mathbf{9}
      $$
  - **Final Output:**
    $$
    ans = dp[7] = \mathbf{9}
    $$
- **Larger Example ($n = 11$):**
  - Anchor $k = 7$ ($dp[7] = 9$):
    - $i = 11 \implies dp[7] \times (11 - 7 - 1) = 9 \times 3 = \mathbf{27}$.
  - Keys: 7 keys to get 9, then `Ctrl-A` (8), `Ctrl-C` (9), `Ctrl-V` (10, 18 'A's), `Ctrl-V` (11, 27 'A's).
- **Small Budget ($n = 3$):**
  - Copy-paste requires at least 4 keys (`A`, `Ctrl-A`, `Ctrl-C`, `Ctrl-V` $\implies 2$).
  - For $n = 3$, direct typing gives $3 \implies \mathbf{3}$.

This instance demonstrates amortized copy-paste overhead modeling and discrete subproblem factorization, mathematically proves why a 2-step setup threshold delays exponential scaling until $n \ge 7$, and derives $O(N^2)$ execution time (or $O(N)$ with optimal 3-4 paste windowing) and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an allowed number of keypresses $n$:
Keys: `A` (type), `Ctrl-A` (select all), `Ctrl-C` (copy), `Ctrl-V` (paste).
Find the **maximum number of `'A'`s** you can print.

```text
n = 7 keypresses:

Sequence:
  Key 1: 'A'      -> Screen: A        (length 1)
  Key 2: 'A'      -> Screen: AA       (length 2)
  Key 3: 'A'      -> Screen: AAA      (length 3)
  Key 4: Ctrl-A   -> Selected 3
  Key 5: Ctrl-C   -> Copied 3
  Key 6: Ctrl-V   -> Screen: AAAAAA   (length 6)
  Key 7: Ctrl-V   -> Screen: AAAAAAAAA(length 9)

Result: 9
```

### The Invariant of the 2-Step Overhead
- `Ctrl-A` and `Ctrl-C` cost **2 keypresses** without adding any letters.
- Therefore, each copy-paste cycle starting from step $k$ requires at least 3 steps ($k + 3$) to paste once, multiplying the text by:
  $$
  \text{Multiplier} = i - k - 1
  $$
- Copy-pasting becomes strictly superior to direct typing only when $n \ge 7$.

---

## 2. Conceptual Foundation & Invariants

### 1. Recurrence Relation:
For $i \in [1, n]$:
$$
dp[i] = i
$$
$$
dp[i] = \max_{1 \le k \le i - 3} \left( dp[k] \cdot (i - k - 1) \right)
$$

### 2. Multiplier Horizon:
- In practice, the optimal number of pastes per copy cycle is 2, 3, or 4 (i.e. multiplying by 3, 4, or 5).
- Checking the last 5 anchor states is mathematically sufficient for an $O(N)$ linear pass.

> **Super-Linear Phase Transition Invariant.** The growth regime transitions from linear $O(n)$ for $n \le 6$ to discrete exponential $O(3^{n/5})$ for $n \ge 7$, as the 2-step fixed cost of selection and copying is amortized by repeated buffer pasting.

---

## 3. Step-by-Step Worked Execution

We trace $n = 7$:

---

### Step 1: Base Typing
- $dp[1]=1, dp[2]=2, dp[3]=3, dp[4]=4, dp[5]=5, dp[6]=6, dp[7]=7$.

---

### Step 2: Evaluate Anchors for $i = 7$
- $k = 1$: $dp[1] \times (7 - 1 - 1) = 1 \times 5 = 5$.
- $k = 2$: $dp[2] \times (7 - 2 - 1) = 2 \times 4 = 8$.
- $k = 3$: $dp[3] \times (7 - 3 - 1) = 3 \times 3 = \mathbf{9}$.
- $k = 4$: $dp[4] \times (7 - 4 - 1) = 4 \times 2 = 8$.

---

### Step 3: Global Maximum
$$
dp[7] = \max(7, 5, 8, 9, 8) = \mathbf{9}
$$

---

## 4. Complete Execution Trace

| Keypress Budget $i$ | Optimal Strategy | Keypress Sequence | Screen Character Count |
|:---:|:---:|:---:|:---:|
| $1$ | Type `A` | `A` | $1$ |
| $2$ | Type `A` | `A, A` | $2$ |
| $3$ | Type `A` | `A, A, A` | $3$ |
| $4$ | Type `A` | `A, A, A, A` | $4$ |
| $5$ | Type `A` | `A, A, A, A, A` | $5$ |
| $6$ | Type or Copy(3) | `A, A, A, A, A, A` | $6$ |
| **$7$** | **Copy(3) + 2 Pastes** | **`A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V`** | **`9`** |

---

## 5. Boundary Cases & Failure Modes

- **$n \le 6$:** Always equals $n$ (direct typing is optimal).
- **$n = 7$:** First value where copy-paste beats typing ($9 > 7$).
- **$n = 8$:** $dp[4] \times 3 = 12$ or $dp[3] \times 4 = 12$.
- **Large $n$ ($n = 50$):** DP computes cleanly without integer overflow issues in $< 1$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Assuming 1 Step Overhead:** Forgetting that both `Ctrl-A` and `Ctrl-C` take separate keypresses undercounts the cost of copying.
- **Copying on Every Step:** Copying repeatedly without multiple pastes wastes keys on the 2-step setup fee.
- **Greedy Paste Without Anchor Search:** Assuming you should always copy at $n - 3$ misses better earlier anchor partitions.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Double loop for $i$ from 3 to $n$ and $j$ from 2 to $i - 1$:
  - Number of operations: $\sum_{i=1}^N i = \mathcal{O}(N^2)$.
  - (Can be restricted to $\mathcal{O}(N)$ by checking only the last 5 anchors).
  - For $N = 50$, executes $\approx 1250$ steps, completing in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the DP array.
