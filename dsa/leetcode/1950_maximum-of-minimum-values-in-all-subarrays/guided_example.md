# Guided Example: Maximum of Minimum Values in All Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 2, 4]}`
- **Required output:** `[4, 2, 1, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of size `n`. You are asked to solve `n` queries for each integer `i` in the range $0 \le i < n$.

The objective is to compute `[4, 2, 1, 0]` from `{"nums": [0, 1, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Ask how wide each value can remain the minimum

Instead of evaluating every window length separately, the solution considers each element `nums[i]` and finds the largest contiguous interval in which that element can serve as a minimum. If that interval has length $m$, then `nums[i]` is an achievable window minimum for length $m$ and for smaller contained windows that include it.

The interval stops immediately before the nearest strictly smaller value on each side. Values equal to `nums[i]` do not stop it because `nums[i]` is still a minimum when equals are present.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find nearest strictly smaller boundaries with monotonic stacks

The left scan maintains indices whose values are strictly increasing on the stack. Before assigning `left[i]`, it pops while the top value is greater than or equal to the current value. After those pops, the remaining top, if any, is the nearest index to the left with a strictly smaller value. If none exists, the sentinel remains `-1`.

The right-to-left scan applies the same rule and stores the nearest strictly smaller index to the right, or sentinel `n`.

For index $i$, every value between these boundaries is at least `nums[i]`, while crossing either boundary would include a smaller value. Therefore the maximum interval length for this minimum is

`m = right[i] - left[i] - 1`.

The code records `nums[i]` as a candidate for answer index `m - 1`, because result index $m-1$ corresponds to window size $m$. Multiple elements may have the same span length, so `max` keeps the best minimum value.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why equal values are handled

Both scans pop equal values. This may let several equal elements claim overlapping wide intervals, but it cannot inflate the answer because they contribute the same value. More importantly, at least one representative of a plateau can claim every window span where that plateau value is the minimum. Strictly smaller values, not equals, are the true limiting boundaries.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4, 2, 1, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4, 2, 1, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate every subarray:** Maintaining minima for all $O(N^2)$ windows is too slow.
- **Sliding minimum for each length:** A deque can solve one fixed length in $O(N)$, but repeating it for all $N$ lengths is quadratic.
- **Use one strict and one non-strict boundary:** This is a common way to assign duplicate spans uniquely. The exact source uses non-strict popping on both sides; overlapping equal claims remain harmless for maximum values.
- **Single element:** Both sentinels bound a span of one, and the result is that element.
- **All equal values:** Every answer should equal that value. Wide spans are recorded and backward propagation fills all lengths.
- **Strictly increasing array:** Each value's right reach extends to the end until a left smaller boundary; the formula derives the expected decreasing answers.
- **Strictly decreasing array:** Symmetric boundary behavior handles minima extending leftward.
- **Zeros:** Zero is a valid minimum and also the initialization value; propagation still works because no true answer is negative.
- **Missing direct length:** The backward monotonicity pass supplies it from a longer achievable span.
- **Nearest strictly smaller:** Equal values must not terminate the region where the current value remains a minimum.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the array length.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
