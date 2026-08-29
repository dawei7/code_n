# Guided Example: Minimum Deletions to Make Array Beautiful

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 2, 3, 5]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`. The array `nums` is **beautiful** if:

The objective is to compute `1` from `{"nums": [1, 1, 2, 3, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Read the condition as independent output pairs

A beautiful array has even length, and every even output index must differ from the following odd output index. In other words, the kept elements can be grouped as

`(answer[0], answer[1])`, `(answer[2], answer[3])`, and so on,

with unequal values inside each pair. There is no restriction between the second element of one pair and the first element of the next. That local pair structure is what permits a greedy scan.

Deleting an element shifts later elements left, so the parity of an original index is not what matters. What matters is how many elements have already been deleted or kept. The solution tracks original-array position `i` and deletion count `ans` in a way that always treats `nums[i]` as the candidate for the next even position of the resulting array.

Initially, `i = 0` and `ans = 0`. The difference `i - ans` is zero, an even position in the conceptual array after deletions. Every loop action preserves the fact that the next unresolved kept position is even:

- if two candidates are equal, the solution records one deletion and advances one original position, so both `i` and `ans` increase by one and `i - ans` stays even;
- if they differ, it keeps them as a complete pair and advances by two, so `i - ans` increases by two and remains even.

This invariant explains why the code can inspect adjacent entries of the original list without physically deleting anything.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 2, 3, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: When adjacent candidates are equal

At the start of a pair, suppose `nums[i] == nums[i + 1]`. Keeping both would place equal values at the next even and odd output positions, immediately violating beauty. At least one of these two occurrences must therefore be deleted before a valid pair can be completed.

The code performs the conceptual deletion by incrementing `ans` and moving `i` forward by one. It can be viewed as deleting `nums[i]` and allowing the equal-valued `nums[i + 1]` to remain the first candidate for the pair. Because the two values are identical, choosing the other occurrence instead would expose the same value to all later elements. Deleting one now is unavoidable and does not sacrifice a better future option.

If a long run contains several copies of the same value, this action repeats. For `[1, 1, 1, 2]`, the first comparison deletes one `1`, the second comparison deletes another `1`, and the remaining `1, 2` forms a valid pair. The scan keeps exactly one useful representative from the run at the pair's first position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: When adjacent candidates differ

If `nums[i] != nums[i + 1]`, these two elements already form a valid next pair. The solution keeps both and advances `i` by two without increasing `ans`.

Keeping them is optimal. They are the earliest available two elements, they satisfy the only constraint applying within their pair, and completing this pair imposes no value restriction on the next pair. Deleting either element could not increase the number kept in the processed portion: the greedy choice keeps two elements using zero deletions, which is the maximum possible contribution of a complete pair.

An exchange argument makes this precise. Consider any optimal result for the current suffix. If the first two available values differ but that result deletes one of them, replace its first eventual valid pair with these two earliest values. They are already unequal, preserve original order, and do not constrain later pairs. The replacement keeps at least as many elements and uses no more deletions. Therefore, some optimum agrees with the greedy choice.

Together, the two cases are safe at every iteration. Equal candidates force at least one deletion, and the greedy method pays exactly that unavoidable cost. Unequal candidates can safely be kept as the next complete pair. Applying these choices repeatedly minimizes deletions needed to build as many valid pairs as possible.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 2, 3, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Construct a separate kept array:** Append a value when it can legally occupy the next position, then remove a trailing element if the result is odd. This can express the state clearly but uses `O(n)` extra space; the index-and-count method represents the same choices in `O(1)` space.
- **Physically delete equal elements:** Repeated deletion from the middle of a Python list shifts later elements and can lead to `O(n^2)` time. Counting conceptual deletions avoids all movement.
- **Dynamic programming over index and parity:** A DP can decide whether to keep or delete every value while remembering the previous kept value and parity. It is much more state than this pair-local condition requires, and the greedy exchange argument gives a linear constant-space solution.
- **Only remove adjacent duplicates once:** Deleting a single member of each original equal adjacency is not enough because earlier deletions change which values become paired. The scan's current pair position, not original parity alone, must guide comparisons.
- **Single element:** The loop never runs. The kept count is odd, so the parity correction returns one, leaving the empty array, which is beautiful.
- **Two equal elements:** One equality deletion is counted, leaving one conceptual element; the parity correction deletes that last element too. The answer is two, and the empty array is the only beautiful result.
- **Two unequal elements:** The scan keeps the pair, the kept length is even, and the answer is zero.
- **All values equal:** Repeated equality handling leaves at most one conceptual element, and the parity correction removes it. No nonempty unequal pair can be formed.
- **Already beautiful input:** Every scanned pair is unequal and the length is even, so `ans` remains zero.
- **Equal values across a pair boundary:** Values at output indices `1` and `2` may be equal because the rule applies only when the left index is even. The algorithm correctly advances by two after completing a pair and does not compare across that boundary.
- **Final unpaired candidate:** Its value does not matter. Even if it differs from the previous element, it cannot remain because a beautiful array must have even length.
- **Input preservation:** All deletions are conceptual. The original `nums` list is unchanged after the method returns.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(nums)`. Each loop iteration advances `i` by either one or two, and `i` never moves backward. Every input position participates in only a constant amount of work, so the main scan takes `O(n)` time. The final parity expression takes `O(1)` time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
