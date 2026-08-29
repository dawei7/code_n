# Guided Example: Count Occurrences in Text

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Files": [{"file_name": "draft1.txt", "content": "The stock exchange predicts a bull market which would make many investors happy."}, {"file_name": "draft2.txt", "content": "The stock exchange predicts a bull market, and analysts say we are awaiting a bear market."}, {"file_name": "draft3.txt", "content": "The stock exchange predicts a bull market, while analysts expect a bear market. As always, uncertainty remains."}]}}`
- **Required output:** `{"columns": ["word", "count"], "rows": [["bull", 3], ["bear", 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Files`

The objective is to compute `{"columns": ["word", "count"], "rows": [["bull", 3], ["bear", 2]]}` from `{"tables": {"Files": [{"file_name": "draft1.txt", "content": "The stock exchange predicts a bull market which would make many investors happy."}, {"file_name": "draft2.txt", "content": "The stock exchange predicts a bull market, and analysts say we are awaiting a bear market."}, {"file_name": "draft3.txt", "content": "The stock exchange predicts a bull market, while analysts expect a bear market. As always, uncertainty remains."}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count files, not repeated appearances inside one file

The requested count for each target is the number of `Files` rows whose `content` contains at least one valid occurrence. A file containing `" bull bull "` must contribute one, not two.

The query handles this naturally with a `WHERE` predicate. Each matching table row reaches `COUNT(*)` once, regardless of how many places within its content satisfy the pattern.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Files": [{"file_name": "draft1.txt", "content": "The stock exchange predicts a bull market which would make many investors happy."}, {"file_name": "draft2.txt", "content": "The stock exchange predicts a bull market, and analysts say we are awaiting a bear market."}, {"file_name": "draft3.txt", "content": "The stock exchange predicts a bull market, while analysts expect a bear market. As always, uncertainty remains."}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Match the exact space-delimited rule

For `bull`, the predicate is:

`content LIKE '% bull %'`.

The leading and trailing percent signs permit arbitrary text before and after the match. The literal pattern inside them contains one ordinary space, then `bull`, then another ordinary space. Thus the target must have a space on both sides somewhere in the content.

The `bear` branch uses the analogous `'% bear %'` pattern.

This deliberately does not implement a general linguistic word boundary. A word at the very beginning or end lacks one required surrounding space. `"bull."` lacks a space immediately after the letters. `"bullet"` has extra letters rather than the required trailing space. All fail as specified.

Tabs and newlines are also not the same as the literal space characters in the pattern. The exact solution follows the source's space-delimited interpretation rather than a regular expression for all whitespace.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: LIKE returns one Boolean decision per row

For each `Files` row, MySQL searches the content for some substring matching the pattern. If one exists, the row passes `WHERE`. `COUNT(*)` then counts the qualifying row.

No grouping by file name is needed because each input row represents one file. The aggregate select returns one row even when no file qualifies, with count zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["word", "count"], "rows": [["bull", 3], ["bear", 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Files": [{"file_name": "draft1.txt", "content": "The stock exchange predicts a bull market which would make many investors happy."}, {"file_name": "draft2.txt", "content": "The stock exchange predicts a bull market, and analysts say we are awaiting a bear market."}, {"file_name": "draft3.txt", "content": "The stock exchange predicts a bull market, while analysts expect a bear market. As always, uncertainty remains."}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["word", "count"], "rows": [["bull", 3], ["bear", 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`UNION ALL`:** Produces the same two labeled rows and avoids duplicate elimination because labels are inherently distinct.
- **Regular expression with spaces:** Can encode the same contract but is more machinery than fixed `LIKE` patterns require.
- **Regex word boundaries:** Incorrect here because they would count punctuation-delimited or boundary-position words excluded by the statement.
- **Count string occurrences:** Incorrect because the task counts matching files, not how many times a word appears within each file.
- **Word at content start:** Does not match because no leading space exists.
- **Word at content end:** Does not match because no trailing space exists.
- **Punctuation after target:** Does not match the literal trailing space.
- **Plural or longer word:** `bears` and `bullet` do not match.
- **No matching files:** Each aggregate still returns its label with count zero.
- **Case behavior:** Depends on the column collation because the query does not normalize case explicitly.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let $S$ be the total number of characters across all `content` values. Each branch may scan the table's text for its fixed pattern, so the total character-search work is $O(S)$ with a constant factor of two. The fixed pattern lengths do not grow with the input.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
