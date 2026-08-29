# Guided Example: All People Report to the Given Manager

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employees": [{"employee_id": 1, "employee_name": "Boss", "manager_id": 1}]}}`
- **Required output:** `{"columns": ["employee_id"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employees`

The objective is to compute `{"columns": ["employee_id"], "rows": []}` from `{"tables": {"Employees": [{"employee_id": 1, "employee_name": "Boss", "manager_id": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the guaranteed depth bound to unroll the manager chain

Each `Employees` row gives one employee and that person's direct manager. The hierarchy may include groups that do not lead to company head `1`. The problem guarantees that a qualifying reporting chain contains at most three manager links, so the exact query follows exactly three links with self-joins rather than using unbounded recursion.

Alias `e1` represents the employee being considered for output. The first join

`JOIN Employees AS e2 ON e1.manager_id = e2.employee_id`

makes `e2` the direct manager of `e1`. The second join

`JOIN Employees AS e3 ON e2.manager_id = e3.employee_id`

makes `e3` the manager of that direct manager. Finally, `e3.manager_id = 1` tests whether the next manager in the chain is the head.

Read from left to right, the tested chain is

`e1 -> e2 -> e3 -> 1`.

That directly covers an employee three links below the head.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employees": [{"employee_id": 1, "employee_name": "Boss", "manager_id": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the same joins also cover shorter chains

The head's row reports `manager_id = 1`, so once a chain reaches employee `1`, additional unrolled joins remain on that same row. This self-reference pads shorter chains.

For a direct report `e1 -> 1`, `e2` is the head row. Because that row's manager is also one, `e3` joins to the head row again, and `e3.manager_id = 1` passes.

For a two-link report `e1 -> manager -> 1`, `e2` is the intermediate manager and `e3` is the head. The final condition again passes.

For a three-link report, `e3` is the employee directly below the head, and its `manager_id` is one. Therefore one, two, and three manager links all satisfy the same fixed query.

This behavior is visible in the example. Employee `2` directly reports to one and qualifies through padded head joins. Employee `4` follows `4 -> 2 -> 1`. Employee `7` follows `7 -> 4 -> 2 -> 1`. All pass.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Excluding the head

Employee `1` would also satisfy the join chain because its manager relationship points back to itself. The condition `e1.employee_id != 1` explicitly removes it. The requested result contains people who report to the head, not the head personally.

No `DISTINCT` is necessary under the schema. `employee_id` is unique, and each employee row has one `manager_id`. Thus each `e1` can join to at most one `e2` and one `e3`, producing at most one output row for that employee.

Employees whose manager identifier does not match a row disappear at an inner join. In a valid hierarchy, manager references are expected to identify actual employees. Separate self-contained hierarchies remain in the joins but fail `e3.manager_id = 1` unless their chain reaches one within the allowed depth.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employees": [{"employee_id": 1, "employee_name": "Boss", "manager_id": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive common table expression:** Start from the head's direct reports and repeatedly join subordinates. This handles arbitrary depth and is more robust if the three-manager guarantee is removed, but is more machinery than the exact contract requires.
- **Three `OR` checks with fewer joins:** One could separately test direct, two-level, and three-level reporting. The padded self-loop formulation expresses all three with one chain and one final condition.
- **Only one join:** That finds direct reports but misses employees two or three links below the head.
- **Head employee:** The self-referential manager row would qualify, so `e1.employee_id != 1` is essential.
- **Direct report:** Repeated joins remain on the head row and correctly preserve qualification.
- **Separate self-managed hierarchy:** A row such as employee `3` managed by `3` keeps joining to itself and fails the final manager-one condition.
- **Chain longer than three links:** The fixed query would miss it; correctness depends on the stated maximum indirect depth.
- **Unique employee identifiers:** They ensure each alias lookup finds at most one manager row and prevent duplicate output paths.
- **Missing manager row:** Inner joins discard that broken chain, so it cannot be reported as reaching the head.
- **Any output order:** No sorting is necessary or promised.
- **Head self-reference assumption:** Padding shorter chains works because employee `1` has `manager_id = 1` in this data model.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of employee rows. With an index or hash lookup on unique `employee_id`, scanning possible `e1` rows and resolving its two managers takes expected $O(n)$ time. The fixed number of joins does not grow with hierarchy depth because that depth is capped.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
