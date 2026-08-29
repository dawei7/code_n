# Guided Example: Majority Element

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 2, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` of size `n`, return *the majority element*.

The objective is to compute `3` from `{"nums": [3, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace full counting with pair cancellation

The majority element appears more than half the time. Imagine repeatedly
removing pairs of different values from the array. Every such pair removes at
most one occurrence of the true majority and exactly one non-majority
occurrence.

Because the majority begins with more occurrences than all other values
combined, it cannot be completely eliminated by these opposite-value pairs.
After all possible cancellations, the surviving value must be the majority.

Boyer–Moore voting performs this cancellation in one left-to-right pass without
physically deleting elements. `m` is the current candidate and `cnt` is its
uncancelled balance.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Start a new candidate when the balance is empty

When `cnt == 0`, all elements represented by the previous voting segment have
been paired away. The current number `x` begins a new segment, so the source
sets `m = x` and `cnt = 1`.

The earlier balanced prefix can be forgotten. If it contained some occurrences
of the true majority, it also contained the same number of other values paired
against them. Removing equal numbers from the two sides of the majority
inequality cannot make a different value become the true global majority.

The initialization `cnt = m = 0` is only placeholder state. Since the input is
nonempty and the first iteration sees `cnt == 0`, `m` is replaced by
`nums[0]` before the placeholder could be returned.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Update the balance for later values

When a candidate is active, seeing the same value increments `cnt`. Seeing a
different value decrements it. A decrement conceptually pairs that different
element with one currently unmatched occurrence of `m`.

The counter is not the candidate's total frequency in the entire prefix. It is
the net surplus of candidate occurrences after cancellations within the
current unresolved segment. That is why it can fall back to zero even when the
candidate appeared several times earlier.

The source uses a special branch when zero: it assigns the candidate and count
one directly. Otherwise, the conditional expression adds either one or
negative one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Frequency map:** Count every value and return the one above half. It is $O(n)$ time but can use $O(n)$ space.
- **Sorting:** The majority must occupy sorted index `n // 2`, but sorting costs $O(n\log n)$ time and may mutate the input.
- **Bit counting:** Reconstruct the majority bit by bit in linear time for a fixed integer width, with more implementation complexity around negatives.
- **Divide and conquer:** Combine half-majority candidates, generally taking $O(n\log n)$ time.
- **One element:** It immediately becomes the candidate and is returned.
- **Candidate changes:** A temporary candidate need not be the true majority; only the final guarantee matters.
- **Counter meaning:** It is a cancellation balance, not a global occurrence count.
- **Negative values:** Equality-only voting handles them unchanged.
- **No guaranteed majority:** A second counting pass would be required to validate the candidate.
- **Missing typing import:** `List` must be supplied for standalone evaluation of annotations.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of elements. The loop examines each value once and does
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
