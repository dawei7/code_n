# Guided Example: Best Position for a Service Centre

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"positions": [[0, 1], [1, 0], [1, 2], [2, 1]]}`
- **Required output:** `4.0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A delivery company wants to build a new service center in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new center in a position such that **the sum of the euclidean distances to all customers is minimum**.

The objective is to compute `4.0` from `{"positions": [[0, 1], [1, 0], [1, 2], [2, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The objective is the geometric median

For candidate center `(x, y)`, the objective is

$$
F(x,y)
=
\sum_i \sqrt{(x-x_i)^2+(y-y_i)^2}.
$$

This is a convex function. Unlike squared distance, ordinary Euclidean distance is not minimized simply by taking coordinate averages. The minimizing point is called a geometric median.

The stored solution uses iterative gradient descent with a decaying step size. It begins at the arithmetic mean of all customer x-coordinates and y-coordinates. The centroid is not always the geometric median, but it is a reasonable central starting point.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"positions": [[0, 1], [1, 0], [1, 2], [2, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Computing the gradient direction

For a center not exactly equal to customer `i`, that customer's distance contributes gradient

$$
\left(
\frac{x-x_i}{d_i},
\frac{y-y_i}{d_i}
\right),
$$

where $d_i$ is the Euclidean distance.

The source loops over all positions, computes `a = x - x1`, `b = y - y1`, and `c = sqrt(a * a + b * b)`. It adds `a / (c + 1e-8)` and `b / (c + 1e-8)` to the gradient components. It also accumulates `dist += c` as the current objective value.

The small denominator addition regularizes the undefined gradient when the candidate exactly matches a customer. At zero distance, both numerators are zero, so that customer's contribution becomes zero rather than causing division by zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Taking and shrinking steps

The initial learning rate `alpha` is 0.5. The proposed movement is

`dx = grad_x * alpha` and `dy = grad_y * alpha`.

The source subtracts these quantities from the current coordinates, moving opposite the gradient toward lower objective values.

After every iteration, `alpha *= 0.999`. This exponential decay gradually reduces movement size. The loop returns when both coordinate changes have absolute value at most `1e-6`.

The returned `dist` was computed at the position before that final tiny update. Since the final movement is small, it is intended as an approximation at essentially the converged location.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4.0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"positions": [[0, 1], [1, 0], [1, 2], [2, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4.0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Weiszfeld's algorithm:** A specialized geometric-median iteration often converges faster, but it needs careful handling when the iterate lands on a customer point.
- **Nested ternary search:** Convexity can support searches over coordinates with inner and outer iterations, which may explain an $I^2$ style bound but is not the stored method.
- **Hill climbing over directions:** Repeatedly test neighboring positions while shrinking a spatial step. It is intuitive but also approximate.
- **One customer:** The exact minimum sum is zero at that customer's location.
- **Two customers:** Every point on their connecting segment is optimal.
- **Duplicate positions:** The regularizing denominator avoids division by zero and naturally gives that location extra weight through repeated entries.
- **Symmetric positions:** Vector contributions cancel at the center.
- **Centroid is not generally optimal:** It is only the initial guess for ordinary-distance minimization.
- **Tiny alpha:** It guarantees eventual small updates but not independently certified objective accuracy.
- **Returned iteration value:** `dist` corresponds to the pre-update point of the terminating iteration.
- **Required import:** `sqrt` must be available from `math`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(NT)$. Let $N$ be the number of customer positions and $T$ the number of iterations until the step-size condition is met. Each iteration scans all $N$ points and uses constant extra state, so exact time is $O(NT)$ and auxiliary space is $O(1)$ beyond the input.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
