# Guided Example: New 21 Game

We trace the step-by-step absorbing Markov chain state transitions, uniform discrete probability convolution ($\frac{1}{maxPts}$ per draw), stopping boundary condition ($i \ge k \implies \mathbb{I}[i \le n]$), suffix probability recurrence relation ($P(i) = P(i+1) + \frac{P(i+1) - P(i+maxPts+1)}{maxPts}$), sliding window expectation maintenance, and final game success probability derivation on representative game configurations:

- **Input:**
  $$
  n = 6, \quad k = 1, \quad maxPts = 10
  $$
- **Required output:** `0.6`
  - Game mechanics and stopping conditions:
    - Alice begins with $0$ points.
    - While her current score is strictly less than $k$ ($score < k$):
      - Alice draws an integer uniformly at random from the range $[1, maxPts]$.
      - Each integer in $\{1, 2, \dots, maxPts\}$ has equal probability $p = \frac{1}{maxPts}$.
      - The drawn integer is added to her score.
    - As soon as Alice's score reaches or exceeds $k$ ($score \ge k$), she stops drawing immediately.
    - Objective: Calculate the probability that Alice's final score is $\le n$.
    - For $n = 6, k = 1, maxPts = 10$:
      - Alice starts at 0 ($0 < 1$).
      - She takes exactly one draw from $[1, 10]$.
      - Since $k = 1$, every outcome in $[1, 10]$ is $\ge 1$, so the game terminates after this single draw!
      - Outcomes where score $\le n = 6$: $\{1, 2, 3, 4, 5, 6\}$ (6 outcomes).
      - Total possible outcomes: $10$.
      - Final probability:
        $$
        \frac{6}{10} = \mathbf{0.6}
        $$
- **Dynamic Programming & Sliding Window Invariant:**
  - **State Definition:**
    - Let $P(i)$ be the conditional probability that Alice finishes with a total score $\le n$, given that her current score is $i$.
  - **Absorbing Boundary States ($i \ge k$):**
    - Once $i \ge k$, no further draws are permitted. Alice's game has concluded:
      $$
      P(i) = \begin{cases}
      1.0 & k \le i \le n \\
      0.0 & i > n
      \end{cases}
      $$
  - **Active State Recurrence ($i < k$):**
    - Alice draws $d \in [1, maxPts]$ uniformly with probability $\frac{1}{maxPts}$:
      $$
      P(i) = \frac{1}{maxPts} \sum_{d = 1}^{maxPts} P(i + d)
      $$
  - **The Telescoping Sliding Difference Invariant:**
    - Comparing consecutive states $P(i)$ and $P(i+1)$:
      $$
      P(i) = \frac{1}{M} \Big( P(i+1) + P(i+2) + \dots + P(i+M) \Big)
      $$
      $$
      P(i+1) = \frac{1}{M} \Big( P(i+2) + P(i+3) + \dots + P(i+M+1) \Big)
      $$
    - Subtracting the two expressions cancels all intermediate terms $P(i+2) \dots P(i+M)$:
      $$
      P(i) - P(i+1) = \frac{P(i+1) - P(i+M+1)}{M}
      $$
    - Rearranging gives the constant-time backward step formula:
      $$
      P(i) = P(i+1) + \frac{P(i+1) - P(i + M + 1)}{M}
      $$
    - This recurrence computes each probability in strictly $\mathcal{O}(1)$ time without summing over $maxPts$ elements!
- **Step-by-Step Worked Execution Trace on $n = 6, k = 1, maxPts = 10$ ($M = 10$):**
  - Stopping threshold: $k = 1$. Success threshold: $n = 6$.
  - **Absorbing States ($i \ge 1$):**
    - For $i \in [1, 6]$: $P(i) = \mathbf{1.0}$ (scores $1, 2, 3, 4, 5, 6 \le 6$).
    - For $i \in [7, 11]$: $P(i) = \mathbf{0.0}$ (scores $7, 8, 9, 10, 11 > 6$).
  - **Target Initial State ($i = 0$):**
    - Since $i = 0 = k - 1$:
      - The window of next possible states is $[0 + 1, \; 0 + 10] = [1, 10]$.
      - Number of successful states in window: $\min(n - k + 1, M) = \min(6 - 1 + 1, 10) = \mathbf{6}$.
      - Probability:
        $$
        P(0) = \frac{6}{10} = \mathbf{0.6}
        $$
- **Step-by-Step Worked Execution Trace on Multi-Draw Game ($n = 3, k = 2, maxPts = 2$):**
  - $n = 3, k = 2, M = 2$.
  - Target: $P(0)$.
  - **Absorbing States ($i \ge 2$):**
    - $P(2) = 1.0$ ($2 \le 3$)
    - $P(3) = 1.0$ ($3 \le 3$)
    - $P(4) = 0.0$ ($4 > 3$)
    - $P(5) = 0.0$ ($5 > 3$)
  - **State $i = 1$ ($1 < 2$):**
    - Draws from 1 lead to $1 + 1 = 2$ and $1 + 2 = 3$.
    - $P(1) = \frac{P(2) + P(3)}{2} = \frac{1.0 + 1.0}{2} = \mathbf{1.0}$.
  - **State $i = 0$ ($0 < 2$):**
    - Using telescoping difference:
      $$
      P(0) = P(1) + \frac{P(1) - P(0 + 2 + 1)}{2} = 1.0 + \frac{1.0 - P(3)}{2} = 1.0 + \frac{1.0 - 1.0}{2} = \mathbf{1.0}
      $$
    - Indeed, starting at 0, draws are at most $2 + 2 = 4$; Alice stops at 2 or 3, both $\le 3$.
