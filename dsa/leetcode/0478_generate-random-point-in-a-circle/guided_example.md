# Guided Example: Generate Random Point in a Circle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"radius": 1, "x_center": 0, "y_center": 0, "random_values": [0, 0], "draws": 2}`
- **Required output:** `[[0, 0], [0, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the radius and the position of the center of a circle, implement the function `randPoint` which generates a uniform random point inside the circle.

The objective is to compute `[[0, 0], [0, 0]]` from `{"radius": 1, "x_center": 0, "y_center": 0, "random_values": [0, 0], "draws": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Uniform angle

`random.uniform(0, 1) * 2 * math.pi` produces an angle `degree` uniformly over a full turn from zero through approximately $2\pi$. Equal angular intervals form sectors with equal fractions of the circle's area when radial sampling is handled correctly.

The variable name `degree` is slightly misleading: the value is in radians, because Python's `sin` and `cos` functions expect radians.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"radius": 1, "x_center": 0, "y_center": 0, "random_values": [0, 0], "draws": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why squared radius must be uniform

For a circle of radius `R`, the fraction of total area lying within distance `r` of the center is

$$
\frac{\pi r^2}{\pi R^2}=\frac{r^2}{R^2}.
$$

Thus a uniform area sample must satisfy cumulative distribution

$$
P(\text{radius}\le r)=\frac{r^2}{R^2}.
$$

If `U` is uniform on `[0, R^2]` and `length = sqrt(U)`, then

$$
P(\texttt{length}\le r)
=P(U\le r^2)
=\frac{r^2}{R^2},
$$

which is exactly the required area distribution.

That is why the code uses

`math.sqrt(random.uniform(0, radius**2))`.

It is equivalent to `R * sqrt(U0)` for `U0` uniform on `[0,1]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a uniform radius would cluster points at the center

If radius itself were uniform, half the samples would lie inside radius `R/2`. But that inner disk has only one quarter of the total area. It would receive twice the probability it should, producing excessive central density. The square root corrects this by assigning only probability `1/4` to radii at most `R/2`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 0], [0, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"radius": 1, "x_center": 0, "y_center": 0, "random_values": [0, 0], "draws": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 0], [0, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Rejection sample a bounding square:** Draw uniformly from the `2R x 2R` square and reject points outside the circle. It is correct with expected about $4/\pi$ attempts, but has unbounded worst-case retries.
- **Choose radius uniformly:** Incorrect; it overweights the center because equal radial bands do not have equal areas.
- **Choose `sqrt(U)` for `U in [0,1]`:** Correct when multiplied by `R`; it is algebraically the same as the exact squared-radius draw.
- **Angle in degrees:** `sin` and `cos` require radians; the exact `2 * pi` scaling is correct despite the variable name.
- **Point at center:** Valid and naturally produced when radial value is zero.
- **Point on circumference:** Valid when radial value equals `R`.
- **Non-origin center:** Adding center coordinates translates every sample without changing uniformity.
- **Very large radius:** Fixed-precision arithmetic handles the stated bounds, though returned coordinates are approximate floating-point values.
- **Deterministic app stream:** Two supplied values reproduce the same radial and angular transformations per point.
- **No input mutation:** Constructor values are stored and remain unchanged across calls.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. One `randPoint` call performs two random draws and a fixed number of arithmetic, square-root, sine, and cosine operations. Under the standard numerical model, expected and worst-case time are $O(1)$ and auxiliary space is $O(1)$ per native call.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
