# Guided Example: Most Frequent Prime

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mat": [[1, 1], [9, 9], [1, 1]]}`
- **Required output:** `19`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a `m x n` **0-indexed **2D** **matrix `mat`. From every cell, you can create numbers in the following way:

The objective is to compute `19` from `{"mat": [[1, 1], [9, 9], [1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Core Step 1

**Enumerate every start and fixed direction.** From each matrix cell, the four nested loops choose direction components `a` and `b` from $-1,0,1$, excluding $(0,0)$. These are exactly the eight compass directions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mat": [[1, 1], [9, 9], [1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The source initializes `v` to the starting digit, then moves once before testing. Each while-loop step appends the new digit:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source initializes `v` to the starting digit, then moves... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Thus it generates every prefix of length at least two along that ray. Single-cell numbers are never tested, which is appropriate because every one-digit value is at most 9 and the result must be greater than 10.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `19` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mat": [[1, 1], [9, 9], [1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `19` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Memoize primality by value:** Repeated generat:** - **Memoize primality by value:** Repeated generated numbers could reuse one result, improving practical speed. The manifest describes this, but the exact source does not implement it.
- **Sieve:** The largest six-digit value is bounded, so a sieve is conceivable, but allocating through that entire range may be wasteful for few tested values.
- **Skip even divisors after testing 2:** It halves trial checks but does not change asymptotic complexity.
- **One-cell matrix:** No direction can take one step, the counter stays empty, and the result is $-1$ even if the digit itself is prime.
- **Direction cannot turn:** Coordinates always add the same $(a,b)$, enforcing the rule.
- **Repeated prime on many paths:** Every occurrence increments frequency.
- **Frequency tie:** The larger prime wins.
- **Composite values:** A divisor through the square root makes `all` false.
- **No qualifying prime:** The initialized answer $-1$ is returned.
- **Manifest mismatch:** There is no primality-result cache in this source.
- **Path prefixes, not only maximal rays:** Primality is checked after every appended digit. A prime such as 19 is counted even when the same ray continues to form 191; testing only the final value would omit required numbers.
- **Leading digit behavior:** Matrix digits range from 1 through 9, so generated decimal numbers never contain an artificial leading zero and numeric construction with multiplication by ten exactly matches digit concatenation.
- **Counter iteration order:** The final answer does not depend on dictionary order because frequency comparisons and explicit `max` tie handling fully determine the winner.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RCL\sqrt V)$. Let $R$ and $C$ be matrix dimensions, $L=\max(R,C)$ the maximum ray length, and $V$ the largest generated value. There are $8RC$ rays and at most $O(L)$ generated values per ray. Each trial-division test costs $O(\sqrt V)$ worst-case. Total time is
- **Auxiliary Space Complexity:** $O(RCL)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
