# Guided Example: Text Justification

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["word"], "maxWidth": 8}`
- **Required output:** `["word    "]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

The objective is to compute `["word    "]` from `{"words": ["word"], "maxWidth": 8}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat the problem as line selection followed by line formatting

The solution becomes much easier to reason about when it does not try to choose words and assign spaces at the same time. The outer loop first selects the largest legal consecutive group of words for one line. Only after that group is fixed does it decide how the spaces must look. This separation matters because the rule for choosing words is always greedy, whereas the rule for inserting spaces changes for the last line and for a line containing one word.

The index `i` is the first input word that has not yet been placed. The list `t` stores the words chosen for the current output line. Since every input word is nonempty and no word is wider than `maxWidth`, the solution can always place at least `words[i]`; therefore the outer loop always makes progress.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["word"], "maxWidth": 8}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Measure the minimum width while greedily packing words

The variable `cnt` is the width the selected words would occupy with exactly one mandatory space between neighboring words. It begins as the length of the first chosen word. For every later candidate, the test

`cnt + 1 + len(words[i]) <= maxWidth`

asks whether the existing minimum-width line, one separator, and the candidate word still fit. If they do, the candidate is appended and `cnt` grows by precisely that separator and word length. If they do not, no later word may skip ahead because word order must be preserved. The current group is therefore the maximum legal consecutive group, exactly as greedy packing requires.

For example, with width 16 and the words `"This"`, `"is"`, `"an"`, and `"example"`, the first three have minimum width $4+1+2+1+2=10$. Adding `"example"` would require $10+1+7=18$, so it belongs to the next line. Notice that this decision uses only one space per gap. Additional justification spaces cannot help another word fit; they consume leftover width only after the word group has been chosen.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle the two left-justified cases first

If `i == n`, the current group contains the final input word and is consequently the last output line. If `len(t) == 1`, there is no gap across which spaces could be distributed. In either case, the required result is the same: join the words with one space, then append enough spaces on the right to reach `maxWidth`.

The construction `left = ' '.join(t)` gives the meaningful left-aligned content. The padding length `maxWidth - len(left)` cannot be negative because the greedy fit test already proved that the group fits with single separators. Appending that many spaces produces exactly the required width. Checking the single-word case also prevents division by zero later, because a one-word line has zero inter-word gaps.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["word    "]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["word"], "maxWidth": 8}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["word    "]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Helper-based design:** A `get_words` helper and a separate `create_line` helper can make the two phases even more explicit. It has the same greedy reasoning and asymptotic cost, at the price of additional calls and parameters.
- **Cycle through gaps:** Repeatedly add one space to gap $0,1,\ldots,k-2$ until the line is full. This is intuitive but can perform more operations than quotient-and-remainder distribution and is easier to make quadratic with immutable strings.
- **Precompute prefix character sums:** Prefix sums can answer the letter total for any candidate range, but the one-pass scan already maintains exactly the needed total and is simpler.
- **One word on a nonfinal line:** It must be followed entirely by right padding; attempting to divide spaces among zero gaps would fail.
- **The final line:** It always uses one space between adjacent words and all remaining spaces on the right, even when full justification would distribute them differently.
- **A word exactly `maxWidth` characters long:** It forms a one-word line with zero right padding.
- **Uneven division:** The first `m` gaps receive one more space than the remaining gaps, so larger gaps are always leftmost.
- **Even division:** When `m` is zero, every gap receives exactly `w` spaces.
- **Minimum width:** With `maxWidth == 1`, every legal word has length one; each word is emitted as a complete line without padding.
- **No trailing spaces on ordinary multiword lines:** Their complete space budget is placed inside gaps. Only left-justified lines may place padding after their content.
- **Input order and content:** Words are only read and appended; the source list and the word strings are not modified.
- **Width accounting:** The greedy check counts one required separator before a candidate, whereas justification later replaces those minimum separators with the complete calculated gap widths.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$. Let $C$ be the total number of characters in all returned lines, including padding spaces. This is the quantity used by the manifest. Every word is examined and selected once. Formatting writes each output word character and each output space a constant number of times, so the total running time is $O(C)$. The temporary slice `t[:-1]`, piece list `row`, joins, and output strings do not change that linear total.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
