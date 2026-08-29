# Guided Example: Maximum Area Rectangle With Point Constraints I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[1, 1], [1, 3], [3, 1], [3, 3]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `points` where $\text{points}[i] = [x_{i}, y_{i}]$ represents the coordinates of a point on an infinite plane.

The objective is to compute `4` from `{"points": [[1, 1], [1, 3], [3, 1], [3, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Treat each point pair as possible opposite corners.** An axis-aligned rectangle is determined by two diagonal corners with different $x$- and $y$-coordinates. The nested loops consider every unordered pair once by pairing current point with `points[:i]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[1, 1], [1, 3], [3, 1], [3, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

For a pair, the source normalizes bounds:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

$$
x_{\min}=\min(x_1,x_2),\quad x_{\max}=\max(x_1,x_2),
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[1, 1], [1, 3], [3, 1], [3, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Corner hash set:** It can test the other two corners in expected $O(1)$, but forbidden-point scanning still remains unless extra geometry structures are used.
- **Enumerate two x-levels and two y-levels:** It generates coordinate boxes but can examine many combinations absent from the points.
- **Prefix grid:** Coordinates are small enough for a dense count grid, though coordinate compression is more general.
- **Fewer than four points:** No check can reach corner count four, so return `-1`.
- **Pair on one vertical line:** The degenerate box has at most two unique corners and fails.
- **Pair on one horizontal line:** It fails symmetrically.
- **Interior point:** It invalidates the rectangle.
- **Non-corner border point:** It also invalidates the rectangle.
- **Point outside bounds:** It has no effect.
- **Two diagonal pairs:** The same rectangle may be checked twice, but maximum area is unchanged.
- **Unique-point guarantee:** It makes `cnt == 4` equivalent to four distinct corners.
- **Positive dimensions:** They follow implicitly from reaching four unique endpoint combinations.
- **Tied maximum areas:** Only the numeric maximum is returned.
- **No hash lookup:** The exact source discovers all corners during the scan.
- **Sentinel `-1`:** Every valid area is positive.
- **Input preservation:** Slices copy references; point coordinates are unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^3)$. There are $O(n^2)$ unordered pairs, and `check` scans $O(n)$ points for each, giving $O(n^3)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
