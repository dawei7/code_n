# Guided Example: Count Items Matching a Rule

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"items": [["a", "b", "c"]], "ruleKey": "name", "ruleValue": "c"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `items`, where each $\text{items}[i] = [\text{type}_{i}, \text{color}_{i}, \text{name}_{i}]$ describes the type, color, and name of the $i^{\text{th}}$ item. You are also given a rule represented by two strings, `ruleKey` and `ruleValue`.

The objective is to compute `1` from `{"items": [["a", "b", "c"]], "ruleKey": "name", "ruleValue": "c"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Map the rule key to one fixed column

Every item has exactly three fields in a fixed order:

- index zero is type,
- index one is color,
- index two is name.

Once `ruleKey` is known, the same field index applies to every item. The exact solution computes that index once, then counts items whose field equals `ruleValue`.

This avoids repeating three full key comparisons for every row.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"items": [["a", "b", "c"]], "ruleKey": "name", "ruleValue": "c"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use the key's first character

The source chooses:

`i = 0 if ruleKey[0] == 't' else (1 if ruleKey[0] == 'c' else 2)`.

The only allowed keys are `"type"`, `"color"`, and `"name"`. Their first characters `t`, `c`, and `n` are distinct, so inspecting character zero uniquely identifies the correct field.

If the first character is `t`, index zero is selected. Otherwise, `c` selects index one. The final else must be `"name"` under the input contract and selects index two.

This compact mapping deliberately relies on the guaranteed key set. With arbitrary keys or two allowed names sharing an initial, a complete dictionary mapping would be safer.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count matching rows with Boolean arithmetic

The return expression is:

`sum(v[i] == ruleValue for v in items)`.

For each item list `v`, `v[i]` retrieves the relevant type, color, or name field. The equality comparison is true exactly when that item matches the rule.

Python treats `true` as one and `false` as zero when summing. The generator therefore contributes one per matching item and zero per nonmatching item.

Because it is a generator expression, it does not allocate a separate list of Booleans.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"items": [["a", "b", "c"]], "ruleKey": "name", "ruleValue": "c"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dictionary mapping:** `{"type": 0, "color": 1, "name": 2}` is more explicit and remains constant time.
- **Full conditional per item:** Test `ruleKey` inside the loop for every row. It is correct but repeats invariant work.
- **Search all fields:** It is incorrect because a value in the wrong column does not satisfy the rule.
- **Filter then length:** Building a list of matching items gives the same count but uses $O(n)$ extra space.
- **Rule type:** Only index zero is examined.
- **Rule color:** Only index one is examined.
- **Rule name:** The final else selects index two.
- **No matches:** Every Boolean is false and `sum` returns zero.
- **All match:** Every item contributes one, returning `len(items)`.
- **Same value in several fields:** Only the rule-selected occurrence matters.
- **Repeated identical items:** Each array position is an item and contributes independently.
- **Guaranteed item length three:** Indexing at zero, one, or two is always safe.
- **Guaranteed rule keys:** The first-character shortcut is unambiguous only because the allowed set is fixed.
- **Generator laziness:** Match indicators are consumed one at a time.
- **Input preservation:** Neither the outer list nor any item row is modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of items. Mapping `ruleKey` to `i` takes constant time. The generator visits each item once, performs one indexed lookup and one bounded-length string comparison, and adds one Boolean. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
