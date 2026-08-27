# Guided Example: Apply Discount to Prices

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sentence": "1 2 $3 4 $5 $6 7 8$ $9 $10$", "discount": 100}`
- **Required output:** `"1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **sentence** is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign `'$'`. A word represents a **price** if it is a sequence of digits preceded by a dollar sign.

The objective is to compute `"1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"` from `{"sentence": "1 2 $3 4 $5 $6 7 8$ $9 $10$", "discount": 100}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat the sentence as complete space-delimited tokens

The definition of a price applies to an entire word: the word must begin with `'$'`, and every character after that sign must be a digit. A dollar sign embedded in a larger word does not begin a price token.

The sentence guarantee says that words are separated by one space with no leading or trailing spaces. Consequently, `sentence.split()` produces exactly the original word sequence. The algorithm examines every word independently, appends either its replacement or its original text to `ans`, and finally restores the sentence with `' '.join(ans)`.

Because spacing is canonical, splitting and rejoining does not alter any valid separator.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sentence": "1 2 $3 4 $5 $6 7 8$ $9 $10$", "discount": 100}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recognize a price only when the whole word matches

The condition has two parts:

`w[0] == '$' and w[1:].isdigit()`.

Every word is nonempty, so reading `w[0]` is safe. The first comparison rejects tokens such as `"5$"` or `"there$1"` because their dollar sign is not the first character.

`w[1:].isdigit()` requires at least one character and requires every remaining character to be a digit. It therefore accepts `"$100"` and rejects:

- `"$"`, because the suffix is empty;
- `"$1e5"`, because `e` is not a digit;
- `"$5$6"`, because another dollar sign appears in the suffix;
- `"$$9"`, for the same reason.

The test describes the full token rather than searching for a price-shaped substring inside it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The condition has two parts:

`w[0] == '$' and w[1:].isdigit... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Convert and apply the discount

For a valid price word, `int(w[1:])` converts the digit suffix to its numeric price. The source guarantees positive prices without leading zeros and at most ten digits, so conversion is direct.

A discount of `discount` percent leaves the fraction

$$
1-\frac{\texttt{discount}}{100}
$$

of the original price. The exact source computes

`int(w[1:]) * (1 - discount / 100)`.

Python's `/` produces a floating-point value. The multiplication therefore also produces a float, even when the mathematical result is a whole number.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sentence": "1 2 $3 4 $5 $6 7 8$ $9 $10$", "discount": 100}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Integer cents:** Compute `price * (100-discoun:** - **Integer cents:** Compute `price * (100-discount)` as an integer number of cents, then divide by 100 for formatting. This avoids binary floating-point rounding and more closely matches the manifest summary.
- **Regular expression:** A full-token pattern such as a dollar sign followed by one or more digits can recognize prices, but the two direct string checks are sufficient.
- **Character-by-character reconstruction:** It can avoid a separate split list but requires careful token-boundary and spacing management.
- **A bare dollar sign:** Its suffix is empty, `isdigit()` is false, and it remains unchanged.
- **Dollar sign inside a word:** The first-character test rejects it.
- **Extra symbol after digits:** The suffix-wide digit test rejects the entire token rather than discounting a prefix.
- **Zero-percent discount:** The numeric value is unchanged, but every valid price is still reformatted with two decimal places.
- **Hundred-percent discount:** Every recognized price formats as `"$0.00"`.
- **Whole-number discounted result:** Fixed-point formatting still appends `.00`.
- **Fractional-cent mathematical result:** `.2f` rounds to two displayed decimal places.
- **Maximum ten-digit price:** Python's integer conversion is safe; the subsequent exact source calculation is floating point.
- **Canonical spaces:** Split and join preserve the sentence's separators only because the contract guarantees exactly one space.
- **Nonempty words:** The spacing guarantees make `w[0]` safe.
- **Input preservation:** New token and result strings are built; `sentence` is not mutated.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the number of characters in `sentence`. Splitting scans the sentence and creates word strings totaling `O(N)` characters. Recognition, digit conversion, and formatting across all words process `O(N)` characters in total. Joining also takes `O(N)` time. Overall time is `O(N)`.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
