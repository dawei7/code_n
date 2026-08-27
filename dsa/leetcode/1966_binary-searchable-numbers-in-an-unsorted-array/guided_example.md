# Guided Example: Binary Searchable Numbers in an Unsorted Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [7]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Consider a function that implements an algorithm **similar** to <a href="https://leetcode.com/explore/learn/card/binary-search/" target="_blank">Binary Search</a>. The function has two input parameters: `sequence` is a sequence of integers, and `target` is an integer value. The purpose of the function is to find if the `target` exists in the `sequence`.

The objective is to compute `1` from `{"nums": [7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Characterize when no pivot can discard the target

Fix target `nums[i] = x`. A pivot chosen to the left of $i$ remains in the same current contiguous sequence as $x$ until one of them is discarded. If that left pivot is greater than $x$, the algorithm takes the “pivot greater than target” branch and removes the pivot and everything to its right—including $x$. Therefore every value left of $i$ must be less than $x$.

Symmetrically, if any value to the right is less than $x$, choosing it as pivot takes the “pivot less than target” branch and removes that pivot and everything to its left, including $x$. Therefore every value right of $i$ must be greater than $x$.

These two conditions are also sufficient. Any left pivot is smaller, so it removes only itself and earlier positions while preserving the target. Any right pivot is larger, so it removes itself and later positions while preserving the target. Repeating arbitrary safe removals eventually selects $x$. Thus $x$ is guaranteed searchable exactly when:

$$
\max(\text{left values}) < x < \min(\text{right values}).
$$

Empty sides impose no restriction.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Mark the left condition with a running maximum

`ok` begins with one for every index. The forward scan maintains `mx`, the greatest value seen earlier.

If current `x < mx`, some earlier value is greater and can destroy the target, so `ok[i]` becomes zero. Otherwise `x` becomes the new running maximum.

Values are unique. Therefore equality with `mx` cannot occur at a later position; the source's strict comparison is sufficient.

The sentinel `-1000000` lies below the allowed minimum, so the first element always passes its empty-left condition.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `ok` begins with one for every index.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark the right condition with a running minimum

The backward scan maintains `mi`, the smallest value seen to the right. If `nums[i] > mi`, a smaller right pivot exists and can discard the target, so the index is invalidated. Otherwise the current value becomes the new suffix minimum.

Sentinel `1000000` lies above every allowed value, so the final array element passes its empty-right condition.

An index stays one only when it is a prefix maximum and a suffix minimum in the strict unique-value sense. `sum(ok)` counts those guaranteed targets.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Prefix and suffix arrays:** Explicitly store t:** - **Prefix and suffix arrays:** Explicitly store the maximum to each left and minimum to each right, then test every index. It is equivalent but uses two $O(N)$ arrays instead of one flag array.
- **Sort and compare positions:** With unique values, a searchable number occupies the same relative position under certain partition properties, but sorting costs $O(N\log N)$.
- **Simulate pivot choices:** The number of possible pivot sequences is exponential and unnecessary once the extrema criterion is derived.
- **Single element:** Both sides are empty, so it is guaranteed and the answer is one.
- **Strictly increasing array:** Every left value is smaller and every right value larger for every index, so all numbers count.
- **Strictly decreasing array:** Only when $N=1$ can an index satisfy both conditions; for longer arrays none count.
- **Negative values:** Sentinels are outside the stated range, so extrema initialization remains safe.
- **Unique-value dependency:** With duplicates, equality and pivot-removal behavior require carefully changing strict conditions, as the follow-up suggests.
- **Both extrema required:** A prefix record can still fail because of the suffix, and a suffix record can still fail because of the prefix.
- **Permanent invalidation:** Once either pass writes zero, the other pass cannot restore the guarantee.
- **Dangerous pivot first:** A single violating value proves failure because it may be selected before any helpful removal.
- **Finite progress:** Every non-target pivot removes itself, so a target that is never discarded must eventually be chosen.
- **Sum of flags:** Flags are integers zero or one, so summation directly returns the count.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the array length.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
