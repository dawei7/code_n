# Guided Example: Replace Question Marks in String to Minimize Its Value

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "???"}`
- **Required output:** `"abc"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s`. $s[i]$ is either a lowercase English letter or `'?'`.

The objective is to compute `"abc"` from `{"s": "???"}` while avoiding redundant calculations and unnecessary overhead.

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

**Rewrite string value in terms of final frequencies.** If a letter appears $f$ times, its occurrences contribute:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "???"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

Therefore the total string value depends only on how many times each letter appears, not on their positions. Adding one new occurrence to a letter currently appearing $f$ times increases value by exactly $f$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

This marginal-cost view determines which letters should replace question marks.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abc"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "???"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abc"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count selected replacements by letter:** Store 26 chosen counts, then emit letters alphabetically into question positions. This avoids `t.sort()` and achieves true $O(N)$ time.
- **Fill heap choices immediately:** It preserves minimum value but can fail the lexicographically smallest tie-break because selected letters may need reordering.
- **No question marks:** `t` is empty and joining `cs` returns the original string.
- **All question marks:** Letters are distributed as evenly as possible, with earlier alphabet letters winning equal marginal costs.
- **Heavily frequent fixed letter:** Its high marginal cost delays choosing it until other letters catch up.
- **Value depends only on counts:** This is why sorting replacement positions afterward is safe.
- **Heap tie order:** Tuple second component prefers smaller letters.
- **Question-position order:** Left-to-right assignment makes the earliest characters as small as possible.
- **Counter question-mark entry:** It is ignored when building lowercase-letter heap entries.
- **Manifest mismatch:** Exact Python sorting makes worst-case time $O(N\log N)$, not strictly linear.
- **Why heap size stays 26:** `heapreplace` updates one existing letter entry rather than adding another, so every lowercase letter has exactly one current marginal-cost record.
- **Final frequencies, not occurrence history:** A letter's total contribution $\binom f2$ is independent of which specific occurrences were fixed versus substituted.
- **Sorting only chosen characters:** Fixed letters cannot move. Lexicographic minimization permutes replacements solely among the original question-mark positions.
- **Stable earliest difference:** If two assignments use the same replacement multiset, placing its sorted sequence left to right makes the first differing question position as small as possible, which decides lexicographic order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+Q\log Q)$. Counting, string scanning, conversion to a character list, and joining cost $O(N)$. $Q$ fixed-size heap replacements cost $O(Q)$ under the 26-letter bound. Sorting `t` costs $O(Q\log Q)$ worst-case. Total exact time is $O(N+Q\log Q)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
