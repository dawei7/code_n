# Guided Example: Finding the Number of Visible Mountains

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"peaks": [[2, 2], [6, 3], [5, 4]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** 2D integer array `peaks` where $\text{peaks}[i] = [x_{i}, y_{i}]$ states that mountain `i` has a peak at coordinates $(x_{i}, y_{i})$. A mountain can be described as a right-angled isosceles triangle, with its base along the `x`-axis and a right angle at its peak. More formally, the **gradients** of ascending and descending the mountain are `1` and `-1` respectively.

The objective is to compute `2` from `{"peaks": [[2, 2], [6, 3], [5, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Transform each mountain into a base interval

A mountain with peak `(x, y)` and slopes 1 and -1 reaches the x-axis at

`x - y` and `x + y`.

Represent it by interval `(l, r) = (x-y, x+y)`.

This transformation turns geometric containment into interval containment. A peak `(x_1,y_1)` lies inside or on mountain `(x_2,y_2)` exactly when

`x_2-y_2 <= x_1-y_1` and `x_1+y_1 <= x_2+y_2`.

In interval terms, the first mountain's interval is contained in the second's interval. Therefore a mountain is invisible when some other interval contains its interval.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"peaks": [[2, 2], [6, 3], [5, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count duplicates before scanning

`cnt = Counter(arr)` records how many mountains have each identical interval.

Two identical peaks produce identical mountains. Each peak lies on or inside the other mountain, so neither copy is visible. Even if their interval is not contained by a larger interval, a duplicated interval must contribute zero to the answer.

The Counter lets the scan distinguish a unique exposed interval from overlapping duplicate mountains.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `cnt = Counter(arr)` records how many mountains have each id... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort possible containers before contained intervals

The array is sorted by increasing left endpoint and, for equal left endpoints, decreasing right endpoint:

`(l ascending, r descending)`.

A containing interval must start no later and end no earlier than the contained interval. Increasing `l` ensures any possible earlier-starting container is processed first. Decreasing `r` for equal left endpoints ensures the widest interval is processed before narrower intervals sharing that start.

Without the descending tie rule, a narrow interval might temporarily look visible before its equal-left wider container is encountered.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"peaks": [[2, 2], [6, 3], [5, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare every pair of mountains:** Direct geom:** - **Compare every pair of mountains:** Direct geometric containment is easy to state but costs `O(n^2)`.
- **Sweep with explicit interval stack:** A stack can retain nested intervals, but the farthest-right scalar already decides containment after the chosen sort.
- **Sort right endpoints ascending on equal left:** This can process contained intervals before their container and count incorrectly.
- **Ignore duplicate counts:** The first of two identical mountains might be counted even though each hides the other.
- **One mountain:** Its interval is unique and uncovered, so the answer is one.
- **Two identical peaks:** The Counter is two; neither is counted.
- **Same left endpoint, different right endpoints:** The widest comes first and hides every narrower one.
- **Same right endpoint, later left endpoint:** The later interval is contained because `r <= cur`.
- **Touching border:** Containment uses non-strict inequalities, so `r == cur` is invisible as required.
- **Overlapping without containment:** If the current interval extends farther right, it remains visible even when its bases overlap.
- **Negative left endpoint:** Mountains may extend left of zero in coordinates; interval arithmetic remains valid.
- **A duplicate interval contained by a larger one:** It is invisible for both reasons; the scan skips it through coverage.
- **Input preservation:** Only transformed interval storage is sorted.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Let `n` be the number of peaks. Building intervals and the Counter takes `O(n)` expected time. Sorting costs `O(n \log n)`, and the final scan is `O(n)`. Total time is `O(n \log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
