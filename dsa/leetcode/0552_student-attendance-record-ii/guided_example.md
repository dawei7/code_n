# Guided Example: Student Attendance Record II

We trace the step-by-step state compression into finite automata states ($(j, k)$ where $j \in \{0, 1\}$ total absences, $k \in \{0, 1, 2\}$ trailing late streak), forward day-by-day dynamic programming transitions ($'P', 'A', 'L'$), modular arithmetic constraints ($10^9 + 7$), and cumulative award-eligible sequence counting on representative record lengths:

- **Input:** $n = 2$
- **Required output:** `8`
  - Total alphabet symbols: $\{'P', 'A', 'L'\}$ (total unconstrained strings of length 2: $3^2 = 9$).
  - Disqualification criteria:
    1. Two or more `'A'`s ($count('A') \ge 2$).
    2. Three or more consecutive `'L'`s (streak of $'L' \ge 3$).
- **State Machine Representation ($dfs(i, j, k)$):**
  - Parameter $i \in [0, n]$: Current day index.
  - Parameter $j \in \{0, 1\}$: Total number of absences (`'A'`) accumulated so far ($j < 2$).
  - Parameter $k \in \{0, 1, 2\}$: Current consecutive run of late days (`'L'`) immediately preceding day $i$.
  - There are exactly $2 \times 3 = \mathbf{6}$ valid structural states per day:
    - State $(0, 0)$: 0 absences, 0 trailing late days (e.g. `""`, `"P"`)
    - State $(0, 1)$: 0 absences, 1 trailing late day (e.g. `"L"`)
    - State $(0, 2)$: 0 absences, 2 trailing late days (e.g. `"LL"`)
    - State $(1, 0)$: 1 absence, 0 trailing late days (e.g. `"A"`, `"AP"`)
    - State $(1, 1)$: 1 absence, 1 trailing late day (e.g. `"AL"`)
    - State $(1, 2)$: 1 absence, 2 trailing late days (e.g. `"ALL"`)
- **Action Transitions from State $(j, k)$:**
  1. **Add `'P'` (Present):** Resets late streak to 0; preserves absences.
     $$
     (j, k) \xrightarrow{\text{'P'}} (j, \; 0)
     $$
  2. **Add `'A'` (Absent):** Resets late streak to 0; increments absences (valid only if $j == 0$).
     $$
     (0, k) \xrightarrow{\text{'A'}} (1, \; 0)
     $$
  3. **Add `'L'` (Late):** Increments late streak by 1 (valid only if $k < 2$).
     $$
     (j, k) \xrightarrow{\text{'L'}} (j, \; k + 1)
     $$
- **Step-by-step DP execution trace for $n = 2$:**
  - **Day 0 (Start):** 1 configuration in state $(0, 0)$.
    - Counts: $(0, 0): 1, \quad \text{all others}: 0$.
  - **Day 1 (Transitions from Day 0):**
    - From $(0, 0)$ with 1 path:
      - Append `'P'` $\to$ State $(0, 0)$: $1$ path (`"P"`)
      - Append `'A'` $\to$ State $(1, 0)$: $1$ path (`"A"`)
      - Append `'L'` $\to$ State $(0, 1)$: $1$ path (`"L"`)
    - Day 1 State distribution (3 valid strings of length 1):
      - $(0, 0) = 1$ (`"P"`)
      - $(0, 1) = 1$ (`"L"`)
      - $(0, 2) = 0$
      - $(1, 0) = 1$ (`"A"`)
      - $(1, 1) = 0$
      - $(1, 2) = 0$
      - Total Day 1: $1 + 1 + 1 = \mathbf{3}$ valid records.
  - **Day 2 (Transitions from Day 1):**
    - **From $(0, 0)$ (`"P"`):**
      - Append `'P'` $\to (0, 0)$: `"PP"`
      - Append `'A'` $\to (1, 0)$: `"PA"`
      - Append `'L'` $\to (0, 1)$: `"PL"`
    - **From $(0, 1)$ (`"L"`):**
      - Append `'P'` $\to (0, 0)$: `"LP"`
      - Append `'A'` $\to (1, 0)$: `"LA"`
      - Append `'L'` $\to (0, 2)$: `"LL"`
    - **From $(1, 0)$ (`"A"`):**
      - Append `'P'` $\to (1, 0)$: `"AP"`
      - Append `'A'` $\to$ **Forbidden!** ($j$ would become 2: `"AA"` disqualified).
      - Append `'L'` $\to (1, 1)$: `"AL"`
    - Day 2 State aggregation:
      - State $(0, 0)$: `"PP"`, `"LP"` $\implies \mathbf{2}$
      - State $(0, 1)$: `"PL"` $\implies \mathbf{1}$
      - State $(0, 2)$: `"LL"` $\implies \mathbf{1}$
      - State $(1, 0)$: `"PA"`, `"LA"`, `"AP"` $\implies \mathbf{3}$
      - State $(1, 1)$: `"AL"` $\implies \mathbf{1}$
      - State $(1, 2)$: none $\implies \mathbf{0}$
    - Total valid records of length 2:
      $$
      2 + 1 + 1 + 3 + 1 + 0 = \mathbf{8}
      $$
    - The 8 valid records: `["PP", "PL", "LL", "LP", "PA", "LA", "AP", "AL"]`.
    - Only 1 string out of $3^2 = 9$ was eliminated: `"AA"`.
