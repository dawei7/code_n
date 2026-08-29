# Guided Example: Count Pairs Whose Sum is Less than Target

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-1, 1, 2, 3, 1], "target": 2}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **0-indexed** integer array `nums` of length `n` and an integer `target`, return *the number of pairs* `(i, j)` *where* $0 \le i < j < n$ *and* $\text{nums}[i] + \text{nums}[j] < target$.

The objective is to compute `3` from `{"nums": [-1, 1, 2, 3, 1], "target": 2}` while avoiding redundant calculations and unnecessary overhead.

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

**Sort so each pair can be counted through one endpoint.** The original index order does not affect whether two values sum below `target`; the condition only requires two distinct positions. Sorting rearranges positions but preserves the multiset of values and therefore preserves the number of unordered index pairs satisfying the sum inequality.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-1, 1, 2, 3, 1], "target": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact source sorts `nums` in place. It then treats each sorted index `j` as the right endpoint of a pair and counts how many earlier indices `i < j` work with it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Turn the sum condition into a threshold for the left value.** For current value `x = nums[j]`,

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-1, 1, 2, 3, 1], "target": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two pointers after sorting:** If the smallest plus largest value is below target, that smallest value pairs with every position through the largest, so count the whole range and advance the left pointer; otherwise decrease the right pointer. This gives $O(n)$ after sorting and matches the manifest's summary.
- **Brute-force nested loops:** It takes $O(n^2)$ time and $O(1)$ space. The small $n\le50$ bound makes it feasible, but it does not exploit ordering.
- **Frequency table over the small value range:** Since values lie between negative fifty and fifty, counts can be combined in constant-range time, with careful handling of equal-value pairs.
- **Strict inequality:** A sum exactly equal to target must be excluded; `bisect_left` enforces this boundary.
- **Negative target and values:** The algebraic threshold and sorted order work without any positivity assumption.
- **Duplicate values:** Every occurrence is a separate index, and lower bound counts each eligible occurrence.
- **First sorted position:** Its prefix is empty, binary search returns zero, and no pair is added.
- **All pairs valid:** For every `j`, the returned count is `j`, summing to $n(n-1)/2$.
- **No pairs valid:** Every lower bound is zero and the answer remains zero.
- **Single-element array:** There are no two-index pairs, so the one loop iteration adds zero.
- **Input order:** Sorting mutates `nums`, even though the returned count does not depend on order.
- **Current index exclusion:** The `hi=j` argument is necessary; searching the entire list could count the current element or later elements and duplicate pairs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Let $n$ be the number of values. Python sorting takes $O(n\log n)$ worst-case time. The loop runs $n$ times, and every `bisect_left` over a prefix takes $O(\log n)$ time. The counting phase is therefore $O(n\log n)$, and total time remains $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
