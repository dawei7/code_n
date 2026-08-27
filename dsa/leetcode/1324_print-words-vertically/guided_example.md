# Guided Example: Print Words Vertically

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "HOW ARE YOU"}`
- **Required output:** `["HAY", "ORO", "WEU"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`. Return all the words vertically in the same order in which they appear in `s`.

The objective is to compute `["HAY", "ORO", "WEU"]` from `{"s": "HOW ARE YOU"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separating the words

`words = s.split()` produces the words in their original order. The contract says there is exactly one space between words, but `split()` also safely handles general whitespace and does not include separators in the resulting strings.

Word order must be preserved because each word becomes one output column. Sorting or otherwise rearranging `words` would change the vertical text.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "HOW ARE YOU"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Determining the number of output rows

`n = max(len(w) for w in words)` finds the longest word length.

There must be one output row for each character position that exists in at least one word. If the longest word has length `n`, valid positions are zero through `n - 1`. No later row could contain any letter, so exactly `n` rows are needed.

The input contains at least one uppercase word, so `max` always has a length to examine.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `n = max(len(w) for w in words)` finds the longest word leng... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Building one vertical row

For fixed character position `j`, the comprehension creates one entry per word:

`w[j] if j < len(w) else " "`.

If the word reaches position `j`, its actual letter is used. Otherwise, a space preserves the column so later words remain aligned.

For example, with words `["TO", "BE", "OR", "NOT", "TO", "BE"]` and `j = 2`, only `"NOT"` has a third character. The temporary row is:

`[" ", " ", " ", "T", " ", " "]`.

The three spaces before `T` are meaningful because they identify the empty third-character positions of the earlier words.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["HAY", "ORO", "WEU"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "HOW ARE YOU"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["HAY", "ORO", "WEU"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Use `zip_longest`:** Transpose the words with :** - **Use `zip_longest`:** Transpose the words with a space fill value, join each tuple, and apply `rstrip`. It is concise but hides some alignment mechanics.
- **Preallocate a character grid:** It works but stores the full padded rectangle even though rows can be produced one at a time.
- **Use `strip`:** This is incorrect because leading spaces can be meaningful output.
- **Use `rstrip`:** It correctly removes trailing padding and is a simpler equivalent to the pop loop for strings.
- **All words equal length:** No padding is created, and every output row has exactly $W$ letters.
- **One word:** Each character becomes a one-character output string.
- **A longest word in an early column:** Later missing columns create trailing spaces, which are removed.
- **A longest word in a late column:** Earlier short words create leading or internal spaces, which must remain.
- **Safety of `t[-1]`:** Every row below the maximum length contains at least one real character, so trimming never empties the list.
- **Input word order:** It defines output column order and must not change.
- **Uppercase-only guarantee:** A literal space can unambiguously represent padding because spaces do not occur inside words.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(WL)$. Let $W$ be the number of words, $L$ the maximum word length, and $C$ the number of characters in the input string.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
