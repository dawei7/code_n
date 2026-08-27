# Guided Example: Maximum Matrix Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[1, -1], [-1, 1]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `n x n` integer `matrix`. You can do the following operation **any** number of times:

The objective is to compute `4` from `{"matrix": [[1, -1], [-1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start from an upper bound

For any element $x$, the largest contribution obtainable from its magnitude is $\lvert x\rvert$. Therefore no final matrix can have sum greater than

$$
S=\sum \lvert x\rvert.
$$

If all nonzero entries can be made positive, this upper bound is attainable. The problem is thus not about deciding a separate desired value for every cell; it is about understanding which sign patterns the pair-flip operation can reach.

The source computes `s` as this absolute-value sum. At the same time, it counts initially negative entries in `cnt` and tracks the smallest magnitude in `mi`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[1, -1], [-1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand what one operation changes

An operation flips the signs at the two endpoints of one grid edge. Imagine recording, for every cell, whether it is flipped an odd or even number of times. Even flips cancel, so only the odd-flipped set determines the final signs.

Every operation toggles exactly two cells. Consequently, the number of cells flipped an odd number of times must be even. Conversely, because the grid is connected, any chosen even-sized set of cells can be toggled: pair its vertices, connect each pair by a grid path, and apply the operation along every edge of that path. Internal path vertices are touched twice and cancel, while the two endpoints are touched once.

This reachability fact is why adjacency does not force a more complicated local greedy strategy. Adjacency restricts individual operations, but paths let sign changes be transported across the connected matrix.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An operation flips the signs at the two endpoints of one gri... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: When the negative count is even

If `cnt` is even, choose all initially negative cells as the odd-flipped set. Its size is even, so the connected-grid argument says this transformation is reachable. Every negative becomes positive, and every initially nonnegative entry can retain its sign.

The resulting sum is exactly `s`, the absolute-value upper bound. Since no arrangement can exceed that bound, this result is optimal. The source returns `s` when `cnt % 2 == 0`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[1, -1], [-1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate adjacent flips greedily:** Local choi:** - **Simulate adjacent flips greedily:** Local choices are difficult to coordinate and do unnecessary work; the parity invariant determines the answer directly.
- **Search over sign configurations:** There are exponentially many patterns, while only the negative-count parity and minimum magnitude matter.
- **Explicitly construct operations:** This can demonstrate reachability using paths, but the problem requests only the maximum sum, not an operation sequence.
- **Even negative count:** Every negative sign can be removed, so return the full sum of absolute values.
- **Odd negative count without zero:** One negative is unavoidable; place it on the smallest magnitude.
- **Odd negative count with zero:** Zero absorbs the parity adjustment, and subtracting twice the minimum subtracts zero.
- **All entries positive:** The negative count is zero and the matrix already attains the upper bound.
- **All entries negative:** Only the parity of the number of cells decides whether one magnitude must remain negative.
- **Several equal minimum magnitudes:** Any one can carry the unavoidable negative sign; the maximum sum is unchanged.
- **Value already zero:** It is not counted as negative because `0 < 0` is false.
- **Large magnitudes and matrix size:** Python integers hold the total exactly without fixed-width overflow.
- **Connectedness is essential to the proof:** A rectangular grid linked by shared borders is connected, so path operations can realize every even endpoint set.
- **Diagonal cells:** They are not directly adjacent, but a border-connected path can still transfer flips between them.
- **Input side effects:** The exact method reads the matrix only and returns a number without changing any entry.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $M$ be the total number of matrix elements. For the required square matrix, $M=n^2$. The nested loops process each value once with constant work, giving $O(M)$ time, equivalently $O(n^2)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
