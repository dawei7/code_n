# Guided Example: Beautiful Arrangement II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "k": 1}`
- **Required output:** `[1, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integers `n` and `k`, construct a list `answer` that contains `n` different positive integers ranging from `1` to `n` and obeys the following requirement:

The objective is to compute `[1, 2, 3]` from `{"n": 3, "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Create large distinct differences first, then repeat one

The output must be a permutation of one through `n`, and adjacent absolute differences must contain exactly `k` distinct values.

Alternating between the smallest and largest unused numbers creates a predictable descending sequence of large differences. Once enough distinct differences have been created, consuming the remaining consecutive numbers from one side produces only difference one repeatedly.

The exact solution maintains the unused interval `[l, r]`, initially `[1, n]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The alternating first phase

For exactly `k` iterations:

- on even iteration `i`, append `l` and increment `l`;
- on odd iteration `i`, append `r` and decrement `r`.

The sequence begins:

`1, n, 2, n - 1, 3, n - 2, ...`.

Among these first `k` elements, adjacent differences are:

`n - 1, n - 2, n - 3, ..., n - k + 1`.

There are `k - 1` of these when `k > 1`, and they are all distinct.

Why does each decrease by one? The chosen low endpoint increases by one whenever it is used, and the chosen high endpoint decreases by one whenever it is used. The distance across the remaining interval therefore shrinks by exactly one on each alternating step.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The monotonic second phase

After `k` alternating choices, all unused values form one consecutive interval from `l` through `r`.

The direction used to consume that interval depends on the parity of `k`:

- if `k` is even, the last alternating value came from the high side, so append remaining values from `r` downward;
- if `k` is odd, the last alternating value came from the low side, so append remaining values from `l` upward.

The first tail value differs from the last alternating value by exactly one. Every later tail step also differs by one because it moves through consecutive integers.

Thus the entire second phase contributes only the distinct difference one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Increasing prefix plus alternating suffix:** Write `1` through `n - k - 1` in order, then alternate endpoints of the remaining `k + 1` values. This is the editorial construction and also gives `O(N)` time.
- **Backtracking over permutations:** It can test difference counts but has factorial search space and ignores the direct construction.
- **Random shuffling:** Finding a valid permutation by chance offers no guarantee and makes correctness difficult to prove.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. The two loops append exactly `n` values in total. Each iteration performs constant-time arithmetic and one list append, so running time is `O(N)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
