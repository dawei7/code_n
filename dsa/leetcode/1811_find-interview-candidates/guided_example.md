# Guided Example: Find Interview Candidates

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Contests": [{"contest_id": 190, "gold_medal": 1, "silver_medal": 5, "bronze_medal": 2}, {"contest_id": 191, "gold_medal": 2, "silver_medal": 3, "bronze_medal": 5}, {"contest_id": 192, "gold_medal": 5, "silver_medal": 2, "bronze_medal": 3}, {"contest_id": 193, "gold_medal": 1, "silver_medal": 3, "bronze_medal": 5}, {"contest_id": 194, "gold_medal": 4, "silver_medal": 5, "bronze_medal": 2}, {"contest_id": 195, "gold_medal": 4, "silver_medal": 2, "bronze_medal": 1}, {"contest_id": 196, "gold_medal": 1, "silver_medal": 5, "bronze_medal": 2}], "Users": [{"user_id": 1, "mail": "sarah@leetcode.com", "name": "Sarah"}, {"user_id": 2, "mail": "bob@leetcode.com", "name": "Bob"}, {"user_id": 3, "mail": "alice@leetcode.com", "name": "Alice"}, {"user_id": 4, "mail": "hercy@leetcode.com", "name": "Hercy"}, {"user_id": 5, "mail": "quarz@leetcode.com", "name": "Quarz"}]}}`
- **Required output:** `{"columns": ["name", "mail"], "rows": [["Sarah", "sarah@leetcode.com"], ["Bob", "bob@leetcode.com"], ["Alice", "alice@leetcode.com"], ["Quarz", "quarz@leetcode.com"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Contests`

