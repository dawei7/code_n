# Guided Example: Maximum Score of a Good Subarray

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 4, 3, 7, 4, 5], "k": 3}`
- **Required output:** `15`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of integers `nums` **(0-indexed)** and an integer `k`.

The objective is to compute `15` from `{"nums": [1, 4, 3, 7, 4, 5], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Fix which value acts as the minimum

The score of a subarray is its minimum value multiplied by its length. For each index $i$, imagine that `nums[i] = v` is the minimum of the chosen subarray. To maximize the score for that fixed minimum, extend as far left and right as possible while every included value remains at least $v$.

The resulting candidate is useful only if its interval contains the required index $k$. A monotonic stack finds the relevant boundaries for every $i$ in linear time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 4, 3, 7, 4, 5], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the nearest strictly smaller value on the left

The first scan moves from left to right. Stack `stk` stores indices whose values form a strictly increasing sequence after cleanup.

For current value `v = nums[i]`, the solution pops while `nums[stk[-1]] >= v`. Every popped index is unusable as a smaller boundary because its value is equal to or greater than $v$. After the popping:

- if the stack is nonempty, its top is the nearest index to the left whose value is strictly less than $v$, so it becomes `left[i]`;
- if the stack is empty, no smaller value exists to the left, and the sentinel `left[i] = -1` remains.

The current index is then pushed for future elements.

Thus every position from `left[i] + 1` through $i$ has value at least $v$, while including `left[i]`, when it exists, would introduce a smaller minimum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the nearest smaller-or-equal value on the right

The second scan moves from right to left with a fresh stack. This time it pops while the top value is strictly greater than `v`, not greater than or equal.

After cleanup, the top is the nearest right index whose value is less than or equal to $v$. It becomes `right[i]`. If there is no such index, the sentinel `n` remains.

The usable candidate interval for $i$ is therefore

$$
[\texttt{left}[i]+1,\ \texttt{right}[i]-1],
$$

with length `right[i] - left[i] - 1`. Every value inside is at least $v$, so this interval's minimum is $v$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `15` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 4, 3, 7, 4, 5], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `15` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Greedy two-pointer expansion from `k`:** Expand toward the larger adjacent value while tracking the current minimum. It achieves $O(n)$ time and $O(1)$ space, matching the manifest's space target, but it is not the protected implementation.
- **Binary-search boundary method:** Prefix minima and binary searches can solve the problem in $O(n\log n)$ time and $O(n)$ space.
- **Enumerate all good subarrays:** There can be $O(n^2)$ intervals containing $k$, and rescanning minima makes the approach even slower.
- **Range-minimum structure:** Fast minimum queries do not remove the quadratic number of candidate intervals by themselves.
- **Equal values:** The `>=` left pop and `>` right pop deliberately assign a plateau to a later equal occurrence.
- **`k = 0`:** A valid candidate must begin at the first position; the sentinel and containment check handle this directly.
- **`k = n - 1`:** Symmetrically, a candidate must reach the final position.
- **Single element:** Both sentinels remain, width is one, and the answer is `nums[0]`.
- **Strictly increasing array:** Left boundaries are nearby smaller values, while right boundaries often reach the end.
- **Strictly decreasing array:** Left boundaries often reach -1, while right boundaries are nearby smaller values.
- **All equal:** Tie handling ensures one occurrence represents the full array, which is the best good subarray for every valid $k$.
- **Positive-value guarantee:** It justifies expanding a fixed-minimum interval as far as possible; negative values would make greater length potentially harmful.
- **Containment check:** A large rectangle-like score is irrelevant if its interval does not include `k`.
- **Input preservation:** The method stores indices and boundaries without changing `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each index is pushed once and popped at most once in the left scan, so its total stack work is $O(n)$. The same amortized argument applies independently to the right scan. The final candidate loop is another $O(n)$ pass. Total time is $O(n)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
