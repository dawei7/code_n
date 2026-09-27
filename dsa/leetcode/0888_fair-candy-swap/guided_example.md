# Guided Example: Fair Candy Swap

We trace the step-by-step global sum balance equation, algebraic target difference derivation $\Delta = \frac{S_A - S_B}{2}$, hash set membership matching, and reciprocal exchange pair identification on representative candy box inventories:

- **Input:**
  $$
  aliceSizes = [1, 1], \quad bobSizes = [2, 2]
  $$
- **Required output:** `[1, 2]`
  - Candy swap exchange rules:
    - Alice has candy boxes of sizes $aliceSizes$, and Bob has candy boxes of sizes $bobSizes$.
    - They want to exchange **exactly one box each** so that after the exchange, they both have the **exact same total amount of candy**.
    - Return an integer array $[a, b]$ where $a$ is the box size Alice gives, and $b$ is the box size Bob gives.
    - For $aliceSizes = [1, 1]$ and $bobSizes = [2, 2]$:
      - Alice's initial sum: $S_A = 1 + 1 = 2$.
      - Bob's initial sum: $S_B = 2 + 2 = 4$.
      - If Alice gives $a = 1$ and Bob gives $b = 2$:
        - Alice's new total: $2 - 1 + 2 = 3$.
        - Bob's new total: $4 - 2 + 1 = 3$.
      - Both totals are equal ($3 == 3$)!
      - Result: **`[1, 2]`**.
