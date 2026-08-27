# Guided Example: Count the Number of Arrays with K Matching Adjacent Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "m": 2, "k": 1}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given three integers `n`, `m`, `k`. A **good array** `arr` of size `n` is defined as follows:

The objective is to compute `4` from `{"n": 3, "m": 2, "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

**Think about boundaries rather than individual array elements.** An array of length $n$ has exactly $n-1$ boundaries between adjacent positions. At each boundary, one of two events happens:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "m": 2, "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- the next value equals the previous value, so the boundary is a matching boundary;
- the next value differs, so the boundary starts a new constant-valued segment.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - the next value equals the previous value, so the boundary ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The problem requires exactly $k$ matching boundaries. Therefore, exactly

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "m": 2, "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Linear inverse-factorial precomputation:** Com:** - **Linear inverse-factorial precomputation:** Compute all factorials, find the inverse of the largest factorial with one modular exponentiation, and fill inverse factorials backward. This reduces startup to $O(M+\log P)$ while preserving $O(1)$ combination queries.
- **Multiplicative binomial coefficient:** Computing $\binom{n-1}{k}$ with $\min(k,n-1-k)$ numerator factors avoids global tables and uses $O(\min(k,n-1-k)+\log P)$ time. That resembles the manifest bound but is not the protected implementation.
- **Dynamic programming over positions and match counts:** A DP can track arrays ending with equal or changed boundaries, but it uses at least $O(nk)$ transitions without further algebra and obscures the direct combinatorial structure.
- **Single allowed value:** If `m == 1`, only the all-ones array exists. It has $n-1$ matching boundaries. The formula returns one when `k == n - 1` because the exponent is zero, and zero otherwise because a positive power of `m - 1` is zero.
- **Length one:** For `n == 1`, necessarily `k == 0`. There are no boundaries, and the formula becomes $\binom00m(m-1)^0=m$. Python's modular `pow` correctly treats the zero exponent as one.
- **All boundaries match:** When `k == n - 1`, the array is constant. There are exactly $m$ choices, which the formula gives because the exponent of $m-1$ is zero.
- **No boundaries match:** When `k == 0`, choose the first value in $m$ ways and each later value in $m-1$ ways, yielding $m(m-1)^{n-1}$.
- **Modulo division:** Dividing reduced factorial residues with `//` would be incorrect. Modular inverses are required because arithmetic is taking place in residues modulo a prime.
- **Global startup timing:** Importing the module performs all precomputation even if `countGoodArrays` is called only once. Complexity discussions and performance investigations should not silently exclude that work.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M\log P)$. Let $M=\texttt{mx}=100010$ and $P=10^9+7$.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
