# Guided Example: Find The Least Frequent Digit

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1553322}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, find the digit that occurs **least** frequently in its decimal representation. If multiple digits have the same frequency, choose the **smallest** digit.

The objective is to compute `1` from `{"n": 1553322}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count decimal digits without converting to text

The source uses a ten-entry list `cnt`, where `cnt[d]` records how many times digit `d` appears in the decimal representation.

Repeatedly applying

`n, x = divmod(n, 10)`

does two things at once:

- `x` is the remainder after division by ten, which is the current last decimal digit.
- The new `n` is the quotient, which removes that last digit.

For example, starting with `155` gives digit five and remaining number fifteen; the next step gives another five and remaining number one; the final step gives digit one and remaining number zero.

The loop processes digits from right to left, but frequency does not depend on order. Each original digit contributes exactly one increment to its corresponding bucket.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1553322}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Consider only digits that actually occur

The phrase “digit that occurs least frequently in its decimal representation” refers to present digits. A digit absent from `n` has frequency zero, but it is not a candidate.

This is why the selection condition includes

`0 < v`.

Without that check, the algorithm would almost always return the smallest absent digit, usually zero, instead of the least frequent present digit.

The constraint `n >= 1` guarantees that the counting loop runs at least once and some bucket is positive. If zero itself were an allowed complete input, the loop would need a special case to count its single decimal digit `0`, but that situation is outside the contract.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Scan candidate digits in increasing order

After counting, the source enumerates `cnt` from digit zero through digit nine. It stores the smallest frequency found so far in `f` and the associated digit in `ans`.

The update occurs only when

`0 < v < f`.

If a digit has a strictly smaller positive frequency, it becomes the new answer. If it ties `f`, the source does not replace the existing answer.

Because candidates are visited in increasing numeric order, the existing answer in a tie is always the smaller digit. Thus the strict update comparison implements both priorities:

1. Minimize frequency.
2. Among equal frequencies, minimize digit value.

This is equivalent to minimizing the pair `(frequency, digit)` over present digits, but the explicit scan avoids constructing pairs or sorting.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1553322}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Convert to a string and use `Counter`:** This is concise and still `O(d)`, but allocates the decimal text and a mapping.
- **Sort present `(frequency, digit)` pairs:** It produces the right lexicographic minimum but performs unnecessary sorting over a ten-value domain.
- **Include zero-frequency buckets:** This returns an absent digit and misinterprets “occurs least frequently.”
- **Replace on equal frequency:** Scanning upward and replacing ties would select the largest tied digit. The source updates only on a strict improvement.
- **Digit zero inside `n`:** Division and remainder count internal or trailing zeros normally, such as the two zeros in `100`.
- **Input `n = 1`:** Only digit one occurs, so it is returned.
- **All digits equally frequent:** The smallest digit that actually occurs is returned.
- **One repeated digit:** That digit is the only candidate even though its frequency may be large.
- **Complete input zero:** It would need special handling, but the constraint `n >= 1` excludes it.
- **Local mutation of `n`:** Replacing the local integer with its quotient does not mutate caller-owned state.
- **Missing import:** The stored source uses `inf` without importing it. Standalone Python needs `from math import inf` unless the harness supplies the name.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let `d` be the number of decimal digits in `n`. The division loop runs exactly `d` times. Scanning all ten buckets takes constant time, so total time is `O(d)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