- **Certain Victory Boundary ($k == 0$ or $n \ge k + maxPts - 1$):**
  - If $k = 0$: Alice never draws $\implies$ score is $0 \le n \implies \mathbf{1.0}$.
  - If $n \ge k + maxPts - 1$: Alice stops at $< k$, so her max possible score is $k - 1 + maxPts \le n$. Alice can never exceed $n \implies \mathbf{1.0}$.

This instance demonstrates stochastic shortest path analysis on acyclic Markov chains and moving average filter inversion, mathematically proves why telescoping state differences reduce linear window summation to constant-time recurrence steps, and derives $O(K + maxPts)$ runtime and $O(K + maxPts)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Alice plays 21:
- Starts at 0 points.
- Draws $[1, maxPts]$ uniformly while $points < k$.
- Stops when $points \ge k$.
Find the probability that final score $\le n$.

```text
n = 6, k = 1, maxPts = 10

Alice draws once from [1, 10].
Draws <= 6: { 1, 2, 3, 4, 5, 6 } -> 6 outcomes
Total outcomes: 10
Probability = 6 / 10 = 0.6

Result: 0.6
```

### The Invariant of the Backward Moving Window
- For absorbing states ($i \ge k$):
  $$
  P(i) = 1.0 \text{ if } i \le n \text{ else } 0.0
  $$
- For active states ($i < k$):
  $$
  P(i) = \frac{1}{maxPts} \sum_{d=1}^{maxPts} P(i + d)
  $$
- Moving window difference:
  $$
  P(i) = P(i+1) + \frac{P(i+1) - P(i + maxPts + 1)}{maxPts}
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. Markov Transition Expectation:
$$
P(i) = \mathbb{E}_{d \sim \mathcal{U}[1, M]}[P(i + d)] = \frac{1}{M} \sum_{j = i + 1}^{i + M} P(j)
$$

### 2. Telescoping Recurrence:
$$
P(i) = P(i + 1) + \frac{P(i + 1) - P(i + M + 1)}{M}
$$
$$
P(k - 1) = \frac{\min(n - k + 1, M)}{M}
$$

> **Dirichlet Problem on Finite DAGs.** The boundary value problem on the integer line with absorbing states $X \ge k$ and constant transition kernel $\mathbb{P}(X_{t+1} - X_t = d) = \frac{1}{M}$ admits a unique harmonic continuation satisfying the discrete Poisson equation with zero boundary drift.

---

## 3. Step-by-Step Worked Execution

We trace $n = 6, k = 1, maxPts = 10$:

---

### Step 1: Absorbing States
- $i \in [1, 6] \implies P(i) = 1.0$.
- $i \in [7, 10] \implies P(i) = 0.0$.

---

### Step 2: Evaluate $P(0)$
- $i = 0 = k - 1$.
- $\min(6 - 1 + 1, 10) / 10 = 6 / 10 = \mathbf{0.6}$.

---

### Step 3: Output
$$
\mathbf{0.6}
$$

---

## 4. Complete Execution Trace

| State $i$ | State Nature | Transition / Window Range | Outcome / Computation | Value $P(i)$ |
|:---:|:---:|:---:|:---:|:---:|
| $i \ge 7$ | Absorbing (Loss) | None ($i > n$) | Terminal outcome $> 6$ | $0.0$ |
| $i \in [1, 6]$ | Absorbing (Win) | None ($k \le i \le n$) | Terminal outcome $\le 6$ | $1.0$ |
| **$i = 0$** | **Active Start** | **$[1, 10]$** | **$\frac{1}{10} \sum_{j=1}^6 1.0 = \frac{6}{10}$** | **`0.6`** |

---

## 5. Boundary Cases & Failure Modes

- **$k = 0$:** Alice stops immediately with 0 points $\le n \implies 1.0$.
- **$n \ge k + maxPts$:** Impossible to exceed $n$ under any circumstances $\implies 1.0$.
- **$n < k$:** Alice can never stop with $\le n$ points ($score \ge k > n$) $\implies 0.0$.
- **Floating Point Precision:** Backward DP maintains precision within $10^{-9}$, easily meeting the $10^{-5}$ contest requirement.

---

## 6. Traps & Common Anti-Patterns

- **Directly Summing $maxPts$ Elements Every Step ($O(K \cdot maxPts)$):** For $K, maxPts = 10,000$, this takes $10^8$ operations and times out. The telescoping recurrence computes each step in $O(1)$.
- **Forward DP vs Backward DP:** Forward DP computes probabilities of reaching points, requiring a second summation pass over $[k, n]$. Backward DP directly outputs $P(0)$ as the answer.
- **Off-By-One on Boundary Condition:** For $i \ge k$, $P(i)$ is 1 if and only if $i \le n$. Do not evaluate draws for $i \ge k$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - States range from $0$ up to $k + maxPts$.
  - Each state is computed in $\mathcal{O}(1)$ time via memoized recursion or loop.
  - Total Time: strictly linear $\mathcal{O}(K + maxPts)$ where $K, maxPts \le 10,000 \implies \le 2 \times 10^4$ operations. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K + maxPts)$ memory for the memoization cache / DP array.
