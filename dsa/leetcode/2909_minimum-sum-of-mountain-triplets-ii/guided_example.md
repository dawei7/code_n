# Guided Example: Minimum Sum of Mountain Triplets II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [8, 6, 1, 5, 3]}`
- **Required output:** `9`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `nums` of integers.

The objective is to compute `9` from `{"nums": [8, 6, 1, 5, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Prepare all future right-side choices

The reverse pass fills an array `right` where `right[i]` is the minimum value from index $i$ through the end of `nums`. It begins with an additional sentinel entry:

`right[n] = inf`.

Then, for $i$ moving from $n-1$ down to $0$,

`right[i] = min(right[i + 1], nums[i])`.

This recurrence is valid because the suffix beginning at $i$ consists of the single current element followed by the suffix beginning at $i+1$. Taking the smaller of those two known quantities produces the minimum of the whole suffix.

For a peak at index $j$, the relevant lookup is `right[j + 1]`. It is the minimum strictly to the right. Using `right[j]` would be a subtle error: that range contains the peak itself, and could falsely treat one array position as two members of the triplet.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [8, 6, 1, 5, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Carry the best past left-side choice

During a left-to-right pass, `left` records the minimum value from the indices already passed. At the beginning it is infinity because no left index exists. For current index $j$, the solution first tests whether `left < nums[j]` and only afterward incorporates `nums[j]` into `left`.

That order gives a useful loop invariant: immediately before evaluating $j$,

$$
\texttt{left} = \min_{0 \le i < j}\texttt{nums}[i].
$$

The suffix construction similarly gives

$$
\texttt{right}[j+1] = \min_{j < k < n}\texttt{nums}[k].
$$

The current element can form the peak of at least one mountain triplet precisely when both minima are strictly smaller than it. When that is true, the best sum for this peak is

`left + nums[j] + right[j + 1]`.

The answer variable retains the minimum of these peak-specific candidates.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | During a left-to-right pass, `left` records the minimum valu... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the two minimum values are guaranteed to be valid choices

It may initially seem that storing only values loses necessary index information. The ranges encoded by the algorithm prevent that problem. `left` was obtained exclusively from indices below $j$, and `right[j + 1]` exclusively from indices above $j$. Therefore their supplying positions automatically satisfy the required index order.

Now suppose there is a valid triplet $(i,j,k)$. Because `left` is the minimum over all earlier positions, `left <= nums[i]`. Since `nums[i] < nums[j]`, the stored left minimum is also strictly below the peak. Likewise, `right[j + 1] <= nums[k] < nums[j]`. The stored pair is therefore valid for this same peak, and its total is no greater than the total of $(i,j,k)$.

This proves two important points at once:

1. If a peak has any valid choices, testing the two side minima will recognize it.
2. The candidate computed for that peak is its smallest possible sum.

Every index is examined as the peak, so the smallest recorded candidate is the smallest valid triplet sum across the entire array.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `9` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [8, 6, 1, 5, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `9` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Cubic enumeration:** Trying every $i<j<k$ is e:** - **Cubic enumeration:** Trying every $i<j<k$ is easy to reason about but costs $O(n^3)$ time, which is unsuitable for the larger constraints of this second version.
- **Quadratic peak expansion:** Fixing each $j$ and rescanning both sides takes $O(n^2)$ time. It discovers the same two minima repeatedly instead of reusing them.
- **Two full range-minimum arrays:** A prefix-minimum array plus a suffix-minimum array also yields $O(n)$ time and $O(n)$ space. Keeping `left` as a scalar is simpler because the forward scan needs only the current prefix minimum.
- **Strict inequality:** A side value equal to the peak is invalid. The two `<` checks must not be weakened to `<=`.
- **Repeated values:** Duplicate numbers are harmless. The suffix and running prefix minima can come from any occurrence in their proper ranges, and the index ordering remains valid.
- **An endpoint cannot be the peak:** A valid peak needs at least one index on each side. Infinity sentinels make the tests fail at the endpoints without accessing outside the array.
- **Smallest values on the same side:** The globally smallest two values are not automatically a usable pair; both could lie to the left or both to the right of a peak. The range-specific minima preserve the ordering constraint.
- **No mountain exists:** Strictly increasing, strictly decreasing, or otherwise unsuitable arrays never update `ans` and correctly return `-1`.
- **Large sums:** The Python implementation uses arbitrary-precision integers, so adding three legal values does not overflow. In a fixed-width language, the maximum possible sum should be checked when choosing the numeric type.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ denote the number of elements.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
