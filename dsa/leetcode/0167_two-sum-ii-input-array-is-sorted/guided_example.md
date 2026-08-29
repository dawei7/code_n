# Guided Example: Two Sum II - Input Array Is Sorted

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"numbers": [2, 7, 11, 15], "target": 9}`
- **Required output:** `[1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **1-indexed** array of integers `numbers` that is already ***sorted in non-decreasing order***, find two numbers such that they add up to a specific `target` number. Let these two numbers be $numbers[\text{index}_{1}]$ and $numbers[\text{index}_{2}]$ where $1 \le \text{index}_{1} < \text{index}_{2} \le \text{numbers.length}$.

The objective is to compute `[1, 2]` from `{"numbers": [2, 7, 11, 15], "target": 9}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn each left value into a complement search

For an index `i`, the only value that can pair with `numbers[i]` is:

`x = target - numbers[i]`.

Because `numbers` is sorted in non-decreasing order, the source can search for
`x` with binary search rather than scanning every later element. It loops over
all possible first indices from zero through `n - 2`.

The search begins at `lo = i + 1`. This boundary is essential: it prevents
using the same array element twice and guarantees the returned first index is
smaller than the second. A matching value at index `i` itself is irrelevant
unless another equal copy exists later.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"numbers": [2, 7, 11, 15], "target": 9}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use lower bound and verify the candidate

`bisect_left(numbers, x, lo=i + 1)` returns the first index at or after
`i + 1` where `x` could be inserted without breaking sorted order.

There are two possible outcomes:

- if `j < n` and `numbers[j] == x`, the complement actually exists and the
  source returns the pair;
- if `j == n` or `numbers[j] != x`, there is no occurrence of `x` in the
  searched suffix, so this `i` cannot begin the solution.

The equality check cannot be omitted. A lower-bound function always returns an
insertion position, even when the requested value is absent.

Duplicates are handled correctly. Lower bound chooses the first suitable copy
after `i`, and the contract's unique-solution guarantee ensures whichever
matching pair is found is the required one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the sorted property makes each rejection conclusive

Binary search compares `x` with middle values of the suffix. If a middle value
is smaller, every earlier value in that current search portion is also too
small; if larger, every later value is too large. This halves the suffix until
the first possible location remains.

If that location is not equal to `x`, no later element can be equal after a
larger value, and no earlier allowed element was skipped by the lower-bound
definition. Moving the outer loop to `i + 1` is therefore safe.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"numbers": [2, 7, 11, 15], "target": 9}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two pointers:** Start at both ends; move the left pointer for a sum below target and the right pointer for a sum above target. It achieves the required $O(n)$ time and $O(1)$ space.
- **Hash map:** Finds complements in expected $O(n)$ time but uses $O(n)$ storage, violating the constant-space requirement.
- **Brute force:** Tests every index pair in $O(n^2)$ time.
- **Duplicate values:** Searching from `i + 1` permits two equal values at distinct indices.
- **Negative target and values:** Subtraction and sorted comparisons remain valid.
- **One-based output:** Both internal indices must be incremented exactly once.
- **Unique solution:** It justifies returning the first match and omitting a no-solution result.
- **Same-element prohibition:** The lower search boundary enforces it.
- **Manifest mismatch:** Repeated binary searches are $O(n\log n)$, not linear.
- **Missing imports:** Both `bisect_left` and `List` must be provided for standalone execution.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length. There can be $O(n)$ outer iterations, and each
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