- **Length $n = 3$ Instance:**
  - Evaluates transitions from Day 2 states $\implies$ yields **`19`** valid records.
- **Length $n = 1$ Instance:**
  - Direct day 1 evaluation $\implies$ **`3`** records (`"P"`, `"A"`, `"L"`).
- **Modulo Reduction ($10^9 + 7$):**
  - For $n = 10^5$, answers reach exponential magnitudes; performing all additions modulo $10^9 + 7$ prevents integer overflow while maintaining exactness.

This instance demonstrates constrained language enumeration via finite-state machine Markov transitions, mathematically proves why 6-state DP contracts combinatorial strings from $O(3^N)$ to $O(N)$, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n$:
Return the number of possible attendance records of length $n$ that earn an attendance award, modulo $10^9 + 7$.
A record is eligible if and only if:
1. Total absences (`'A'`) is strictly less than 2 ($< 2$).
2. It contains no 3 or more consecutive late days (never contains `"LLL"`).

```text
Evaluating n = 2:
  All 9 possible combinations:
    PP, PA, PL, AP, AA, AL, LP, LA, LL

  Disqualified:
    AA (2 absences >= 2)

  Valid (8 records):
    PP, PA, PL, AP, AL, LP, LA, LL

Result = 8
```

### From Exponential Branching to Finite State Machine
- Brute-force generation of all strings takes $O(3^n)$ time, which is impossible for $n = 10^5$ ($3^{100000} \gg 10^{47700}$).
- However, the validity of extending a prefix depends on only **two scalar numbers**:
  1. How many `'A'`s have been seen so far ($j \in \{0, 1\}$).
  2. How many consecutive `'L'`s are at the tail ($k \in \{0, 1, 2\}$).
- Any two prefixes with the same $(j, k)$ are completely equivalent with respect to future characters!
- This reduces the state space to exactly $2 \times 3 = 6$ states per day.

---

## 2. Conceptual Foundation & Invariants

### 1. State Space:
$dp(i, j, k)$:
- $i$: current length ($0 \dots n$).
- $j$: accumulated absences ($0$ or $1$).
- $k$: trailing consecutive late days ($0, 1,$ or $2$).

### 2. Transition Recurrence:
At state $(i, j, k)$:
1. Append `'P'`: Late streak resets to $0$.
   $$
   \text{Next: } (i + 1, \; j, \; 0)
   $$
2. Append `'A'` (only legal if $j == 0$): Late streak resets to $0$, absences become $1$.
   $$
   \text{Next: } (i + 1, \; 1, \; 0)
   $$
3. Append `'L'` (only legal if $k < 2$): Late streak increments.
   $$
   \text{Next: } (i + 1, \; j, \; k + 1)
   $$
4. Base case: If $i == n$, return $1$.

### 3. Modulo Invariant:
All intermediate sums must be evaluated modulo $M = 10^9 + 7$:
$$
ans \leftarrow (ans_P + ans_A + ans_L) \pmod{10^9 + 7}
$$

