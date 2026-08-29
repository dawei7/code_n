# Guided Example: Maximum Units on a Truck

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"boxTypes": [[1, 3], [2, 2], [3, 1]], "truckSize": 4}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are assigned to put some amount of boxes onto **one truck**. You are given a 2D array `boxTypes`, where $\text{boxTypes}[i] = [\text{numberOfBoxes}_{i}, \text{numberOfUnitsPerBox}_{i}]$:

The objective is to compute `8` from `{"boxTypes": [[1, 3], [2, 2], [3, 1]], "truckSize": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each truck slot should receive the most valuable available box

Every box consumes exactly one unit of truck capacity, regardless of its type. The only quantity that differs is the number of units contributed by that box. Therefore, whenever capacity remains, taking a box with more units per box is never worse than taking one with fewer.

The source sorts `boxTypes` with `key=lambda x: -x[1]`. Negating the units-per-box value makes Python's ascending sort place larger original values first. The result is a new sorted list; the input `boxTypes` is not reordered by this call.

After sorting, a type represented by `[a, b]` has `a` available boxes and `b` units in each box. Types are visited from greatest `b` to least.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"boxTypes": [[1, 3], [2, 2], [3, 1]], "truckSize": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Take as many as capacity permits

For the current type, `min(truckSize, a)` is the number of boxes that can actually be loaded. If at least `a` slots remain, all boxes of the type are taken. If fewer slots remain, the truck takes only that remaining capacity and becomes full.

The contribution is

`b * min(truckSize, a)`,

which is added to `ans`. Multiplication is correct because every box within one type has the same unit count.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand the source's capacity update

After adding the correct number of units, the exact code executes `truckSize -= a`, subtracting the entire available batch count rather than the smaller number actually loaded.

When all `a` boxes fit, this is the ordinary remaining-capacity update. When only part of the batch fits, `truckSize` becomes zero or negative instead of exactly zero. The next condition `if truckSize <= 0: break` immediately stops, so that negative value is never used to load another type. The computed contribution already used the proper minimum, making this implementation detail harmless.

An alternative spelling could subtract `min(truckSize, a)` and stop at exactly zero, but that is not what this file does.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"boxTypes": [[1, 3], [2, 2], [3, 1]], "truckSize": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeatedly search for the best type:** Finding the maximum remaining units in a full scan can cost $O(t^2)$ across all types.
- **Max-heap of types:** Heapify by negative units and pop in priority order. It also works in $O(t\log t)$ time and $O(t)$ space.
- **Counting by unit value:** Because units per box are bounded by 1000, a frequency/count array can achieve $O(t+U)$ time, where $U$ is the value range.
- **Expand every box:** Sorting individual boxes can require space and time proportional to the total number of boxes and is unnecessary.
- **Truck fits all boxes:** Every type is processed and all units are included, even though `truckSize` remains positive.
- **Partial final type:** The contribution uses `min`, and the subsequent negative capacity triggers immediate termination.
- **Capacity filled exactly:** Subtracting the batch makes `truckSize == 0` and the loop breaks.
- **One type:** Load the smaller of its count and capacity.
- **Equal unit values:** Any order among tied types produces the same answer.
- **Large truck capacity:** Runtime does not depend on iterating individual slots.
- **Positive unit guarantee:** Taking another available box never reduces the objective.
- **Input preservation:** `sorted` returns a new outer list; it does not reorder `boxTypes`.
- **Capacity variable after partial load:** Its negative value is internal control state only and does not represent an actual negative number of slots.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(t\log t)$. Let $t$ be the number of box types. Sorting takes $O(t\log t)$ time. The loop visits at most all $t$ types and performs constant work per type, adding $O(t)$. Total time is $O(t\log t)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(t)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
