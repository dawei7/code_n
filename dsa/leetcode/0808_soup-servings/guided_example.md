# Guided Example: Soup Servings

We trace the step-by-step stochastic 2-pot soup serving process, discrete 25 mL quantum scaling ($\lceil n / 25 \rceil$), 4-way uniform random branching ($p = 0.25$), absorbing boundary conditions (A first $\to 1.0$, tie $\to 0.5$, B first $\to 0.0$), expected drift asymmetry ($E[\Delta A] = 2.5 > E[\Delta B] = 1.5$), and large-$N$ asymptotic convergence saturation threshold ($n > 4800 \implies 1.0$) on representative liquid volumes:

- **Input:** $n = 50$
- **Required output:** `0.625`
  - Stochastic serving operations:
    - We begin with $n$ mL of Soup A and $n$ mL of Soup B.
    - At each step, one of four serving operations is chosen with equal probability $p = 0.25$:
      1. Operation 1: Serve $100$ mL of A, $0$ mL of B
      2. Operation 2: Serve $75$ mL of A, $25$ mL of B
      3. Operation 3: Serve $50$ mL of A, $50$ mL of B
      4. Operation 4: Serve $25$ mL of A, $75$ mL of B
    - If a pot has less than the requested amount, whatever remains is served, emptying that pot.
    - Objective: Calculate the probability that **Soup A empties first**, plus **half** the probability that both pots empty simultaneously:
      $$
      P = P(\text{A empties before B}) + 0.5 \times P(\text{A and B empty together})
      $$
    - For $n = 50$ mL:
      - Scale in 25 mL increments: $50 / 25 = 2$ units for each pot.
      - After 1 turn:
        - Operation 1 (4 A, 0 B): A loses 4 (empties), B loses 0 $\implies$ A empty first ($1.0$).
        - Operation 2 (3 A, 1 B): A loses 3 (empties), B loses 1 $\implies$ A empty first ($1.0$).
        - Operation 3 (2 A, 2 B): A loses 2 (empties), B loses 2 (empties) $\implies$ Both empty together ($0.5$).
        - Operation 4 (1 A, 3 B): A loses 1, B loses 3 (empties) $\implies$ B empty first ($0.0$).
      - Weighted expectation:
        $$
        0.25 \times (1.0 + 1.0 + 0.5 + 0.0) = 0.25 \times 2.5 = \mathbf{0.625}
        $$
- **25 mL Scaling & Markov Drift Invariant:**
  - **Quantum Simplification:**
    - Because all operations are multiples of 25 mL, normalize units:
      $$
      N = \left\lceil \frac{n}{25} \right\rceil = \left\lfloor \frac{n + 24}{25} \right\rfloor
      $$
    - Operations in normalized units $(a, b)$:
      - Op 1: $(-4, \; 0)$
      - Op 2: $(-3, \; -1)$
      - Op 3: $(-2, \; -2)$
      - Op 4: $(-1, \; -3)$
  - **Absorbing Boundary States ($dfs(i, j)$):**
    - State $(i, j)$ represents $i$ units of A and $j$ units of B remaining:
      1. Both empty ($i \le 0 \land j \le 0$): Return $0.5$.
      2. A empty first ($i \le 0 \land j > 0$): Return $1.0$.
      3. B empty first ($i > 0 \land j \le 0$): Return $0.0$.
      4. General recurrence:
         $$
         dfs(i, j) = 0.25 \times \Big( dfs(i - 4, j) + dfs(i - 3, j - 1) + dfs(i - 2, j - 2) + dfs(i - 1, j - 3) \Big)
         $$
  - **The Drift Asymmetry & Asymptotic Saturation:**
    - Calculate expected consumption per turn:
      $$
      E[\Delta A] = \frac{4 + 3 + 2 + 1}{4} = \mathbf{2.5} \text{ units}
      $$
      $$
      E[\Delta B] = \frac{0 + 1 + 2 + 3}{4} = \mathbf{1.5} \text{ units}
      $$
    - Soup A is consumed on average $2.5 / 1.5 = 1.67\times$ faster than Soup B!
    - By the Law of Large Numbers, the probability of A emptying first approaches $1.0$ exponentially.
    - When $n > 4800$ ($N > 192$ units), the probability $P$ satisfies $1.0 - P < 10^{-5}$.
    - Thus, for $n > 4800$, we immediately return $1.0$ without simulation!
