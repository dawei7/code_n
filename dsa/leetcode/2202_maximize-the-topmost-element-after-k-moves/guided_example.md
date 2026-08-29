# Guided Example: Maximize the Topmost Element After K Moves

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 2, 2, 4, 0, 6], "k": 4}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` representing the contents of a **pile**, where $\text{nums}[0]$ is the topmost element of the pile.

The objective is to compute `5` from `{"nums": [5, 2, 2, 4, 0, 6], "k": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Handle zero moves

If `k == 0`, no operation is allowed. The pile remains unchanged and `nums[0]` is still top.

Returning immediately also avoids expressions such as `nums[:k - 1]` with a negative stop having unintended meaning.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 2, 2, 4, 0, 6], "k": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand a one-element pile

When `n == 1`, operations alternate between two forced states:

- one removal makes the pile empty;
- the only possible addition restores that same value.

After an odd number of moves the pile is empty, so the answer is `-1`. After an even number, the sole value is back on top.

No different removed value exists, so this parity behavior cannot be bypassed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Restore one of the first `k - 1` elements

Suppose the final, $k$-th move adds a removed value back. Before that move, at most the first `k - 1` original elements can have been removed through straightforward popping.

Any value at original index zero through `k - 2` can be made available and then restored on the final move. The best such candidate is

`max(nums[: k - 1], default=-1)`.

The endpoint is exclusive, so index `k - 1` is not included. If only `k - 1` removals expose that element, the final move must still be performed; restoring something covers it again.

The `default=-1` handles `k = 1`, where the slice is empty and no previously removed value can be restored after zero earlier moves.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 2, 2, 4, 0, 6], "k": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generator over indices:** Compute the restoration maximum without slicing to attain $O(1)$ auxiliary space.
- **Simulate pile states:** Explicit move search branches exponentially and is unnecessary once final-move possibilities are characterized.
- **`k = 0`:** The original top is forced.
- **One element, odd `k`:** The pile ends empty and returns `-1`.
- **One element, even `k`:** Alternating removal and restoration returns the original value.
- **`k = 1` with several elements:** No restoration candidate exists; one removal exposes `nums[1]`.
- **`k < n`:** Both restoration and exposure candidates may compete.
- **`k == n`:** Consecutive removals empty the pile, so only restoration candidates matter.
- **`k > n`:** Extra cycles allow restoration; the slice clamps safely at array length.
- **Zero-valued elements:** They are valid top candidates and still exceed the sentinel `-1`.
- **Index `k - 1`:** It cannot remain top because one exact move is still required.
- **Input preservation:** The slice is copied and the original list is not mutated.
- **Manifest discrepancy:** The algorithmic idea is constant-state, but the exact slice uses linear temporary space.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\min(n,k)$. Let $q=\min(n,\max(0,k-1))$ be the slice length. Finding its maximum and copying `nums[:k - 1]` take $O(q)$ time. All other operations are constant, so time is $O(\min(n,k))$.
- **Auxiliary Space Complexity:** $O(\min(n,k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
