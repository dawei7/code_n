# Guided Example: Most Frequent Number Following Key In an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 100, 200, 1, 100], "key": 1}`
- **Required output:** `100`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`.** **You are also given an integer `key`, which is present in `nums`.

The objective is to compute `100` from `{"nums": [1, 100, 200, 1, 100], "key": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generate adjacent pairs directly

`pairwise(nums)` yields

`(nums[0], nums[1])`, `(nums[1], nums[2])`, and so on through the final adjacent pair.

Each yielded pair is assigned to `a, b`. Here `a` represents `nums[i]` and `b` represents `nums[i + 1]` for one index `i`.

This avoids manual index arithmetic while covering exactly the allowed range from zero through `len(nums) - 2`. The last array element appears as a follower but never as the first component of a nonexistent pair beyond the array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 100, 200, 1, 100], "key": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filter on the key position

The code enters its counting block only when `a == key`. In that case, `b` is precisely a target that immediately follows an occurrence of `key`, so `cnt[b]` increases by one.

If `a` is not the key, the adjacent value `b` is irrelevant for this problem and no counter changes.

Notice that `b` may itself equal `key`. Consecutive copies of the key are valid: in `[2,2,2]`, the second two follows the first, and the third follows the second, so target two receives two votes.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain the best count online

`mx` stores the greatest follower frequency observed so far, and `ans` stores the follower that achieved it.

After incrementing `cnt[b]`, the code compares it with `mx`. If it is strictly larger, both `mx` and `ans` are updated. If it merely ties the current maximum, the stored answer remains unchanged.

The contract guarantees that the final maximum target is unique. Temporary ties during the scan therefore do not create ambiguity in the returned result. The eventual unique winner must at some point raise its count above every competitor and trigger an update.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `100` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 100, 200, 1, 100], "key": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `100` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count then call `most_common`:** First build all follower counts, then select the maximum. It is correct but performs a separate pass over distinct targets.
- **Fixed frequency array:** Values are at most 1000, so a 1001-entry list can replace the Counter and make the constant-space interpretation explicit.
- **Manual index loop:** Iterate `i` through `range(len(nums) - 1)` and inspect `nums[i + 1]`. It has identical behavior.
- **Consecutive keys:** The key itself is a valid target when one key immediately follows another.
- **Key at the final index:** That occurrence creates no pair because nothing follows it.
- **Several key occurrences:** Each immediate follower occurrence contributes independently, even when positions share the same target value.
- **Temporary tie:** Strict comparison keeps the earlier leader, but the guaranteed unique final maximum eventually overtakes all others.
- **Unique final winner:** No explicit tie-breaking rule is needed.
- **Minimum array length two:** There is one adjacent pair, which is counted if its first value is the key.
- **Values unrelated to key:** Followers after non-key values never enter the Counter.
- **Lazy adjacency:** `pairwise` avoids an $O(n)$ list of tuples.
- **Input preservation:** The array and key are only read.
- **Fixed-domain space:** The Counter is logically bounded by 1000 possible positive values under the contract.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. `pairwise` produces $n-1$ adjacent pairs, and each iteration performs expected constant-time Counter operations. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
