# Guided Example: Check if Word Equals Summation of Two Words

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"firstWord": "acb", "secondWord": "cba", "targetWord": "cdb"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **letter value** of a letter is its position in the alphabet **starting from 0** (i.e. `'a' -> 0`, `'b' -> 1`, `'c' -> 2`, etc.).

The objective is to compute `true` from `{"firstWord": "acb", "secondWord": "cba", "targetWord": "cdb"}` while avoiding redundant calculations and unnecessary overhead.

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

**Each permitted letter is exactly one decimal digit.** The strings contain only letters from `'a'` through `'j'`. Subtracting the character code of `'a'` maps them to `0` through `9`: `'a' -> 0`, `'b' -> 1`, and `'j' -> 9`. The upper bound at `'j'` is essential. If letters could map to values above nine, simply treating every value as one base-ten digit would no longer match concatenation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"firstWord": "acb", "secondWord": "cba", "targetWord": "cdb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Build the numerical value from left to right.** Helper `f(s)` starts `ans` at zero. For each mapped digit `x`, the update `ans = ans * 10 + x` shifts the value already constructed one decimal place to the left and puts `x` into the newly opened units place. After reading digits `d_0, d_1, ..., d_i`, the accumulator equals the integer represented by their concatenation. This is the same operation people use when reading a decimal number one digit at a time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

For example, `acb` maps to digits `0, 2, 1`. The accumulator progresses as `0`, then `0 * 10 + 2 = 2`, then `2 * 10 + 1 = 21`. The conceptual digit string is `"021"`, and its integer value is `21`. Leading zeros need no explicit removal because integer arithmetic naturally gives them no positional contribution while still shifting correctly for later digits.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"firstWord": "acb", "secondWord": "cba", "targetWord": "cdb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Create a mapped digit string and parse it:** Joining `str(ord(c) - ord('a'))` for all letters and calling `int` matches the definition, but allocates intermediate strings and needs care if the mapped text is empty. The running accumulator is simpler and constant-space.
- **Dictionary lookup:** A mapping from each letter to its digit would work, but the values are consecutive character-code offsets, so a table adds unnecessary storage and setup.
- **Leading `a` letters:** They represent leading zero digits and vanish in the integer value. Words such as `aab` and `b` both evaluate to one, which is intentional.
- **All letters `a`:** Any nonempty all-`a` word evaluates to zero regardless of length. Equality is numeric, not textual.
- **Letter `j`:** It maps to digit nine, confirming that every mapped value remains a single decimal digit. This is the largest supported letter.
- **Different word lengths:** Lengths do not need to match. Each complete word is converted independently before addition.
- **Case sensitivity and alphabet range:** The code assumes lowercase consecutive letters beginning at `'a'`. Uppercase or letters after `'j'` would violate the contract and would not preserve the intended one-digit mapping.
- **Boolean result:** The equality expression already returns Python `true` or `false`. Wrapping it in another conditional would add no behavior.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let $S$ be the total number of characters across `firstWord`, `secondWord`, and `targetWord`. Each character is visited exactly once and performs one character-code subtraction, multiplication by ten, and addition. Under the stated maximum word length of eight, these integers have bounded size, so each operation is constant time and total time is $O(S)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
