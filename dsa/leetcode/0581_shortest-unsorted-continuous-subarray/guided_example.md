# Guided Example: Shortest Unsorted Continuous Subarray

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 6, 4, 8, 10, 9, 15]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, you need to find one **continuous subarray** such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

The objective is to compute `5` from `{"nums": [2, 6, 4, 8, 10, 9, 15]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Creating the target arrangement

`arr = sorted(nums)` returns a new list containing the same values as `nums` in non-decreasing order. It does not mutate the input. Because sorting the whole original is the desired final condition, `arr` is an explicit model of the target arrangement.

Duplicates are handled naturally. Sorting does not require strict increase; equal adjacent values are valid. Comparing values position by position is sufficient even though equal elements are indistinguishable, because the sorted value sequence is unique as a sequence of values.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 6, 4, 8, 10, 9, 15]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Finding the first mismatch

The left pointer begins at zero:



As long as the original value already equals the target at `l`, that position does not need to be included. Advancing `l` skips the longest matching prefix. The guard `l <= r` prevents the pointers from crossing and then indexing beyond the unresolved interval.

When this loop stops, either all positions matched, or `l` is the first index where the original differs from sorted order. Every index before `l` is already fixed and can remain outside the subarray.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The left pointer begins at zero:



As long as the original ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Finding the last mismatch

The right pointer begins at the last index and moves left while values agree:



This skips the longest matching suffix without crossing the left pointer. If an unsorted interval exists, `r` finishes at its final mismatch. Every index after `r` already equals its final target value and need not be sorted.

The result is `r - l + 1`, the inclusive interval length. If the whole array was already sorted, the first loop advances `l` to $n$ while $r=n-1$. The second loop does not run because `l <= r` is false. The expression becomes $(n-1)-n+1=0$, correctly representing that no subarray needs sorting.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 6, 4, 8, 10, 9, 15]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Linear-time constant-space boundary discovery::** - **Linear-time constant-space boundary discovery:** Scan left-to-right while tracking the maximum seen; whenever a value is below that maximum, update the right boundary. Scan right-to-left while tracking the minimum seen; whenever a value is above that minimum, update the left boundary. This achieves the manifest’s $O(n)$ time and $O(1)$ space but is not the exact source shown here.
- **Monotonic stacks:** One increasing-stack pass finds the left boundary and one decreasing-stack pass finds the right. Time is $O(n)$ but stack space is $O(n)$.
- **Find disorder, then expand by its minimum and maximum:** Detect the first and last local inversions, find the interval’s minimum and maximum, and expand into the sorted prefix/suffix where needed. This is $O(n)$ and $O(1)$ but requires a careful multi-step proof.
- **Already sorted array:** Every position matches `arr`; crossed pointers make the returned length zero.
- **Single element:** It necessarily matches its sorted copy, so the answer is zero.
- **All values equal:** Non-decreasing order permits equality, every position matches, and the answer is zero.
- **Entire array reversed:** Usually the first and last positions mismatch, so the required interval is the whole array.
- **Duplicates near a boundary:** Looking only for a local inversion can choose a boundary that is too narrow. Comparing against the fully sorted sequence handles duplicate placement correctly.
- **Inclusive length:** Boundaries $l$ and $r$ are both included, so the formula must be $r-l+1$, not $r-l$.
- **Input preservation:** `sorted(nums)` returns a copy. Using `nums.sort()` would destroy the original before comparison unless another copy were made.
- **Metadata fidelity:** Do not describe this particular implementation as $O(n)$/$O(1)$. That improvement belongs to an alternative implementation, even though the manifest requests it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. Python’s `sorted` takes $O(n\log n)$ time in the general case and creates a new list of $n$ values. The two pointer scans together examine at most $O(n)$ positions. Sorting dominates, so the exact implementation takes $O(n\log n)$ time and $O(n)$ auxiliary space.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
