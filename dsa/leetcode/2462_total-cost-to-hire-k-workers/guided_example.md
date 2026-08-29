# Guided Example: Total Cost to Hire K Workers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"costs": [17, 12, 10, 2, 7, 2, 11, 20, 8], "k": 3, "candidates": 4}`
- **Required output:** `11`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `costs` where $\text{costs}[i]$ is the cost of hiring the $i^{\text{th}}$ worker.

The objective is to compute `11` from `{"costs": [17, 12, 10, 2, 7, 2, 11, 20, 8], "k": 3, "candidates": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only currently exposed workers are eligible

In each session, candidates come from the first `candidates` remaining workers and the last `candidates` remaining workers. Hiring from one side exposes one new worker from that same side of the still-hidden middle.

A min-heap stores each exposed worker as `(cost,index)`. Python compares tuples lexicographically, so it chooses smaller cost first and smaller original index on a tie, exactly matching the rule.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"costs": [17, 12, 10, 2, 7, 2, 11, 20, 8], "k": 3, "candidates": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Handle overlapping candidate sides

If `2*candidates >= n`, the first and last candidate regions cover every remaining worker from the beginning. After any hire, fewer workers remain, so all of them continue to be eligible. Each session simply chooses the globally cheapest remaining worker, breaking ties by index.

The exact shortcut sorts all costs and sums the first `k`. It does not include indices in the sort, but for total cost the tie-breaking choice among equal costs does not change the sum. Thus the shortcut returns the correct total.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Initialize disjoint exposed regions

When `2*candidates < n`, the left and right initial regions do not overlap. The source pushes indices 0 through `candidates-1` and `n-candidates` through `n-1` into one heap.

Pointers `l=candidates` and `r=n-candidates-1` delimit the hidden middle. `l` is the next unseen worker from the left, and `r` is the next unseen worker from the right.

Calling `heapify` after already using `heappush` is redundant but harmless: the list is already a heap, and heapifying preserves it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `11` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"costs": [17, 12, 10, 2, 7, 2, 11, 20, 8], "k": 3, "candidates": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `11` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two heaps:** Maintain separate left and right min-heaps, compare their tops, and replenish the chosen side. This is equivalent but requires explicit cross-heap tie handling by index.
- **Sort all workers unconditionally:** It ignores exposure rules when candidate regions do not cover the middle, so it is valid only in the overlap shortcut.
- **Repeated linear scans:** Searching exposed workers in every session costs $O(kc)$, which can be quadratic.
- **Candidate regions overlap:** The shortcut prevents inserting the same worker twice.
- **Equal costs:** Tuple ordering selects the smaller original index in the heap branch.
- **No hidden middle:** After `l>r`, popping continues without replenishment.
- **Hire every worker:** The heap eventually exposes and pops all indices, and the total becomes `sum(costs)`.
- **One candidate per side:** The heap compares only the current leftmost and rightmost remaining workers.
- **Tie behavior in shortcut:** Equal-cost worker order does not affect the requested total, even though the exact hired identities would follow indices.
- **Input preservation:** The heap branch does not mutate `costs`; the shortcut uses `sorted` rather than in-place sorting.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(c)$. Let $c=\texttt{candidates}$. In the disjoint branch, initialization handles $2c$ workers. The heap size stays $O(c)$. Each of $k$ sessions performs one pop and at most one push, each $O(\log c)$, for $O((c+k)\log c)$ time and $O(c)$ heap space.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
