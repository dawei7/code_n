# Guided Example: Valid Word Square

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["abcd", "bnrt", "crmy", "dtye"]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `words`, return `true` *if it forms a valid **word square***.

The objective is to compute `true` from `{"words": ["abcd", "bnrt", "crmy", "dtye"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View the words as a possibly ragged character matrix

Place `words[i]` in row `i`. Character `words[i][j]`, when it exists, occupies coordinate `(i,j)`. A valid word square requires reflection across the main diagonal: every existing coordinate `(i,j)` must have a mirrored coordinate `(j,i)` containing the same character.

Rows may have different lengths, so this is not necessarily a rectangular matrix. Correctness requires checking both character equality and whether the mirrored coordinate exists at all. Simply comparing characters without bounds checks can raise an indexing error or overlook a row/column length mismatch.

The solution examines every character that actually exists. The outer loop gives row index `i` and row string `w`; the inner loop gives column index `j` and character `c = words[i][j]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["abcd", "bnrt", "crmy", "dtye"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Validate the mirrored coordinate in a safe order

For coordinate `(i,j)`, three conditions can make the square invalid:

`j >= m`

means there is no row `j`, so column position `j` in row `i` has no possible mirrored row. For instance, if there are three words but the first word has a fourth character, that character would belong to a fourth column with no fourth row to match it.

`i >= len(words[j])`

means row `j` exists but is too short to contain mirrored column `i`. The reflected coordinate `(j,i)` is missing.

`c != words[j][i]`

means both cells exist but their characters differ.

These checks appear in one `or` expression. Python evaluates `or` from left to right and stops once a condition is true. Therefore `words[j]` is accessed only after `j < m` is known, and `words[j][i]` is accessed only after `i < len(words[j])` is known. The order prevents out-of-range access while expressing the logical requirements directly.

If any check fails, the method returns `false` immediately. If all existing cells pass, it returns `true`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For coordinate `(i,j)`, three conditions can make the square... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why scanning existing row characters is enough

At first glance, the loop seems to check only cells that exist in rows, so one might worry about a character existing at `(j,i)` while `(i,j)` is missing. But every existing character is eventually visited from its own row.

Suppose `(j,i)` exists and `(i,j)` does not. When the loop reaches row `j`, column `i`, it checks the mirror `(i,j)`. Either row `i` does not exist, caught by the first condition, or row `i` is too short, caught by the second. Thus every one-sided coordinate is detected from the side where the character does exist.

This symmetry argument means there is no need to compute a maximum width, pad rows, or separately build column strings.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["abcd", "bnrt", "crmy", "dtye"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Construct every column string:** Generate colu:** - **Construct every column string:** Generate column words and compare them with the row list. This is correct but uses $O(C)$ additional space and repeats data already available through mirrored indexing.
- **Pad rows into a rectangle:** Padding introduces sentinel characters and requires careful comparison semantics; direct existence checks are simpler and avoid extra memory.
- **Check only overlapping coordinates:** Comparing characters only when both sides exist is insufficient because an extra unmirrored character must invalidate the square. The two bounds checks are essential.
- **Require all rows to have equal length:** This is too strict. Valid word squares can be ragged, as the second example demonstrates.
- **One word of length one:** Its only character mirrors itself, so the result is true.
- **One word longer than one:** At `j = 1`, no second row exists, so the result is false.
- **A row longer than the number of rows:** The first condition detects its first unrepresentable column.
- **A mirrored row that is too short:** The second condition detects the missing reflected character before indexing it.
- **Diagonal characters:** Coordinates `(i,i)` mirror themselves and necessarily compare equal when they exist.
- **Early mismatch:** The method may finish before scanning all $C$ characters, but $O(C)$ remains the worst-case bound.
- **Lowercase-only guarantee:** Character equality needs no normalization or case folding.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$. Let
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