- **The Algebraic Parity & Balance Equation Invariant:**
  - **The Conservation Recurrence:**
    - Let $S_A = \sum aliceSizes$ and $S_B = \sum bobSizes$.
    - If Alice trades box $a$ for box $b$:
      $$
      \text{Alice's final sum} = S_A - a + b
      $$
      $$
      \text{Bob's final sum} = S_B - b + a
      $$
    - Equating the two final sums:
      $$
      S_A - a + b = S_B - b + a
      $$
    - Regrouping terms:
      $$
      2a - 2b = S_A - S_B \iff a - b = \frac{S_A - S_B}{2}
      $$
    - Defining the constant required difference:
      $$
      \Delta = \frac{S_A - S_B}{2}
      $$
    - This establishes that for **any candidate box $a$ from Alice**, the exact matching box $b$ from Bob must satisfy:
      $$
      b = a - \Delta
      $$
  - **Hash Set $\mathcal{O}(1)$ Membership Lookup:**
    - We precompute the set of unique box sizes owned by Bob: $S = \text{set}(bobSizes)$.
    - We iterate through each $a \in aliceSizes$:
      - Compute required partner $b = a - \Delta$.
      - If $b \in S$, we have discovered the guaranteed exchange pair $[a, b]$!

---

## 1. Instance & Teaching Goal

Given $aliceSizes = [1, 1]$ and $bobSizes = [2, 2]$, derive the balance condition and find the matching pair.

```text
Initial State:
  Alice Total (S_A) = 1 + 1 = 2
  Bob Total (S_B)   = 2 + 2 = 4
  Target Equal Total = (2 + 4) / 2 = 3

Required Offset:
  Delta = (S_A - S_B) / 2 = (2 - 4) / 2 = -1

Matching Rule:
  For any box 'a' from Alice, Bob must provide b = a - (-1) = a + 1

Candidate Evaluation:
  Alice has box a = 1.
  Required b = 1 + 1 = 2.
  Does Bob have box 2? Yes!

Valid Swap: [1, 2]
```

The teaching goal is to demonstrate how converting a two-variable equation into an offset lookup reduces a quadratic search into a linear-time set probe.

---

## 2. Conceptual Foundation & Invariants

### 1. Global Conservation Metric:
$$
\text{Total Candy} = S_A + S_B
$$
$$
\text{Fair Share} = \frac{S_A + S_B}{2}
$$

### 2. Pairwise Balance Invariant:
$$
\Delta = \frac{S_A - S_B}{2}
$$
$$
b^*(a) = a - \Delta
$$
The problem guarantees at least one valid answer exists.

---

## 3. Step-by-Step Worked Execution

We trace $aliceSizes = [1, 1], bobSizes = [2, 2]$:

---

### Step 1: Compute Initial Sums and Difference
- Compute $S_A$:
  $$
  S_A = 1 + 1 = 2
  $$
- Compute $S_B$:
  $$
  S_B = 2 + 2 = 4
  $$
- Compute target offset $\Delta$:
  $$
  \Delta = \frac{S_A - S_B}{2} = \frac{2 - 4}{2} = \mathbf{-1}
  $$

---

### Step 2: Construct Bob's Hash Set
- Insert all items of $bobSizes$ into hash set $S$:
  $$
  S = \{2\}
  $$

---

### Step 3: Test Alice's Boxes
- **Inspect first box $a = 1$:**
  - Compute required $b$:
    $$
    b = a - \Delta = 1 - (-1) = 1 + 1 = \mathbf{2}
    $$
  - Query hash set $S$:
    $$
    2 \in S \implies \mathbf{Match\ Found!}
    $$
  - Return pair immediately: $[1, 2]$.

---

### Verification:
- Alice gives $1$, receives $2$: $2 - 1 + 2 = 3$.
- Bob gives $2$, receives $1$: $4 - 2 + 1 = 3$.
- Balanced at $3 == 3$.
- **Output:** **`[1, 2]`**.

---

## 4. Complete Execution Trace

| Step | Entity Evaluated | Value | Formula / Relationship | Result |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | Alice Sum $S_A$ | $2$ | $\sum aliceSizes$ | $2$ |
| $2$ | Bob Sum $S_B$ | $4$ | $\sum bobSizes$ | $4$ |
| $3$ | Difference $\Delta$ | $-1$ | $(S_A - S_B) / 2$ | $-1$ |
| $4$ | Bob Hash Set $S$ | $\{2\}$ | $\text{set}(bobSizes)$ | Ready |
| $5$ | Alice Box $a$ | $1$ | First element of $aliceSizes$ | $a = 1$ |
| $6$ | Target $b$ | $2$ | $b = a - \Delta = 1 - (-1)$ | $b = 2$ |
| **$7$** | **Membership Check** | **`2 in S`** | **Set lookup in $\{2\}$** | **`True -> Return [1, 2]`** |

---

## 5. Boundary Cases & Failure Modes

- **$S_A > S_B$ (e.g. Alice has more):** $\Delta > 0 \implies b = a - \Delta < a$, so Alice gives a larger box and receives a smaller box.
- **$S_A < S_B$ (e.g. Bob has more):** $\Delta < 0 \implies b = a - \Delta > a$, so Alice gives a smaller box and receives a larger box.
- **Duplicate Elements:** Handled naturally by set deduplication without altering validity.

---

## 6. Traps & Common Anti-Patterns

- **Nested Loops ($\mathcal{O}(N_A \cdot N_B)$):** Testing all pairs $(a, b)$ with nested loops takes quadratic time, causing TLE on arrays of length $10^5$. Hash set lookup reduces time to $\mathcal{O}(N_A + N_B)$.
- **Integer Truncation on Odd Sums:** The problem guarantees a fair swap exists, meaning $S_A - S_B$ is always an even integer, so division by 2 is exact.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Summing $aliceSizes$ and $bobSizes$: $\mathcal{O}(N_A + N_B)$.
  - Creating hash set of $bobSizes$: $\mathcal{O}(N_B)$.
  - Iterating through $aliceSizes$ with $\mathcal{O}(1)$ hash set lookups: $\mathcal{O}(N_A)$.
  - Total Time: strictly $\mathcal{O}(N_A + N_B)$, executing in $< 5$ ms for $10^5$ items.
- **Auxiliary Space Complexity:**
  - Hash set storing unique values of $bobSizes$: $\mathcal{O}(N_B)$ space.