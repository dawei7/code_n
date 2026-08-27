# Guided Example: Next Day

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"date": "2014-06-20"}`
- **Required output:** `"2014-06-21"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write code that enhances all date objects such that you can call the `date.nextDay()` method on any date object and it will return the next day in the format *YYYY-MM-DD* as a string.

The objective is to compute `"2014-06-21"` from `{"date": "2014-06-20"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the date engine for calendar arithmetic

The task sounds like adding one to the day number, but dates do not have a fixed maximum day in every month. February depends on leap-year rules, some months have thirty days, December must roll into a new year, and local clocks can cross daylight-saving transitions. The exact solution delegates those rules to JavaScript's `Date` implementation instead of reproducing a calendar by hand.

It performs three conceptual steps:

1. Clone the receiver with `new Date(this)`.
2. Advance the clone by one UTC calendar day using `getUTCDate` and `setUTCDate`.
3. Convert the result to an ISO string and keep its date portion.

Each choice prevents a different class of bug.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"date": "2014-06-20"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Clone before changing anything

`Date` objects are mutable. Methods such as `setUTCDate` change the object on which they are called. The method is installed on `Date.prototype`, so `this` is the original Date supplied by the caller. Directly calling `this.setUTCDate(...)` would unexpectedly alter that original object.

`const next = new Date(this)` constructs another Date with the same millisecond timestamp. All later mutation is applied to `next`. The caller can invoke `date.nextDay()` and still use `date` afterward with its original value unchanged. This is especially important for a utility method: a return value that looks like a pure calculation should not silently move the source date.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `Date` objects are mutable.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why setting an out-of-range day is useful

`next.getUTCDate()` returns the day of the month in UTC. The solution adds one and passes the result to `next.setUTCDate(...)`. JavaScript normalizes out-of-range calendar fields. If the current UTC date is January 31, setting the day to 32 rolls into February 1. If it is December 31, the normalization advances both the month and year. On February 28, the result becomes February 29 in a leap year and March 1 otherwise.

This means the code does not need a table of month lengths or a separate leap-year condition. The platform date engine already implements the Gregorian normalization needed by the problem.

The method advances a calendar day, not simply a label inside the same month. The normalization behavior is exactly what makes `current day + 1` safe at every boundary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"2014-06-21"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"date": "2014-06-20"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"2014-06-21"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Mutate `this` directly:** This can compute the:** - **Mutate `this` directly:** This can compute the date but introduces an observable side effect. The exact solution clones first so the original Date remains intact.
- **Add `24 * 60 * 60 * 1000` milliseconds:** For a UTC-oriented result this can often work, but field-based UTC calendar arithmetic states the intent directly and avoids reasoning about local daylight-saving day lengths.
- **Use local `getDate` and `setDate`:** Combining local calendar operations with `toISOString` can return an unexpected UTC date near timezone boundaries. The exact code keeps all stages in UTC.
- **Manual month-length table:** It adds branching for thirty-day months, February, leap years, and year rollover. JavaScript Date normalization already owns those rules.
- **Manual string formatting:** It must handle zero-based months and leading zeros. `toISOString().slice(0, 10)` provides the exact required shape.
- **End of a thirty-day or thirty-one-day month:** Passing the next out-of-range day to `setUTCDate` automatically enters the following month.
- **Leap day:** February 28 advances to February 29 only when the Date engine recognizes a leap year; February 29 then advances to March 1.
- **End of year:** December 31 normalizes to January 1 of the next year without a separate condition.
- **Non-midnight receiver:** The method preserves the UTC time-of-day on the clone but returns only the date portion, so the calculation still advances the receiver's UTC calendar date exactly once.
- **Invalid Date receiver:** `toISOString` throws for an invalid Date. The exact code assumes a valid Date under the problem contract and does not add recovery behavior.
- **Subclass or borrowed call:** The method expects `this` to be a valid Date-compatible value. Calling it with an unrelated object is outside the intended prototype contract.
- **Timezone expectations:** The returned date is explicitly the next UTC date. A caller expecting the next date in some named local timezone would need a different contract and timezone-aware logic.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The implementation performs one Date construction, one UTC getter, one UTC setter, one ISO conversion, and one fixed-length slice. Under the JavaScript runtime model, each operation handles a fixed-size timestamp and fixed-format string, so the time complexity is `O(1)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
