# Guided Example: Plus One

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"digits": [1, 2, 3]}`
- **Required output:** `[1, 2, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **large integer** represented as an integer array `digits`, where each $\text{digits}[i]$ is the $i^{\text{th}}$ digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

The objective is to compute `[1, 2, 4]` from `{"digits": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Addition begins at the least significant digit

The array stores the most significant digit first, so the units digit is at the final index. Adding one affects that digit first. Only when it overflows from 9 to 0 does a carry need to move left.

The loop therefore visits indices from `n - 1` down to 0. It stops as soon as a digit absorbs the increment without overflow. Digits farther left are then unchanged, exactly as in ordinary decimal addition.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"digits": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How three short statements encode carry propagation

For the current digit, the source performs:

1. add one;
2. reduce modulo 10;
3. return if the result is not zero.

Given the contract that every entry is from 0 through 9, there are only two cases. An original digit from 0 through 8 becomes 1 through 9 after modulo, which is nonzero. It absorbs the carry, so the complete answer is ready. An original 9 becomes 10 and then 0, which means one carry must be applied to the next position on the left.

The test `digits[i] != 0` is therefore equivalent to “the carry has ended” for this exact operation. It would not be a general carry test for arbitrary added values, but it is exact when adding one to one decimal digit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace without a long carry

For `[1,2,3]`, the loop visits only the final digit. It becomes 4, remains nonzero, and the method returns `[1,2,4]`. The first two entries are never touched.

For `[1,2,9]`, the final 9 becomes 0 and the loop continues. The 2 becomes 3, so the method returns `[1,3,0]`. The zero already written at the end is the correct result of the propagated carry.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"digits": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit carry variable:** Start `carry = 1`, use `divmod(digit + carry, 10)`, and stop when carry becomes zero. It generalizes more easily to adding other values.
- **Check for 9 directly:** Set a 9 to zero; otherwise increment and return. This is the competitive branch's more verbal form of the same logic.
- **Convert to an integer:** It is concise in Python but defeats the digit-array exercise and would overflow fixed-width types for long input.
- **Final digit below 9:** Only one array entry changes, giving best-case constant time.
- **Trailing run of nines:** Exactly that suffix becomes zero, and the first lower digit increments.
- **All nines:** A new leading 1 is prepended to the zeroed original digits.
- **Single zero:** It becomes `[1]`; zero is the one valid representation that may contain digit 0 alone.
- **Single nine:** The original list becomes `[0]`, and the returned new list is `[1,0]`.
- **No leading zeros:** The algorithm never needs to normalize or discard a prefix.
- **Caller-visible mutation:** The input is modified even in the branch that ultimately returns a newly allocated list.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. In the worst case, every digit is 9 and the loop visits all $n$ entries. Constructing the longer result also copies $n$ zeros, so time is $O(n)$. When the last digit is below 9, the method returns after constant work.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