> **Equivalence Class Invariant.** Any attendance prefix is uniquely summarized by its absence count $j \in \{0, 1\}$ and its tail late streak $k \in \{0, 1, 2\}$, compressing $3^i$ paths into 6 equivalence classes.

---

## 3. Step-by-Step Worked Execution

We trace $n = 2$ using top-down memoized recursion:

---

### Step 1: Base Cases ($i = 2$)
Any state reaching $i = 2$ with valid $(j, k)$ returns $1$.

---

### Step 2: Solve $i = 1$ States
- $dfs(1, 0, 0)$ (`"P"`):
  - Add `'P'`: $dfs(2, 0, 0) = 1$
  - Add `'A'`: $dfs(2, 1, 0) = 1$
  - Add `'L'`: $dfs(2, 0, 1) = 1$
  - Total: $1 + 1 + 1 = \mathbf{3}$.
- $dfs(1, 0, 1)$ (`"L"`):
  - Add `'P'`: $dfs(2, 0, 0) = 1$
  - Add `'A'`: $dfs(2, 1, 0) = 1$
  - Add `'L'`: $dfs(2, 0, 2) = 1$
  - Total: $1 + 1 + 1 = \mathbf{3}$.
- $dfs(1, 1, 0)$ (`"A"`):
  - Add `'P'`: $dfs(2, 1, 0) = 1$
  - Add `'A'`: Cannot add `'A'` ($j = 1$).
  - Add `'L'`: $dfs(2, 1, 1) = 1$
  - Total: $1 + 0 + 1 = \mathbf{2}$.

---

### Step 3: Solve Root State $dfs(0, 0, 0)$
At day $0$:
- Add `'P'`: $dfs(1, 0, 0) = 3$
- Add `'A'`: $dfs(1, 1, 0) = 2$
- Add `'L'`: $dfs(1, 0, 1) = 3$
Total combinations:
$$
3 + 2 + 3 = \mathbf{8}
$$

---

### Step 4: Final Output
$$
ans = \mathbf{8}
$$

---

## 4. Complete Execution Trace

| Day Step $i$ | State $(j, k)$ | Options Available | Child States Invoked | Sum of Valid Subpaths |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | $(0, 0)$ | `'P'`, `'A'`, `'L'` | $(2, 0, 0), (2, 1, 0), (2, 0, 1)$ | $1 + 1 + 1 = 3$ |
| $1$ | $(0, 1)$ | `'P'`, `'A'`, `'L'` | $(2, 0, 0), (2, 1, 0), (2, 0, 2)$ | $1 + 1 + 1 = 3$ |
| $1$ | $(1, 0)$ | `'P'`, `'L'` (no `'A'`) | $(2, 1, 0), (2, 1, 1)$ | $1 + 1 = 2$ |
| **$0$** | **$(0, 0)$** | `'P'`, `'A'`, `'L'` | **$(1, 0, 0), (1, 1, 0), (1, 0, 1)$** | **$3 + 2 + 3 = \mathbf{8}$** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$:** States $(1, 0, 0) + (1, 1, 0) + (1, 0, 1) = 1 + 1 + 1 = \mathbf{3}$ (`"P"`, `"A"`, `"L"`).
- **Large $n = 10^5$:** Standard recursion with caching visits $6 \times 10^5$ states, completing in $< 100$ ms.
- **Consecutive Late Limit:** When $k = 2$, adding another `'L'` is forbidden, preventing any sequence from generating `"LLL"`.

---

## 6. Traps & Common Anti-Patterns

- **Resetting Absence Count on Present Days:** Absences `'A'` are global across all $n$ days; $j$ can never decrease. Only late streaks $k$ reset on non-`'L'` days.
- **Forgetting Modulo During Intermediate Additions:** In languages with fixed integer sizes, summing three large DP values without modulo overflows 32-bit or 64-bit integers. Modulo must be applied at every addition.
- **Using 3D Array without Cache Cleansing:** Leaving large cache dictionaries alive between test cases exhausts heap memory. Explicitly clearing caches via `dfs.cache_clear()` preserves memory integrity.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Number of distinct states: $n \times 2 \times 3 = 6n$.
  - Each state performs at most 3 transitions taking $O(1)$ operations each.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^5$, $6 \times 10^5$ operations complete in $< 120$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory to store the recursion stack and memoization cache table.