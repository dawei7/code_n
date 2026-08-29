# Guided Example: Heaters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"houses": [1, 2, 3], "heaters": [2]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

The objective is to compute `1` from `{"houses": [1, 2, 3], "heaters": [2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort positions to enable one forward sweep

After sorting, houses are considered left to right and heaters are also considered left to right. Pointer `i` identifies the first house not yet covered. Pointer `j` identifies the current heater under consideration.

For radius `r`, heater `heaters[j]` covers the closed interval

$$
[\texttt{heaters}[j]-r,\ \texttt{heaters}[j]+r].
$$

Call these endpoints `mi` and `mx`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"houses": [1, 2, 3], "heaters": [2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Three cases in `check(r)`

Compare the current house with that heater interval:

1. If `houses[i] < mi`, the house lies left of the current heater's coverage. Every later heater is at least as far right, so its left endpoint is no smaller. No later heater can cover this house. Earlier heaters were already passed because their right coverage ended too early. Return false.
2. If `houses[i] > mx`, the house lies right of the current heater's coverage. This heater cannot cover this house or any later house, so advance `j` and keep the same `i`.
3. Otherwise, `mi <= houses[i] <= mx`. The current house is covered, so advance `i` while retaining the heater, which may cover additional houses.

If all houses are advanced past, return true. If heaters run out first, return false.

Each pointer moves only forward, so one feasibility check is linear rather than testing every house against every heater.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the sweep never skips a possible cover

When the algorithm advances a heater, its right endpoint is already left of the current house. Because houses are sorted, it cannot help any future house. When it declares a house too far left, all later heaters begin even farther right. These decisions discard only positions that are provably useless, so `check(r)` returns true exactly when radius `r` covers every house.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"houses": [1, 2, 3], "heaters": [2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Binary-search heaters for each house:** After sorting heaters, find each house's insertion point and compare its nearest left and right heater. This takes $O(T\log T+H\log T)$ time and directly computes the maximum nearest distance.
- **Two-pointer nearest-distance sweep:** Sort both lists and move the heater pointer toward each house's closest heater, achieving linear work after sorting without radius binary search.
- **Test every radius sequentially:** Coordinates reach one billion, so linear search over radius is infeasible.
- **House exactly at a heater:** Radius zero covers it because intervals are closed.
- **Houses outside the heater range:** The first or last heater determines their distance; the sweep's left/right failure logic handles them.
- **Duplicate positions:** Sorting and closed interval comparisons handle duplicates naturally.
- **One heater:** The answer is the larger distance from that heater to the extreme houses.
- **Large coordinate gap:** The one-billion upper bound remains sufficient under the source limits.
- **Input mutation:** Both arrays are reordered by in-place sorting.
- **Common radius:** Different houses may use different heaters, but every heater shares the same binary-searched radius.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(H\log H+T\log T+(H+T)$. Let $H$ be the number of houses, $T$ the number of heaters, and $C=10^9$ the coordinate search bound.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
