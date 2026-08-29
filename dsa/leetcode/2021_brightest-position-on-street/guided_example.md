# Guided Example: Brightest Position on Street

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"lights": [[-3, 2], [1, 2], [3, 3]]}`
- **Required output:** `-1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A perfectly straight street is represented by a number line. The street has street lamp(s) on it and is represented by a 2D integer array `lights`. Each $\text{lights}[i] = [\text{position}_{i}, \text{range}_{i}]$ indicates that there is a street lamp at position $\text{position}_{i}$ that lights up the area from $[\text{position}_{i} - \text{range}_{i}, \text{position}_{i} + \text{range}_{i}]$ (**inclusive**).

The objective is to compute `-1` from `{"lights": [[-3, 2], [1, 2], [3, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert each inclusive interval into two events

A lamp at position `i` with range `j` covers integer positions from

`l = i - j`

through

`r = i + j`,

both inclusive.

The difference map adds one at `l` and subtracts one at `r + 1`. The extra one is what preserves coverage at `r`: the lamp stops contributing only at the next integer position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"lights": [[-3, 2], [1, 2], [3, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sweep coordinates in increasing order

`s` is the brightness after applying all events at the current coordinate. Starting from zero, the loop visits sorted event keys and executes `s += d[k]`.

Between this event coordinate and the next one, brightness remains constant because no lamp begins or ends.

Only event coordinates need inspection. A new maximum brightness can first appear exactly where positive events are applied, not in the middle of an unchanged region.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Preserve the smallest position on ties

`mx` stores the greatest brightness seen. The source updates `ans=k` only when `mx < s`, a strict improvement.

Because event coordinates are processed from smallest to largest, the first coordinate attaining the global maximum is the smallest brightest position. Later equal values do not overwrite it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `-1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"lights": [[-3, 2], [1, 2], [3, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `-1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicitly visit every illuminated position:** Impossible when ranges span up to $10^8$; event compression avoids coordinate-range dependence.
- **Separate sorted start and end arrays:** A two-list sweep is possible, but difference events are simpler.
- **Use a heap of active intervals:** More machinery than needed when only counts and endpoints matter.
- **Zero range:** Produces +1 at the lamp position and -1 at the next integer.
- **Negative positions:** Sorted dictionary keys handle them naturally.
- **Several lamps start together:** Their positive changes accumulate.
- **One lamp ends where another starts:** Net event gives correct brightness and tie logic keeps the earliest maximum.
- **Long constant maximum interval:** Its left endpoint is recorded.
- **Several separated maximum regions:** Strict update keeps the first/smallest.
- **Inclusive right endpoint:** Requires subtraction at `r+1`, not `r`.
- **At least one lamp:** Ensures the zero answer initialization is replaced.
- **Input preservation:** The source builds a separate event map.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be number of lamps and $E\le2N$ distinct event coordinates. Building the map takes expected $O(N)$ time. Sorting keys costs $O(E\log E)=O(N\log N)$, and sweeping costs $O(E)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