The objective is to compute `{"columns": ["name", "mail"], "rows": [["Sarah", "sarah@leetcode.com"], ["Bob", "bob@leetcode.com"], ["Alice", "alice@leetcode.com"], ["Quarz", "quarz@leetcode.com"]]}` from `{"tables": {"Contests": [{"contest_id": 190, "gold_medal": 1, "silver_medal": 5, "bronze_medal": 2}, {"contest_id": 191, "gold_medal": 2, "silver_medal": 3, "bronze_medal": 5}, {"contest_id": 192, "gold_medal": 5, "silver_medal": 2, "bronze_medal": 3}, {"contest_id": 193, "gold_medal": 1, "silver_medal": 3, "bronze_medal": 5}, {"contest_id": 194, "gold_medal": 4, "silver_medal": 5, "bronze_medal": 2}, {"contest_id": 195, "gold_medal": 4, "silver_medal": 2, "bronze_medal": 1}, {"contest_id": 196, "gold_medal": 1, "silver_medal": 5, "bronze_medal": 2}], "Users": [{"user_id": 1, "mail": "sarah@leetcode.com", "name": "Sarah"}, {"user_id": 2, "mail": "bob@leetcode.com", "name": "Bob"}, {"user_id": 3, "mail": "alice@leetcode.com", "name": "Alice"}, {"user_id": 4, "mail": "hercy@leetcode.com", "name": "Hercy"}, {"user_id": 5, "mail": "quarz@leetcode.com", "name": "Quarz"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normalize three medal columns into one event stream

The two candidate rules are easier to evaluate when every medal is represented as one row containing `contest_id`, `user_id`, and medal `type`.

CTE `S` creates that form with three branches:

- gold medalists receive `type = 1`;
- silver medalists receive `type = 2`;
- bronze medalists receive `type = 3`.

The branches use `UNION`. Because medal type differs across branches and each contest has one row, valid medal events are distinct; `UNION ALL` could avoid duplicate elimination, but plain `UNION` is the exact source.

After normalization, gold counting filters type one, while consecutive-contest detection ignores type and treats any medal equally.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Contests": [{"contest_id": 190, "gold_medal": 1, "silver_medal": 5, "bronze_medal": 2}, {"contest_id": 191, "gold_medal": 2, "silver_medal": 3, "bronze_medal": 5}, {"contest_id": 192, "gold_medal": 5, "silver_medal": 2, "bronze_medal": 3}, {"contest_id": 193, "gold_medal": 1, "silver_medal": 3, "bronze_medal": 5}, {"contest_id": 194, "gold_medal": 4, "silver_medal": 5, "bronze_medal": 2}, {"contest_id": 195, "gold_medal": 4, "silver_medal": 2, "bronze_medal": 1}, {"contest_id": 196, "gold_medal": 1, "silver_medal": 5, "bronze_medal": 2}], "Users": [{"user_id": 1, "mail": "sarah@leetcode.com", "name": "Sarah"}, {"user_id": 2, "mail": "bob@leetcode.com", "name": "Bob"}, {"user_id": 3, "mail": "alice@leetcode.com", "name": "Alice"}, {"user_id": 4, "mail": "hercy@leetcode.com", "name": "Hercy"}, {"user_id": 5, "mail": "quarz@leetcode.com", "name": "Quarz"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Detect consecutive contest IDs with row-number subtraction

CTE `T` partitions medal events by `user_id` and orders each user's rows by `contest_id`. `ROW_NUMBER()` assigns 1, 2, 3, and so on within that user's medal history.

For each row it computes

`diff = contest_id - row_number`.

This is the gaps-and-islands technique. If a user medals in contests 190, 191, and 192, the row numbers are 1, 2, and 3, so all differences equal 189. Consecutive IDs increase by one at exactly the same rate as row number.

If a contest is missed, contest ID jumps by more than one while row number increases by only one, changing `diff` and starting a new group.

The statement guarantees globally consecutive contest IDs with no skipped ID. Thus adjacent numeric IDs truly mean adjacent contests, not merely adjacent stored rows.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build candidates satisfying either rule

CTE `P` combines two user sets.

The first branch reads `S`, keeps `type = 1`, groups by user, and retains `COUNT(1) >= 3`. This finds users with at least three gold medals in any contests; consecutiveness is irrelevant.

The second branch groups `T` by `user_id, diff`. Each group is one consecutive run of contests in which that user won some medal. `HAVING COUNT(1) >= 3` retains runs of length at least three.

`SELECT DISTINCT user_id` removes duplicate user IDs when a user has multiple qualifying streak groups. The surrounding `UNION` also removes overlap between users qualifying by both rules.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name", "mail"], "rows": [["Sarah", "sarah@leetcode.com"], ["Bob", "bob@leetcode.com"], ["Alice", "alice@leetcode.com"], ["Quarz", "quarz@leetcode.com"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Contests": [{"contest_id": 190, "gold_medal": 1, "silver_medal": 5, "bronze_medal": 2}, {"contest_id": 191, "gold_medal": 2, "silver_medal": 3, "bronze_medal": 5}, {"contest_id": 192, "gold_medal": 5, "silver_medal": 2, "bronze_medal": 3}, {"contest_id": 193, "gold_medal": 1, "silver_medal": 3, "bronze_medal": 5}, {"contest_id": 194, "gold_medal": 4, "silver_medal": 5, "bronze_medal": 2}, {"contest_id": 195, "gold_medal": 4, "silver_medal": 2, "bronze_medal": 1}, {"contest_id": 196, "gold_medal": 1, "silver_medal": 5, "bronze_medal": 2}], "Users": [{"user_id": 1, "mail": "sarah@leetcode.com", "name": "Sarah"}, {"user_id": 2, "mail": "bob@leetcode.com", "name": "Bob"}, {"user_id": 3, "mail": "alice@leetcode.com", "name": "Alice"}, {"user_id": 4, "mail": "hercy@leetcode.com", "name": "Hercy"}, {"user_id": 5, "mail": "quarz@leetcode.com", "name": "Quarz"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name", "mail"], "rows": [["Sarah", "sarah@leetcode.com"], ["Bob", "bob@leetcode.com"], ["Alice", "alice@leetcode.com"], ["Quarz", "quarz@leetcode.com"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Three self-joins for streaks of exactly three:** It can detect a three-contest window but becomes awkward for the follow-up parameter $n$; gaps-and-islands naturally supports arbitrary streak length.
- **`LAG` comparisons:** Checking previous IDs can mark streak continuations, but run-length aggregation still needs additional logic.
- **`UNION ALL` in `S`:** Valid medal events are already distinct, so it can avoid set deduplication.
- **Inner join to Users:** It is sufficient when every candidate ID is guaranteed to exist and avoids null detail rows.
- **User qualifies twice:** `UNION` returns the user only once.
- **Several qualifying streaks:** `DISTINCT` in the streak branch collapses them to one user ID.
- **Exactly three golds:** The `>= 3` condition includes the user.
- **Golds need not be consecutive:** Only the count matters in the first branch.
- **Any-medal streak:** Gold, silver, and bronze rows all participate equally in `T`.
- **Gap of one missed contest:** It changes `diff` and splits the streak.
- **Contest IDs start above one:** Subtraction grouping works regardless of the starting ID.
- **No skipped global IDs:** It makes numeric consecutiveness equivalent to contest consecutiveness.
- **One candidate condition:** Set union implements logical OR, not AND.
- **Any result order:** No final sorting is necessary.
- **Parameterized streak length:** Replace the second `HAVING COUNT(1) >= 3` threshold with the procedure parameter.
- **Participation-only follow-up:** The normalized medal events would need to be aligned with a participation table before defining consecutive considered contests.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C+U)$. Let $C$ be the number of contests and $U$ the number of users. `S` produces at most $3C$ medal rows.
- **Auxiliary Space Complexity:** $O(C + U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
