# Guided Example: Uncommon Words from Two Sentences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s1": "this apple is sweet", "s2": "this apple is sour"}`
- **Required output:** `["sweet", "sour"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **sentence** is a string of single-space separated words where each word consists only of lowercase letters.

The objective is to compute `["sweet", "sour"]` from `{"s1": "this apple is sweet", "s2": "this apple is sour"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

A word is uncommon only when its total behavior across both sentences is “appears exactly once.” If a word appears once in one sentence and never in the other, its combined count is one. Every other situation produces a different combined count:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s1": "this apple is sweet", "s2": "this apple is sour"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- repeated in its own sentence gives at least two;
- present in both sentences gives at least two;
- absent from both sentences means it never becomes a candidate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - repeated in its own sentence gives at least two;
- present... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Therefore the two-sentence definition can be reduced to one frequency table over all words from both sentences.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["sweet", "sour"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s1": "this apple is sweet", "s2": "this apple is sour"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["sweet", "sour"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One Counter over concatenated word lists:** `C:** - **One Counter over concatenated word lists:** `Counter(s1.split() + s2.split())` expresses the same combined-count idea. It creates an additional concatenated list, while Counter addition keeps the two stages explicit.
- **Manual dictionary:** Increment a normal mapping for every word from both splits. This has the same asymptotic behavior and avoids relying on Counter addition syntax.
- **Set symmetric difference:** It ignores repeated occurrences within one sentence and can report words that are not uncommon.
- **Compare every word with every other word:** This is unnecessarily quadratic; frequency counting summarizes all comparisons.
- **Word occurs once in each sentence:** Combined count is two, so it is correctly excluded.
- **Word repeats only in one sentence:** Combined count exceeds one, so it is excluded even though absent from the other sentence.
- **Every word is shared:** No count equals one, and the result is empty.
- **Every word is globally unique:** Every word is returned.
- **One-word sentences:** Equal words produce no answer; different words produce both words.
- **Any output order:** The comprehension follows Counter iteration order in current Python, but correctness must not depend on that order.
- **Lowercase-only contract:** Word comparison is case-sensitive, but uppercase forms never occur in valid input.
- **Single-space guarantee:** `split()` produces no empty words. It would also safely ignore extra whitespace in a broader input.
- **Output multiplicity:** Each uncommon word appears exactly once globally, so it appears once in the returned list.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L$ be the total number of characters in `s1` and `s2`, including spaces. Splitting, hashing words, combining counters, and filtering together process total text proportional to $L$ under expected hash-table behavior.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
