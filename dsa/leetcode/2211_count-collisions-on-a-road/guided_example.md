# Guided Example: Count Collisions on a Road

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"directions": "RLRSLL"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` cars on an infinitely long road. The cars are numbered from `0` to $n - 1$ from left to right and each car is present at a **unique** point.

The objective is to compute `5` from `{"directions": "RLRSLL"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Remove leading left-moving cars

`directions.lstrip("L")` removes only `L` characters from the beginning.

These cars have no car to their left. They all move left at the same speed, so cars behind them cannot catch them, and they never collide.

The stripping stops at the first `R` or `S`. A later `L` is not guaranteed to escape because a right-moving or stationary car lies somewhere to its left.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"directions": "RLRSLL"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Remove trailing right-moving cars

`rstrip("R")` then removes only `R` characters from the end of the already left-trimmed string.

These cars have no car to their right and move away forever at equal speed. A right-moving car earlier in the string is not stripped if some non-`R` car remains to its right and can eventually block it.

The resulting core `s` contains exactly the cars not eliminated by obvious outward escape.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `rstrip("R")` then removes only `R` characters from the end ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every moving car in the core collides

Consider an `R` inside `s`. Because all trailing `R` cars were removed, there is some `L` or `S` to its right. Moving toward a stationary car, an oncoming left car, or a stopped collision group eventually prevents this `R` from escaping; it collides.

Symmetrically, every `L` in the core has some `R` or `S` to its left because all leading `L` cars were removed. It eventually collides with a moving or stationary obstruction.

Stationary cars do not move, but they can become collision points for several incoming cars.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"directions": "RLRSLL"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **State simulation:** Track pending right-moving:** - **State simulation:** Track pending right-moving cars and stopped regions in one pass. It also runs in $O(n)$ time but uses more branching.
- **Two pointers without slicing:** Find the first non-`L` and last non-`R` indices, then count movers between them for constant extra space.
- **All `L`:** Every car escapes left; trimming leaves empty and returns zero.
- **All `R`:** Every car escapes right; trimming also leaves empty.
- **All `S`:** No moving car exists, so length minus stationary count is zero.
- **Head-on `RL`:** Both remain in the core, contributing two.
- **Moving into stationary `RS` or `SL`:** The one moving character contributes one.
- **Collision chain:** Each later incoming moving car contributes one when it hits the stopped group.
- **Leading stationary car:** It prevents following left-moving cars from escaping through it.
- **Trailing stationary car:** It prevents preceding right-moving cars from escaping.
- **Same-direction cars:** Equal speeds prevent catching, but an obstruction ahead can stop the whole sequence through successive collisions.
- **Empty core:** String methods and count handle it naturally.
- **Input preservation:** Stripping returns new strings; `directions` remains unchanged.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. `lstrip` scans a leading prefix, `rstrip` scans a trailing suffix of the intermediate string, and `count` scans the remaining core. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
