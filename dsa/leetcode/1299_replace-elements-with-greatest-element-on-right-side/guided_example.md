# Guided Example: Replace Elements with Greatest Element on Right Side

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [17, 18, 5, 4, 6, 1]}`
- **Required output:** `[18, 6, 6, 6, 1, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `arr`, replace every element in that array with the greatest element among the elements to its right, and replace the last element with `-1`.

The objective is to compute `[18, 6, 6, 6, 1, -1]` from `{"arr": [17, 18, 5, 4, 6, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the scan starts with negative one

The last element has no elements to its right and must be replaced with `-1`. The code initializes `mx = -1` so that the same assignment used everywhere automatically handles the last index.

The input values are all at least one, so `-1` is smaller than every original value. After the last element is processed, taking a maximum with its positive original value removes the sentinel from future suffix maxima. Even without that ordering fact, the explicit requirement for the last replacement makes `-1` the correct initial answer for the empty right suffix.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [17, 18, 5, 4, 6, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Visiting indices in reverse

`reversed(range(len(arr)))` produces the indices

$$
n-1,\;n-2,\;\ldots,\;1,\;0.
$$

It does not reverse the array contents. It only determines the order in which positions are visited. This avoids making a reversed copy and ensures that, before index `i` is handled, every index greater than `i` has already contributed its original value to `mx`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Saving the original value before overwriting

Inside the loop, the first operation is

`x = arr[i]`.

The temporary `x` is essential because the next statement, `arr[i] = mx`, destroys the original value at index `i`. That original value must still become a candidate for the suffix maximum used at index `i - 1`.

After saving it, the algorithm writes `mx` into `arr[i]`. At this moment, `mx` summarizes only original elements at indices greater than `i`, so it is exactly the greatest element strictly to the right. It intentionally does not yet include `x`; including the current element would violate the word “right.”

Finally,

`mx = max(mx, x)`

expands the summary to include the original value at index `i`. When the loop moves to `i - 1`, the indices strictly to its right are `i` through `n - 1`, exactly the values now represented by the updated maximum.

Changing the order of these operations would break the solution. If `arr[i]` were overwritten before its original value was saved, that value could never influence earlier positions. If `mx` were updated with `x` before assignment, the replacement at `i` could incorrectly use the element itself.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[18, 6, 6, 6, 1, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [17, 18, 5, 4, 6, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[18, 6, 6, 6, 1, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Precompute a suffix-maximum array:** A separate array can store the maximum beginning at every position, after which each answer uses the next entry. It is correct and linear-time but uses $O(n)$ extra space when one running maximum is sufficient.
- **Scan to the right for every index:** This direct method is easy to state but repeats comparisons across overlapping suffixes and costs $O(n^2)$ time.
- **Monotonic stack:** A stack is useful for the next greater element, but this task needs the greatest value anywhere to the right. A single suffix maximum is simpler and uses less machinery.
- **Left-to-right traversal:** Without preprocessing, it cannot know future values. Attempting to maintain a prefix maximum solves the opposite problem.
- **Single-element array:** The reverse loop runs once with `mx = -1`, so the only value becomes `-1`.
- **Strictly increasing values:** Each position becomes the original final value, except the final position becomes `-1`, because that last value is the greatest in every earlier right suffix.
- **Strictly decreasing values:** Each position becomes its immediate right neighbor, since that neighbor is the greatest value in the remaining suffix.
- **Duplicate maximum values:** `max` handles ties naturally. The output needs the greatest value, not the position of a unique greatest element.
- **Saving before writing:** Removing `x = arr[i]` or moving it after the overwrite loses original data and gives wrong maxima to earlier indices.
- **Updating after writing:** `mx` must represent a strictly-right suffix during assignment. Updating it with the current value first would allow an element to replace itself.
- **Positive-value constraint:** It makes the `-1` sentinel smaller than all originals. The final-element rule is still explicit, but a generalized problem with arbitrary negative values should reason about the empty suffix separately rather than treating `-1` as a universal mathematical identity.
- **Input mutation visible to callers:** The returned object is `arr` itself. If preserving the caller's list matters outside the problem contract, the method should first copy it, accepting $O(n)$ additional space.
- **No empty-array case:** The contract guarantees at least one element. If an empty list were supplied outside the contract, the loop would do nothing and return an empty list, though the problem does not define a special last element for that case.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `arr`. `range` and `reversed` provide an iterator over the indices without constructing an $n$-element reversed list. The loop runs exactly once per element.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
