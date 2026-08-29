# Guided Example: Find the Number of Ways to Place People II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[1, 1], [2, 2], [3, 3]]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D array `points` of size `n x 2` representing integer coordinates of some points on a 2D-plane, where $\text{points}[i] = [x_{i}, y_{i}]$.

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

**Replace “empty rectangle” checks with a skyline.** A valid ordered placement uses Alice at an upper-left point $A=(x_A,y_A)$ and Bob at a lower-right point $B=(x_B,y_B)$. Hence

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

The axis-aligned rectangle between them, including all four boundaries, may contain no other point. Checking every third point for every candidate pair would take $O(N^3)$ time, which is too slow for $N$ up to 1000. The exact solution sorts the points so horizontal eligibility is automatic, then represents all possible blockers for a fixed Alice with one number.

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

- **Third-point scan for every pair:** It directly implements the definition but takes $O(N^3)$ time.
- **Coordinate compression plus 2D prefix sums:** Rectangle population queries become constant time after preprocessing, but the compressed grid may use quadratic space and is unnecessary for the one-frontier insight.
- **Range trees or Fenwick structures:** More advanced geometric data structures can answer related dominance queries, but they add implementation complexity without improving this source's needed $O(N^2)$ pair traversal.
- **Index-based suffix traversal:** It preserves the exact skyline logic and time bound while removing slice allocations. The protected implementation uses slicing, so its real peak space remains linear.
- **Equal $x$ coordinates:** Descending $y$ order makes upper points precede lower points and correctly supports zero-width fences.
- **Equal $y$ coordinates:** Only the first visible point at that height can be Bob; a farther point is blocked by it on the fence boundary.
- **Bob above Alice:** The `y2 <= y1` condition rejects the orientation.
- **Third point exactly on an edge:** It blocks the pair. Strict frontier growth ensures equality is treated as blocked, not clear.
- **Third point below Bob:** It lies outside the rectangle and does not affect validity; a higher stored frontier already captures all relevant obstruction.
- **Point above Alice:** It is ignored for this Alice because it cannot enter any rectangle extending downward from her.
- **Distinct points but repeated coordinates:** Complete coordinate pairs are distinct, yet $x$ or $y$ alone may repeat, so both sort and strictness details remain necessary.
- **Input mutation:** The method returns only the count but leaves `points` sorted by $(x,-y)$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Sorting costs $O(N\log N)$ time. The nested loops inspect all suffix pairs, totaling $N(N-1)/2=O(N^2)$ iterations. The total time complexity is $O(N^2)$, which dominates sorting and is suitable for $N\le1000$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
