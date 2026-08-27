# Guided Example: Minimum Moves to Equal Array Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` of size `n`, return *the minimum number of moves required to make all array elements equal*.

The objective is to compute `3` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Equality is unchanged by a uniform shift

Suppose one move increments every element except the element at index `j`. Immediately after that move, imagine subtracting `1` from every array element. This imaginary uniform subtraction does not affect whether the elements are equal: adding or subtracting the same amount from all values preserves every pairwise difference.

The combined effect is:

- Every incremented element receives `+1` and then `-1`, for a net change of zero.
- The excluded element receives no increment and then `-1`, for a net change of `-1`.

Thus, up to an irrelevant uniform shift, “increment `n - 1` elements by one” is exactly equivalent to “decrement one chosen element by one.” Every sequence of original moves corresponds to the same number of single-element decrements, and conversely each chosen decrement tells us which element to exclude from the corresponding original move.

The transformed problem is much easier: how many single-element decrements are needed to make all values equal?

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The transformed target must be the minimum

Decrements can only lower values. Therefore a common target `t` cannot exceed the original minimum value `m = min(nums)`, because an element already equal to `m` cannot be increased in the transformed view.

For a chosen target $t\le m$, element `nums[i]` needs exactly

$$
\texttt{nums}[i]-t
$$

decrements. The total is

$$
\sum_{i=0}^{n-1}(\texttt{nums}[i]-t).
$$

Choosing a smaller target increases the required decrement count for every element. The largest legal target, and therefore the one requiring the fewest moves, is exactly the original minimum `m`.

The minimum number of moves is consequently

$$
\sum_{i=0}^{n-1}(\texttt{nums}[i]-m).
$$

Distributing the sum gives the formula used by the code:

$$
\sum_{i=0}^{n-1}\texttt{nums}[i] - n\cdot m.
$$

That is `sum(nums) - min(nums) * len(nums)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Decrements can only lower values.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A direct example

For `nums = [1,2,3]`, the minimum is `1`. In the decrement view:

- `1` needs zero decrements.
- `2` needs one decrement.
- `3` needs two decrements.

The total is $0+1+2=3$. The formula agrees: $1+2+3-3\cdot1=3$.

Mapping those three decrements back to the original operation yields a valid three-move sequence. Decrementing `3` in the transformed view means incrementing the other two original elements; decrementing it again repeats that exclusion, and decrementing `2` corresponds to excluding its position. Uniform shifts make the absolute intermediate numbers look different, but the pairwise gaps close in exactly the same way.

For `[1,1,1]`, every value already equals the minimum. Each difference is zero, so the result is zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sum individual gaps:** First find `m`, then ac:** - **Sum individual gaps:** First find `m`, then accumulate `x - m` for each `x`. It has the same $O(n)$ time and $O(1)$ space and may reduce intermediate-overflow risk in fixed-width languages.
- **Sort the array:** After sorting, sum every difference from the first value. This is correct but wastes $O(n\log n)$ time merely to discover the minimum.
- **Simulate one move at a time:** Repeatedly incrementing `n - 1` elements can require an enormous number of operations and touches many array positions per move.
- **Raise everything to the maximum:** That reasoning fits an operation that increments one element, not this operation. Incrementing all but one is relatively equivalent to lowering the excluded element.
- **All values equal:** Every gap from the minimum is zero, so no moves are needed.
- **One-element array:** A move would increment zero elements, but the sole value is already equal to every array element. The formula returns zero.
- **Repeated minimum values:** Each minimum contributes zero; only elements above the minimum require transformed decrements.
- **Negative values:** Subtraction from the minimum still produces nonnegative gaps and the same formula remains valid.
- **Large magnitudes:** Use wide accumulation in fixed-width languages even though the promised final answer fits 32 bits.
- **Input preservation:** The one-line calculation only reads `nums`, leaving its order and values unchanged.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. `sum(nums)` scans all $n$ values once, and `min(nums)` scans them once again. Multiplication, subtraction, and `len(nums)` are constant-time operations under the standard fixed-width arithmetic model. The total time is therefore $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
