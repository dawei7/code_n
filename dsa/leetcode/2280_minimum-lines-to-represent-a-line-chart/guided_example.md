# Guided Example: Minimum Lines to Represent a Line Chart

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"stockPrices": [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `stockPrices` where $\text{stockPrices}[i] = [\text{day}_{i}, \text{price}_{i}]$ indicates the price of the stock on day $\text{day}_{i}$ is $\text{price}_{i}$. A **line chart** is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:

The objective is to compute `3` from `{"stockPrices": [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Put chart points into day order

The line chart connects points in increasing day order, not in the arbitrary input order. `stockPrices.sort()` sorts each two-element record lexicographically, so the distinct day coordinate orders the points correctly.

After sorting, every consecutive pair represents one required chart edge. Because all days are distinct, each horizontal difference `dx1 = x1 - x` is positive. Vertical differences may be positive, zero, or negative as the price rises, stays constant, or falls.

The sort mutates `stockPrices`, so callers observe the reordered points after the method returns.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"stockPrices": [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A single line can cover a whole run of equal slopes

Every adjacent pair must be connected, but several consecutive edges can be drawn as one straight line when their slopes are equal. A new line is necessary exactly when the current edge's slope differs from the preceding edge's slope.

Therefore, the answer is the number of maximal consecutive runs of equal edge slopes. The solution scans the edges once and counts the start of each run.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compare slopes without floating point

For one edge, slope is `dy / dx`. For the next edge, it is `dy1 / dx1`. Since both horizontal differences are nonzero, the slopes are equal exactly when

$$
\texttt{dy}\cdot\texttt{dx1}
=
\texttt{dx}\cdot\texttt{dy1}.
$$

The code tests the negation, `dy * dx1 != dx * dy1`, to detect a new line.

Cross multiplication avoids floating-point rounding. Two rational slopes such as one-third and two-sixths compare equal exactly even if their decimal forms cannot be represented precisely. It also avoids reducing fractions by greatest common divisors.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"stockPrices": [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Floating-point slopes:** They are easy to write but can misclassify mathematically equal rational slopes due to rounding.
- **Reduced fraction pairs:** Dividing `dy` and `dx` by their greatest common divisor gives exact comparable slopes, but cross multiplication is simpler.
- **Store every slope:** Only the immediately previous direction is needed because the goal is consecutive slope runs.
- **Compare all triples after sorting:** It gives the same collinearity test; the stored previous direction is its constant-state form.
- **One point:** There are no adjacent edges, so zero lines are returned.
- **Two points:** The sentinel ensures the only edge contributes one line.
- **Horizontal edges:** `dy = 0` compares correctly.
- **Falling prices:** Negative `dy` values preserve exact slope signs.
- **Different step sizes on one line:** Proportional vectors pass the cross-product equality.
- **A slope reappears later:** A change away and back creates separate line runs and must be counted again.
- **Distinct days:** They guarantee every real `dx` is positive and eliminate vertical chart edges.
- **Large coordinates:** Cross-products require wide arithmetic outside Python.
- **Input order:** Sorting is required before adjacency has chart meaning.
- **Input mutation:** `stockPrices.sort()` changes the caller's list order.
- **Inclusive point connection:** Each line run shares endpoints with its neighboring run, which is allowed in the chart.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Let `n` be the number of points. Sorting costs `O(n \log n)` time. `pairwise` produces `n - 1` edges and the scan uses constant arithmetic for each, adding `O(n)`. Total time is `O(n \log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
