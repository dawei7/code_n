# Guided Example: Number of Days in a Month

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"year": 1992, "month": 7}`
- **Required output:** `31`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a year `year` and a month `month`, return *the number of days of that month*.

The objective is to compute `31` from `{"year": 1992, "month": 7}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only February depends on the year

Month lengths follow a fixed calendar table. April, June, September, and November have thirty days. February has either twenty-eight or twenty-nine. Every other valid month has thirty-one.

Therefore, the only computation involving `year` is whether it is a Gregorian leap year. After that Boolean is known, a direct month-indexed lookup gives the answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"year": 1992, "month": 7}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Apply the complete leap-year rule

A year is a leap year when either:

- it is divisible by four but not divisible by one hundred, or
- it is divisible by four hundred.

The expression:

`(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`

implements those clauses exactly.

The century exception matters. Year 1900 is divisible by four, but it is also divisible by one hundred and not by four hundred, so it is not a leap year. Year 2000 is divisible by four hundred, so the second clause makes it a leap year.

Ordinary years such as 1992 that are divisible by four and not by one hundred satisfy the first clause.

The rule can be understood as successive refinement. Divisibility by four supplies the normal extra-day pattern. Divisibility by one hundred removes that extra day for century years. Divisibility by four hundred restores it for every fourth century. The Boolean expression encodes those exceptions without needing nested conditionals.

Remainder zero is the exact test for divisibility. For example, `1900 % 100 == 0` activates the century exclusion, while `1900 % 400 != 0` prevents restoration. For 2000, both century tests are true but the four-hundred clause independently makes the entire `or` expression true.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build a one-based lookup table

The list `days` begins with an unused zero at index zero. This aligns list indices directly with month numbers one through twelve, avoiding a repeated `month - 1` conversion.

February’s entry is `29 if leap else 28`. Every other entry is the fixed length for that month:

`[31, February, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`.

Returning `days[month]` is safe because the contract guarantees `1 <= month <= 12`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `31` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"year": 1992, "month": 7}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `31` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional branches:** Return thirty for months four, six, nine, and eleven; handle February separately; return thirty-one otherwise. It avoids list allocation but can be less visually systematic.
- **Calendar library:** A standard library can supply month lengths, but the leap rule is simple and the interview problem expects direct reasoning.
- **Store February as twenty-eight then add leap:** A fixed table plus `int(leap)` for month two is equivalent.
- **Year divisible by four:** It is not automatically leap if it is also a non-four-hundred century.
- **Year 1900:** Divisible by one hundred but not four hundred, so February has twenty-eight days.
- **Year 2000:** Divisible by four hundred, so February has twenty-nine days.
- **Thirty-day month:** April, June, September, and November map to thirty regardless of year.
- **January and December:** Both map to thirty-one.
- **Minimum and maximum years:** The modular rule applies uniformly throughout the stated range.
- **Valid month guarantee:** Index zero is never returned, and no out-of-range list access occurs.
- **One-based sentinel:** The initial zero is alignment padding, not a possible month length.
- **Boolean precedence:** Parentheses make the two leap-year clauses explicit and prevent misreading the mixture of `and` and `or`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The repository playbook classifies this as a bounded-domain problem. Each call selects one of exactly twelve months and performs a fixed number of remainder, comparison, Boolean, list-construction, and indexing operations.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
