# Guided Example: Max Points on a Line

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[1, 1], [2, 2], [3, 3]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of `points` where $\text{points}[i] = [x_{i}, y_{i}]$ represents a point on the **X-Y** plane, return *the maximum number of points that lie on the same straight line*.

The objective is to compute `3` from `{"points": [[1, 1], [2, 2], [3, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Define a line by two distinct points

All input coordinates are distinct, so any pair `points[i]` and `points[j]` determines exactly one straight line.

The selected source tries every pair with `i < j`. It starts `cnt = 2` for the two defining points, then checks later points `k > j` and adds one whenever the third point is collinear with the pair.

This is a direct enumeration approach. It avoids hash maps and avoids representing slopes as floating-point numbers.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[1, 1], [2, 2], [3, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Derive the cross-product equality

Let:

- the first point be $(x_1,y_1)$;
- the second be $(x_2,y_2)$;
- the candidate third point be $(x_3,y_3)$.

The slopes from the first point would be:

$$
\frac{y_2-y_1}{x_2-x_1}
\quad\text{and}\quad
\frac{y_3-y_1}{x_3-x_1}.
$$

Equal slopes indicate collinearity, but either denominator may be zero for a vertical line. Cross multiplication removes division:

$$
(y_2-y_1)(x_3-x_1)
=
(y_3-y_1)(x_2-x_1).
$$

The source stores the two products as `a` and `b` and tests `a == b`.

This formula naturally handles every orientation:

- vertical lines make both products zero in the corresponding way;
- horizontal lines make both vertical differences zero;
- negative slopes retain their signs;
- no special representation is needed for infinity.

Python integer multiplication is exact, so the comparison has no floating-point rounding risk.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a Boolean can be added to the count

In Python, `bool` is an integer subtype: `true` behaves like one and `false` like zero. Therefore:

`cnt += a == b`

increments exactly for a collinear third point.

Writing an explicit `if a == b: cnt += 1` would be equivalent and perhaps more obvious, but the compact expression is valid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[1, 1], [2, 2], [3, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Normalized rational slopes per anchor:** Divide `dy` and `dx` by their greatest common divisor and normalize signs, then count pairs in a map. It gives $O(n^2)$ time and $O(n)$ space with exact arithmetic.
- **Floating slopes per anchor:** Count `dy / dx` and use a special vertical key. It is concise but can be vulnerable to rounding outside tightly bounded domains.
- **Line equation keys:** Normalize coefficients in $Ax+By+C=0$. This can count global lines but requires careful common-factor and sign normalization.
- **One or two points:** Initialization and pair counting return one or two directly.
- **Vertical line:** Cross multiplication works without division by zero.
- **Negative coordinates:** Differences and exact products preserve the equation.
- **Duplicate points outside the contract:** A duplicate defining pair would make every third point appear collinear; this source relies on uniqueness.
- **Index-order undercount:** Individual later pairs may omit earlier collinear points, but the two smallest indices on a maximum line provide a complete witness pair.
- **Runtime dependency:** The source uses nested `List` annotations without importing the type. Standalone Python needs `from typing import List`.
- **Manifest mismatch:** Its actual tradeoff is cubic time with constant auxiliary storage.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the number of points.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
