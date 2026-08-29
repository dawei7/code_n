# Guided Example: Super Washing Machines

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"machines": [1, 0, 5]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have `n` super washing machines on a line. Initially, each washing machine has some dresses or is empty.

The objective is to compute `3` from `{"machines": [1, 0, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

The final number of dresses in every machine is forced by conservation: moves only transfer dresses, so the total never changes. If there are `n` machines and total `D`, each must finish with `D / n` dresses.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"machines": [1, 0, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`divmod(sum(machines), n)` returns the quotient `k` and remainder `mod` together. If `mod != 0`, the total cannot be divided evenly among integer machine counts, so no sequence of moves can succeed and the method returns `-1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

When division is exact, `k` is the target dresses per machine.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"machines": [1, 0, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate individual moves:** Choosing transfers round by round creates a huge state space and obscures the closed-form bottlenecks. The prefix method derives the answer without constructing a schedule.
- **Use only maximum prefix imbalance:** This fails for `[0, 3, 0]`, where one machine must send twice but every boundary needs net flow only one.
- **Use only maximum local surplus:** This misses cases such as `[1, 0, 5]`, where several dresses must cross the same boundary over three moves.
- **Non-divisible total:** Return `-1` immediately because dresses cannot be split fractionally.
- **Already balanced:** Every normalized value and prefix is zero, so the answer remains zero.
- **One machine:** Its total is automatically divisible by one and it already equals the average, producing zero moves.
- **Deficit between two suppliers:** It may receive from both sides in one move, explaining why negative local imbalance is not converted with `abs`.
- **Large counts:** Python integers avoid overflow in totals and prefix balances; fixed-width languages should use a sufficiently wide type.
- **Final prefix:** It must be zero for feasible normalization, but the maximum earlier absolute prefix determines cross-boundary work.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Computing the sum scans $n$ values, and the main loop scans them once more. Each iteration performs constant arithmetic, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
