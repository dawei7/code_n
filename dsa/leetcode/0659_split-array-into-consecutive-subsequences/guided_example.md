# Guided Example: Split Array into Consecutive Subsequences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 3, 4, 5]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` that is **sorted in non-decreasing order**.

The objective is to compute `true` from `{"nums": [1, 2, 3, 3, 4, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store only what future numbers need to know

Every constructed subsequence is consecutive, so after processing some prefix of the sorted input, a future value needs only two facts about a subsequence:

- the value at which it currently ends;
- its current length.

The earlier members are determined implicitly by those facts and are not needed to decide whether the next number can extend it.

The exact solution uses `d[end_value]` as a min-heap of the lengths of all subsequences currently ending at that value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 3, 4, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why heaps are grouped by ending value

A current number `v` can extend only a subsequence ending at `v - 1`. It cannot extend one ending at `v` because the next value must be exactly one larger, and it cannot extend a smaller ending value because that would create a gap.

Looking directly at `d[v - 1]` therefore finds exactly the eligible chains. Grouping by ending value avoids searching through unrelated subsequences.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Extend the shortest eligible chain

If `d[v - 1]` is nonempty, the solution removes its smallest length with `heappop`, adds one, and pushes the new length into `d[v]`. This moves that subsequence's endpoint from `v - 1` to `v`.

Choosing the shortest eligible chain is the critical greedy rule. A short chain is in greater danger of ending below the required length three. A longer chain that is already valid, or closer to validity, can more safely be left unchanged.

For example, suppose chains of lengths two and three both end at two, and the current value is three. Extending the length-three chain would leave the length-two chain invalid if no more threes appear. Extending the length-two chain makes both lengths three.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 3, 4, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Remaining-frequency and tails maps:** First count unused values. For each number, extend an existing chain ending at the previous value if possible; otherwise reserve the next two values to start a valid length-three chain. This gives expected `O(N)` time and matches the manifest.
- **Global heap of start/end pairs:** Store all subsequences ordered by endpoint and length. It works but is more complicated than separate heaps keyed directly by endpoint.
- **Store complete subsequence lists:** This uses unnecessary memory and copying. Endpoint plus length is sufficient metadata for decisions and validation.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N log N)$. Let `N` be the number of input elements.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
