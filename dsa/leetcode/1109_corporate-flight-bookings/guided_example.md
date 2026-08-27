# Guided Example: Corporate Flight Bookings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"bookings": [[1, 2, 10], [2, 3, 20], [2, 5, 25]], "n": 5}`
- **Required output:** `[10, 55, 45, 25, 25]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` flights that are labeled from `1` to `n`.

The objective is to compute `[10, 55, 45, 25, 25]` from `{"bookings": [[1, 2, 10], [2, 3, 20], [2, 5, 25]], "n": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A booking adds the same value across an inclusive range

Booking `[first, last, seats]` contributes `seats` to every flight label from `first` through `last`, inclusive. Updating each flight separately would repeat work when ranges are long.

A difference array records only where a contribution begins and where it stops. Later, one prefix sum reconstructs the total active contribution at every flight.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"bookings": [[1, 2, 10], [2, 3, 20], [2, 5, 25]], "n": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Translate one-based flight labels to zero-based indices

The answer list has indices zero through `n - 1`, while flights are labelled one through `n`. Therefore, a booking begins at array index `first - 1`. The update:

`ans[first - 1] += seats`

means that every prefix sum from this point onward includes the booking.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The answer list has indices zero through `n - 1`, while flig... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Cancel immediately after the inclusive endpoint

The booking must remain active through flight `last` and disappear before flight `last + 1`. In zero-based indexing, flight `last + 1` corresponds to array index `last`. Thus:

`ans[last] -= seats`

marks the cancellation.

When `last == n`, there is no array position after the final flight. The booking should remain active through the end, so no cancellation entry is needed. The guard `if last < n` prevents an out-of-range write and expresses exactly that boundary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[10, 55, 45, 25, 25]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"bookings": [[1, 2, 10], [2, 3, 20], [2, 5, 25]], "n": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[10, 55, 45, 25, 25]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Direct range updates:** Add seats to every cov:** - **Direct range updates:** Add seats to every covered flight for every booking. It is easy to understand but can require $O(Bn)$ time.
- **Fenwick tree:** Range additions and point queries can solve the problem, but all bookings are known before one final output pass, so a difference array is simpler.
- **Segment tree:** Supports more dynamic query patterns than needed and adds substantial implementation overhead.
- **Booking for one flight:** Start and cancellation are adjacent, so the contribution appears in exactly one prefix value.
- **Booking through flight `n`:** No cancellation slot exists or is needed; the guard skips it.
- **Booking starting at flight one:** The start marker is written at index zero.
- **Overlapping bookings:** Their active contributions add in the prefix total.
- **Identical bookings:** Each input row is a separate reservation and both contributions are counted.
- **Width exactly all flights:** A booking from one through `n` adds once at index zero and remains active to the end.
- **Positive seat counts:** Totals never need special handling for negative reservations; only cancellation markers are negative.
- **Input order:** Boundary additions commute, so sorting bookings is unnecessary.
- **One flight:** Every valid booking covers that flight, and all seat counts accumulate at the sole index.
- **Iterator conversion:** Returning `accumulate(ans)` directly would return an iterator rather than the required list, so `list` is essential.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B)$. Let $B$ be the number of bookings. Recording two constant-time boundary updates per booking costs $O(B)$. Prefix accumulation visits the $n$ flight positions once, costing $O(n)$. Total time is $O(B+n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
