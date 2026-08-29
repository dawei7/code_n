# Guided Example: Sort the Students by Their Kth Score

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"score": [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], "k": 2}`
- **Required output:** `[[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a class with `m` students and `n` exams. You are given a **0-indexed** `m x n` integer matrix `score`, where each row represents one student and $\text{score}[i][j]$ denotes the score the $i^{\text{th}}$ student got in the $j^{\text{th}}$ exam. The matrix `score` contains **distinct** integers only.

The objective is to compute `[[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]` from `{"score": [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat each row as one indivisible student record

Each row stores all exam scores for one student. Sorting students must move entire rows together; sorting individual columns would destroy the relationship between a student and their other scores.

The selected key for row `x` is `x[k]`, the score in the requested zero-indexed exam.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"score": [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reverse order through a negative key

Python's `sorted` orders keys from smallest to largest. The lambda returns:

`-x[k]`.

If one student has a larger exam score, its negative is smaller and appears earlier.

For scores 11, 9, and 3, keys are $-11$, $-9$, and $-3$, producing the required descending score order.

An equivalent implementation could use `reverse=true` with key `x[k]`. The exact source chooses negation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Return whole rows

`sorted(score,...)` returns a new outer list containing the original row objects in reordered sequence.

No row's internal exam-score order changes. Column `k` remains the ranking exam, and every other exam score travels with the same student row.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"score": [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`reverse=true`:** `sorted(score,key=lambda row:row[k],reverse=true)` avoids negating keys.
- **In-place `sort`:** It would mutate the outer input list instead of returning a separately ordered list.
- **One student:** The only row is returned.
- **One exam:** `k` must be zero and rows sort by their sole value.
- **Distinct scores:** No tie-breaker is needed.
- **Whole-row movement:** Never sort just the kth column.
- **Zero-indexed exam:** Use `x[k]` directly.
- **Large scores:** Negation is exact in Python.
- **Other columns:** They do not affect rank but remain attached to the student.
- **Row sharing:** The returned outer list references original unmodified rows.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m log m)$. Let $m$ be the number of students. Computing keys costs $O(m)$. Comparison sorting costs $O(m\log m)$ time.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
