# Guided Example: Count the Number of Experiments

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Experiments": [{"experiment_id": 4, "platform": "IOS", "experiment_name": "Programming"}, {"experiment_id": 13, "platform": "IOS", "experiment_name": "Sports"}, {"experiment_id": 14, "platform": "Android", "experiment_name": "Reading"}, {"experiment_id": 8, "platform": "Web", "experiment_name": "Reading"}, {"experiment_id": 12, "platform": "Web", "experiment_name": "Reading"}, {"experiment_id": 18, "platform": "Web", "experiment_name": "Programming"}]}}`
- **Required output:** `{"columns": ["platform", "experiment_name", "num_experiments"], "rows": [["Android", "Reading", 1], ["Android", "Sports", 0], ["Android", "Programming", 0], ["IOS", "Reading", 0], ["IOS", "Sports", 1], ["IOS", "Programming", 1], ["Web", "Reading", 2], ["Web", "Sports", 0], ["Web", "Programming", 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Experiments`

The objective is to compute `{"columns": ["platform", "experiment_name", "num_experiments"], "rows": [["Android", "Reading", 1], ["Android", "Sports", 0], ["Android", "Programming", 0], ["IOS", "Reading", 0], ["IOS", "Sports", 1], ["IOS", "Programming", 1], ["Web", "Reading", 2], ["Web", "Sports", 0], ["Web", "Programming", 1]]}` from `{"tables": {"Experiments": [{"experiment_id": 4, "platform": "IOS", "experiment_name": "Programming"}, {"experiment_id": 13, "platform": "IOS", "experiment_name": "Sports"}, {"experiment_id": 14, "platform": "Android", "experiment_name": "Reading"}, {"experiment_id": 8, "platform": "Web", "experiment_name": "Reading"}, {"experiment_id": 12, "platform": "Web", "experiment_name": "Reading"}, {"experiment_id": 18, "platform": "Web", "experiment_name": "Programming"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generate the complete category grid first

Grouping only rows that exist in `Experiments` cannot produce categories with zero observations. The query therefore constructs the required output domain explicitly before looking at the data.

CTE `P` contains exactly the three platform literals: Android, IOS, and Web. CTE `Exp` contains exactly the three experiment-name literals: Reading, Sports, and Programming.

Each uses `UNION` to form its constant relation. The literals are distinct, so duplicate removal changes nothing, but the result is the intended three-row list.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Experiments": [{"experiment_id": 4, "platform": "IOS", "experiment_name": "Programming"}, {"experiment_id": 13, "platform": "IOS", "experiment_name": "Sports"}, {"experiment_id": 14, "platform": "Android", "experiment_name": "Reading"}, {"experiment_id": 8, "platform": "Web", "experiment_name": "Reading"}, {"experiment_id": 12, "platform": "Web", "experiment_name": "Reading"}, {"experiment_id": 18, "platform": "Web", "experiment_name": "Programming"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Take the Cartesian product

CTE `T` selects from `P, Exp` without a join condition. In SQL, this is a cross join. Every platform row pairs with every experiment-name row, creating $3\cdot3=9$ category combinations.

This fixed nine-row table is the backbone of the solution. Even a category absent from the actual experiments already has a row that can survive to the output.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Attach matching experiment records

`T AS t LEFT JOIN Experiments USING (platform, experiment_name)` matches each category pair with every recorded experiment having both the same platform and experiment name.

The left join is essential. If a pair has no experiment, its `T` row remains and the columns coming from `Experiments`, including `experiment_id`, are null.

`USING` is shorthand for equality on both named columns and exposes one merged copy of each join key. It is appropriate because both tables use the exact same key names.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["platform", "experiment_name", "num_experiments"], "rows": [["Android", "Reading", 1], ["Android", "Sports", 0], ["Android", "Programming", 0], ["IOS", "Reading", 0], ["IOS", "Sports", 1], ["IOS", "Programming", 1], ["Web", "Reading", 2], ["Web", "Sports", 0], ["Web", "Programming", 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Experiments": [{"experiment_id": 4, "platform": "IOS", "experiment_name": "Programming"}, {"experiment_id": 13, "platform": "IOS", "experiment_name": "Sports"}, {"experiment_id": 14, "platform": "Android", "experiment_name": "Reading"}, {"experiment_id": 8, "platform": "Web", "experiment_name": "Reading"}, {"experiment_id": 12, "platform": "Web", "experiment_name": "Reading"}, {"experiment_id": 18, "platform": "Web", "experiment_name": "Programming"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["platform", "experiment_name", "num_experiments"], "rows": [["Android", "Reading", 1], ["Android", "Sports", 0], ["Android", "Programming", 0], ["IOS", "Reading", 0], ["IOS", "Sports", 1], ["IOS", "Programming", 1], ["Web", "Reading", 2], ["Web", "Sports", 0], ["Web", "Programming", 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Group `Experiments` directly:** Misses category pairs whose count should be zero.
- **Conditional aggregation:** Can count all experiment names per platform, but still needs an explicit platform domain and may produce a wide rather than requested row format.
- **Separate tables for enum domains:** Preferable in a normalized extensible schema; cross joining those tables follows the same idea.
- **`COUNT(*)`:** Incorrectly counts the null-extended placeholder as one for absent categories.
- **`COUNT(experiment_id)`:** Correct because only actual matched rows have nonnull IDs.
- **Empty `Experiments` table:** The cross product still yields all nine pairs, each with zero.
- **Many rows in one category:** Every nonnull ID is counted once.
- **Unique experiment IDs:** Prevent accidental duplication within the source table.
- **Two-key join:** Both platform and experiment name are necessary; joining on only one mixes categories.
- **Fixed enum values:** Explicit CTE literals ensure categories absent from data still appear.
- **Any output order:** No `ORDER BY` is needed.
- **Positional grouping:** `GROUP BY 1, 2` refers to the two selected category columns.
- **No mutation:** The query reads and aggregates `Experiments`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of rows in `Experiments`. The generated category table always has nine rows. With hashing or a single scan/group plan, matching and aggregation take $O(N)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
