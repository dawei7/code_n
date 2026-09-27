# Guided Example: Poor Pigs

We trace the step-by-step Information Theory encoding, round-to-state base transformation ($B = \lfloor \frac{\text{test}}{\text{die}} \rfloor + 1$), multi-dimensional coordinate mapping ($B^p \ge \text{buckets}$), and information capacity scaling on representative testing setups:

- **Input:** $buckets = 1000, \quad minutesToDie = 15, \quad minutesToTest = 60$
- **Required output:** `5`
  - Step 1: Compute total testing rounds:
    $$
    R = \lfloor 60 / 15 \rfloor = 4 \text{ rounds}
    $$
  - Step 2: Determine distinguishable states per pig:
    - State 1: Pig dies in Round 1
    - State 2: Pig dies in Round 2
    - State 3: Pig dies in Round 3
    - State 4: Pig dies in Round 4
    - State 5: Pig survives all 4 rounds
    - Total states per pig: $B = R + 1 = 4 + 1 = \mathbf{5}$
  - Step 3: Compute required dimensions (pigs $p$):
    - Each pig acts as one digit in base $5$.
    - With $p$ pigs, total distinguishable buckets is $5^p$:
      - $p = 1: 5^1 = 5 < 1000$
      - $p = 2: 5^2 = 25 < 1000$
      - $p = 3: 5^3 = 125 < 1000$
      - $p = 4: 5^4 = 625 < 1000$
      - $p = 5: 5^5 = 3125 \ge 1000$
    - Smallest integer $p$ with $5^p \ge 1000$ is $p = \mathbf{5}$.
- **One-Round Instance:** $buckets = 4, minutesToDie = 15, minutesToTest = 15$
  - Rounds: $R = 1 \implies B = 1 + 1 = 2$ states (dead or alive).
  - Capacity: $2^p \ge 4 \implies p = \mathbf{2}$ pigs.
  - 2D grid test: Arrange buckets into a $2 \times 2$ matrix $[(0, 0), (0, 1), (1, 0), (1, 1)]$.
    - Pig 1 drinks Row 0; Pig 2 drinks Column 0.
    - If both die $\implies (0, 0)$. If Pig 1 dies $\implies (0, 1)$. If Pig 2 dies $\implies (1, 0)$. If neither dies $\implies (1, 1)$.
- **Single Bucket ($buckets = 1$):** $B^0 = 1 \ge 1 \implies \mathbf{0}$ pigs needed (bucket is known a priori).

This instance demonstrates Shannon entropy and multi-dimensional state coordinates, mathematically proves the necessary and sufficient conditions for uniquely identifying the poison bucket, and derives $O(\log_{B} (\text{buckets}))$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given $buckets = 1000$, $minutesToDie = 15$, and $minutesToTest = 60$:
Exactly one bucket contains poison; all others contain water.
When a pig drinks poison, it dies in 15 minutes.
You can perform simultaneous or sequential tests within the total 60-minute window.
Find the **minimum number of pigs** needed to figure out which bucket contains poison.

```text
Time Analysis:
  Total Testing Window: 60 minutes
  Time Required per Test: 15 minutes
  Total Possible Sequential Rounds: 60 / 15 = 4 rounds

States of a Single Pig:
  - Dies in Round 1
  - Dies in Round 2
  - Dies in Round 3
  - Dies in Round 4
  - Survives All Rounds
  Total Distinguishable Outcomes: 4 + 1 = 5 states (Base 5)
```

### The Multi-Dimensional Information Theory Perspective
A naive sequential strategy uses 1 pig and tests 1 bucket per round, which only tests 4 buckets.
However, pigs can drink mixtures from multiple buckets simultaneously!
- In information theory, determining 1 item out of $N$ requires $\log_2(N)$ bits of information.
- A pig does not merely produce a binary result (alive/dead). Because there are $R$ rounds, a pig can die at Round 1, Round 2, ..., Round $R$, or survive.
- Thus, each pig provides $\log_2(R + 1)$ bits of information, representing a single digit in **base $B = R + 1$**.
- $p$ pigs can address $B^p$ unique coordinates in a $p$-dimensional discrete space.

---

## 2. Conceptual Foundation & Invariants

### 1. Base Dimension Formula:
The maximum number of sequential testing rounds is:
$$
R = \left\lfloor \frac{\text{minutesToTest}}{\text{minutesToDie}} \right\rfloor
$$
Each pig yields exactly $B = R + 1$ mutually exclusive outcomes.

### 2. Multi-Dimensional Hypercube Encoding:
Every bucket is assigned a unique $p$-digit identifier in base $B$:
$$
\text{Bucket ID} = (d_0, d_1, \dots, d_{p-1}) \quad \text{where } d_k \in \{0, 1, \dots, R\}
$$
- Pig $k$ controls coordinate dimension $k$.
- In Round $r$ (where $r \in [0, R - 1]$):
  - Pig $k$ drinks from all buckets whose $k$-th coordinate is $d_k == r$.
