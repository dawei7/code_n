# Guided Example: Minimum Array Length After Pair Removals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `num` sorted in non-decreasing order.

The objective is to compute `0` from `{"nums": [1, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

**What one operation really changes.** An operation removes two elements only when their values are different. The positions of those elements do not otherwise matter: after deletion, the remaining elements keep their order, but no future choice depends on adjacency. It is therefore useful to forget the individual indices and keep only the frequency of each distinct value. If the multiset has frequencies such as `4, 3, 1`, one operation chooses two different frequency buckets and subtracts one from each.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The protected solution implements exactly that multiset view. `Counter(nums)` creates the frequency table. It then negates every frequency and places the negated values in `pq`. Python's heap is a min-heap, so the most negative entry represents the largest remaining frequency. Negation is the standard way to use a min-heap as a max-heap.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Why always take the two largest buckets.** The obstruction is concentration. A value cannot be paired with another copy of itself, so copies of the most frequent value need copies of all other values as partners. If one bucket is allowed to remain much larger than the rest, those surplus copies can eventually become impossible to remove. Taking one item from each of the two largest buckets reduces the greatest concentrations as evenly as possible.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sorted-run formula:** Because `nums` is already non-decreasing, scan once to find the maximum run length $m$, then return $\max(n\bmod 2,2m-n)$. This genuinely achieves $O(n)$ time and $O(1)$ auxiliary space and is the best match for the manifest.
- **Two-pointer pairing:** Pair elements from the first half with sufficiently larger elements from the second half. This also exploits sorted order, but the frequency formula is shorter and makes the unavoidable remainder more explicit.
- **Only one distinct value:** The heap starts with one entry, the loop never executes, and the answer remains $n$. No two equal values form a legal pair.
- **Perfectly balanceable even length:** When the largest frequency is at most $n/2$, every item can be removed and the result is `0`.
- **Perfectly balanceable odd length:** Pair removals always change the length by two, so an odd array cannot become empty. The best possible remainder is `1`.
- **Large majority:** If one value occurs more often than all other values combined, every minority copy is consumed as a partner and exactly $2m-n$ majority copies remain.
- **Input ordering:** The heap solution does not actually use the promised sorted order; it remains correct for an unsorted array. The constant-space formula alternative does rely on sorted runs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+n\log u)$. Let $n$ be the number of elements and $u$ the number of distinct values. Building the counter takes expected $O(n)$ time and stores $u$ entries. Creating and heapifying the frequency list takes $O(u)$ time. Every loop iteration removes one legal pair, so there are at most $\lfloor n/2\rfloor$ iterations. Each iteration performs two heap pops and up to two pushes, each costing $O(\log u)$ in the worst case. The exact implementation therefore takes $O(n\log u)$ worst-case time after counting, or $O(n+n\log u)=O(n\log u)$ overall.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
