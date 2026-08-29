# Guided Example: Build Array from Permutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 2, 1, 5, 3, 4]}`
- **Required output:** `[0, 1, 2, 4, 5, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **zero-based permutation** `nums` (**0-indexed**), build an array `ans` of the **same length** where $\text{ans}[i] = nums[\text{nums}[i]]$ for each $0 \le i < \text{nums.length}$ and return it.

The objective is to compute `[0, 1, 2, 4, 5, 3]` from `{"nums": [0, 2, 1, 5, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the formula directly into array lookups

The required value at answer index $i$ is `nums[nums[i]]`. There are two lookups in that expression. The first lookup, `nums[i]`, produces another valid index. The second lookup uses that result to obtain the value that belongs in the answer. The permutation guarantee is what makes this safe: every element of `nums` is between $0$ and $N-1$, so every value can be used as an index into the same length-$N$ array.

The exact solution expresses this operation with the list comprehension `[nums[num] for num in nums]`. Although the comprehension does not explicitly mention an index `i`, it performs precisely the operation in the definition. Iterating `for num in nums` visits the values `nums[0]`, `nums[1]`, and so on in their original order. During the iteration for position $i$, the variable `num` therefore equals `nums[i]`. Appending `nums[num]` consequently appends `nums[nums[i]]`. Because the iteration order is the original array order, that appended value becomes answer element $i$.

For `nums = [0, 2, 1, 5, 3, 4]`, consider the values encountered by the comprehension:

| Answer position | Current `num` | Value appended, `nums[num]` |
|---:|---:|---:|
| 0 | 0 | `nums[0] = 0` |
| 1 | 2 | `nums[2] = 1` |
| 2 | 1 | `nums[1] = 2` |
| 3 | 5 | `nums[5] = 4` |
| 4 | 3 | `nums[3] = 5` |
| 5 | 4 | `nums[4] = 3` |

The resulting list is `[0, 1, 2, 4, 5, 3]`. It is useful to distinguish the role of a value from its numeric appearance here. A value such as `5` is not copied directly to the answer. It is first interpreted as an address, and the value stored at that address is copied.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 2, 1, 5, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a new list is the natural fit for this solution

Every required lookup must observe the original permutation. If the algorithm overwrote `nums[i]` with its answer too early, a later lookup might read that new answer rather than the original value and produce the wrong result. The comprehension avoids that dependency completely. Python evaluates every lookup from the unchanged input list while building a separate output list. Only after all elements have been evaluated is that new list returned.

This also means the function has no surprising mutation side effect. A caller that still holds a reference to `nums` sees the original permutation after the method returns. That behavior is often easier to reason about than an encoding-based in-place method, even though the problem includes an optional follow-up asking about constant auxiliary memory.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the construction is correct

Fix any answer index $i$ from $0$ through $N-1$. When the comprehension reaches its $i$-th iteration, Python supplies the $i$-th input element to `num`, so `num = nums[i]`. The expression in front of `for` is then evaluated as `nums[num] = nums[nums[i]]`. That value is appended as the $i$-th output element because a list comprehension preserves iteration order. Thus the returned list satisfies the required equation at this arbitrary index. Since the same reasoning applies to every valid $i$, all answer elements are correct.

No special branching is necessary for fixed points or cycles in the permutation. If `nums[i] = i`, the two-level lookup simply returns `nums[i]`. If several indices form a cycle, each answer position independently follows exactly two edges of that cycle. The algorithm never needs to discover or traverse a whole cycle.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1, 2, 4, 5, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 2, 1, 5, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1, 2, 4, 5, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **In-place quotient-and-remainder encoding:** Because every original value is in $[0,N-1]$, one can temporarily store both the old and new values in each integer, usually with a base of $N$, then decode in a second pass. That meets the follow-up's $O(1)$ auxiliary-memory target but mutates the input and requires careful use of remainders whenever a previously encoded cell is read.
- **Explicit indexed loop:** Initializing an answer list and assigning `ans[i] = nums[nums[i]]` is equivalent to the comprehension. It may be more familiar to a beginner, but it has the same $O(N)$ time and $O(N)$ returned-space costs.
- **Accidental in-place overwrite:** Simply assigning `nums[i] = nums[nums[i]]` from left to right is unsafe. A later position may depend on an original value that was already replaced. It is only correct with an encoding technique or another way to preserve old values.
- **Single-element permutation:** The only possible input is `[0]`. The lookup is `nums[nums[0]] = nums[0]`, so the method correctly returns `[0]`.
- **Fixed points:** An index with `nums[i] = i` maps to its own value. It needs no special treatment.
- **Long permutation cycles:** A cycle of any length is harmless because each result follows exactly two indexed links from the unchanged input.
- **Index safety:** The solution relies on the stated zero-based permutation contract. If arbitrary negative or out-of-range integers were allowed, Python indexing semantics could produce an unintended value or raise an error; such inputs are outside the problem.
- **Input preservation:** The exact solution returns a new list and leaves `nums` untouched. This is a behavioral advantage over the constant-extra-memory follow-up technique.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be `len(nums)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
