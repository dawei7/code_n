# Guided Example: Concatenate Array With Reverse

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `[1, 2, 3, 3, 2, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`.

The objective is to compute `[1, 2, 3, 3, 2, 1]` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the description into index equations

For an original index $i$, where $0\le i<n$, the value `nums[i]` belongs at answer index $i$. That gives the first assignment:

`ans[i] = x`,

where `x` is the value supplied by `enumerate(nums)`.

The second half begins at index $n$. Its first position must receive the last input value, its second position must receive the next-to-last value, and so on. When the loop variable is $i$, the matching source index is

$$
n-1-i.
$$

The corresponding destination index is $n+i$, so the second assignment is:

`ans[i + n] = nums[n - i - 1]`.

These two equations are the whole algorithm. Thinking in indices is especially useful here because it removes any ambiguity about whether the middle boundary or an endpoint is duplicated incorrectly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Walking through the positions

Consider an illustrative input `nums = [4, 7, 2]`. Its length is $n=3$, so the source first creates six slots:

`[0, 0, 0, 0, 0, 0]`.

The loop then performs two useful writes per iteration:

- At $i=0$, it places `4` at index $0$ and `nums[2] = 2` at index $3$.
- At $i=1$, it places `7` at index $1$ and `nums[1] = 7` at index $4$.
- At $i=2$, it places `2` at index $2$ and `nums[0] = 4` at index $5$.

The completed array is `[4, 7, 2, 2, 7, 4]`. The two copies of `2` at the boundary are intentional: the result concatenates the entire original array with the entire reversed array. Neither half drops an endpoint.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Consider an illustrative input `nums = [4, 7, 2]`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every destination is filled exactly once

During the loop, $i$ ranges over all indices from $0$ to $n-1$. The first assignment therefore fills exactly the destination interval

$$
[0,n-1].
$$

Adding $n$ to the same loop indices makes the second assignment fill exactly

$$
[n,2n-1].
$$

Those intervals are disjoint and together cover the complete allocated answer. No placeholder zero remains unwritten, and no destination receives competing writes.

For the reversed half, the expression $n-1-i$ starts at $n-1$ when $i=0$ and ends at $0$ when $i=n-1$. It decreases by one on each iteration. Thus it visits every valid input index exactly once in descending order. This establishes that the second half is neither an arbitrary permutation nor merely another forward copy: it is exactly the reversal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3, 3, 2, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3, 3, 2, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Use slicing and concatenation:** `nums + nums[:** - **Use slicing and concatenation:** `nums + nums[::-1]` is compact and has the same $O(n)$ time and output-space bounds, but it normally materializes a reversed temporary list before constructing the concatenated result. The source makes the mapping and single result allocation explicit.
- **Append the forward pass, then append a reverse traversal:** This is also correct and easy to read. It grows the result dynamically and uses two loops instead of filling two known destinations during one loop.
- **Reverse the input in place:** Mutating `nums` would lose the original ordering unless it had first been copied, and it would create an unnecessary side effect visible to the caller.
- **Insert repeatedly at the front:** Front insertion in a Python list shifts existing values and can turn a linear task into quadratic work. Direct indexed writes avoid all shifting.
- **Single-element input:** The one value appears twice. For `[x]`, both the original and its reversal are `[x]`, so the result is `[x, x]`.
- **Repeated or symmetric values:** Equal values do not change the index reasoning. Even if the output visually resembles another ordering, the source still writes each half from the correct source indices.
- **Zeros in the input:** The zeros used for initial allocation cannot be mistaken for unfinished slots because every position is overwritten exactly once.
- **Logically empty input:** If an empty list were supplied, the allocation and loop would produce an empty list, which is the concatenation of the empty list with its reverse. The source handles this naturally even if the formal constraints guarantee a nonempty input.
- **Large integer values:** Values are copied, not arithmetically transformed, so their magnitudes have no effect on the algorithm or its index safety.
- **Aliasing expectations:** The returned list is new. Later assignment to an element of `ans` does not alter the corresponding top-level element slot in `nums`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. Allocating `ans` with $2n$ entries takes $O(n)$ time. The loop runs exactly $n$ iterations and performs a constant amount of work in each iteration: one enumerated read, one indexed read, a few integer index calculations, and two indexed writes. The total time complexity is therefore $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
