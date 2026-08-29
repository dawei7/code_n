# Guided Example: Reformat Date

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"date": "20th Oct 2052"}`
- **Required output:** `"2052-10-20"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a `date` string in the form `Day Month Year`, where:

The objective is to compute `"2052-10-20"` from `{"date": "20th Oct 2052"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separating the three input fields

The valid input always contains a day token, a three-letter month token, and a four-digit year token separated by spaces. `date.split()` produces a list in the order

`[day, month, year]`.

The target format begins with the year, so `s.reverse()` changes that list in place to

`[year, month, day]`.

The remaining work is to convert the month name to two digits, remove the day suffix, and pad single-digit values.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"date": "20th Oct 2052"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the month lookup string works

The source stores all month abbreviations in one string:

`" JanFebMarAprMayJunJulAugSepOctNovDec"`.

The leading space is intentional. Every month occupies exactly three characters after that one-character offset. January begins at index one, February at index four, March at index seven, and so on.

`months.index(s[1])` finds the starting index of the valid month abbreviation. Integer division by three, followed by adding one, converts those positions to month numbers:

- January starts at one, and `1 // 3 + 1` is one.
- February starts at four, and `4 // 3 + 1` is two.
- December starts at thirty-four, and `34 // 3 + 1` is twelve.

The numeric month is converted back to text and `zfill(2)` adds a leading zero when necessary. Months ten through twelve already have two characters and remain unchanged.

Using one concatenated string is compact. A dictionary mapping abbreviations to numbers would make the relationship more explicit but is not required for the valid fixed vocabulary.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Cleaning and padding the day

After reversal, `s[2]` is the original day token, such as `20th` or `6th`. Every permitted ordinal suffix has exactly two letters: `st`, `nd`, `rd`, or `th`.

The slice `s[2][:-2]` removes those final two characters without needing to decide which suffix it was. This leaves the decimal day digits. `zfill(2)` changes one-digit days such as `6` to `06` and leaves two-digit days such as `20` unchanged.

The validity guarantee means the code does not need to verify that suffixes agree grammatically with the day or that a date exists in the calendar.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"2052-10-20"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"date": "20th Oct 2052"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"2052-10-20"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Month dictionary:** Map each abbreviation directly to its two-digit string. This is more explicit and avoids relying on string offsets, with the same bounded complexity.
- **Date parsing library:** It can parse and format dates robustly but is unnecessary for the constrained English grammar and may introduce locale behavior.
- **Regular expression:** Capture day digits, month, and year. It is flexible but more machinery than a three-token split needs.
- **Single-digit day:** Removing the suffix leaves one character, and `zfill(2)` supplies the leading zero.
- **Double-digit day:** Padding leaves its two digits unchanged.
- **Months January through September:** Their numeric strings receive a leading zero.
- **Months October through December:** They already have two digits.
- **Ordinal suffix variants:** Removing exactly the last two characters handles `st`, `nd`, `rd`, and `th` uniformly.
- **Leading-zero year concerns:** The contract always provides a valid four-digit year, and the source preserves it as text.
- **Invalid date:** Validation is intentionally absent because inputs are guaranteed valid.
- **Extra whitespace:** `split()` collapses it even though the formal representation uses single spaces.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Under the fixed contract, the date has bounded length: four year digits, at most two day digits plus suffix, one three-letter month, and separators. Every split, reverse, search, slice, padding, and join therefore operates on a constant-size amount of text. Time and auxiliary space are $O(1)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
