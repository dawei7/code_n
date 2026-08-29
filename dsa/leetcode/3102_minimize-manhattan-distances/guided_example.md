# Guided Example: Minimize Manhattan Distances

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[3, 10], [5, 15], [10, 2], [4, 4]]}`
- **Required output:** `12`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `points` representing integer coordinates of some points on a 2D plane, where $\text{points}[i] = [x_{i}, y_{i}]$.

The objective is to compute `12` from `{"points": [[3, 10], [5, 15], [10, 2], [4, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Transform Manhattan distance into one-dimensional spreads.** For point $(x,y)$ define:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[3, 10], [5, 15], [10, 2], [4, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
u=x+y
\qquad\text{and}\qquad
v=x-y.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

For any two points, their Manhattan distance satisfies:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `12` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[3, 10], [5, 15], [10, 2], [4, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `12` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two smallest and two largest values:** For each transform, retain extrema with point indices so deleting one point can expose the next. This achieves $O(n)$ time and $O(1)$ extra space and matches the manifest idea.
- **Recompute all pair distances:** Trying every removal and every remaining pair can take $O(n^3)$.
- **Recompute transformed extrema after each removal:** It avoids an ordered multiset but still takes $O(n^2)$ time.
- **Duplicate points:** Their Manhattan distance is zero, and multiset multiplicity preserves all remaining copies correctly.
- **Duplicate transformed extrema:** Removing one occurrence must not remove the shared extreme value entirely.
- **All points identical:** Every transformed range is zero, so every candidate and the answer are zero.
- **Point interior to both ranges:** Its removal changes neither maximum distance nor either endpoint spread.
- **Point extreme in one transform only:** It can still be the best removal because only the larger of the two post-removal ranges determines the candidate.
- **Exactly three points:** Removing one leaves two; their single Manhattan distance is represented by both range formulas.
- **Exactly one removal:** Values are restored after each trial so candidates are independent.
- **Large coordinates:** `x+y` and `x-y` fit safely in Python integers; fixed-width languages should use a type covering roughly twice the coordinate range.
- **Negative transformed values:** `x-y` may be negative, but sorted ordering and max-minus-min work unchanged.
- **Why two transforms:** Using only `x+y` misses point pairs whose coordinate differences have opposite signs.
- **Why no square root:** Manhattan distance is not Euclidean distance; the diagonal transform gives an exact max identity.
- **Source/manifest discrepancy:** The exact multiset solution is correct but has $O(n\log n)$ time and $O(n)$ space, not the advertised extrema-only bounds.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Building the two sorted multisets performs $2n$ insertions. Each `SortedList.add` costs $O(\log n)$ amortized for its ordered structure, so initialization is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
