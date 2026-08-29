# Guided Example: 3Sum Smaller

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-2, 0, 1, 3], "target": 2}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of `n` integers `nums` and an integer `target`, find the number of index triplets `i`, `j`, `k` with $0 \le i < j < k < n$ that satisfy the condition $\text{nums}[i] + \text{nums}[j] + \text{nums}[k] < target$.

The objective is to compute `2` from `{"nums": [-2, 0, 1, 3], "target": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sorting does not lose index multiplicity

Sorting rearranges occurrences, but it is a bijection between original array positions and sorted positions. Every occurrence remains present exactly once. If equal values appear several times, their sorted positions are still separate choices, and pointer-distance counting includes each index combination. This is why the method can sort even though the problem phrases the answer using original indices.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-2, 0, 1, 3], "target": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: When the largest current sum is small enough

For fixed `i` and `j`, first test

$$
x=\text{nums}[i]+\text{nums}[j]+\text{nums}[k].
$$

If $x<target$, then replacing `k` by any position `p` with $j<p\le k$ cannot increase the sum, because the array is sorted and `nums[p] <= nums[k]`. Therefore, every triplet

$$
(i,j,j+1),(i,j,j+2),\ldots,(i,j,k)
$$

is valid. There are exactly `k - j` such third positions, so the algorithm adds that number to `ans` in one operation.

All triples using this fixed `i` and `j` within the remaining range have now been counted. The solution advances `j` to discover triples with the next second position. It does not decrease `k`, because the larger second value may or may not still work with the same far-right endpoint; testing will decide.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: When the sum is too large

If $x\ge target$, the triplet at the current boundaries is invalid. More importantly, keeping the same `k` and moving `j` right cannot help: every later second value is at least `nums[j]`, so the sum would stay the same or grow. Thus no valid remaining pair for this fixed `i` can use the current third position `k`.

The only useful move is `k -= 1`, replacing the largest candidate by a smaller value. This discards no valid triplet.

The strict comparison matters. A sum equal to `target` does not qualify, so it follows the same branch as a larger sum and moves `k` left.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-2, 0, 1, 3], "target": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Three nested loops:** Test every triplet directly in $O(n^3)$ time and $O(1)$ extra space. It is simple but too slow near `n = 3500`.
- **Binary search for each `(i, j)`:** Find the last valid `k` in the sorted suffix, giving $O(n^2\log n)$ time. Two pointers reuse monotonic progress and remove the logarithmic factor.
- **Frequency counting over the bounded value range:** Since values lie from `-100` to `100`, a combinatorial frequency method is possible, but it requires careful multiplicity cases. The sorted two-pointer method is more general.
- **Sum exactly equals target:** It is invalid because the condition is strictly smaller; the code correctly moves `k` left.
- **Duplicate values:** They remain distinct sorted positions. Adding `k - j` counts index triplets with equal values according to their multiplicity.
- **All negative values:** Sorting and monotonic sum arguments remain valid; signs do not change pointer logic.
- **Empty, one-element, or two-element input:** No first position leaves two later indices, so the function returns zero.
- **Exactly three elements:** The inner loop performs one comparison and returns either one or zero.
- **All triples valid:** For each `i` and `j`, the algorithm counts the entire remaining right block, efficiently accumulating $\binom{n}{3}$.
- **No triples valid:** The right pointer repeatedly moves left for each `i`; runtime remains quadratic in the worst case.
- **Input mutation:** `nums.sort()` destroys original ordering. Use `sorted(nums)` when the caller must retain it.
- **Answer size:** The constraints guarantee the count fits within $10^9$; Python would handle larger integers anyway.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the number of elements. Sorting takes $O(n\log n)$ time. For one fixed `i`, each inner-loop iteration moves either `j` right or `k` left. Neither pointer reverses direction, so that scan takes $O(n)$ time. Repeating it for $O(n)$ first positions costs $O(n^2)$, which dominates sorting. Total time is $O(n^2)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
