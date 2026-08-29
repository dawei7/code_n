# Guided Example: Color the Triangle Red

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3}`
- **Required output:** `[[1, 1], [2, 1], [2, 3], [3, 1], [3, 5]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`. Consider an equilateral triangle of side length `n`, broken up into $n^{2}$ unit equilateral triangles. The triangle has `n` **1-indexed** rows where the $i^{\text{th}}$ row has $2i - 1$ unit equilateral triangles.

The objective is to compute `[[1, 1], [2, 1], [2, 3], [3, 1], [3, 5]]` from `{"n": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Understand the triangle's adjacency pattern

Row $i$ contains coordinates one through $2i-1$. Consecutive coordinates in one row share a side.

The alternating triangle orientations also create cross-row edges: an odd-positioned triangle $(i,2q-1)$ shares a side with even-positioned triangle $(i+1,2q)$ immediately below it.

These horizontal and diagonal connections are why a repeating row pattern can make every initially white triangle acquire two red neighbors.

The exact solution always selects top triangle $(1,1)$ and then processes rows from bottom to top using a four-phase pattern.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The four initial-color patterns

Variable `k` cycles through zero, one, two, and three as row index `i` decreases.

- Phase zero colors every odd position `1,3,5,...,2i-1`.
- Phase one colors only position two.
- Phase two colors odd positions `3,5,...,2i-1`, omitting position one.
- Phase three colors only position one.

Then `k = (k + 1) % 4` repeats the pattern for the next four rows above.

All produced coordinates lie in their row: the range endpoints and the single positions are valid whenever their corresponding phase can occur.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a row of odd seeds fills itself

In phase zero, every even-positioned triangle lies horizontally between two red odd-positioned triangles.

It therefore has at least two red neighbors and can be colored. Once all even positions are added, the entire row is red.

This fully seeded odd row acts as support for neighboring rows in the four-row motif.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 1], [2, 1], [2, 3], [3, 1], [3, 5]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 1], [2, 1], [2, 3], [3, 1], [3, 5]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Search all initial subsets:** Exponential in $n^2$ and infeasible.
- **Simulate after choosing the pattern:** Useful for verification but unnecessary to construct the proven percolating set.
- **Different optimal pattern:** Allowed if it meets the same lower bound and percolates.
- **`n = 1`:** The fixed root is the complete answer.
- **Partial final four-row block:** The root seed handles the top boundary.
- **Coordinate parity:** Odd-position ranges and the two single even/odd anchors must remain exactly aligned.
- **Bottom-up phase order:** `k` advances as rows decrease, so changing loop direction changes the construction.
- **Minimum proof:** Sufficiency alone is not enough; the global edge-count lower bound establishes optimality.
- **Output order:** It does not affect which triangles start red.
- **Large `n`:** The output itself is quadratic, matching the algorithm's time and space.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. The nested range loops append exactly the output coordinates. Their count is $\Theta(n^2)$ in the asymptotic worst case, so time is $O(n^2)$.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
