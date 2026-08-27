# Guided Example: Element Appearing More Than 25% In Sorted Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [1, 2, 2, 6, 6, 6, 6, 7, 10]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array **sorted** in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

The objective is to compute `6` from `{"arr": [1, 2, 2, 6, 6, 6, 6, 7, 10]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sorted equal values form contiguous blocks

Let $n$ be the array length and $q=\lfloor n/4\rfloor$. An element appearing more than 25 percent of the time has an integer frequency greater than $n/4$, which means at least $q+1$ occurrences.

Because the array is sorted, all copies of one value occupy one contiguous block. If a block begins at index $s$ and has at least $q+1$ elements, both `arr[s]` and `arr[s + q]` lie inside it and are equal.

The exact source scans starting positions `i` and checks `arr[i] == arr[i + q]`, where `n >> 2` computes floor division by four for nonnegative $n$.

Right-shifting a nonnegative integer by two bits is equivalent to integer division by $2^2=4$. The shift is therefore only a compact spelling of `n // 4`; it does not change the mathematical threshold or inspect array values as bits.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [1, 2, 2, 6, 6, 6, 6, 7, 10]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why equality proves the frequency threshold

If the values at positions $i$ and $i+q$ are equal, sorted order forces every element between them to be equal as well. That block contains at least $q+1$ elements.

Since $q=\lfloor n/4\rfloor$, $q+1>n/4$. Therefore the value occupies more than 25 percent of the array and must be the guaranteed special element.

This implication also prevents returning an ordinary shorter block. Any equality at that spacing is sufficient proof of the required frequency.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If the values at positions $i$ and $i+q$ are equal, sorted o... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the loop returns before its index could go out of range

The source uses `enumerate(arr)` rather than explicitly stopping at `n - q`. For late indices, `i + q` could exceed the array bounds. Nevertheless, the problem guarantee ensures the function returns first.

Let $s$ be the first index of the guaranteed special block. Its frequency is at least $q+1$, so `s + q <= n - 1`. When the loop reaches `i = s`, the indexed comparison is valid and equal, and the function returns. It never proceeds to a dangerous later index.

Without the guaranteed qualifying element, this exact loop would need a bounded range and a fallback return to be robust.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [1, 2, 2, 6, 6, 6, 6, 7, 10]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Quartile candidates plus binary search:** The :** - **Quartile candidates plus binary search:** The special block must cover at least one of the quarter positions. Binary-searching each candidate's first and last occurrence achieves $O(\log n)$ time and $O(1)$ space.
- **Frequency hash map:** Counting all values takes $O(n)$ time and $O(n)$ space but ignores sorted order.
- **Run-length scan:** Count each contiguous block and return the one longer than $n/4$. It is robust and linear but maintains more explicit state.
- **Bound the exact loop:** Iterating only through `range(n - q)` avoids relying on guaranteed early return and is safer general code.
- **Small arrays with `q = 0`:** The first self-comparison succeeds; the uniqueness guarantee determines that this is valid.
- **Special block at the beginning:** The first comparison may return immediately.
- **Special block at the end:** The loop reaches its valid block start and returns before any out-of-range access.
- **Strictly more than 25 percent:** Requiring $q+1$ occurrences correctly handles lengths not divisible by four.
- **Sorted-order requirement:** Without sorting, equal endpoints would not prove that the elements between them match.
- **Missing valid element:** Outside the contract, the exact source could run out of bounds and has no fallback return.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. In the worst case, the special block may begin late enough that the loop examines $O(n)$ indices before finding it. Each comparison is constant time, so the exact shipped source takes $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