- **Step-by-Step Worked Execution Trace on $n = 50$ ($N = 2$):**
  - State evaluated: $dfs(2, 2)$.
  - **Branch 1 (Op 1: Consume 4 A, 0 B):**
    - Transition: $(2 - 4, \; 2) = (-2, \; 2)$.
    - Boundary check: $i = -2 \le 0$ and $j = 2 > 0 \implies \mathbf{A\ Empties\ First!}$
    - Payoff:
      $$
      P_1 = \mathbf{1.0}
      $$
  - **Branch 2 (Op 2: Consume 3 A, 1 B):**
    - Transition: $(2 - 3, \; 2 - 1) = (-1, \; 1)$.
    - Boundary check: $i = -1 \le 0$ and $j = 1 > 0 \implies \mathbf{A\ Empties\ First!}$
    - Payoff:
      $$
      P_2 = \mathbf{1.0}
      $$
  - **Branch 3 (Op 3: Consume 2 A, 2 B):**
    - Transition: $(2 - 2, \; 2 - 2) = (0, \; 0)$.
    - Boundary check: $i = 0 \le 0$ and $j = 0 \le 0 \implies \mathbf{Simultaneous\ Empty!}$
    - Payoff:
      $$
      P_3 = \mathbf{0.5}
      $$
  - **Branch 4 (Op 4: Consume 1 A, 3 B):**
    - Transition: $(2 - 1, \; 2 - 3) = (1, \; -1)$.
    - Boundary check: $i = 1 > 0$ and $j = -1 \le 0 \implies \mathbf{B\ Empties\ First!}$
    - Payoff:
      $$
      P_4 = \mathbf{0.0}
      $$
  - **Expectation Calculation:**
    $$
    dfs(2, 2) = 0.25 \times (P_1 + P_2 + P_3 + P_4) = 0.25 \times (1.0 + 1.0 + 0.5 + 0.0)
    $$
    $$
    dfs(2, 2) = 0.25 \times 2.5 = \mathbf{0.625}
    $$
- **Deeper 4-Unit State Trace ($n = 100 \implies N = 4$):**
  - Recursion descends 2 levels deep.
  - Op 1 reaches $(-0, 4) \to 1.0$.
  - Op 2 reaches $(1, 3)$ which recurses further.
  - Aggregated weighted sum:
    $$
    ans = \mathbf{0.71875}
    $$
- **Asymptotic Threshold Cutoff Trace ($n = 5000$):**
  - $n = 5000 > 4800$.
  - Threshold guard returns **`1.0`** immediately in $\mathcal{O}(1)$ time!

This instance demonstrates 2D discrete random walks with asymmetric drift and absorbing boundaries, mathematically proves why central limit drift dominance enables asymptotic truncation of infinite half-plane Markov chains, and derives $O(M^2)$ runtime (where $M \le 200$) and $O(M^2)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given $n$ mL of Soup A and Soup B:
Four operations each serve combinations of A and B with $p = 0.25$.
Find probability A empties first $+ 0.5 \times$ probability both empty together.

```text
n = 50 mL -> Scale by 25 mL -> 2 units of A, 2 units of B.

4 equal operations from (2, 2):
  1. (-4,  0) -> (-2,  2): A empties first -> 1.0
  2. (-3, -1) -> (-1,  1): A empties first -> 1.0
  3. (-2, -2) -> ( 0,  0): Both empty!    -> 0.5
  4. (-1, -3) -> ( 1, -1): B empties first -> 0.0

Average = 0.25 * (1.0 + 1.0 + 0.5 + 0.0) = 0.625
Result: 0.625
```

### The Invariant of Asymmetric Drift Convergence
- A loses 2.5 units on average; B loses 1.5 units on average.
- Because A empties much faster, the probability converges to 1.0 very rapidly.
- For $n > 4800$, return 1.0 immediately; for $n \le 4800$, memoized DFS takes $< 5$ ms.

