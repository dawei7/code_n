# Guided Example: Points That Intersect With Cars

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [[3, 6], [1, 5], [4, 7]]}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** 2D integer array `nums` representing the coordinates of the cars parking on a number line. For any index `i`, $\text{nums}[i] = [\text{start}_{i}, \text{end}_{i}]$ where $\text{start}_{i}$ is the starting point of the $i^{\text{th}}$ car and $\text{end}_{i}$ is the ending point of the $i^{\text{th}}$ car.

The objective is to compute `7` from `{"nums": [[3, 6], [1, 5], [4, 7]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Count the union of inclusive integer intervals.** Each car covers every integer point from `start` through `end`, including both endpoints. A point covered by several cars must still be counted only once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [[3, 6], [1, 5], [4, 7]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The coordinate range is fixed at one through one hundred, so the exact solution uses a difference array rather than sorting and merging intervals.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Represent range additions at two boundaries.** Array `d` has length 102, providing indices zero through 101. For interval `[start, end]`:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [[3, 6], [1, 5], [4, 7]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Set of covered points:** Add every integer in each inclusive range. With endpoints at most 100 this is simple, but it performs work proportional to total interval lengths.
- **Sort and merge intervals:** This handles huge coordinates in $O(n\log n)$ time and computes integer union lengths with inclusive endpoint adjustments.
- **Boolean coverage array:** Mark every point in each interval. It is easy but uses one update per covered coordinate instead of two per interval.
- **Single-point car:** When start equals end, the start update and removal at the next coordinate cover exactly one point.
- **Overlapping cars:** Prefix coverage may exceed one, but the positivity test counts the coordinate only once.
- **Adjacent intervals:** Intervals ending at three and starting at four cover distinct consecutive points; difference updates handle them without a gap.
- **Duplicate intervals:** They increase coverage counts but not the Boolean union count.
- **Endpoint one:** The sentinel coordinate zero remains uncovered.
- **Endpoint one hundred:** Array index 101 safely receives the removal update.
- **Inclusive semantics:** The `end + 1` boundary is essential.
- **Fixed-domain assumption:** Constant space relies on the documented maximum coordinate of one hundred.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+C)$. Let $n$ be the number of car intervals and $C=102$ the fixed difference-array length. Applying two updates per interval takes $O(n)$ time. Accumulating and summing across `d` takes $O(C)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
