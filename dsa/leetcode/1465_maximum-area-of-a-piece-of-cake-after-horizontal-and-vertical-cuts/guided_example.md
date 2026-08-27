# Guided Example: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"h": 5, "w": 4, "horizontalCuts": [1, 2, 4], "verticalCuts": [1, 3]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a rectangular cake of size `h x w` and two arrays of integers `horizontalCuts` and `verticalCuts` where:

The objective is to compute `4` from `{"h": 5, "w": 4, "horizontalCuts": [1, 2, 4], "verticalCuts": [1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate height from width.** Every cake piece is formed by one horizontal interval and one vertical interval. Its area is the interval height multiplied by the interval width. The greatest possible piece therefore combines the largest gap between horizontal boundaries with the largest gap between vertical boundaries.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"h": 5, "w": 4, "horizontalCuts": [1, 2, 4], "verticalCuts": [1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

This independence is valid because every horizontal cut crosses every vertical strip and every vertical cut crosses every horizontal strip. The rectangle at the intersection of the widest strip and tallest strip always exists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | This independence is valid because every horizontal cut cros... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Add the outside boundaries as cut coordinates.** The supplied arrays contain only interior cuts. The top and bottom cake edges also bound pieces, at horizontal positions zero and `h`. Likewise, the left and right edges are at vertical positions zero and `w`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"h": 5, "w": 4, "horizontalCuts": [1, 2, 4], "verticalCuts": [1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Handle edge gaps separately:** Sort only inter:** - **Handle edge gaps separately:** Sort only interior cuts, compare the first coordinate, adjacent differences, and dimension minus the last coordinate. It avoids mutating the lists with boundary values but needs more cases.
- **Use sorted copies:** `sorted(horizontalCuts + [0, h])` preserves caller inputs at the cost of explicit `O(H + V)` copied storage.
- **Test every rectangle:** Combining every horizontal and vertical gap is unnecessary; the product of independent maxima proves the answer directly.
- **Unsorted gap scan:** Differences between adjacent input entries are meaningless until coordinates are ordered.
- **One cut in each direction:** Boundaries still create two gaps per dimension, and the larger of each is selected.
- **Cut near an edge:** The small edge gap competes normally with all other gaps.
- **Largest gap at an outer edge:** Appending zero and the full dimension ensures it is included.
- **Several equal maximum gaps:** Any intersection of a maximum height and width gives the same maximum area.
- **Distinct-cut guarantee:** Adjacent sorted differences are positive. Duplicate cuts outside the contract would create zero-width gaps without affecting the maximum.
- **Very large dimensions:** Python avoids multiplication overflow; other languages should widen before multiplying.
- **Modulo placement:** Apply it after choosing and multiplying true maximum gaps.
- **Input mutation:** The exact source extends and sorts both cut lists. Reusing those lists later will observe the changes.
- **Pairwise laziness:** It does not allocate a complete list of adjacent pairs.
- **No need to locate the piece:** Only the area is requested, so retaining gap endpoints is unnecessary.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(H \log H + V \log V)$. Let `H` and `V` be the original numbers of horizontal and vertical cuts. Adding two boundaries to each list takes constant amortized work. Sorting costs `O(H log H + V log V)`. Pairwise gap scans take `O(H + V)` and are dominated by sorting.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
