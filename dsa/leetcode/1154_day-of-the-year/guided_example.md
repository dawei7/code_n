# Guided Example: Day of the Year

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"date": "2019-01-09"}`
- **Required output:** `9`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `date` representing a <a href="https://en.wikipedia.org/wiki/Gregorian_calendar" target="_blank">Gregorian calendar</a> date formatted as `YYYY-MM-DD`, return *the day number of the year*.

The objective is to compute `9` from `{"date": "2019-01-09"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert the date into year, month, and day numbers

The input always has the fixed format `YYYY-MM-DD`. Splitting on `'-'` produces the three strings for year, month, and day. The generator expression applies `int` to each part, and tuple unpacking assigns them to `y`, `m`, and `d`.

For example, `"2019-02-10"` becomes year `2019`, month `2`, and day `10`. Leading zeros are accepted naturally by integer conversion.

The contract guarantees a valid Gregorian date, so the solution does not need to reject malformed separators, nonexistent months, or an out-of-range day within a month.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"date": "2019-01-09"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Apply the complete Gregorian leap-year rule

February has 28 days in an ordinary year and 29 in a leap year. A Gregorian year is a leap year when either:

- it is divisible by 400; or
- it is divisible by 4 but not divisible by 100.

The code expresses this as

`y % 400 == 0 or (y % 4 == 0 and y % 100)`.

The final `y % 100` is an integer rather than an explicit comparison. In Python's Boolean context, zero is false and any nonzero value is true. Therefore, this expression means `y % 100 != 0`. The logic is equivalent to the conventional fully explicit rule.

This distinction is necessary around century years. Year 1900 is divisible by 100 but not 400, so it is not a leap year. Year 2000 is divisible by 400, so it is a leap year. Merely testing divisibility by four would get 1900 wrong.

The conditional expression stores the February length in `v`: 29 when the leap rule is true and 28 otherwise.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build the month-length table

The list `days` contains the twelve Gregorian month lengths in order:

`[31, v, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`.

Only February depends on the year, so every other entry is a fixed constant. The list has exactly one entry per month, with January at index zero and December at index eleven.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `9` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"date": "2019-01-09"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `9` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use a date-library day-of-year formatter:** A standard library can solve the task, but its parsing conventions and platform behavior add dependencies to a calculation that needs only twelve fixed month lengths.
- **Use cumulative month offsets:** Precomputing the number of days before each month avoids the slice and sum. A leap-day adjustment after February would still be needed.
- **Loop through earlier months:** An explicit loop is equivalent to `sum(days[: m - 1])` and remains constant because there are only twelve months.
- **Test only divisibility by four:** This incorrectly treats years such as 1900 as leap years. Century years require the 400-year exception.
- **January dates:** No earlier month contributes, so the result equals `d`.
- **February 29:** It occurs only in a valid leap-year input. The February length is 29, and the returned ordinal includes it correctly.
- **Dates after February in a leap year:** The earlier-month sum includes the extra day, increasing the ordinal by one relative to an ordinary year.
- **December 31:** The method sums the first eleven months and adds 31, producing 365 or 366 according to the leap rule.
- **Year 1900:** Divisible by 100 but not 400, so February has 28 days.
- **Year 2000:** Divisible by 400, so February has 29 days.
- **Truthiness of `y % 100`:** A nonzero remainder means “not divisible by 100.” Rewriting it as `y % 100 != 0` would be more explicit but not change behavior.
- **Valid-input guarantee:** The code assumes the calendar date, separators, month, and day are valid because the contract guarantees them.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Splitting a ten-character string, converting three bounded-length numeric fields, evaluating a fixed number of remainder operations, constructing a twelve-element list, and summing at most eleven entries all take bounded work. The time complexity is `O(1)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
