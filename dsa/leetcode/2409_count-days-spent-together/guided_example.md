# Guided Example: Count Days Spent Together

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arriveAlice": "08-15", "leaveAlice": "08-18", "arriveBob": "08-16", "leaveBob": "08-19"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Alice and Bob are traveling to Rome for separate business meetings.

The objective is to compute `3` from `{"arriveAlice": "08-15", "leaveAlice": "08-18", "arriveBob": "08-16", "leaveBob": "08-19"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Find the intersection endpoints first

Alice's inclusive date interval and Bob's inclusive date interval overlap from the later arrival through the earlier departure.

The exact source computes:



Because every date uses fixed-width zero-padded format `"MM-DD"` within the same year, lexicographic string order is chronological order. The month occupies the first two characters, and when months tie, the day occupies the last two.

This property would fail for formats such as `"M-D"` without leading zeros or for dates spanning different years, but both are excluded.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arriveAlice": "08-15", "leaveAlice": "08-18", "arriveBob": "08-16", "leaveBob": "08-19"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Convert one date to its day-of-year ordinal

The month-length tuple lists the twelve non-leap-year month sizes. For date string `a`:



adds all days in months strictly before `a`'s month, then adds its one-based day within the current month. January 1 becomes ordinal one.

The same conversion produces `y` for overlap end `b`.

For August 16, the prefix sums January through July, then adds sixteen. Comparing or subtracting ordinals now works across month boundaries without separate date cases.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The month-length tuple lists the twelve non-leap-year month ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count an inclusive interval

If overlap start ordinal is `x` and end ordinal is `y`, the number of included days is:

$$
y-x+1.
$$

The plus one counts both endpoints. When both travelers share exactly one date, `x = y` and the formula returns one.

If the intervals do not overlap, the later arrival lies after the earlier departure, so `y - x + 1` is zero or negative. The final:



returns zero instead of a negative day count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arriveAlice": "08-15", "leaveAlice": "08-18", "arriveBob": "08-16", "leaveBob": "08-19"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Convert all four dates first:** Then compute m:** - **Convert all four dates first:** Then compute max ordinal arrivals and min ordinal departures. It is equally correct but performs two extra conversions.
- **Precomputed month-prefix array:** Store cumulative days before each month and convert with one lookup. Useful for many queries but unnecessary for one call.
- **Simulate every calendar day:** It works over one year but is more complex than interval arithmetic.
- **Same one shared day:** Inclusive plus one returns one.
- **Adjacent non-overlapping visits:** Later arrival one day after earlier leave produces zero after clamping.
- **Identical intervals:** The full inclusive interval length is returned.
- **Cross-month overlap:** Ordinals handle it without special branches.
- **February:** It has 28 days because the year is explicitly non-leap.
- **Fixed-width requirement:** Lexicographic date comparison depends on leading zeros.
- **Same-year requirement:** Without a year field, cross-year chronology could not be inferred.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The date strings have fixed length five, and the month tuple has fixed length twelve. String max/min, slicing, integer parsing, and summing at most eleven month values all take constant bounded work.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
