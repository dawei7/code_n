# Guided Example: 4Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 0, -1, 0, -2, 2], "target": 0}`
- **Required output:** `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` of `n` integers, return *an array of all the **unique** quadruplets* `[nums[a], nums[b], nums[c], nums[d]]` such that:

The objective is to compute `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]` from `{"nums": [1, 0, -1, 0, -2, 2], "target": 0}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn an unordered search into an ordered one

The task asks for value quadruplets, but the four values must come from four distinct array indices. Trying every index quadruple would use four nested loops and take $O(n^4)$ time. The selected implementation removes one entire factor of $n$ by sorting `nums`, explicitly choosing the first two positions, and finding the remaining two positions with a two-pointer scan.

Sorting is the key that makes pointer movement meaningful. After `nums.sort()`, moving a pointer to the right cannot decrease its value, and moving a pointer to the left cannot increase its value. Equal values also become adjacent, which lets the code suppress duplicate value quadruplets without storing all answers in a set.

The sort changes the caller's list in place. That is acceptable for the problem contract because only the returned quadruplets are specified; preserving the original ordering of `nums` is not required.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 0, -1, 0, -2, 2], "target": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Give the four positions a permanent order

The implementation always maintains indices

$$
i < j < k < l.
$$

The outer loop chooses `i`, the inner loop chooses `j`, and then `k = j + 1` and `l = n - 1` delimit the remaining suffix. Because each pointer occupies a different ordered position, a reported quadruplet can never reuse an index. No additional distinct-index check is needed.

The initial guard returns an empty list when `n < 4`. Four distinct indices cannot exist in that case. The loop bounds also reflect how many positions must remain: `i` stops before the last three indices, while `j` stops before the last two.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The implementation always maintains indices

$$
i < j < k < ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Fix two values and reduce 4Sum to sorted 2Sum

For one fixed pair `nums[i]` and `nums[j]`, the code starts `k` at the smallest available suffix value and `l` at the largest. It computes the complete candidate sum



and compares it with `target`.

- If `x < target`, the sum is too small. Decreasing `l` would make the sum no larger, so that cannot help. The only useful move is `k += 1`, which tries a value that is at least as large.
- If `x > target`, the sum is too large. Increasing `k` would make it no smaller, so that cannot help. The only useful move is `l -= 1`, which tries a value that is at most as large.
- If `x == target`, the four sorted values form a valid answer. The code appends them, then moves both `k` and `l` inward because that exact endpoint pair has already been consumed.

These moves do not skip a possible solution. Suppose `x < target`. With the current `k`, every index between `k + 1` and `l` used as the right endpoint has value at most `nums[l]`, so every such pair sum is also too small. Thus no solution can still use that `k`. The argument is symmetric when `x > target`: no solution can still use the current `l`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 0, -1, 0, -2, 2], "target": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Four nested loops:** It is conceptually direct:** - **Four nested loops:** It is conceptually direct but costs $O(n^4)$ and still needs careful value-level deduplication.
- **Recursive generalized k-Sum:** Fix one value recursively until reaching a two-pointer 2Sum base case. It generalizes cleanly to 5Sum and beyond, but the direct two-loop form here is simpler for exactly four values.
- **Pair-sum hash table:** Store index pairs by their sum and match complementary sums. It can reduce repeated arithmetic, but may require $O(n^2)$ or more memory and careful enforcement of non-overlapping indices and unique outputs.
- **Hash-set 2Sum after fixing two values:** This preserves $O(n^3)$ time but uses extra per-scan storage and makes deterministic duplicate handling less transparent than sorted pointers.
- **Fewer than four values:** The explicit `n < 4` guard returns `[]` immediately.
- **Exactly four values:** The loops examine the only possible index quadruple and return it precisely when its sum equals `target`.
- **All values equal:** Enough copies may form one answer, as five copies of `2` with target `8` do; duplicate skipping returns `[[2, 2, 2, 2]]` only once.
- **Negative values and a negative target:** Pointer monotonicity depends on sorted order, not on values being positive, so the same comparisons remain valid.
- **Repeated values are not forbidden:** Only indices must be distinct. Duplicate suppression removes repeated output rows, not legal use of equal values from different positions.
- **Any output order:** Sorting causes every row and the overall traversal to be deterministic, but the contract does not require that order.
- **Input mutation:** `nums.sort()` rearranges the provided list; callers that need the original order must pass a copy, although this problem imposes no such requirement.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^3)$. Let $n$ be `len(nums)` and let $A$ be the number of returned quadruplets.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
