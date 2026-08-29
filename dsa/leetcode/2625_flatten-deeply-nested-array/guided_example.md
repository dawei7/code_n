# Guided Example: Flatten Deeply Nested Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [], "n": 5}`
- **Required output:** `[]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **multi-dimensional** array `arr` and a depth `n`, return a **flattened** version of that array.

The objective is to compute `[]` from `{"arr": [], "n": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Define depth from the current container

The outermost input array is visited with `depth = 0`. While scanning a container at depth $d$, a nested array value is expanded only when:

$$
d<n.
$$

If expanded, its contents are visited with depth $d+1$. If not expanded, that entire nested array is appended as one output value.

This convention matches the statement:

- with $n=0$, even arrays directly inside the outer array are not flattened;
- with $n=1$, those direct subarrays are flattened, but arrays nested inside them remain intact;
- larger $n$ permits correspondingly deeper expansion.

Thinking of `depth` as the number of array boundaries already flattened on the path avoids off-by-one confusion.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [], "n": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use one result array for the whole traversal

`result` begins empty and is captured by recursive helper `visit`.

The helper loops through `values` from left to right. For each `value`:

- if it is an array and current `depth < n`, recurse into it;
- otherwise, append it to `result`.

All recursive calls write into the same output. This avoids constructing and repeatedly concatenating intermediate arrays, which could copy already-produced elements many times.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `Array.isArray` is the right type test

JavaScript reports arrays as objects under `typeof`. Therefore `typeof value === "object"` cannot distinguish a nested array from an ordinary object.

`Array.isArray(value)` performs the intended distinction. Only nested arrays are containers to flatten; numbers are appended, and under a broader JSON-style input an ordinary object would also remain a value.

The contract specifically describes integers and arrays, so every leaf is a number, but using the precise built-in predicate keeps the recursive rule explicit.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [], "n": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit stack:** Avoid recursion-depth limits; push elements in reverse order so popping preserves left-to-right output.
- **Queue with repeated splicing:** Can preserve order but may shift or copy many elements and become inefficient.
- **Built-in `Array.flat`:** Direct but explicitly forbidden.
- **`n = 0`:** No nested array is expanded, though a new outer result array is still produced.
- **Depth exceeds maximum nesting:** Every subarray is flattened and all numeric leaves appear in order.
- **Empty outer array:** The traversal appends nothing and returns an empty array.
- **Empty nested array:** Expanding it contributes no values; preserving it at the limit contributes the empty array itself.
- **Preserved nested reference:** An unflattened subarray is appended without cloning.
- **Order preservation:** Complete each expanded subarray before continuing with its parent's next item.
- **Deep nesting:** Recursion uses one call frame per expanded level and may motivate an iterative stack in stricter runtimes.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V)$. Let $V$ be the number of array containers and values actually visited, and let $R$ be the number of items placed in the result. The traversal performs constant work per visited item, so time is $O(V)$, with $R\le V$ under a node-count interpretation.
- **Auxiliary Space Complexity:** $O(V + D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
