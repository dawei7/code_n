# Guided Example: Minimum Area Rectangle II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[1, 2], [2, 1], [1, 0], [0, 1]]}`
- **Required output:** `2.0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of points in the **X-Y** plane `points` where $\text{points}[i] = [x_{i}, y_{i}]$.

The objective is to compute `2.0` from `{"points": [[1, 2], [2, 1], [1, 0], [0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use one corner and two perpendicular sides

An arbitrarily rotated rectangle can be characterized by:

- one corner `p1`;
- two adjacent corners `p2` and `p3`;
- perpendicular vectors from `p1` to those adjacent corners;
- a fourth corner determined by parallelogram geometry.

The solution enumerates triples that might play these roles and checks whether the required fourth point exists.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[1, 2], [2, 1], [1, 0], [0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store points for constant-time membership

Set `s` contains every coordinate pair. Once three candidate corners determine fourth coordinate `p4`, membership `p4 in s` takes expected constant time.

The input points are unique, so set conversion does not lose multiplicity information.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Constructing the fourth corner

Let:

- `p1 = (x1, y1)` be the shared corner;
- `p2 = (x2, y2)` and `p3 = (x3, y3)` be adjacent corners.

For a parallelogram, the opposite corner is:

`p4 = p2 - p1 + p3`.

Coordinatewise, the code computes:

- `x4 = x2 - x1 + x3`;
- `y4 = y2 - y1 + y3`.

If this coordinate is absent, these three points cannot complete the desired rectangle.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2.0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[1, 2], [2, 1], [1, 0], [0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2.0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Group diagonals by midpoint and length:** Rectangle diagonals share midpoint and squared length. Grouping pairs can reduce some repeated work but needs more storage.
- **Check every four-point subset:** It costs `O(P^4)` and performs redundant geometric tests.
- **Axis-aligned-only logic:** Matching equal x and y pairs misses rotated rectangles.
- **No rectangle:** Infinity remains unchanged and zero is returned.
- **Axis-aligned rectangle:** It is also detected because horizontal and vertical vectors have dot product zero.
- **Rotated rectangle:** Vector arithmetic works without slopes or angle special cases.
- **Vertical lines:** Dot products avoid division-by-zero issues that slope comparisons would encounter.
- **Multiple equal minimum rectangles:** Only area is requested, so duplicates are harmless.
- **Large coordinates:** Python integer dot products and squared differences remain exact.
- **Floating tolerance:** Square roots introduce floating values, but the accepted error margin covers normal rounding.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P^3)$. Let `P` be the number of points.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
