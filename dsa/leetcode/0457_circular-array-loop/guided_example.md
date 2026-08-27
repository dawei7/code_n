# Guided Example: Circular Array Loop

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, -1, 1, 2, 2]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are playing a game involving a **circular** array of non-zero integers `nums`. Each $\text{nums}[i]$ denotes the number of indices forward/backward you must move if you are located at index `i`:

The objective is to compute `true` from `{"nums": [2, -1, 1, 2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compute circular destinations

For index `i`, `next(i)` returns

$$
(i + (\texttt{nums}[i]\bmod n) + n)\bmod n.
$$

Modulo wraps forward jumps beyond the last index back to the front and wraps backward jumps before zero back to the end. In Python, `nums[i] % n` is already nonnegative, so the extra `+ n` is redundant but harmless. Reducing the jump before addition also handles magnitudes larger than the array length.

Input values initially are nonzero. The algorithm later uses zero as an internal “already processed” marker; for such a slot, `next(i)` becomes `i`, but sign-product checks prevent that marker from joining a valid search.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, -1, 1, 2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Floyd detection under one fixed direction

For an unmarked start `i`, initialize `slow = i` and `fast = next(i)`. On each loop iteration, slow is prepared to advance one edge and fast two edges.

The loop continues only while

`nums[slow] * nums[fast] > 0`

and

`nums[slow] * nums[next(fast)] > 0`.

A positive product means the two jumps have the same nonzero sign. The first check confirms that slow and fast remain in one direction; the second confirms that fast's next landing also has that direction before fast takes its second step. If either product is nonpositive, the route changes sign or reaches a zero marker, so it cannot be the required uniform-direction cycle for this start.

When the checks pass and `slow == fast`, Floyd's method has found a repeated position. The code then tests `slow != next(slow)`. If the next jump returns to the same position, the cycle length is one and is forbidden. Otherwise the meeting lies on a cycle of length greater than one, and all traversed cycle jumps have the verified common sign, so the method returns `true`.

If no meeting occurs yet, slow advances once and fast advances twice. In any finite functional graph, pointers restricted to a genuine cycle eventually meet because fast gains one cycle position on slow per iteration.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For an unmarked start `i`, initialize `slow = i` and `fast =... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace the valid first example

For `[2,-1,1,2,2]`, start at index `0`. Its route is `0 -> 2 -> 3 -> 0`. Values at those indices are `2`, `1`, and `2`, all positive. Slow moves one edge at a time while fast moves two; they eventually meet inside this three-index cycle. Since the meeting index does not point to itself, the method returns `true`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, -1, 1, 2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Corrected in-place cleanup:** Cache `next(j)` :** - **Corrected in-place cleanup:** Cache `next(j)` before writing zero. This preserves the same logic and restores the intended $O(n)$ amortized time with $O(1)$ auxiliary space.
- **Per-start visited set:** Record indices along each walk and detect repeats directly. It is simpler to visualize but can use $O(n)$ extra space and repeat work unless global state is also maintained.
- **Three-state visitation array:** Mark nodes unseen, active in the current walk, or fully processed. This gives $O(n)$ time and clear cycle ownership, but uses $O(n)$ space.
- **Ignore direction:** Ordinary functional-graph cycle detection would wrongly accept routes containing both positive and negative jumps.
- **One-element array:** Every jump returns to the sole index, producing only a forbidden length-one cycle; the result is false.
- **Jump divisible by `n`:** Its destination is the same index even though the stored jump is nonzero, so the explicit self-loop test is necessary.
- **Mixed-sign repeated route:** Repetition alone is insufficient; sign-product guards reject it.
- **All-positive or all-negative valid cycle:** Direction checks remain positive products in either case because two negatives multiply to a positive number.
- **Zero values:** Original inputs cannot contain zero. Zeros are reserved for internal marking and cause future traversals to stop.
- **Input mutation:** Failed starts are replaced with zero. Callers that need the original jumps must pass a copy.
- **Negative modulo:** Python already produces a nonnegative remainder for positive `n`; other languages may need the double-modulo normalization shown by the formula.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The manifest states $O(n)$ time and $O(1)$ auxiliary space, which are the standard bounds for Floyd detection combined with complete path marking. With the corrected cleanup order, every failed-path index is zeroed once, so later searches skip it; all pointer work amortizes to $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
