# Guided Example: Maximum Points After Enemy Battles

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"enemyEnergies": [3, 2, 2], "currentEnergy": 2}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `enemyEnergies` denoting the energy values of various enemies.

The objective is to compute `3` from `{"enemyEnergies": [3, 2, 2], "currentEnergy": 2}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate the repeatable action from the one-time sacrifice.** Gaining a point by fighting an unmarked enemy spends that enemy's energy value but does not mark the enemy. The same unmarked enemy can therefore be used repeatedly for points. The other operation marks an enemy and adds its energy to the current pool; it is a one-time sacrifice, available after at least one point has been earned. Points are not spent by that sacrifice.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"enemyEnergies": [3, 2, 2], "currentEnergy": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

To maximize how many point operations a fixed amount of energy can buy, repeatedly fight an enemy of minimum energy cost. Any point bought from a more expensive enemy could be replaced by a minimum-cost fight, earning the same one point while leaving at least as much energy for the future.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The code sorts `enemyEnergies`, making `enemyEnergies[0]` the minimum $m$. That minimum enemy is kept unmarked while other enemies are converted into energy.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"enemyEnergies": [3, 2, 2], "currentEnergy": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Linear formula:** Find `m = min(enemyEnergies)` and `total = sum(enemyEnergies)` in one pass. Return zero if initial energy is below $m$; otherwise return `(currentEnergy + total - m) // m`. This is $O(n)$ time and $O(1)$ space and matches the manifest.
- **Priority-based simulation:** A min-heap for fights and max-heap for sacrifices resembles other token problems, but repeated fights and nondecreasing points make full heap machinery unnecessary.
- **Fight a more expensive enemy:** It earns the same one point while spending more energy, so replacing it with a minimum-enemy fight never worsens a strategy.
- **Initial energy below the minimum:** No point can be obtained, so the sacrifice prerequisite can never be unlocked.
- **Initial energy equals the minimum:** Exactly one first point is available, which unlocks all one-time energy sacrifices.
- **Single enemy:** It can be fought repeatedly but should not be marked before point conversion. The quotient gives the exact answer.
- **Several minimum enemies:** One can stay repeatable while the others contribute their energy through marking.
- **Final energy remainder:** Any amount below $m$ cannot buy another point and may remain unused.
- **Points are never spent:** The “at least one point” condition is a permanent unlock after the first point, not a token cost for each sacrifice.
- **Last addition in the loop:** Adding `enemyEnergies[0]` after the final quotient is unused but does not corrupt the returned count.
- **Large values:** The total energy may exceed 32-bit range; Python handles it without overflow.
- **Input mutation:** Sorting permanently reorders `enemyEnergies`, including when the method returns zero immediately afterward.
- **Manifest mismatch:** The exact source is sort-based $O(n\log n)$ time with Python sorting workspace, while the formula alternative is the claimed linear constant-space method.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of enemies. The exact source sorts the list, which costs $O(n\log n)$ time. Its reverse loop has $n$ constant-time iterations, so sorting dominates. This contradicts the manifest's $O(n)$ time claim; a linear scan for the minimum and total sum would support that faster bound, but `solution.py` sorts.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
