# Guided Example: Find the Number of Ways to Place People I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[1, 1], [2, 2], [3, 3]]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D array `points` of size `n x 2` representing integer coordinates of some points on a 2D plane, where $\text{points}[i] = [x_{i}, y_{i}]$.

The objective is to compute `0` from `{"points": [[1, 1], [2, 2], [3, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Turn geometry into a visibility scan.** Alice must occupy the upper-left corner $A=(x_A,y_A)$ and Bob the lower-right corner $B=(x_B,y_B)$. Therefore a candidate orientation requires

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[1, 1], [2, 2], [3, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
x_A\le x_B
\quad\text{and}\quad
y_A\ge y_B.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The rectangle, including its boundary, must contain no third point. A direct method could select two points and scan every other point, but that would cost cubic time. The exact solution removes the third scan by ordering points and keeping one vertical boundary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[1, 1], [2, 2], [3, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Triple-loop rectangle check:** Select Alice and Bob, then test every other point. It is easy to derive but costs $O(N^3)$ time.
- **Two-dimensional prefix sums:** Coordinate compression plus a grid prefix sum can query rectangle populations, but it uses substantially more machinery and space for this small-$N$ version.
- **Iterate by index without slicing:** Replacing the suffix slice with `for j in range(i + 1, n)` preserves the same $O(N^2)$ algorithm while avoiding the per-iteration lists. That would improve auxiliary space, but it is not the exact protected source.
- **Sort equal $x$ by ascending $y$:** This is incorrect for vertical fences because a lower same-column point could appear before the upper Alice candidate, breaking the one-direction scan and blocker logic.
- **Bob above Alice:** `y2 <= y1` fails, so the orientation is rejected even if the rectangle would otherwise be empty.
- **Alice and Bob on one vertical line:** Equal $x$ is allowed; the fence may have zero area. The descending-$y$ tie order handles it correctly.
- **Alice and Bob on one horizontal line:** Equal $y$ is allowed. Once one point at that height is accepted, another farther right at the same height is blocked by the strict `max_y < y2` test.
- **A point on the rectangle boundary:** It blocks the pair just like an interior point. The non-strict coordinate containment and strict frontier update correctly enforce this.
- **Distinct point coordinates as pairs:** Individual $x$ or $y$ values may repeat even though complete points are distinct, which is why the tie rules matter.
- **Input mutation:** The returned count is independent of original order, but the caller receives `points` rearranged into sorted order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Let $N$ be the number of points. Sorting costs $O(N\log N)$ time. The nested scans examine
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
