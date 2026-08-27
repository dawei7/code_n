# Guided Example: Sort Transformed Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-4, -2, 2, 4], "a": 1, "b": 3, "c": 5}`
- **Required output:** `[3, 9, 15, 33]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **sorted** integer array `nums` and three integers `a`, `b` and `c`, apply a quadratic function of the form $f(x) = ax^2 + bx + c$ to each element $\text{nums}[i]$ in the array, and return *the array in a sorted order*.

The objective is to compute `[3, 9, 15, 33]` from `{"nums": [-4, -2, 2, 4], "a": 1, "b": 3, "c": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The helper evaluates the exact polynomial.

The local function `f(x)` returns `a * x * x + b * x + c`. It avoids storing a separate transformed array. Each loop iteration evaluates only the currently exposed left and right endpoints.

The input contains integers and all coefficients are integers, so every transformed result is an integer. Duplicate input values or different inputs that produce equal outputs remain separate occurrences because the algorithm performs exactly one placement per input position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-4, -2, 2, 4], "a": 1, "b": 3, "c": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why endpoints contain an extreme.

Consider only the currently unprocessed values `nums[i]` through `nums[j]`. They occupy a closed interval of $x$ values, possibly with gaps and duplicates.

If $a>0$, the quadratic is convex: its graph opens upward. A convex function's maximum over a closed interval occurs at an endpoint. The minimum may be near the vertex in the interior, but the largest remaining transformed value must be either `f(nums[i])` or `f(nums[j])`.

If $a<0$, the quadratic is concave and opens downward. Its minimum over a closed interval occurs at an endpoint. The maximum may be internal, but the smallest remaining transformed value must be one of the two endpoint results.

If $a=0$, the function is linear, $f(x)=bx+c$. A linear function is monotone increasing, monotone decreasing, or constant, so both its minimum and maximum over the remaining interval occur at endpoints. The source groups this case with `a <= 0` and repeatedly selects the smaller endpoint value, which is valid for every sign of $b$.

These endpoint properties continue to hold after one pointer moves inward, because the remaining inputs still form an ordered subarray and therefore lie within a smaller closed interval.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Consider only the currently unprocessed values `nums[i]` thr... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Upward parabola: fill the answer from the end.

When `a > 0`, the method compares `y1 = f(nums[i])` and `y2 = f(nums[j])`. The larger one is the largest value still unplaced. It belongs at index `n - k - 1`, moving from the last output position toward the first as `k` increases.

If `y1 > y2`, the left endpoint supplies that maximum and `i` advances. Otherwise the right endpoint is used and `j` retreats. Equality may choose the right copy; either choice is safe because equal values are interchangeable in sorted order and both occurrences will eventually be placed.

Filling from the back is essential. The first extremes found for an upward parabola are large, not small. Writing them from left to right would produce descending order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 9, 15, 33]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-4, -2, 2, 4], "a": 1, "b": 3, "c": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 9, 15, 33]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Transform then sort:** Map every input through:** - **Transform then sort:** Map every input through `f` and sort the results. This is simple and correct but costs $O(n\log n)$ time, missing the linear follow-up.
- **- **Find the vertex and merge outward:** Locate $-:** - **Find the vertex and merge outward:** Locate $-b/(2a)$, split inputs around it, and merge transformed monotone runs. This can also run in $O(n)$ but requires more careful boundary and sign handling than endpoint extremes.
- **- **`a = 0`, positive `b`:** The transformation is:** - **`a = 0`, positive `b`:** The transformation is increasing, so the left endpoint is repeatedly selected and the output follows input order.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. The loop has exactly $n$ iterations. Each iteration performs two constant-time polynomial evaluations, one comparison, one output assignment, and one pointer update. Total running time is $O(n)$, satisfying the follow-up.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
