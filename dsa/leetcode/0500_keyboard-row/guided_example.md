# Guided Example: Keyboard Row

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["Hello", "Alaska", "Dad", "Peace"]}`
- **Required output:** `["Alaska", "Dad"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `words`, return *the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below*.

The objective is to compute `["Alaska", "Dad"]` from `{"words": ["Hello", "Alaska", "Dad", "Peace"]}` while avoiding redundant calculations and unnecessary overhead.

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

A word is valid when every distinct letter it uses belongs to one keyboard row. Repeated letters do not change that condition: if `"a"` is on the middle row, using it five times still uses only the middle row. This makes set containment a natural representation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["Hello", "Alaska", "Dad", "Peace"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution creates three constant keyboard-row sets:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution creates three constant keyboard-row sets:... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `s1 = set('qwertyuiop')`;
- `s2 = set('asdfghjkl')`;
- `s3 = set('zxcvbnm')`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["Alaska", "Dad"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["Hello", "Alaska", "Dad", "Peace"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["Alaska", "Dad"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Character-by-character row lookup:** Map each :** - **Character-by-character row lookup:** Map each letter to a row number, use the first letter's row as the target, and reject any mismatch. This avoids constructing a per-word set and has the same linear time.
- **Regular expressions:** Three case-insensitive patterns can test the rows, but set containment states the condition more directly and avoids regex overhead.
- **Convert row strings repeatedly:** Testing every letter with `in` on short fixed strings is still effectively linear, but prebuilt sets make membership intent explicit.
- **Mixed capitalization:** Lowercasing is used only for validation, so output spelling and capitalization remain unchanged.
- **Repeated letters:** Set construction removes duplicates because multiplicity cannot introduce a new keyboard row.
- **One-letter word:** Its singleton set belongs to exactly one row, so it is always accepted.
- **Input order:** Words are considered once from left to right and appended immediately, so accepted words retain their original order.
- **English-letter guarantee:** The row sets cover all lowercase English letters. Unexpected symbols would make every subset check fail.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(c)$. Let $c$ be the total number of characters across all input words. Lowercasing and building the set for one word takes time proportional to its length. Subset checks inspect at most the distinct letters of that word, at most twenty-six under the English alphabet. Across all words, total time is $O(c)$.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
