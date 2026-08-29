# Guided Example: Subsets II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 2]}`
- **Required output:** `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` that may contain duplicates, return *all possible* *subsets** (the power set)*.

The objective is to compute `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]` from `{"nums": [1, 2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Meaning of one recursive state

At the start of `dfs(i)`, the list `t` contains the values selected from positions before `i`, and the recursion must generate every distinct continuation using positions from `i` onward. The state makes two conceptual choices concerning `nums[i]`:

- include this occurrence, or
- include no additional occurrence of this value from the run beginning at `i`.

The first branch executes `t.append(nums[i])` and calls `dfs(i + 1)`. Moving by only one position is intentional. If the next position contains the same value, the recursive call may include that next copy too. Repeated include decisions are how the algorithm produces multiplicities one, two, three, and so on.

After that whole branch finishes, `x = t.pop()` both restores the path and remembers which value was just considered. Restoration matters because the second branch must begin with exactly the selections that existed before the current decision. Without the `pop`, the supposed exclusion branch would still contain the value.

The `while` loop then advances `i` across every immediately following occurrence equal to `x`. Finally, `dfs(i + 1)` starts after the entire equal-value run. This is the zero-additional-copies branch.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A complete trace for `[1, 2, 2]`

After sorting, the array is unchanged.

1. At index `0`, include `1`. The path is `[1]`.
2. At the first `2`, include it. The path is `[1, 2]`.
3. At the second `2`, include it and reach the end, recording `[1, 2, 2]`.
4. Back at the second `2`, exclude it and record `[1, 2]`.
5. Back at the first `2`, its exclusion branch skips the second equal `2`, recording `[1]`. It does not create another path that selects only the second copy, because that would duplicate `[1, 2]`.
6. Back at `1`, exclude it and repeat the same multiplicity choices for the `2` run, recording `[2, 2]`, `[2]`, and `[]`.

The output order may differ from the Reference example, which is allowed. The significant fact is that every distinct subset appears once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why no valid subset is missed

Think of the sorted input as groups of equal values. If a value occurs $c$ times, a subset may contain it exactly $0,1,\ldots,c$ times. The recursion represents those choices without naming them explicitly. Taking the include branch $k$ consecutive times and then taking the exclusion branch selects exactly $k$ copies. Taking exclusion immediately selects zero copies. Therefore every possible multiplicity for the current group is represented.

Once that multiplicity is fixed, recursion continues with the next distinct value group. Combining one valid multiplicity choice from every group describes every possible subset of the input multiset. Thus the traversal is complete.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative cascading:** Start with `[[]]` and extend all existing subsets for a new value, but extend only the subsets created in the immediately preceding step when seeing another copy of that value. This avoids recursion and has the same output-sensitive time bound.
- **Frequency-map recursion:** Compress the sorted input into `(value, count)` groups, then explicitly loop over choosing zero through `count` copies. This can make the multiplicity model especially clear, at the cost of building the compressed representation.
- **Bitmask plus a set:** Enumerate all $2^n$ position masks, canonicalize each produced subset, and deduplicate with a hash set. It is easier to adapt from the distinct-elements problem but deliberately creates duplicates and uses output-scale auxiliary storage.
- **Do not skip duplicates in the include branch:** Later equal copies must remain available so subsets containing two or more copies can be formed. Skipping belongs only to the branch that chooses no further copy of the current value.
- **Sorting mutates the input:** `nums.sort()` changes the caller-provided list order. The contract does not forbid this, but copy and sort into a new list if input preservation is required by a surrounding application.
- **All values equal:** For $n$ copies of one value, the valid answers are exactly the $n+1$ possible multiplicities. The recursion generates those without exploring $2^n$ duplicate position combinations.
- **All values distinct:** The `while` loop never advances extra positions, reducing the method to ordinary include/exclude subset generation with $2^n$ outputs.
- **Negative values and zero:** Sorting and equality are the only value-sensitive operations. Their signs have no effect on the argument.
- **Single element:** The two leaves return the one-element subset and the empty subset, each exactly once.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(nU)$. Let $n$ be `len(nums)`, and let $U$ be the number of distinct subsets returned. If the distinct values have frequencies $c_1,c_2,\ldots,c_k$, then
- **Auxiliary Space Complexity:** $O(nU)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
