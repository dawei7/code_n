# Guided Example: Manhattan Distances of All Arrangements of Pieces

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"m": 2, "n": 2, "k": 2}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given three integers `m`, `n`, and `k`.

The objective is to compute `8` from `{"m": 2, "n": 2, "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

**Reverse the order of counting.** Directly enumerate arrangements, then every pair of pieces inside each arrangement, would be enormous. Instead, fix an unordered pair of grid cells first and ask how many arrangements contain pieces in both cells.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"m": 2, "n": 2, "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 4

be the number of cells. Once two distinct cells are fixed as occupied, the remaining $k-2$ identical pieces may occupy any $k-2$ cells among the other $N-2$. Therefore, every cell pair appears together in exactly

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"m": 2, "n": 2, "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate arrangements:** There are $\binom Nk$ of them, making direct generation infeasible even at the stated $N\le10^5$.
- **Enumerate all cell pairs explicitly:** This takes $O(N^2)$ time. Separating row and column distances gives closed forms.
- **Precompute factorials:** Factorial and inverse-factorial arrays answer combinations in $O(1)$ after $O(N)$ preprocessing but require $O(N)$ space. One binomial query does not need them.
- **Exactly two pieces:** `chosen = 0`, both products remain one, and the answer is simply the sum of distances over all cell pairs.
- **Every cell occupied:** The multiplicity is $\binom{N-2}{N-2}=1$; there is only one arrangement.
- **One row:** `row_distance` becomes zero and the column formula alone gives all distances.
- **One column:** The symmetric column contribution is zero and row distance remains.
- **Identical pieces:** Occupied cell subsets, not permutations of labeled pieces, are the valid arrangements.
- **Unordered pairs:** The distance formulas count each pair once. Multiplying by two would incorrectly treat the two piece orders as different.
- **Modular division:** Ordinary integer division of residues is invalid. Fermat inversion is safe because the denominator contains factors only below the prime modulus.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log P)$. Let $b=\min(k-2,N-k)$. The two distance formulas take $O(1)$ arithmetic operations. The multiplicative binomial loop runs $b$ times, and modular inversion takes $O(\log P)$ multiplications. Exact time is $O(b+\log P)$, which is $O(N)$ because $b\le N$ and $N=mn$. This supports the manifest's broader $O(N)$ bound.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
