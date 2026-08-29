# Guided Example: Third Maximum Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 2, 1]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return *the **third distinct maximum** number in this array. If the third maximum does not exist, return the **maximum** number*.

The objective is to compute `1` from `{"nums": [3, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track ranks, not occurrences

The problem asks for the third distinct maximum. Repeated appearances of the same value do not create additional ranks. For example, in `[2,2,3,1]`, the two copies of `2` together occupy only the second-distinct-maximum position.

The solution makes one pass while storing the three largest distinct values seen so far:

- `m1` is the largest;
- `m2` is the second largest; and
- `m3` is the third largest.

All three begin at negative infinity, written `-inf`, meaning that the corresponding rank has not yet been filled. Negative infinity is smaller than every permitted integer, including $-2^{31}$. This distinction matters: using the smallest legal integer as a sentinel would be ambiguous if that exact value appeared in the input.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Discard duplicates before ranking

For each `num`, the condition `num in [m1, m2, m3]` checks whether that distinct value already occupies a tracked rank. If so, the iteration continues without changing anything.

This duplicate check must occur before the comparisons. Suppose `m1` is already `5` and another `5` arrives. If it were processed as a new contender, shifting ranks could incorrectly place `5` in both `m1` and `m2`, turning occurrences into ranks. Skipping it preserves strict ordering among all filled slots.

The temporary list contains exactly three items, so membership testing is constant work. Its size does not depend on `nums`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Insert a new distinct value into the correct position

After duplicates have been removed, there are four possible placements.

If `num > m1`, the new value is the largest seen so far. The old largest becomes second, and the old second becomes third. The simultaneous assignment

`m3, m2, m1 = m2, m1, num`

performs that full shift. Python evaluates all right-hand values before assigning the left-hand variables, so the old values are not overwritten prematurely.

If the first condition is false but `num > m2`, then `num` is smaller than `m1` yet larger than the old second maximum. It belongs in `m2`, and the old `m2` moves to `m3`:

`m3, m2 = m2, num`

If both earlier conditions are false but `num > m3`, it lies below the first two ranks and above the current third, so only `m3` changes.

If none succeeds, `num` is smaller than all three tracked maxima. It cannot affect the requested third maximum and is ignored.

Strict `>` comparisons are correct because equality was already handled by the duplicate check. They also maintain the ordering $m1 > m2 > m3$ among real stored values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort in descending order:** After sorting, scan past duplicates until the third distinct value is reached. This is straightforward but costs $O(n\log n)$ time and may mutate the input.
- **Convert the whole input to a set:** Distinctness becomes automatic, after which sorting or repeated maximum selection finds the answer. The set can require $O(n)$ extra space, unlike the three-slot solution.
- **Min-heap of at most three values plus a set:** Keep the three largest distinct values and discard the smallest when a larger contender arrives. Because the heap never exceeds size three, time remains $O(n)$, but coordinating heap membership is more machinery than three variables.
- **Use a legal integer as the empty sentinel:** This is unsafe. The minimum allowed value, $-2^{31}$, can genuinely be the third maximum. `-inf` cannot collide with any input integer.
- **One distinct value:** Only `m1` is filled, so the algorithm returns that maximum.
- **Exactly two distinct values:** `m3` remains `-inf`, and the larger value in `m1` is returned.
- **Exactly three distinct values:** All slots fill, and `m3` is returned even if it equals the smallest legal integer.
- **Many duplicates:** Every duplicate of a tracked maximum is skipped, so frequency never affects rank.
- **Strictly decreasing input:** Values fill `m1`, then `m2`, then `m3`; later smaller values are ignored.
- **Strictly increasing input:** Each new value shifts the previous first and second maxima down one rank, leaving the correct last three distinct values.
- **Negative-only input:** Negative infinity remains smaller than every real value, so comparisons and fallback logic work without a special case.
- **Simultaneous assignment semantics:** Performing the shifts as separate assignments in the wrong order could lose an old maximum. Python's tuple assignment preserves all old right-hand values before updating any slot.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. The loop visits each element exactly once. Duplicate testing checks three slots, and rank insertion uses a constant number of comparisons and assignments. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
