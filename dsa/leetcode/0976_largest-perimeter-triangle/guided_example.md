# Guided Example: Largest Perimeter Triangle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 2]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return *the largest perimeter of a triangle with a non-zero area, formed from three of these lengths*. If it is impossible to form any triangle of a non-zero area, return `0`.

The objective is to compute `5` from `{"nums": [2, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort lengths so the best candidate is local

For positive side lengths `a <= b <= c`, a non-degenerate triangle exists exactly when:

`a + b > c`.

The other triangle inequalities hold automatically because positive `c` is at least each smaller side. Equality would form a flat, zero-area shape, so the comparison must be strict.

After sorting `nums` in ascending order, the solution scans possible largest sides from right to left and tests the two immediately preceding lengths.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why use the two largest smaller sides

Fix largest candidate `c = nums[i]`.

Among every pair selected from indices below `i`, the largest possible sum is `nums[i - 1] + nums[i - 2]`. If even this pair does not exceed `c`, no smaller pair can satisfy the triangle inequality.

Therefore, for a fixed largest side, checking only its two immediate predecessors is sufficient.

If they do satisfy the inequality, they also give the largest possible perimeter among triangles whose largest side is `c`, because replacing either with a smaller length can only reduce the sum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the first valid triple is globally best

The scan starts with the largest array value and moves left.

The first valid triple uses consecutive sorted values `nums[i - 2], nums[i - 1], nums[i]`. Any candidate considered later has largest side at most `nums[i - 1]` and its other sides no larger than the corresponding already-considered high values.

More directly, any triple whose largest index is below `i` uses three values drawn from a smaller sorted prefix. Its perimeter cannot exceed the sum of the three consecutive values at the first successful index.

Thus the method can return immediately rather than collecting every valid triangle.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check every triple:** `O(N^3)` and ignores sorted dominance.
- **Check every pair for each largest side:** `O(N^2)`; the two largest smaller values are always best.
- **Equality case:** `a + b = c` is degenerate and must fail.
- **Exactly three lengths:** Perform one triangle test.
- **Duplicate lengths:** They are separate usable sides and sorting handles them.
- **Very large side:** If the next two largest cannot exceed it, no pair for that side can.
- **No valid triangle:** Return zero.
- **First valid early return:** Safe because the scan is in descending perimeter opportunity.
- **Positive-length guarantee:** Avoids separate checks for zero or negative sides.
- **Input mutation:** `nums.sort()` changes original order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N log N)$. Let `N` be length count.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
