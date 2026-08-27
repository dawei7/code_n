# Guided Example: Valid Boomerang

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[1, 1], [2, 3], [3, 2]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `points` where $\text{points}[i] = [x_{i}, y_{i}]$ represents a point on the **X-Y** plane, return `true` *if these points are a **boomerang***.

The objective is to compute `true` from `{"points": [[1, 1], [2, 3], [3, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Three points form a boomerang exactly when their area is nonzero

Three distinct points fail the definition only when they lie on one straight line. Geometrically, three points form a triangle, and a triangle has positive area precisely when its points are noncollinear.

The method tests this using a two-dimensional cross product. It avoids computing slopes, so vertical lines and fractional values need no special cases.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[1, 1], [2, 3], [3, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build two direction vectors

After unpacking the three points, consider the vector from point one to point two:

$$
u=(x_2-x_1,\ y_2-y_1).
$$

Consider the vector from point two to point three:

$$
v=(x_3-x_2,\ y_3-y_2).
$$

The points are collinear exactly when these vectors are parallel or antiparallel. In two dimensions, that happens exactly when their cross product is zero:

$$
u_xv_y-u_yv_x=0.
$$

Substituting coordinates gives

$$
(x_2-x_1)(y_3-y_2)
-
(y_2-y_1)(x_3-x_2)=0.
$$

The code rearranges this equality. It returns true when

`(y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)`.

The two products being unequal is exactly the statement that the cross product is nonzero, with the terms moved to opposite sides.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After unpacking the three points, consider the vector from p... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why consecutive vectors work

A common area formula uses vectors from the same starting point, such as point one to point two and point one to point three. The exact code instead uses point one to point two and point two to point three.

These are equivalent because

$$
\overrightarrow{P_2P_3}
=
\overrightarrow{P_1P_3}
-
\overrightarrow{P_1P_2}.
$$

Taking the cross product with `\overrightarrow{P_1P_2}`, the self-cross-product term is zero. The remaining value is the same signed double area. Thus consecutive edge vectors detect collinearity just as reliably.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[1, 1], [2, 3], [3, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Slope comparison:** It expresses the same geom:** - **Slope comparison:** It expresses the same geometry but needs vertical-line handling and may suffer floating-point precision problems. Cross multiplication is exact and uniform.
- **Shoelace area formula:** Compute twice the triangle area from all three coordinates and test whether it is nonzero. This is algebraically equivalent to the cross product.
- **Pairwise distance checks:** Distances can prove points are distinct, but they do not by themselves detect collinearity. An area or orientation test is still needed.
- **Explicit duplicate set:** Checking `len(set(map(tuple, points))) == 3` can enforce distinctness, followed by a collinearity test. The determinant already rejects duplicates, making the set unnecessary.
- **Vertical line:** Both relevant horizontal differences are zero, so both cross-multiplied products are zero and the points are correctly rejected without division.
- **Horizontal line:** Both vertical differences are zero, producing the same correct rejection.
- **Negative slope:** Signs are preserved in integer products, so diagonal direction does not need a separate case.
- **Clockwise versus counterclockwise:** The determinant sign changes, but any nonzero sign returns true because orientation is irrelevant.
- **Two identical points:** One direction vector is zero, making both sides equal and returning false.
- **First and third points identical:** The vectors are opposites, still giving zero cross product and returning false.
- **Very small nonzero area:** Integer arithmetic distinguishes it exactly; there is no epsilon threshold.
- **Point order:** Permuting three distinct noncollinear points may change determinant sign but never whether it is zero, so boomerang validity is order-independent.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The input always contains exactly three points. Unpacking coordinates and evaluating two products, four differences, and one comparison takes a fixed amount of work. Time complexity is `O(1)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