---

## 2. Conceptual Foundation & Invariants

### 1. Absorbing Boundary Values:
$$
dfs(i, j) = \begin{cases}
0.5 & i \le 0 \land j \le 0 \\
1.0 & i \le 0 \land j > 0 \\
0.0 & i > 0 \land j \le 0
\end{cases}
$$

### 2. Markov Expectation Step:
$$
dfs(i, j) = 0.25 \sum_{(da, db) \in \{(4,0), (3,1), (2,2), (1,3)\}} dfs(i - da, \; j - db)
$$
$$
n > 4800 \implies \text{return } 1.0
$$

> **Random Walk Drift Invariant.** The discrete Markov chain $(X_t, Y_t)$ on $\mathbb{Z}_{\le 0}^2$ has drift vector $\mu = (-2.5, -1.5)$. The probability of hitting the horizontal boundary $\{X \le 0, Y > 0\}$ converges exponentially to 1 as the initial distance $N \to \infty$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 50$ ($N = 2$ units):

---

### Step 1: Op 1 (Serve 4 A, 0 B)
- Reaches $(-2, 2) \implies$ A empty $\implies 1.0$.

---

### Step 2: Op 2 (Serve 3 A, 1 B)
- Reaches $(-1, 1) \implies$ A empty $\implies 1.0$.

---

### Step 3: Op 3 (Serve 2 A, 2 B)
- Reaches $(0, 0) \implies$ Tie $\implies 0.5$.

---

### Step 4: Op 4 (Serve 1 A, 3 B)
- Reaches $(1, -1) \implies$ B empty $\implies 0.0$.

---

### Step 5: Output
- $0.25 \times (1.0 + 1.0 + 0.5 + 0.0) = \mathbf{0.625}$.

---

## 4. Complete Execution Trace

| Branch Operation | Units Served $(A, B)$ | Resulting State $(i', j')$ | Absorbing Condition | Branch Payoff | Probability Weight |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Op 1 | $(4, 0)$ | $(-2, 2)$ | A empty first ($i \le 0$) | $1.0$ | $0.25$ |
| Op 2 | $(3, 1)$ | $(-1, 1)$ | A empty first ($i \le 0$) | $1.0$ | $0.25$ |
| Op 3 | $(2, 2)$ | $(0, 0)$ | Both empty ($i \le 0, j \le 0$) | $0.5$ | $0.25$ |
| **Op 4** | **$(1, 3)$** | **$(1, -1)$** | **B empty first ($j \le 0$)** | **$0.0$** | **$0.25$** |
| **Weighted Total** | — | — | — | **`0.625`** | **`1.0`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 0$:** Both pots start empty $\implies 0.5$.
- **Large Values ($n = 10^9$):** Cutoff $n > 4800$ returns 1.0 without computing millions of states.
- **Tied Residuals:** When both pots reach $\le 0$ in the same step, return 0.5 (must check $i \le 0 \land j \le 0$ before checking $i \le 0$).
- **Scaling Offsets:** $(n + 24) // 25$ properly handles non-multiples of 25 (e.g. $n = 26 \implies 2$ units).

---

## 6. Traps & Common Anti-Patterns

- **Checking Single-Pot Emptying Before Both-Pot Emptying:** If you check `if i <= 0: return 1.0` before checking `if i <= 0 and j <= 0: return 0.5`, ties will be falsely rewarded with 1.0! The dual-empty check must come first.
- **Simulating Without Memoization:** Branching factor of 4 without `@cache` leads to $4^{n/25}$ exponential explosion.
- **Simulating Beyond $n = 4800$:** For $n = 10^9$, memory and time will be exceeded. Recognizing the drift asymmetry allows capping $N \le 200$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - If $n > 4800$: $\mathcal{O}(1)$.
  - If $n \le 4800$: state space has size at most $200 \times 200 = 40,000$ states.
  - Each state transitions in $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(1)$ (bounded by $\approx 4 \times 10^4$ operations). Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ memory (at most $200 \times 200$ floats cached in memory).
