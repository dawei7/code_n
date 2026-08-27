# Guided Example: Product of Array Except Self

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4]}`
- **Required output:** `[24, 12, 8, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return *an array* `answer` *such that* $\text{answer}[i]$ *is equal to the product of all the elements of* `nums` *except* $\text{nums}[i]$.

The objective is to compute `[24, 12, 8, 6]` from `{"nums": [1, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the empty-side product is one

At index `0`, there are no elements to the left. At index `n - 1`, there are no elements to the right. The product of an empty collection is defined as `1`, the multiplicative identity. That choice is not an arbitrary special case: multiplying by `1` leaves the existing product unchanged. Consequently, the first answer becomes the product of its right side, and the last answer becomes the product of its left side.

The variables `left` and `right` both begin at `1` for this reason.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Forward pass: store the exclusive prefix product

Before processing index `i`, `left` equals the product of all elements whose indices are smaller than `i`:

$$
\text{left}=\prod_{j=0}^{i-1}\text{nums}[j].
$$

The solution first assigns `ans[i] = left`. Only afterward does it execute `left *= nums[i]`, preparing `left` for the next index. This order is essential. If `nums[i]` were multiplied first, `ans[i]` would include the very element that must be excluded.

After the forward loop, every `ans[i]` contains the complete left factor needed by the formula. The output array is serving as useful working storage; no separate prefix array is necessary.

For `nums = [1, 2, 3, 4]`, the states written to `ans` are:

| Index `i` | `left` before including `nums[i]` | Stored `ans[i]` | `left` after update |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 2 |
| 2 | 2 | 2 | 6 |
| 3 | 6 | 6 | 24 |

Thus the intermediate output is `[1, 1, 2, 6]`, precisely the exclusive prefix products.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Before processing index `i`, `left` equals the product of al... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Backward pass: generate suffix products on demand

The second loop travels from `n - 1` down to `0`. Before processing index `i`, `right` equals the product of all elements strictly after `i`:

$$
\text{right}=\prod_{j=i+1}^{n-1}\text{nums}[j].
$$

At that moment, `ans[i]` already holds the product strictly before `i`. Multiplying `ans[i] *= right` combines the two disjoint sides and produces the final product except  The solution then runs `right *= nums[i]`, adding the current element only for the benefit of the next index to the left.

Again, update order matters. The suffix accumulator must be used before `nums[i]` enters it; otherwise the result would incorrectly contain the excluded element.

Continuing the example, the backward pass behaves as follows:

| Index `i` | Stored left product | `right` before update | Final `ans[i]` | `right` after update |
|---:|---:|---:|---:|---:|
| 3 | 6 | 1 | 6 | 4 |
| 2 | 2 | 4 | 8 | 12 |
| 1 | 1 | 12 | 12 | 24 |
| 0 | 1 | 24 | 24 | 24 |

The result is `[24, 12, 8, 6]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[24, 12, 8, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[24, 12, 8, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Total product followed by division:** This can:** - **Total product followed by division:** This can be linear time for arrays without zero, but division is explicitly forbidden. It also needs special counting logic for zero values and is therefore not the intended formulation.
- **One multiplication loop per output:** For each index, multiplying every other element is simple but repeats almost all work. It takes $O(n^2)$ time and is too slow for up to $10^5$ elements.
- **Separate prefix and suffix arrays:** Building `left[i]` and `right[i]` arrays makes the same identity visually explicit and still runs in $O(n)$ time, but it consumes $O(n)$ auxiliary space. The implemented solution compresses one side into the output and the other into one scalar.
- **One zero:** Only the zero's own position can have a nonzero result; the two-pass multiplication obtains this without detecting the zero explicitly.
- **Multiple zeros:** Every output contains a zero among its included factors, so all results are zero. No branch or reset is required.
- **Negative elements:** Prefix and suffix multiplication preserve signs normally. An odd number of included negative factors gives a negative output; an even number gives a nonnegative output.
- **Array of length two:** The forward and backward invariants still apply. For `[a, b]`, the empty products ensure the answer is `[b, a]`.
- **Values equal to one or minus one:** They do not break either invariant. They merely preserve or flip the accumulated product as ordinary multiplication dictates.
- **Overflow assumptions:** The statement guarantees that the relevant products fit in a 32-bit integer. Python integers can grow beyond that anyway, but implementations in fixed-width languages may rely on the stated guarantee rather than introducing division or floating-point arithmetic.
- **In-place overwrite of `nums`:** Reusing the input array would destroy original values still needed by the backward pass unless they were saved elsewhere. Using the required output array as prefix storage avoids that dependency and preserves the input.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of elements in `nums`. The forward pass visits all $n$ indices once, and the backward pass visits all $n$ indices once. Each visit performs a constant amount of work, so the total running time is $O(n)$. The two passes are additive—$O(n)+O(n)=O(n)$—rather than multiplicative.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
