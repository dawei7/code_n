# Guided Example: Create a DataFrame from List

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"args": {"student_data": [[1, 15], [2, 11], [3, 11], [4, 20]]}}`
- **Required output:** `{"columns": ["student_id", "age"], "rows": [[1, 15], [2, 11], [3, 11], [4, 20]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a solution to **create** a DataFrame from a 2D list called $\text{student}_{data}$. This 2D list contains the IDs and ages of some students.

The objective is to compute `{"columns": ["student_id", "age"], "rows": [[1, 15], [2, 11], [3, 11], [4, 20]]}` from `{"args": {"student_data": [[1, 15], [2, 11], [3, 11], [4, 20]]}}` while avoiding redundant calculations and unnecessary overhead.

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

**The input already has the right row structure.** `student_data` is a two-dimensional Python list. Each inner list is one student record, and its two positions mean student identifier followed by age. The requested output has exactly the same rows in exactly the same order; the only missing information is the pair of column labels.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"args": {"student_data": [[1, 15], [2, 11], [3, 11], [4, 20]]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution passes both pieces directly to the pandas constructor:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution passes both pieces directly to the pandas const... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`pd.DataFrame(student_data, columns=['student_id', 'age'])`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id", "age"], "rows": [[1, 15], [2, 11], [3, 11], [4, 20]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"args": {"student_data": [[1, 15], [2, 11], [3, 11], [4, 20]]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id", "age"], "rows": [[1, 15], [2, 11], [3, 11], [4, 20]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Create then rename:** `pd.DataFrame(student_da:** - **Create then rename:** `pd.DataFrame(student_data).rename(columns={0: 'student_id', 1: 'age'})` works but performs schema definition in a second, unnecessary step.
- **Dictionary of columns:** Transposing the rows into two lists and constructing from a dictionary is more verbose and allocates extra intermediates.
- **Manual row loop:** Repeatedly appending rows to a DataFrame is slower and obscures the direct row-record representation.
- **Empty input:** The explicit `columns` argument still creates an empty DataFrame with the two required column names.
- **Row order:** The constructor preserves the outer-list order; it does not sort by `student_id`.
- **Inner-list width:** The contract supplies two items per row. A malformed row with the wrong width can cause construction errors or missing data and is outside the valid input.
- **Duplicate identifiers:** The constructor preserves them because it is not asked to enforce uniqueness or use identifiers as the index.
- **Column-label order:** Labels must be `student_id` first and `age` second to match the positions in every inner list.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of student rows. There are exactly two fields per row, so the constructor processes $2n$ cells, which is $O(n)$ time. Creating the two column arrays, the default index, and DataFrame metadata requires $O(n)$ output space. These bounds match the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
