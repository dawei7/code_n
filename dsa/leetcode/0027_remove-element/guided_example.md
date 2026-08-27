# Guided Example: Remove Element

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 2, 2, 3], "val": 3}`
- **Required output:** `{"return_value": 2, "prefix": [2, 2]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">**in-place**</a>. The order of the elements may be changed. Then return *the number of elements in *`nums`* which are not equal to *`val`.

The objective is to compute `{"return_value": 2, "prefix": [2, 2]}` from `{"nums": [3, 2, 2, 3], "val": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Interpret removal as writing a valid prefix

An array-backed Python list cannot physically discard arbitrary entries in constant time without shifting later elements. The custom judge does not require that. It asks for a count `k` and requires only `nums[:k]` to contain every original value not equal to `val`. Positions from `k` onward are unspecified.

The selected implementation therefore performs stable in-place compaction: scan every original value, copy each retained value into the next prefix position, and ignore each occurrence of `val`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 2, 2, 3], "val": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Let `k` be both a count and a destination

The source initializes `k = 0`. Before each scanned value `x`, the invariant is:

> `nums[:k]` contains exactly the already scanned values that are not equal to `val`, in their original relative order.

Because a prefix containing `k` values occupies indices zero through `k - 1`, index `k` is also the next free output position. This dual meaning avoids maintaining a separate write index and result count.

If `x == val`, the method performs no write and does not increment `k`. The retained prefix is unchanged, which is correct because this value must be excluded. If `x != val`, the source executes



The value is appended to the logical prefix and the next destination advances. This preserves the invariant.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source initializes `k = 0`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why mutating during `for x in nums` is safe

The loop reads source positions from left to right while writes move only to the left or remain at the current position. Before processing source index `i`, at most `i` earlier values have been retained, so `k <= i`. Therefore `nums[k] = x` never writes into an unvisited position after `i`.

The loop variable `x` receives the current value before the body writes anything. Overwriting an earlier array cell cannot change `x` or any future source value. This directionality is the key safety fact; a method that wrote beyond the current read position could destroy data before scanning it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"return_value": 2, "prefix": [2, 2]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 2, 2, 3], "val": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"return_value": 2, "prefix": [2, 2]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Swap with the active tail:** On an unwanted va:** - **Swap with the active tail:** On an unwanted value, replace it with the final unchecked value and shrink the active range. This can reduce writes when removals are rare but does not preserve order.
- **List comprehension or filtering:** It is concise but allocates $O(n)$ additional storage and does not implement the requested in-place prefix contract by itself.
- **Repeated deletion:** Removing individual Python-list elements shifts suffixes and can require $O(n^2)$ total time.
- **Empty input:** The loop performs no work and returns zero.
- **No occurrence of `val`:** Every value is written, possibly to its existing position, and `k = n`.
- **Every value equals `val`:** No write occurs; the returned logical prefix is empty.
- **Repeated retained values:** They are all kept because only equality with `val` causes removal.
- **`val` outside the array's value range:** No element matches, so the full array remains meaningful.
- **Order:** This exact source preserves relative order even though the judge does not require it.
- **Tail:** Never inspect positions at or beyond the returned `k` as part of the filtered result.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)` and let $k$ be the number of retained occurrences.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
