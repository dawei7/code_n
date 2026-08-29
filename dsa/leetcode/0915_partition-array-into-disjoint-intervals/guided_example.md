# Guided Example: Partition Array into Disjoint Intervals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 0, 3, 8, 6]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, partition it into two (contiguous) subarrays `left` and `right` so that:

The objective is to compute `3` from `{"nums": [5, 0, 3, 8, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

A partition after the first `i` elements is valid exactly when

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 0, 3, 8, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
\max(\texttt{nums}[0:i])
\le
\min(\texttt{nums}[i:n]).
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The solution precomputes suffix minima so each possible split can be checked while scanning prefix maxima from left to right. The first valid split is automatically the one with the smallest left side.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 0, 3, 8, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One-pass constant-space method:** Track the current left maximum, global maximum seen, and boundary; extend the boundary whenever a later value is below the left maximum. This matches the manifest's $O(1)$ space.
- **Prefix maxima plus suffix minima arrays:** Precompute both and test splits. It is clear but uses two $O(n)$ arrays instead of one.
- **Try every pair across every split:** This can cost $O(n^3)$ and ignores extreme summaries.
- **Sort values:** Sorting destroys contiguity and original split positions.
- **Smallest valid left size one:** The first test returns immediately.
- **Equal boundary values:** The condition allows equality, so `mx <= mi[i]` is correct.
- **Repeated numbers:** Minima and maxima naturally handle them.
- **Guaranteed partition:** Ensures return before the empty-right sentinel split.
- **Nonnegative values:** Justifies `mx = 0`; broader inputs need a different initialization.
- **Two elements:** The only legal split is after the first element and is guaranteed valid by the test data.
- **Suffix sentinel:** Infinity makes the recurrence simple but should not be used to accept an empty right side.
- **Input unchanged:** The solution reads values and builds summaries without rearranging the array.
- **Minimality:** Early return is correct only because split sizes are scanned from smallest to largest.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The backward suffix pass and forward prefix pass are both linear.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
