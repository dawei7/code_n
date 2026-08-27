# Guided Example: Count Positions on Street With Required Brightness

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "lights": [[0, 1], [2, 1], [3, 2]], "requirement": [0, 2, 1, 4, 1]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`. A perfectly straight street is represented by a number line ranging from `0` to $n - 1$. You are given a 2D integer array `lights` representing the street lamp(s) on the street. Each $\text{lights}[i] = [\text{position}_{i}, \text{range}_{i}]$ indicates that there is a street lamp at position $\text{position}_{i}$ that lights up the area from $[max(0, \text{position}_{i} - \text{range}_{i}), min(n - 1, \text{position}_{i} + \text{range}_{i})]$ (**inclusive**).

The objective is to compute `4` from `{"n": 5, "lights": [[0, 1], [2, 1], [3, 2]], "requirement": [0, 2, 1, 4, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each lamp contributes one to an inclusive interval

A lamp at position `p` with range `r` illuminates from

`i = max(0, p - r)`

through

`j = min(n - 1, p + r)`,

including both endpoints. The brightness at a street position is the number of these intervals covering it.

Incrementing every position in every lamp interval would be too slow when both the street and number of lamps are large. The solution records only where each interval's contribution begins and where it stops, using a difference array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "lights": [[0, 1], [2, 1], [3, 2]], "requirement": [0, 2, 1, 4, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Represent an interval with two events

The list `d` has length `n + 1`. For one inclusive interval `[i, j]`, the code performs:

- `d[i] += 1` to begin one additional active lamp;
- `d[j + 1] -= 1` to end that contribution immediately after `j`.

When cumulative sums are later taken, the added one remains active from `i` through `j`. At `j + 1`, the subtraction cancels it.

The extra sentinel position at index `n` makes `j + 1` valid even when `j = n - 1`. Without that slot, a lamp reaching the street's final position would require a separate branch.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The list `d` has length `n + 1`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Clipping preserves the finite street

`max(0, p - r)` prevents a lamp's mathematical range from extending below position zero. `min(n - 1, p + r)` prevents it from extending beyond the last street position.

Only clipped endpoints create events. Light outside the represented street contributes to no requested brightness and should not occupy any array position.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "lights": [[0, 1], [2, 1], [3, 2]], "requirement": [0, 2, 1, 4, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Increment every illuminated position per lamp::** - **Increment every illuminated position per lamp:** This direct simulation can take `O(nm)` time when many lamps cover most of the street.
- **Sweep sorted interval endpoints:** A general event map can work, but positions are already a dense range from zero to `n - 1`, making an array simpler.
- **Segment tree:** Range additions and point queries are supported, but all updates occur before one full scan, so a difference array is lighter and faster.
- **Lamp with zero range:** It creates events at `p` and `p + 1` and contributes only at its own position.
- **Lamp covering the entire street:** Its clipped interval is `[0, n - 1]` and its negative event uses sentinel index `n`.
- **Position requirement zero:** It always passes, even with no covering lamp.
- **Brightness exactly equal to requirement:** `>=` includes the position.
- **Overlapping lamps:** Their event contributions add, producing the correct larger brightness.
- **Street length one:** Events use indices zero and one; `zip` evaluates only position zero.
- **Range extending left or right:** Endpoint clipping prevents invalid indices without losing any on-street illumination.
- **Sentinel value:** It is needed to terminate final-position intervals but is intentionally not paired with a requirement.
- **Input preservation:** Neither source array is changed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + m)$. Let `m = len(lights)`. Processing each lamp performs constant endpoint and event work, taking `O(m)` time. The cumulative scan and requirement comparisons process `n` positions, taking `O(n)` time. Total time is `O(n + m)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
