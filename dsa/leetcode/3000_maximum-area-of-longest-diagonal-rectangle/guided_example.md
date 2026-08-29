# Guided Example: Maximum Area of Longest Diagonal Rectangle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"dimensions": [[9, 3], [8, 6]]}`
- **Required output:** `48`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D **0-indexed **integer array `dimensions`.

The objective is to compute `48` from `{"dimensions": [[9, 3], [8, 6]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compare squared diagonals instead of square roots

A rectangle with length $l$ and width $w$ has diagonal:

$$
\sqrt{l^2+w^2}.
$$

The square-root function is strictly increasing for nonnegative inputs. Therefore, whichever rectangle maximizes $l^2+w^2$ also has the longest diagonal. The code stores this squared value as `t = l**2 + w**2`.

Avoiding square roots keeps all calculations exact integers. Floating-point approximations are unnecessary and could complicate equality comparisons between diagonals.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"dimensions": [[9, 3], [8, 6]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain the best primary and secondary criteria

`mx` is the largest squared diagonal seen so far. `ans` is the greatest area among rectangles having that exact diagonal.

For each rectangle:

- if `t > mx`, it has a strictly longer diagonal than every earlier rectangle. The code replaces both `mx` and `ans` with this rectangle’s values;
- if `t == mx`, the primary criterion ties, so `ans = max(ans, l * w)` applies the required area tie-break;
- if `t < mx`, the rectangle cannot win regardless of its area and is ignored.

Initializing both values to zero is safe because all dimensions are positive, making every actual squared diagonal and area positive. The first rectangle necessarily replaces the initial state.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why area cannot override a shorter diagonal

The problem uses lexicographic priorities: longest diagonal first, maximum area only among ties. A rectangle with enormous area but a shorter diagonal must not replace the current answer.

That is why the area comparison appears only in the `t == mx` branch. Comparing areas globally would solve a different problem.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `48` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"dimensions": [[9, 3], [8, 6]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `48` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Compute floating square roots:** Ordering would be equivalent, but it adds unnecessary floating-point work and makes exact tie testing less direct.
- **Sort by diagonal and area:** Sorting works with key `(l*l+w*w, l*w)` but costs $O(N\log N)$ and extra implementation machinery.
- **Choose maximum area globally:** This violates the primary longest-diagonal requirement.
- **Equal diagonals, different areas:** The tie branch keeps the greater area.
- **Equal diagonals and equal areas:** Either rectangle yields the same required integer.
- **One rectangle:** It replaces the zero initialization and its area is returned.
- **Swapped dimensions:** Both criteria are unchanged.
- **Positive-dimension guarantee:** It makes zero a safe initial sentinel.
- **Input preservation:** No rectangle dimensions are reordered or changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of rectangles. The loop visits each row once and performs a constant number of multiplications, additions, and comparisons. Running time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
