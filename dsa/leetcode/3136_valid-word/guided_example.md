# Guided Example: Valid Word

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "234Adas"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A word is considered **valid** if:

The objective is to compute `true` from `{"word": "234Adas"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat the definition as four independent requirements

A word is valid only if all of these are true:

1. its length is at least three;
2. every character is an English letter or a digit;
3. at least one character is a vowel;
4. at least one character is a consonant.

The method checks the length first because a short word can never become valid through anything discovered later in the scan. This early return is conclusive and avoids unnecessary work.

For a word of sufficient length, the code tracks two facts with `has_vowel` and `has_consonant`. Both begin as `false`. They only ever change to `true`, so they summarize whether the corresponding category has appeared anywhere in the processed prefix.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "234Adas"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Classify one character at a time

The fixed set `vs = set("aeiouAEIOU")` contains all ten allowed uppercase and lowercase vowel forms. A set gives a direct membership test without repeatedly converting case.

For each character `c`, the code first checks `c.isalnum()`. Under the stated input alphabet, this is true exactly for English letters and digits and false for the possible special characters `'@'`, `'#'`, and `'$'`. Encountering a false result immediately proves the whole word invalid, so the method returns `false`.

If `c.isalpha()` is true, the character is a letter. Membership in `vs` distinguishes the two required letter categories:

- a member sets `has_vowel = true`;
- any other English letter sets `has_consonant = true`.

If `c.isalpha()` is false after passing `isalnum()`, it is a digit. Digits are allowed, but they are neither vowels nor consonants, so neither flag changes.

After every character has passed the allowed-character check, the method returns `has_vowel and has_consonant`. Both categories must have appeared. Having only one of them is not enough even if the word is long and contains valid digits.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The fixed set `vs = set("aeiouAEIOU")` contains all ten allo... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Loop invariant

After processing a prefix of the word:

- every character in that prefix is alphanumeric, or the method has already returned false;
- `has_vowel` is true exactly when the prefix contains at least one vowel;
- `has_consonant` is true exactly when the prefix contains at least one consonant.

The invariant is initially true for the empty prefix. Processing an invalid symbol exits correctly. Processing a vowel or consonant sets the matching flag, and processing a digit leaves both category facts unchanged. Therefore, it remains true through the complete scan.

At the end, the initial length check proves condition 1, the absence of an early return proves condition 2, and the two flags exactly represent conditions 3 and 4. The final conjunction is therefore equivalent to the full definition of a valid word.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "234Adas"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Regular expression:** A lookahead-based expres:** - **Regular expression:** A lookahead-based expression can enforce length, alphabet, vowel, and consonant conditions, but it is harder to read and still scans the word.
- **Lowercase each character:** Test `c.lower() in "aeiou"` for letters. This avoids listing uppercase vowels but creates or computes a case-normalized character each iteration.
- **Four separate passes:** Check allowed characters, vowels, and consonants independently. It remains $O(n)$ but repeats work and delays failure.
- **Explicit ASCII ranges:** Tests such as `'A' <= c <= 'Z'` precisely enforce the English-only contract and avoid Unicode classifier semantics.
- **Length exactly three:** It can be valid; “minimum of three” includes the boundary.
- **Digits only:** Digits satisfy the alphabet requirement but supply neither required letter category, so the result is false.
- **Vowels plus digits only:** `has_consonant` remains false.
- **Consonants plus digits only:** `has_vowel` remains false.
- **Uppercase letters:** The vowel set includes uppercase forms, and other uppercase English letters count as consonants.
- **Special character anywhere:** The method returns false immediately, even if all other requirements have already been satisfied.
- **Repeated vowels or consonants:** The flags record existence, not counts, so repetitions require no extra handling.
- **Unicode outside the contract:** Python might classify it as alphanumeric. The solution is correct because such input is excluded by the stated constraints.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `word`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
