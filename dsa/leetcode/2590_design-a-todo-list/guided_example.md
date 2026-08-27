# Guided Example: Design a Todo List

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"commands": ["TodoList", "addTask", "addTask", "getAllTasks", "getAllTasks", "addTask", "getTasksForTag", "completeTask", "completeTask", "getTasksForTag", "getAllTasks"], "inputs": [[], [1, "Task1", 50, []], [1, "Task2", 100, ["P1"]], [1], [5], [1, "Task3", 30, ["P1"]], [1, "P1"], [5, 1], [1, 2], [1, "P1"], [1]]}`
- **Required output:** `[null, 1, 2, ["Task1", "Task2"], [], 3, ["Task3", "Task2"], null, null, ["Task3"], ["Task3", "Task1"]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a Todo List Where users can add **tasks**, mark them as **complete**, or get a list of pending tasks. Users can also add **tags** to tasks and can filter the tasks by certain tags.

The objective is to compute `[null, 1, 2, ["Task1", "Task2"], [], 3, ["Task3", "Task2"], null, null, ["Task3"], ["Task3", "Task1"]]` from `{"commands": ["TodoList", "addTask", "addTask", "getAllTasks", "getAllTasks", "addTask", "getTasksForTag", "completeTask", "completeTask", "getTasksForTag", "getAllTasks"], "inputs": [[], [1, "Task1", 50, []], [1, "Task2", 100, ["P1"]], [1], [5], [1, "Task3", 30, ["P1"]], [1, "P1"], [5, 1], [1, 2], [1, "P1"], [1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store each user's tasks in due-date order

`tasks` is a `defaultdict(SortedList)`. Accessing a user ID that has not appeared creates an empty sorted collection automatically.

Each task record is stored as:

`[dueDate, taskDescription, set(tags), taskId, false]`.

Placing `dueDate` first makes the SortedList order records by due date. Due dates are globally unique under the constraints, so later fields never need to break a due-date tie.

The final boolean is the completion flag. false means pending and true means completed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"commands": ["TodoList", "addTask", "addTask", "getAllTasks", "getAllTasks", "addTask", "getTasksForTag", "completeTask", "completeTask", "getTasksForTag", "getAllTasks"], "inputs": [[], [1, "Task1", 50, []], [1, "Task2", 100, ["P1"]], [1], [5], [1, "Task3", 30, ["P1"]], [1, "P1"], [5, 1], [1, 2], [1, "P1"], [1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate global sequential IDs

`i` begins at one. `addTask` saves the current value as `taskId`, increments the counter, inserts the record under the specified user, and returns the saved ID.

Because the counter belongs to the whole TodoList rather than one user, task IDs increase globally across users exactly in call order.

Converting `tags` to a set makes later membership tests such as `tag in x[2]` expected constant time and removes duplicate tags without changing their yes-or-no meaning.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `i` begins at one.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why sorting at insertion answers queries in order

SortedList inserts each new record at its due-date position. Iterating `tasks[userId]` therefore visits all that user's records in ascending due date.

`getAllTasks` filters out records whose completion flag is true and projects field one, the description. Filtering does not disturb the relative order of surviving records, so the returned descriptions remain due-date ordered.

`getTasksForTag` applies both pending and tag-membership conditions before projecting the description. It likewise preserves iteration order.

No query-time sort is needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, 1, 2, ["Task1", "Task2"], [], 3, ["Task3", "Task2"], null, null, ["Task3"], ["Task3", "Task1"]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"commands": ["TodoList", "addTask", "addTask", "getAllTasks", "getAllTasks", "addTask", "getTasksForTag", "completeTask", "completeTask", "getTasksForTag", "getAllTasks"], "inputs": [[], [1, "Task1", 50, []], [1, "Task2", 100, ["P1"]], [1], [5], [1, "Task3", 30, ["P1"]], [1, "P1"], [5, 1], [1, 2], [1, "P1"], [1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, 1, 2, ["Task1", "Task2"], [], 3, ["Task3", "Task2"], null, null, ["Task3"], ["Task3", "Task1"]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Task-ID index:** A dictionary from task ID to :** - **Task-ID index:** A dictionary from task ID to record and owner would make completion expected $O(1)$ while keeping per-user ordering separately.
- **Sort on every query:** Plain per-user lists simplify insertion but make each retrieval $O(u\log u)$; SortedList pays ordering cost incrementally.
- **Delete completed tasks:** Removal would shrink scans but loses stored history and requires locating the record in the ordered container.
- **Unknown user:** Defaultdict supplies an empty SortedList, and query methods return an empty list.
- **Wrong owner completion:** Searching only that user's records ensures another user's task cannot be completed.
- **Repeated completion:** The flag is already true, so observable state does not change.
- **Empty tags:** The stored set is empty and no tag query can match it.
- **Unique due dates:** They guarantee record ordering never depends on mutable later fields.
- **Global task IDs:** One shared counter, not a per-user counter, satisfies sequential creation order.
- **Completed filtering:** Records remain ordered and stored but never appear in either pending-task query.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q^2 log q)$. For a user with $u$ tasks and a new tag list of size $z$, `addTask` uses $O(z)$ set construction plus SortedList insertion, conventionally $O(\log u)$ search with container insertion overhead. `getAllTasks` costs $O(u)$ plus output. `getTasksForTag` costs expected $O(u)$ because each set lookup is expected constant time. `completeTask` costs $O(u)$ worst case.
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
