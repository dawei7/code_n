# Guided Example: Sort Integers by Binary Reflection

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 5, 4]}`
- **Required output:** `[4, 4, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `[4, 4, 5]` from `{"nums": [4, 5, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn binary reflection into a numeric sort key

Each input value needs two ordering components:

1. its binary reflection;
2. the original value, used when reflections tie.

The source computes the reflection arithmetically and sorts with key `(f(x), x)`. Python compares tuples lexicographically, so it first compares reflected values and consults the original values only when the first components are equal.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 5, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Read the original bits from right to left

The helper `f(x)` maintains an output accumulator `y`, initially zero. While `x` is positive, it repeats

`y = (y << 1) | (x & 1)`

and

`x >>= 1`.

`x & 1` extracts the least significant remaining bit of `x`. The right shift removes that bit from `x`. Therefore the loop sees the original binary digits from last to first, which is exactly the order required in the reflection.

Before appending a bit, `y << 1` makes room on the right. Bitwise OR places the extracted zero or one in that new position. This is the binary analogue of building a decimal number with `result = result * 10 + digit`.

Although the helper reassigns its local parameter `x`, integers are immutable and the array occurrence is not changed by these shifts.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace a reflection one bit at a time

Take `x=6`, whose binary representation is `110`.

- The first extracted bit is 0. Shifting zero and appending zero leaves `y=0`; `x` becomes binary `11`.
- The next bit is 1. `y` becomes binary `1`; `x` becomes binary `1`.
- The last bit is 1. `y` becomes binary `11`, which is decimal 3.

Thus 6 reflects to 3, matching the written reversal `110 -> 011` and the numeric interpretation of `011`.

For `x=5`, bits are read as 1, 0, 1, so `y` becomes binary `101` and remains decimal 5.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4, 4, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 5, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4, 4, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Reverse a binary string:** `int(bin(x)[2:][::-1], 2)` directly mirrors the definition and has the same $O(B)$ key cost, but the exact source uses bit operations.
- **Precompute repeated reflections:** A cache can avoid recomputing `f` for duplicate values. Python's sort already calls the key once per occurrence, and $N\le100$ makes the simple form sufficient.
- **Sort only by reflection:** Reflection collisions exist, such as 3 and 6 both reflecting to 3. Omitting original `x` violates the required tie-break.
- **Sort only by original value:** Numeric order and reflected order can differ sharply; 8 must precede 3 in the example because its reflection is 1.
- **Deduplicate before sorting:** Repeated occurrences must remain repeated in the result.
- **Power of two:** Its binary form is one followed by zeros, so its reflection is 1.
- **Binary palindrome:** A value such as 5 or 7 reflects to itself.
- **Trailing binary zeros:** They become ignored leading zeros of the reflected numeral automatically.
- **Equal reflection, different bit lengths:** The original-value component still gives the specified order.
- **Equal original values:** Both key components tie; both occurrences remain in the list.
- **Positive-input guarantee:** The loop always processes at least one bit. In a generalized call with zero, `f(0)` would return zero because the loop is skipped.
- **Input mutation:** The returned ordering is also written into the caller-provided `nums` list.
- **Fixed bit width versus ordinary representation:** The method reverses only significant binary digits, not a padded 32-bit or 64-bit representation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $N$ be the number of array occurrences and $B$ the maximum bit length of a value.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
