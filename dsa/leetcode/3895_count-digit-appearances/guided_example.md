# Guided Example: Count Digit Appearances

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [12, 54, 32, 22], "digit": 2}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `digit`.

The objective is to compute `4` from `{"nums": [12, 54, 32, 22], "digit": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: How modulo 10 reveals the last digit

For any positive integer $x$, Euclidean division by 10 gives

$$
x=10q+r,
\qquad 0\le r<10.
$$

The remainder $r=x\bmod10$ is exactly the rightmost decimal digit, and the quotient $q=\lfloor x/10\rfloor$ is the number formed by removing that digit.

The source expresses these two steps as



After comparing `v` with the requested `digit`, integer division moves the next decimal position into the units place. Repeating this process walks from right to left through the number.

For example, with $x=1202$ and `digit = 2`:

1. $1202\bmod10=2$, so the answer increases; integer division leaves 120.
2. $120\bmod10=0$, so nothing is added; integer division leaves 12.
3. $12\bmod10=2$, so the answer increases again; integer division leaves 1.
4. $1\bmod10=1$, so nothing is added; integer division leaves 0.

The loop then stops. Both occurrences of 2 were counted, including the one separated from the other by a zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [12, 54, 32, 22], "digit": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the loop visits every written digit once

A positive integer with $d$ decimal digits satisfies

$$
10^{d-1}\le x<10^d.
$$

Each floor division by 10 removes exactly one decimal position. After $d$ divisions the value becomes zero, while it remains positive before then. Therefore `while x` performs exactly $d$ iterations.

On iteration $q$, the modulo operation reveals the position that has not yet been visited at the right edge. No position can be skipped, because division removes only the digit just inspected. No position can be repeated, because that digit is permanently removed before the next iteration.

The condition



adds one for precisely the visited positions whose value equals the requested digit. After all numbers have been processed, `ans` is the sum of those per-position indicators, which is the requested total.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A positive integer with $d$ decimal digits satisfies

$$
10^... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why zeros inside a number are handled

When the requested digit is zero, it is important not to confuse an internal written zero with nonexistent leading zeros.

For a number such as 1005, the successive remainders are 5, 0, 0, and 1. The two actual zeros are exposed and counted. Once division reduces the remaining prefix to zero, the loop stops. It does not continue producing an unlimited sequence of artificial leading-zero remainders.

Thus the arithmetic loop matches the ordinary decimal representation: internal and trailing zeros count, while leading zeros that are not written do not.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [12, 54, 32, 22], "digit": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **String conversion:** Summing `str(x).count(str:** - **String conversion:** Summing `str(x).count(str(digit))` is concise and still $O(S)$, but it allocates decimal strings; the source performs the same scan arithmetically with constant auxiliary space.
- **Frequency table for every digit:** Building ten counts while visiting each position is useful if many digit queries share the same array, but it stores and computes information unnecessary for one requested digit.
- **Requested digit zero:** Actual zero positions inside positive numbers are counted, while nonexistent leading zeros are not.
- **Trailing zeros:** A value such as 1200 exposes two zero remainders before the quotient becomes 12, so both zeros count.
- **Repeated requested digit:** Every matching position increments `ans` independently; a number contributes more than one when appropriate.
- **No matches:** The accumulator remains zero and is returned directly.
- **Single-digit number:** The inner loop runs once, compares that sole digit, and then terminates.
- **Maximum value \(10^6\):** Its decimal representation has seven positions, including six zeros after the leading one; the loop handles all seven.
- **Input value zero outside the contract:** `while x` would skip it and fail to count its conventional single zero digit. Supporting zero-valued elements would require a special case.
- **Negative values outside the contract:** Python's floor division keeps negative values negative, so this loop would not terminate correctly for them. The positive-integer constraint is essential.
- **Input preservation:** Reassigning the loop variable does not change `nums` because the array elements are immutable integers.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