- **Decoding Rule:**
  - If Pig $k$ dies in Round $r$, then the poison bucket's $k$-th digit must be $r$.
  - If Pig $k$ never dies, the poison bucket's $k$-th digit must be $R$ (the buckets Pig $k$ never drank from).
- Thus, the death timings of the $p$ pigs directly reveal the exact base-$B$ coordinates of the poisoned bucket!

### 3. Capacity Condition:
To uniquely identify any of the $buckets$ candidates:
$$
B^p \ge buckets \iff (R + 1)^p \ge buckets
$$
Solving for the minimal integer $p$:
$$
p = \lceil \log_{R + 1}(buckets) \rceil
$$

> **Information Invariant.** A system of $p$ pigs observing $R$ sequential test rounds has an information capacity of $(R + 1)^p$ discrete states, which is both mathematically necessary and physically sufficient to locate the poison bucket.

---

## 3. Step-by-Step Worked Execution

We trace $buckets = 1000, minutesToDie = 15, minutesToTest = 60$:

---

### Step 1: Compute Testing Rounds $R$ and Base $B$
- Available time: $60$ minutes.
- Poison duration: $15$ minutes.
- Total rounds:
  $$
  R = \lfloor 60 / 15 \rfloor = \mathbf{4}
  $$
- Distinguishable outcomes per pig:
  $$
  B = R + 1 = 4 + 1 = \mathbf{5}
  $$

---

### Step 2: Exponential Search for Dimension $p$
Compute capacity $5^p$ for increasing values of $p$:
- **$p = 0$:** $5^0 = 1 < 1000$
- **$p = 1$:** $5^1 = 5 < 1000$
- **$p = 2$:** $5^2 = 25 < 1000$
- **$p = 3$:** $5^3 = 125 < 1000$
- **$p = 4$:** $5^4 = 625 < 1000$
- **$p = 5$:** $5^5 = 3125 \ge 1000$ (**Capacity Condition Satisfied**)

---

### Step 3: Conclusion
With $p = 5$ pigs, their combined outcomes span $5^5 = 3125$ states, which strictly exceeds $1000$.
Minimum pigs needed: **`5`**.

---

## 4. Complete Execution Trace

| Number of Pigs $p$ | Base $B = R + 1$ | State Capacity $B^p$ | Target Buckets | Can Identify 1000? | Action |
|:---:|:---:|:---:|:---:|:---:|:---|
| **$0$** | $5$ | $1$ | $1000$ | No ($1 < 1000$) | Increment $p$ |
| **$1$** | $5$ | $5$ | $1000$ | No ($5 < 1000$) | Increment $p$ |
| **$2$** | $5$ | $25$ | $1000$ | No ($25 < 1000$) | Increment $p$ |
| **$3$** | $5$ | $125$ | $1000$ | No ($125 < 1000$) | Increment $p$ |
| **$4$** | $5$ | $625$ | $1000$ | No ($625 < 1000$) | Increment $p$ |
| **$5$** | $5$ | **$3125$** | $1000$ | **Yes ($3125 \ge 1000$)** | **Optimal $p = 5$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Bucket ($buckets = 1$):** Zero tests needed since the only bucket is guaranteed to be poisonous $\implies p = 0$.
- **Only One Round Allowed ($minutesToTest == minutesToDie$):** $R = 1 \implies B = 2$ (binary alive/dead). Problem reduces to standard binary search on bits: $2^p \ge buckets \implies p = \lceil \log_2(buckets) \rceil$.
- **Zero Rounds Allowed ($minutesToTest < minutesToDie$):** Cannot run even 1 round $\implies R = 0, B = 1$. Only $1^0 = 1$ bucket solvable.
- **Equal Capacity and Buckets ($buckets = 25, R = 4 \implies B = 5$):** $5^2 = 25 \ge 25 \implies p = 2$ exactly.

---

## 6. Traps & Common Anti-Patterns

- **Assuming Pigs Can Only Distinguish 2 States:** Treating pigs as purely binary (alive vs dead) ignores the temporal dimension. The round in which a pig dies conveys distinct information; $R$ rounds create $R + 1$ states, not 2.
- **Simulating Pig Drinking Schedules:** Building explicit schedules or matrix allocations is unnecessary. The answer is purely informational and determined by the base-$B$ logarithm.
- **Floating-Point Precision in `log()`:** In Python, computing `ceil(log(buckets, base))` can suffer from floating-point inaccuracies (e.g. `log(125, 5)` returning `3.0000000000000004` $\to 4$). An integer multiplication loop `while p < buckets: p *= base` avoids all floating-point roundoff issues.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Base determination takes $O(1)$ arithmetic time.
  - The multiplication loop iterates at most $\lceil \log_{B} (buckets) \rceil$ times.
  - For $buckets = 1000$ and $B = 5$, exactly 5 loop iterations occur.
  - Total Time: $\mathcal{O}(\log_{B} (\text{buckets})) = \mathcal{O}(1)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ using scalar integer registers.
