# Guided Example: Add Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num1": "11", "num2": "123"}`
- **Required output:** `"134"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two non-negative integers, `num1` and `num2` represented as string, return *the sum of* `num1` *and* `num2` *as a string*.

The objective is to compute `"134"` from `{"num1": "11", "num2": "123"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Recreate elementary addition one decimal column at a time

The inputs may contain up to $10^4$ digits, so converting an entire string to a built-in integer is both forbidden and contrary to the purpose of the problem. The optimal method performs the same right-to-left addition taught on paper.

Decimal place values align at the right edge. The final character of each string is the ones digit, the preceding character is the tens digit, and so on. The pointers

`i = len(num1) - 1` and `j = len(num2) - 1`

therefore begin at corresponding least-significant digits. Moving both pointers left after each iteration advances to the next place value.

The result digits are discovered from least significant to most significant. They are appended to `ans` in that convenient discovery order and reversed only once at the end.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num1": "11", "num2": "123"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Treat a missing digit as zero

The two strings need not have equal lengths. While pointer `i` remains valid, `a = int(num1[i])`; once it becomes negative, `a = 0`. The same rule produces `b` from `num2` and pointer `j`.

Converting one character such as `'7'` to the small integer `7` is not converting the input number as a whole. It is exactly the per-digit interpretation required for manual arithmetic. A missing higher place in the shorter input contributes zero, just as writing leading zeros for alignment would do, but the algorithm does not actually allocate padded strings.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Separate the current digit from the carry

The variable `c` is the carry entering the current column. Initially it is zero. For digit values `a` and `b`, the column total is `a + b + c`.

The line

`c, v = divmod(a + b + c, 10)`

computes quotient and remainder when that total is divided by ten. The remainder `v` is the output digit for the current place, because it lies from `0` through `9`. The quotient becomes the carry into the next column.

The maximum total is `9 + 9 + 1 = 19`, so the new carry is always either zero or one. For example, adding digits `8` and `7` with incoming carry `1` gives `16`; `divmod(16, 10)` returns `(1, 6)`. The algorithm appends `'6'` now and carries `1` leftward.

The digit is converted back to text with `str(v)` before being appended. As a result, `ans` is a list of string pieces ready for the final join.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"134"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num1": "11", "num2": "123"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"134"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Convert both full strings to integers:** This violates the explicit contract and may rely on arbitrary-precision library behavior the exercise asks the solution to implement.
- **Prepend each new digit to a string:** It mirrors written order but is inefficient with immutable strings because every prepend can copy the accumulated result. A list plus one reversal is linear.
- **Pad the shorter input with leading zeros:** This can simplify indexing and still be correct, but it allocates extra strings unnecessarily. Conditional zero digits provide the same alignment in constant auxiliary state beyond the result.
- **Use character-code subtraction instead of `int` per digit:** `ord(ch) - ord('0')` is equivalent and avoids the digit conversion helper. Both respect the prohibition on converting the complete input.
- **Different input lengths:** Once one pointer is negative, its digit is zero while the other number continues normally.
- **Final carry:** Sums such as `"9" + "1"` need an additional most-significant digit. Including `c` in the loop condition produces it.
- **No final carry:** The loop stops after the last real column and adds no spurious leading zero.
- **Both inputs equal zero:** One column produces `'0'`, and the normalized result is exactly `"0"`.
- **Long chains of carries:** Inputs such as `"9999" + "1"` propagate `c = 1` across every column; the invariant handles each independently.
- **Normalized input guarantee:** Except for `"0"`, inputs have no leading zeros. The algorithm would still compute the numeric sum if leading zeros were present, but normalization of the returned representation relies on the stated contract.
- **Maximum-length inputs:** Work and storage grow linearly with the number of digits; no recursion or whole-number conversion risks numeric overflow.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\max(m,n)$. Let $m = \lvert\texttt{num1}\rvert$ and $n = \lvert\texttt{num2}\rvert$. The loop processes one decimal column per iteration and may run once more for a final carry. It therefore executes at most $\max(m,n)+1$ times, giving $O(\max(m,n))$ time. Reversing the digit list and joining it also take linear time in the output length, so the bound is unchanged.
- **Auxiliary Space Complexity:** $O(\max(m,n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
