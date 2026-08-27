# Guided Example: Maximum Number of Intersections on the Chart

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"y": [1, 2, 1, 2, 1, 3, 2]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a line chart consisting of `n` points connected by line segments. You are given a **1-indexed** integer array `y`. The $$k^{\text{th}}$$ point has coordinates $(k, y[k])$. There are no horizontal lines; that is, no two consecutive points have the same y-coordinate.

The objective is to compute `5` from `{"y": [1, 2, 1, 2, 1, 3, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn every segment into a vertical interval

A nonhorizontal line segment between heights $u$ and $v$ intersects a horizontal line at every height between them. If all segment intervals were simply closed at both ends, a chart vertex shared by two adjacent segments could be counted twice even though the horizontal line meets one geometric point there.

The solution assigns each segment a consistent half-open convention: include its left endpoint and exclude its right endpoint. The final chart point, which is no segment’s left endpoint, is then added separately.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"y": [1, 2, 1, 2, 1, 3, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why doubled coordinates encode open and closed endpoints

Event coordinates use twice the real height. Ordinary vertex height $h$ is represented by `2*h`, while `2*h+1` represents a level infinitesimally above $h$ for sweep-order purposes.

For a rising segment from `first < second`, the left endpoint is the lower one. The events:

- add one at `2*first`;
- subtract one at `2*second`

encode interval $[\textit{first},\textit{second})$.

For a falling segment, the left endpoint is the higher one and the right endpoint is the lower one. The events:

- add one at `2*second + 1`;
- subtract one at `2*first + 1`

encode $(\textit{second},\textit{first}]$: exclude the lower right endpoint and include the higher left endpoint.

Both formulas implement “left chart endpoint included, right chart endpoint excluded,” expressed in vertical order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Event coordinates use twice the real height.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Add the last vertex

Every segment accounts for its left endpoint. The last chart point is only a right endpoint, so it would otherwise be excluded. The two events at `2*y[-1]` and `2*y[-1]+1` create a singleton-height interval that contributes exactly one intersection at that final vertex.

Now every chart vertex is owned exactly once, while crossings strictly inside segments remain counted normally.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"y": [1, 2, 1, 2, 1, 3, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Closed intervals for every segment:** This dou:** - **Closed intervals for every segment:** This double-counts shared vertices.
- **Evaluate only integer heights:** The maximum can occur between vertex heights, such as at 1.5, so fractional regions matter.
- **Floating epsilon endpoints:** Doubled integers encode endpoint order exactly without floating-point error.
- **Brute-force candidate heights against all segments:** Testing $O(N)$ height regions with $O(N)$ segments costs $O(N^2)$.
- **Strictly increasing chart:** Every horizontal line within the height range intersects once, and the sweep returns one.
- **Local peaks and valleys:** Endpoint ownership ensures each shared point contributes once.
- **Repeated nonconsecutive heights:** Events combine correctly; only consecutive equality is forbidden.
- **Last vertex:** Its explicit singleton is necessary because all segment right endpoints are excluded.
- **Large height values:** Doubling values up to $10^9$ is safe in Python integer arithmetic.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N log N)$. Let $N$ be the number of chart points. There are $N-1$ segments plus one final singleton, producing $O(N)$ distinct event keys. Building the map takes expected $O(N)$ time.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
