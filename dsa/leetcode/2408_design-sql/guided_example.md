# Guided Example: Design SQL

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["SQL", "ins", "sel", "ins", "exp", "rmv", "sel", "exp"], "arguments": [[["one", "two", "three"], [2, 3, 1]], ["two", ["first", "second", "third"]], ["two", 1, 3], ["two", ["fourth", "fifth", "sixth"]], ["two"], ["two", 1], ["two", 2, 2], ["two"]]}`
- **Required output:** `[null, true, "third", true, ["1,first,second,third", "2,fourth,fifth,sixth"], null, "fifth", ["2,fourth,fifth,sixth"]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two string arrays, `names` and `columns`, both of size `n`. The $i^{\text{th}}$ table is represented by the name $\text{names}[i]$ and contains $\text{columns}[i]$ number of columns.

The objective is to compute `[null, true, "third", true, ["1,first,second,third", "2,fourth,fifth,sixth"], null, "fifth", ["2,fourth,fifth,sixth"]]` from `{"operations": ["SQL", "ins", "sel", "ins", "exp", "rmv", "sel", "exp"], "arguments": [[["one", "two", "three"], [2, 3, 1]], ["two", ["first", "second", "third"]], ["two", 1, 3], ["two", ["fourth", "fifth", "sixth"]], ["two"], ["two", 1], ["two", 2, 2], ["two"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What the exact source actually stores

The implementation creates:



Each dictionary key is a table name, and its value is a Python list of rows. A row is stored exactly as the provided list of strings. The constructor receives `names` and `columns` but does not use either one, so it does not pre-create declared tables or remember their expected column counts.

A `defaultdict(list)` creates an empty list whenever an unknown name is accessed. This makes insertion convenient, but it also means unknown names are silently accepted rather than rejected under the expanded local contract.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["SQL", "ins", "sel", "ins", "exp", "rmv", "sel", "exp"], "arguments": [[["one", "two", "three"], [2, 3, 1]], ["two", ["first", "second", "third"]], ["two", 1, 3], ["two", ["fourth", "fifth", "sixth"]], ["two"], ["two", 1], ["two", 2, 2], ["two"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Insertion in the exact implementation

`insertRow(name, row)` appends the row to the list:



List position implicitly serves as row ID: the first appended row is at index zero and is selected with row ID one; the second is at index one and has row ID two.

Append preserves insertion order and takes amortized constant time. The method returns Python `null` because it has no explicit return statement.

It performs no validation of table name or row length. It also stores the caller's row list by reference rather than copying it, so external mutation of that same list could change the stored values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Selection by converting one-based IDs

`selectCell(name, rowId, columnId)` returns:



Both public identifiers are one-based, while Python list indices are zero-based. Subtracting one performs the conversion.

For a valid existing row and valid column, this is direct constant-time indexing. For an unknown table, defaultdict first creates an empty table and indexing raises `IndexError`. Missing rows or columns can also raise `IndexError`. The source does not return `"<null>"` for invalid access.

Python negative indexing introduces another discrepancy: `rowId = 0` or `columnId = 0` would address the last list element rather than be rejected, though valid platform calls may avoid such inputs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, true, "third", true, ["1,first,second,third", "2,fourth,fifth,sixth"], null, "fifth", ["2,fourth,fifth,sixth"]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["SQL", "ins", "sel", "ins", "exp", "rmv", "sel", "exp"], "arguments": [[["one", "two", "three"], [2, 3, 1]], ["two", ["first", "second", "third"]], ["two", 1, 3], ["two", ["fourth", "fifth", "sixth"]], ["two"], ["two", 1], ["two", 2, 2], ["two"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, true, "third", true, ["1,first,second,third", "2,fourth,fifth,sixth"], null, "fifth", ["2,fourth,fifth,sixth"]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sparse ID-to-row dictionaries:** Store only surviving rows plus a monotone next-ID counter. This is the appropriate full-contract design when many deletions create holes.
- **List with tombstones:** Keep row IDs as stable indices and replace deleted rows with `null`. Lookup is simple, but memory remains proportional to the largest assigned ID.
- **Unknown table insertion:** The exact defaultdict silently creates it, contrary to required validation.
- **Wrong row width:** The exact method appends it because constructor column counts are ignored.
- **Deletion:** The exact method is a no-op, so removed rows remain selectable.
- **Invalid selection:** The exact source may raise or use negative indexing instead of returning `"<null>"`.
- **Auto-increment after deletion:** A proper independent counter must never reuse removed IDs.
- **Export:** It is absent from the source and would require CSV formatting plus stable surviving-row order.
- **Caller mutates a row list:** The exact implementation stores the same object; copying on insert would isolate database state.
- **Artifact status:** The exact code supports only a narrow valid append/select subset and does not satisfy the complete local reference contract.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + q + E)$. For the exact source, construction initializes one dictionary in $O(1)$ time and space; it does not process the $n$ schema declarations.
- **Auxiliary Space Complexity:** $O(n + S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
