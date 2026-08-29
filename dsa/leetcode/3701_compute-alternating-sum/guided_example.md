# Guided Example: Compute Alternating Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 5, 7]}`
- **Required output:** `-4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `-4` from `{"nums": [1, 3, 5, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reading slice notation

A Python slice has the form:

`sequence[start:stop:step]`.

When `stop` is omitted, slicing continues to the end of the sequence.

The slice:

`nums[0::2]`

starts at index zero and advances by two, so it selects:

$$
\texttt{nums}[0],\texttt{nums}[2],\texttt{nums}[4],\ldots
$$

These are exactly the even-indexed elements.

The slice:

`nums[1::2]`

starts at index one and also advances by two, selecting:

$$
\texttt{nums}[1],\texttt{nums}[3],\texttt{nums}[5],\ldots
$$

These are exactly the odd-indexed elements.

Every valid array index belongs to exactly one of the two slices, so no element is omitted or counted twice.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 5, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Grouping like signs

The alternating sum is written position by position as:

$$
\texttt{nums}[0]-\texttt{nums}[1]+\texttt{nums}[2]-\texttt{nums}[3]+\cdots.
$$

Addition and subtraction can be regrouped as:

$$
\left(\sum_{\substack{i=0\\i\text{ even}}}^{n-1}\texttt{nums}[i]\right)
-
\left(\sum_{\substack{i=0\\i\text{ odd}}}^{n-1}\texttt{nums}[i]\right).
$$

The source computes these two parenthesized quantities directly. Subtracting the odd-index sum applies one negative sign to every odd-position value.

For `nums = [1, 3, 5, 7]`:

- `nums[0::2]` is `[1, 5]`, with sum six;
- `nums[1::2]` is `[3, 7]`, with sum ten;
- the result is $6-10=-4$.

The answer is allowed to be negative. The positivity of individual elements does not imply a positive alternating total because the odd-index sum may be larger.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why slicing preserves the intended indices

The sign depends on an element's original position, not on its position inside a new list. Slicing chooses positions according to the original index before constructing the result.

For example, original index two is selected by the even slice because the range generated from start zero with step two includes two. It remains a positive term even though it becomes index one inside the temporary slice `[nums[0], nums[2], ...]`.

The method does not sort, filter by value, or modify the input. Only original index parity matters.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `-4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 5, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `-4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One running accumulator:** Add `x` at even indices and subtract it at odd indices. This retains $O(n)$ time while achieving the manifest's intended $O(1)$ auxiliary space.
- **Signed generator:** `sum(x if i % 2 == 0 else -x for i, x in enumerate(nums))` also avoids materialized slices and uses constant auxiliary space.
- **Multiply by `(-1) ** i`:** This matches the signs mathematically but performs unnecessary exponentiation or sign computation compared with parity.
- **One element:** The odd slice is empty, its sum is zero, and the single even-indexed value is returned.
- **Even array length:** The two slices contain the same number of elements.
- **Odd array length:** The even slice contains one additional final element, which correctly receives a positive sign.
- **Negative final answer:** This is valid when the odd-index total exceeds the even-index total.
- **Repeated values:** Signs depend on positions, so equal values at different indices may contribute with opposite signs.
- **Input mutation:** Slicing creates new lists and leaves the original order and contents unchanged.
- **Indexing convention:** The first element is index zero and therefore positive; treating the array as one-indexed would reverse every sign.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
