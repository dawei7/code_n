# Guided Example: Shuffle the Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 5, 1, 3, 4, 7], "n": 3}`
- **Required output:** `[2, 3, 5, 4, 1, 7]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the array `nums` consisting of `2n` elements in the form `[x_1,x_2,...,x_n,y_1,y_2,...,y_n]`.

The objective is to compute `[2, 3, 5, 4, 1, 7]` from `{"nums": [2, 5, 1, 3, 4, 7], "n": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Split the structured input into corresponding halves.** The first `n` entries are `x_1` through `x_n`, and the remaining `n` entries are `y_1` through `y_n`. The slices `nums[:n]` and `nums[n:]` create those two sequences.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 5, 1, 3, 4, 7], "n": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Because `nums.length = 2n`, both slices have exactly `n` elements. Position zero of the first slice corresponds to position zero of the second, position one corresponds to position one, and so on.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Because `nums.length = 2n`, both slices have exactly `n` ele... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Zip corresponding x and y values.** `zip(nums[:n], nums[n:])` lazily yields pairs `(x_1, y_1)`, `(x_2, y_2)`, through `(x_n, y_n)`. This captures the desired association directly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 3, 5, 4, 1, 7]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 5, 1, 3, 4, 7], "n": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 3, 5, 4, 1, 7]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit result loop:** Append `nums[i]` and `:** - **Explicit result loop:** Append `nums[i]` and `nums[n+i]` for every `i`. It avoids the two half slices while still using `O(n)` output space.
- **Preallocated result:** Create a length-`2n` list and assign positions `2i` and `2i+1`. It makes the index mapping explicit.
- **In-place bit packing:** Given the bounded values, two numbers can temporarily share one integer's bits. This can achieve constant auxiliary space but is much harder to read and mutates input.
- **Generator output:** A generator could yield alternating values with constant working space, but the required return type is a list.
- **n equals one:** Zip creates one pair and the output is the two original values in the same order.
- **Duplicate values:** Pairing uses positions, so duplicates cause no ambiguity.
- **Equal halves:** Identical values are still copied once from every original position.
- **Equal-length guarantee:** It ensures `zip` does not silently drop an unmatched element.
- **Input preservation:** Slicing and result construction leave `nums` unchanged.
- **Output length:** Every one of the `n` pairs contributes two entries, giving exactly `2n`.
- **Order inside a pair:** Iterating the tuple yields first-half value before second-half value, as required.
- **Slice allocation:** The concise implementation uses linear temporary storage in addition to the linear output.
- **Value bounds:** They do not matter to this direct construction; they matter only for optional bit-packing alternatives.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Creating the two slices copies `2n` references in total, taking `O(n)` time and space. Zip yields `n` pairs, and flattening appends two values per pair, taking another `O(n)` time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
