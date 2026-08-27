# Guided Example: Strong Password Checker

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"password": "a"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A password is considered strong if the below conditions are all met:

The objective is to compute `5` from `{"password": "a"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Three independent requirements can often share one edit

A strong password must satisfy a length interval, contain all three required character types, and avoid runs of three equal characters. The challenge is not merely to count violations and add them: one insertion or replacement can repair several violations simultaneously. For example, replacing one character inside `"aaa"` with an uppercase letter can both break the repetition and add a missing uppercase type.

The solution first counts how many required types already appear. `countTypes` scans every character and sets one flag for lowercase letters, one for uppercase letters, and one for digits. The returned `types` is between zero and three, so `3 - types` is the number of missing categories. The `elif` chain is appropriate because one character belongs to at most one of these three categories; punctuation such as `'.'` and `'!'` sets none of them.

The optimal strategy then separates passwords into three length regimes. Insertions are forced when the string is shorter than six, replacements are sufficient when the length is already from six through twenty, and deletions are forced when it exceeds twenty. The relationship between edits and repeated runs differs in each regime.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"password": "a"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Case 1: fewer than six characters

If `n < 6`, at least `6 - n` insertions are unavoidable because replacement and deletion cannot increase length. At least `3 - types` edits are also unavoidable because one edit can introduce at most one missing character category. This gives the lower bound

`max(6 - n, 3 - types)`.

The same number is sufficient. Mandatory insertions can be chosen from missing categories and placed inside repeated runs to break them. If more categories are missing than insertions are required, the remaining edits can be replacements that both add a category and break a repetition when needed. Because the original length is at most five, these strategically placed edits are enough to prevent any triple while reaching length six.

For `"a"`, the length deficit is five and two types are missing, so five insertions dominate. For `"aA1"`, the three types already exist but three characters must be inserted, so the answer is three. For `"aaaaa"`, one insertion is needed for length and two types are missing; two edits suffice, for example one insertion and one replacement placed to split the run.

This is why the short case does not separately scan repeated runs. Their repairs can be absorbed into the edits already counted by the larger of the two fundamental deficits.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `n < 6`, at least `6 - n` insertions are unavoidable beca... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count replacements required by a repeated run

For passwords of valid or excessive length, the code scans maximal runs of identical characters. The sentinel `prev = '~'` is safe because the input alphabet does not contain `~`; the first real character therefore starts a new run with `cnt = 1`.

A run of length $L$ needs `L // 3` replacements if no deletions are applied. One replacement can be placed in every third position, splitting the run so that no segment retains three equal consecutive characters. Fewer replacements cannot work because the disjoint groups of positions `0..2`, `3..5`, and so on each need at least one changed character.

When a new character begins, `cnt // 3` for the completed run is added to `replace`, and `cnt` resets to one for the new run. The final run is added after the loop because no later character arrives to flush it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"password": "a"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Breadth-first search over edited strings:** It:** - **Breadth-first search over edited strings:** It could find a minimum in principle, but the branching factor over insertions, deletions, positions, and characters makes the state space enormous.
- **Add all violation counts:** Summing length deficit, missing types, and repetition replacements overcounts because one replacement or insertion can repair a repetition and a missing category together.
- **Replace every third repeated character before deleting:** For strings longer than twenty, this wastes mandatory deletions. Deleting from carefully chosen runs can eliminate some replacements for free beyond the deletion cost.
- **Delete from longest runs only:** Length alone does not determine immediate efficiency. A length-six run needs one deletion to save a replacement, while a length-five run needs three; modulo three controls the priority.
- **Already strong password:** Length is valid, `replace` and missing types are both zero, so the method returns zero.
- **Only punctuation:** `types` remains zero. Punctuation still contributes to length and repeated runs, but it satisfies no category.
- **Repeated punctuation:** The equality scan treats `'.'` or `'!'` exactly like repeated letters, correctly enforcing the no-three-identical rule.
- **Run ending at the last character:** The explicit post-loop flush is necessary; otherwise its replacements and deletion opportunities would be omitted.
- **Exactly length six or twenty:** These belong to the middle regime; no length edit is required.
- **Exactly length twenty-one:** One deletion is mandatory and is preferentially assigned to a remainder-zero run if one exists.
- **Several missing types inside repeated runs:** Replacement characters can be chosen from different missing categories, allowing repair costs to overlap.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the password length. `countTypes` scans the string once. The applicable run-counting branch scans it once more, performing constant work per character. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
