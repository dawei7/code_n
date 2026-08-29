# Guided Example: Maximum Students on a Single Bench

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"students": [[1, 2], [2, 2], [3, 3], [1, 3], [2, 3]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array of student data `students`, where $\text{students}[i] = [\text{student}_{id}, \text{bench}_{id}]$ represents that student $\text{student}_{id}$ is sitting on the bench $\text{bench}_{id}$.

The objective is to compute `3` from `{"students": [[1, 2], [2, 2], [3, 3], [1, 3], [2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Count distinct student IDs separately for each bench.** Each input row says that one student is associated with one bench. Repeated copies of the same pair must count only once, while the same student appearing on different benches counts once on each of those benches.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"students": [[1, 2], [2, 2], [3, 3], [1, 3], [2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

This is exactly the behavior of a mapping from bench ID to a set of student IDs. The source uses `defaultdict(set)` so the first access to a new bench automatically creates an empty set.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"students": [[1, 2], [2, 2], [3, 3], [1, 3], [2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count every row:** A numeric counter per bench would overcount duplicate student-bench pairs.
- **Deduplicate all pairs globally first:** A set of tuples followed by bench counts is correct but less direct than one set per bench.
- **Sort pairs:** Sorting by bench and student allows a linear unique scan after $O(n\log n)$ sorting; hashing avoids that cost.
- **Boolean matrix:** With the stated IDs it is possible, but allocates for all combinations even when input is sparse.
- **Empty input:** The explicit early return avoids an invalid empty `max` call.
- **One bench:** Its set size is returned directly.
- **Repeated identical rows:** Set insertion keeps one student occurrence.
- **Same student on multiple benches:** Each bench owns a different set, so the student counts on each.
- **Tied benches:** Only the maximum count is requested, so no bench ID tie-break is needed.
- **Input preservation:** The method reads rows without sorting or modifying `students`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\lvert\texttt{students}\rvert$. Each row performs one expected-$O(1)$ dictionary lookup and set insertion. Computing all set lengths visits each distinct bench key, at most $n$. Total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
