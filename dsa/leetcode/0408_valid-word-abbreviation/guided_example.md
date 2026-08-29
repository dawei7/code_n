# Guided Example: Valid Word Abbreviation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "internationalization", "abbr": "i12iz4n"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A string can be **abbreviated** by replacing any number of **non-adjacent**, **non-empty** substrings with their lengths. The lengths **should not** have leading zeros.

The objective is to compute `true` from `{"word": "internationalization", "abbr": "i12iz4n"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Interpret the abbreviation as instructions

Each abbreviation token is either:

- a literal lowercase letter that must equal the next unconsumed word character;
- a positive decimal number telling how many word characters to skip.

The exact solution scans `abbr` once while tracking where those instructions would place it in `word`.

Its variables are:

- `i`: the number of word characters already consumed;
- `j`: the current abbreviation index;
- `x`: the numeric skip value currently being accumulated from consecutive digits.

The number is applied when the next literal arrives or when the abbreviation ends.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "internationalization", "abbr": "i12iz4n"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build multi-digit lengths correctly

For a digit, the update



appends that decimal digit. Reading `1`, then `2` changes `x` from zero to one to twelve. This ensures `12` means skip twelve characters, not skip one and then skip two.

Consecutive digit characters form one number token. This also reflects the non-adjacent replacement rule: two replaced substrings written next to one another would be indistinguishable from one replacement whose length is their sum, so a valid abbreviation treats a maximal digit run as one skip.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reject a leading zero immediately

The condition



detects a zero at the start of a numeric token. At that moment `x == 0` means no nonzero digit has begun the current number.

This rejects both an abbreviation length of zero, such as `"0"`, and a leading-zero form such as `"01"` or `"010"`. Replacing a nonempty substring requires a positive length, and written lengths may not have leading zeros.

A zero after a nonzero prefix is legal. In `"10"`, `x` is already one when the zero arrives, so it becomes ten rather than being rejected.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "internationalization", "abbr": "i12iz4n"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Expand the abbreviation:** Replacing numeric tokens with placeholder characters and comparing could use $O(w)$ extra space and unnecessary construction. Pointer arithmetic performs the same validation directly.
- **Regular expression:** A generated pattern could represent skips, but parsing numeric lengths and leading-zero rules explicitly is clearer and avoids regex complexity.
- **Recursive parser:** Recursion over tokens is possible but adds call-stack state without any branching benefit.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a)$. Let $w$ be the word length and $a$ the abbreviation length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
