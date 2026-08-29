# Guided Example: Queue Reconstruction by Height

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"people": [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]}`
- **Required output:** `[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of people, `people`, which are the attributes of some people in a queue (not necessarily in order). Each $\text{people}[i] = [h_{i}, k_{i}]$ represents the $i^{\text{th}}$ person of height $h_{i}$ with **exactly** $k_{i}$ other people in front who have a height greater than or equal to $h_{i}$.

The objective is to compute `[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]` from `{"people": [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Place people whose constraints are easiest to isolate first

A person `[h, k]` cares only about people in front whose height is at least `h`. Shorter people are invisible to this constraint.

This suggests placing taller people first. When a person of height `h` is processed, everyone already in the partial queue has height at least `h`. Therefore, inserting this person at list index `k` puts exactly `k` qualifying people before them.

Later insertions involve people no taller than the current person. Strictly shorter people do not change the current person’s count, even if inserted before them. This makes the greedy decision permanent.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"people": [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The exact sorting order

The method sorts with key



Negating height puts larger heights first. For equal height, ordinary ascending `k` order is used.

The equal-height tie rule is essential because people of the same height count one another. Processing smaller `k` first ensures that when another equal-height person with larger `k` is inserted, the equal-height people that must precede them are already available in the partial queue.

For example, among height-seven people `[7,0]` and `[7,1]`, `[7,0]` must be placed first. Inserting it at index zero gives one partial person. Inserting `[7,1]` at index one then places exactly one height-seven person before it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why insertion index equals `k`

At the moment `[h, k]` is processed, every person currently in `ans` is at least as tall as `h`. Python list index `k` means exactly `k` current entries lie before the inserted position. Since all of those entries qualify, the newly inserted person’s condition is satisfied immediately.

The input guarantee ensures reconstruction is possible, so the required insertion index is valid for the partial queue at that point.

The method performs



for each sorted person. The person pair itself is inserted; no new pair needs to be constructed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"people": [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fenwick tree over empty positions:** Sort shorter people first with an appropriate tie order and use a Fenwick tree to locate the required empty slot in $O(\log n)$. This realizes $O(n\log n)$ time but is much harder to explain and implement.
- **Balanced order-statistics sequence:** Supports insertion by rank in $O(\log n)$, preserving the same tall-first greedy idea. Python’s built-in list does not provide that bound.
- **Sort shortest first without empty-slot logic:** Direct insertion at `k` would be invalid because existing shorter people would not all count for the new person. Tall-first ordering is what makes list index equal the qualifying count.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the number of people.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
