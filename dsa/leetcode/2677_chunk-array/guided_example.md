# Guided Example: Chunk Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [1, 2, 3, 4, 5], "size": 1}`
- **Required output:** `[[1], [2], [3], [4], [5]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `arr` and a chunk size `size`, return a **chunked** array.

The objective is to compute `[[1], [2], [3], [4], [5]]` from `{"arr": [1, 2, 3, 4, 5], "size": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A chunk is one consecutive half-open range

The output must preserve every element and its order while grouping consecutive elements into subarrays of at most `size` elements.

For a chunk beginning at index `i`, the intended indices are:

$$
i,i+1,\ldots,\min(i+\texttt{size},n)-1.
$$

JavaScript's `slice(start, end)` uses exactly this half-open convention: it includes `start` and stops before `end`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [1, 2, 3, 4, 5], "size": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Start only at chunk boundaries

The loop initializes `i = 0` and advances with `i += size`. Its successive values are:

$$
0,\texttt{size},2\cdot\texttt{size},\ldots
$$

These are precisely the first indices of the desired chunks. There is no need for an inner loop to search for boundaries because the positive chunk size fixes them.

At each boundary, the implementation appends:

`arr.slice(i, i + size)`.

That slice becomes one independent subarray in `ans`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the final chunk needs no special branch

The last starting index may have fewer than `size` elements remaining. `slice` safely limits its end to `arr.length` when `i + size` lies beyond the array.

For `arr = [1, 9, 6, 3, 2]` and `size = 3`:

- `slice(0, 3)` produces `[1, 9, 6]`;
- `slice(3, 6)` reaches the physical end and produces `[3, 2]`.

The result follows the contract without padding and without reading nonexistent values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1], [2], [3], [4], [5]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [1, 2, 3, 4, 5], "size": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1], [2], [3], [4], [5]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Nested loops with `push`:** Also $O(n)$ and avoids `slice`, but requires more manual boundary bookkeeping.
- **Use `reduce`:** It can append to the latest chunk or create a new one, though the stride formulation exposes boundaries more directly.
- **Use `splice`:** It can remove chunks from the front, but it mutates the input and front removals can be costly.
- **Lodash `_.chunk`:** Explicitly disallowed by the problem.
- **Empty input:** Returns `[]` rather than `[[]]`.
- **Size one:** Produces one single-element subarray per input element.
- **Size equal to length:** Produces one full-size chunk.
- **Size larger than length:** Produces one shorter chunk for nonempty input.
- **Non-divisible length:** Only the final chunk has fewer than `size` elements.
- **Exactly divisible length:** No trailing empty chunk is created.
- **Object elements:** References are copied shallowly; nested objects are not cloned.
- **Input preservation:** `slice` leaves `arr` and its ordering unchanged.
- **Positive-size guarantee:** It ensures the loop advances and terminates.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop itself runs $\lceil n/\texttt{size}\rceil$ times. A slice copies the number of elements in its range, and the ranges partition all $n$ elements. Total time is therefore $O(n)$ rather than the number of chunks multiplied by $n$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
