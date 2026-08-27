# Guided Example: Find Most Frequent Vowel and Consonant

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "successes"}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters (`'a'` to `'z'`).

The objective is to compute `6` from `{"s": "successes"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate frequency counting from category selection

The task asks for two independent maxima:

- the largest frequency among vowels `a,e,i,o,u`;
- the largest frequency among all other lowercase letters.

It does not ask which letters attain those maxima, and ties may be resolved arbitrarily. Therefore, first count every distinct character, then update one of two running maxima based on its category.

The source uses:

`cnt = Counter(s)`.

After this pass, `cnt[c]` is the exact number of occurrences of letter `c`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "successes"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain one maximum for each category

`a` stores the greatest vowel frequency seen so far, and `b` stores the greatest consonant frequency. Both begin at zero.

For every `(character,frequency)` pair:

- if `character in "aeiou"`, update `a = max(a,frequency)`;
- otherwise, update `b = max(b,frequency)`.

The input contains only lowercase English letters, so every non-vowel is a consonant for this problem. There are no digits, spaces, punctuation marks, or uppercase characters requiring another category.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `a` stores the greatest vowel frequency seen so far, and `b`... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why zero initialization handles missing categories

If the string has no vowels, no loop iteration updates `a`, so it remains zero. That is exactly the rule for a missing category.

The same applies to `b` when every character is a vowel. No separate boolean or postprocessing condition is needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "successes"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Use a 26-element frequency array:** This avoid:** - **Use a 26-element frequency array:** This avoids hashing and also gives `O(n)` time and fixed space.
- **Sort the characters:** Frequencies can be grouped after sorting, but `O(n log n)` work is unnecessary.
- **Track only the globally most frequent letter:** The answer requires one maximum from each category, not merely the overall maximum.
- **Sum all vowel and consonant counts:** The task asks for maximum individual-letter frequencies, not category totals.
- **No vowels:** `a` remains zero and only the consonant maximum contributes.
- **No consonants:** `b` remains zero and only the vowel maximum contributes.
- **One-character string:** Its category maximum is one and the other is zero.
- **Tied vowels:** Any tied letter is acceptable; the stored frequency is the same.
- **Tied consonants:** The same reasoning applies.
- **All letters identical:** That letter's full string length becomes its category maximum.
- **Lowercase guarantee:** The membership string lists every vowel relevant to the input domain.
- **Counter order:** Explicit maximum operations make iteration order irrelevant.
- **Fixed alphabet complexity:** Storing up to 26 counts is conventionally `O(1)` rather than `O(n)`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(s)`. Building the Counter scans `n` characters, taking `O(n)` expected time. The second loop visits at most 26 distinct lowercase letters, which is `O(1)` under the fixed alphabet. Total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
