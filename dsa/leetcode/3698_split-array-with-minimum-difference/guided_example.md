# Guided Example: Split Array With Minimum Difference

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 2]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `2` from `{"nums": [1, 3, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Prefix sums

The line:

`s = list(accumulate(nums))`

creates cumulative sums, so:

$$
s[i]=\sum_{j=0}^{i}\texttt{nums}[j].
$$

For a split after `i`, the left sum is directly `s[i]`. The total array sum is `s[n - 1]`, so the right sum is:

`s[n - 1] - s[i]`.

This avoids summing either subarray again for each boundary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Marking strictly increasing prefixes

The boolean array `f` has this meaning:

`f[i]` is true exactly when `nums[0..i]` is strictly increasing.

A one-element prefix is vacuously strictly increasing, so `f[0]` begins true.

For every later position, the source first copies the previous prefix status:

`f[i] = f[i - 1]`

and then checks the new adjacent pair. If:

`nums[i] <= nums[i - 1]`

the required strict increase fails, so `f[i]` becomes false.

Both equality and a decrease invalidate the prefix. Once a prefix is invalid, extending it cannot remove the earlier bad pair, so copying `f[i-1]` correctly keeps every later prefix false.

Equivalently:

$$
f[i]=f[i-1]\land(\texttt{nums}[i-1]<\texttt{nums}[i]).
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The boolean array `f` has this meaning:

`f[i]` is true exac... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Marking strictly decreasing suffixes

The array `g` is built in the opposite direction:

`g[i]` is true exactly when `nums[i..n-1]` is strictly decreasing.

The one-element suffix at $n-1$ is vacuously valid. Scanning backward, the suffix beginning at `i` remains valid only if the already-checked suffix beginning at `i+1` is valid and:

$$
\texttt{nums}[i]>\texttt{nums}[i+1].
$$

The source marks failure with:

`if nums[i] <= nums[i + 1]:`

`    g[i] = false`

Again, equality is not allowed because the order must be strict.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every split and rescan both parts:** Valid:** - **Try every split and rescan both parts:** Validating order and recomputing sums at each boundary can take $O(n^2)$ time.
- **Constant-space boundary analysis:** One can locate the farthest valid increasing prefix and earliest valid decreasing suffix, then scan sums with a running prefix total. This can achieve $O(1)$ auxiliary space and matches the manifest's intent.
- **Prefix and suffix sum arrays:** Two sum arrays work, but one prefix-sum array already derives the right sum from the total.
- **Two-element array:** Both parts contain one element and are vacuously ordered, so the sole split is valid.
- **Equal adjacent values:** Equality violates both strict increase and strict decrease where that pair belongs.
- **Singleton side:** A one-element left or right part is always valid; the initial true boundary flags model this.
- **Every split invalid:** Infinity remains untouched and the method returns $-1$.
- **Difference zero:** A perfectly balanced valid split returns zero, which is distinct from the no-split sentinel.
- **Positive values:** They make cumulative sums monotone, but the prefix-sum and order logic would also work with arbitrary integers.
- **Input size:** Storing three linear arrays is feasible for $n\le10^5$, though it does not meet the manifest's claimed constant-space bound.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
