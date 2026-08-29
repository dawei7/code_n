# Guided Example: Number of Days Between Two Dates

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"date1": "2019-06-29", "date2": "2019-06-30"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a program to count the number of days between two dates.

The objective is to compute `1` from `{"date1": "2019-06-29", "date2": "2019-06-30"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Apply the Gregorian leap-year rule exactly

A year is a leap year when it is divisible by four, except that century years must also be divisible by four hundred. The helper returns
`year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)`.

This handles the important cases:

- 2020 is divisible by four and not by one hundred, so it is a leap year.
- 1900 is divisible by one hundred but not four hundred, so it is not a leap year.
- 2000 is divisible by four hundred, so it is a leap year.

A leap year has 366 days; an ordinary year has 365.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"date1": "2019-06-29", "date2": "2019-06-30"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Give February its correct length

`daysInMonth` constructs the twelve month lengths. Every fixed month uses its usual number of days. February is `28 + int(isLeapYear(year))`, so the Boolean contributes one only in a leap year.

The function receives a one-based month and indexes the list with `month - 1`. Valid-date input guarantees that the month is in the supported range.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Convert a date to one cumulative count

`calcDays` splits a string such as `"2020-01-15"` at hyphens and converts the three fields to integers.

It then adds three pieces:

1. For every complete year from 1971 through `year - 1`, add 365 plus its leap-day indicator.
2. For every complete month before `month` in the target year, add that month’s length.
3. Add `day` for the position inside the target month.

The resulting scale is one-based: 1971-01-01 maps to one rather than zero. That offset is harmless because both dates use the same reference and convention. Subtracting their ordinals cancels the common one.

For two consecutive dates, the later ordinal is exactly one greater. At a year boundary, all completed months of the old year and the first day of the new year still differ by one. At February 29 in a leap year, the extra day exists in the month table and is counted exactly once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"date1": "2019-06-29", "date2": "2019-06-30"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Standard date library:** Parse both dates and subtract date objects. It is concise, but an interview may expect the calendar arithmetic to be implemented directly.
- **Closed-form ordinal:** Count ordinary days plus leap years using divisions by four, one hundred, and four hundred. This avoids the year loop and stays $O(1)$ for unbounded years.
- **Simulate day by day:** Correct but unnecessarily slow for large date ranges and much more prone to month-boundary mistakes.
- **Equal dates:** Their ordinal difference is zero.
- **Reverse input order:** The absolute value makes the result symmetric.
- **Leap day:** February 29 is counted only when the year helper returns true.
- **Century boundary:** A year such as 2100 is not a leap year because it is not divisible by four hundred.
- **January date:** The month loop is empty, and only complete years plus the day are counted.
- **December date:** All eleven earlier month lengths are included before adding the day.
- **One-based ordinal:** Mapping the reference date to one instead of zero does not affect differences.
- **Valid-date guarantee:** The code does not reject malformed strings or impossible dates; the contract guarantees correct formatting and calendar validity.
- **Reference-year inclusion:** The year loop excludes the target year and the month loop supplies only its completed months, preventing the current year’s days from being counted twice.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. For a date in year $Y$, `calcDays` loops through $Y - 1971$ complete years and at most eleven months. Under the stated fixed range from 1971 through 2100, both loop bounds are capped constants, so each conversion and the whole method run in $O(1)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
