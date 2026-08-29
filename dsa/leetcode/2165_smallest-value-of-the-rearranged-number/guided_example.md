# Guided Example: Smallest Value of the Rearranged Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 310}`
- **Required output:** `103`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `num.` **Rearrange** the digits of `num` such that its value is **minimized** and it does not contain **any** leading zeros.

The objective is to compute `103` from `{"num": 310}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate the sign from the digits

The boolean `neg = num < 0` remembers whether the result must be negative. The assignment `num = abs(num)` removes the sign so every remaining operation deals only with decimal digits.

A ten-entry frequency array `cnt` stores how many copies of each digit occur. Repeatedly taking `num % 10` extracts the last digit, and `num //= 10` removes it. Incrementing `cnt[digit]` preserves duplicates without needing to remember their original order, because arbitrary rearrangement is allowed.

The special input zero makes the extraction loop empty. All counts remain zero and the method later returns zero, which is already the only rearrangement.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 310}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Construct a negative answer in descending digit order

For a negative input, minimizing the signed value means maximizing its positive magnitude. Among numbers with the same number of digits, the largest digit must occupy the highest place value, the next-largest the next position, and so on.

The loop visits digits from nine down to zero. For every occurrence, `ans *= 10` shifts the number left one decimal place and `ans += i` appends digit `i`.

An exchange argument proves this order. If a smaller digit $a$ appears before a larger digit $b$, swapping them increases the magnitude because the larger digit receives the greater place-value coefficient. Repeating exchanges yields descending order and maximum magnitude. Returning `-ans` then gives the smallest signed value.

For `-7605`, descending digits form magnitude 7650, and the result is `-7650`.

Leading zeros are not a concern in the negative branch: if any nonzero digit exists, descending order places it first. If all digits are zero, the original number is simply zero and never enters this branch.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Construct a positive answer without a leading zero

For a positive input, ascending digit order would ordinarily minimize the number, but a zero cannot be the first written digit. If zeros exist, the code finds the smallest digit from one through nine with a positive count. It places that digit into `ans` first and decrements its frequency.

All remaining digits are then appended in ascending order from zero through nine. Consequently, every zero follows the required nonzero leading digit and occupies the earliest remaining, most valuable positions.

This is optimal because the leading position must contain some nonzero digit, so choosing the smallest available nonzero digit minimizes the greatest place-value contribution. After that forced choice, ordinary ascending order minimizes every remaining suffix position by the same exchange argument.

For `310`, the smallest nonzero digit one is placed first. The remaining digits zero and three are appended ascending, producing 103 rather than illegal `013`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `103` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 310}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `103` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort digit characters:** Sorting ascending for positives and descending for negatives is concise, but the positive leading-zero repair is still required.
- **Enumerate permutations:** This is factorial in the digit count and repeats arrangements when digits are duplicated.
- **Positive number with no zero:** All digits are appended in ordinary ascending order.
- **Positive number with several zeros:** Exactly one smallest nonzero digit leads, followed immediately by all zeros, then remaining positive digits.
- **Negative number with zeros:** Descending order naturally places zeros at the end, increasing magnitude relative to placing them earlier.
- **Input zero:** The extraction loop is empty and the final answer remains zero.
- **Repeated digits:** Frequency counts preserve every copy and avoid redundant sorting comparisons.
- **Single nonzero digit plus zeros:** That digit must lead a positive result; all zeros follow it.
- **Sign preservation:** `abs` is only temporary; `neg` determines whether the constructed magnitude is negated.
- **No leading-zero string is built:** The method constructs an integer arithmetically, and its positive first appended digit enforces legality.
- **Bounded digit alphabet:** Scanning all ten digit values is constant regardless of how often each occurs.
- **Input immutability:** Reassigning local integer `num` cannot mutate the caller’s integer object.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d+10)$. Let $d$ be the number of decimal digits. Extraction takes $O(d)$ time. Construction scans ten possible digit values and appends exactly $d$ digits, so total time is $O(d+10)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
