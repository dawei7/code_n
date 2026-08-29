# Guided Example: Most Common Course Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"course_completions": [{"user_id": 1, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-05", "course_rating": 5}, {"user_id": 1, "course_id": 102, "course_name": "SQL Fundamentals", "completion_date": "2024-02-10", "course_rating": 4}, {"user_id": 1, "course_id": 103, "course_name": "JavaScript", "completion_date": "2024-03-15", "course_rating": 5}, {"user_id": 1, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-04-20", "course_rating": 4}, {"user_id": 1, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-05-25", "course_rating": 5}, {"user_id": 1, "course_id": 106, "course_name": "Docker", "completion_date": "2024-06-30", "course_rating": 4}, {"user_id": 2, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-08", "course_rating": 4}, {"user_id": 2, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-02-14", "course_rating": 5}, {"user_id": 2, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-03-20", "course_rating": 4}, {"user_id": 2, "course_id": 106, "course_name": "Docker", "completion_date": "2024-04-25", "course_rating": 5}, {"user_id": 2, "course_id": 107, "course_name": "AWS Fundamentals", "completion_date": "2024-05-30", "course_rating": 4}, {"user_id": 3, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-10", "course_rating": 3}, {"user_id": 3, "course_id": 102, "course_name": "SQL Fundamentals", "completion_date": "2024-02-12", "course_rating": 3}, {"user_id": 3, "course_id": 103, "course_name": "JavaScript", "completion_date": "2024-03-18", "course_rating": 3}, {"user_id": 3, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-04-22", "course_rating": 2}, {"user_id": 3, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-05-28", "course_rating": 3}, {"user_id": 4, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-12", "course_rating": 5}, {"user_id": 4, "course_id": 108, "course_name": "Data Science", "completion_date": "2024-02-16", "course_rating": 5}, {"user_id": 4, "course_id": 109, "course_name": "Machine Learning", "completion_date": "2024-03-22", "course_rating": 5}]}}`
- **Required output:** `{"columns": ["first_course", "second_course", "transition_count"], "rows": [["Node.js", "Docker", 2], ["React Basics", "Node.js", 2], ["Docker", "AWS Fundamentals", 1], ["JavaScript", "React Basics", 1], ["Python Basics", "React Basics", 1], ["Python Basics", "SQL Fundamentals", 1], ["SQL Fundamentals", "JavaScript", 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: $\text{course}_{completions}$

The objective is to compute `{"columns": ["first_course", "second_course", "transition_count"], "rows": [["Node.js", "Docker", 2], ["React Basics", "Node.js", 2], ["Docker", "AWS Fundamentals", 1], ["JavaScript", "React Basics", 1], ["Python Basics", "React Basics", 1], ["Python Basics", "SQL Fundamentals", 1], ["SQL Fundamentals", "JavaScript", 1]]}` from `{"tables": {"course_completions": [{"user_id": 1, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-05", "course_rating": 5}, {"user_id": 1, "course_id": 102, "course_name": "SQL Fundamentals", "completion_date": "2024-02-10", "course_rating": 4}, {"user_id": 1, "course_id": 103, "course_name": "JavaScript", "completion_date": "2024-03-15", "course_rating": 5}, {"user_id": 1, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-04-20", "course_rating": 4}, {"user_id": 1, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-05-25", "course_rating": 5}, {"user_id": 1, "course_id": 106, "course_name": "Docker", "completion_date": "2024-06-30", "course_rating": 4}, {"user_id": 2, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-08", "course_rating": 4}, {"user_id": 2, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-02-14", "course_rating": 5}, {"user_id": 2, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-03-20", "course_rating": 4}, {"user_id": 2, "course_id": 106, "course_name": "Docker", "completion_date": "2024-04-25", "course_rating": 5}, {"user_id": 2, "course_id": 107, "course_name": "AWS Fundamentals", "completion_date": "2024-05-30", "course_rating": 4}, {"user_id": 3, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-10", "course_rating": 3}, {"user_id": 3, "course_id": 102, "course_name": "SQL Fundamentals", "completion_date": "2024-02-12", "course_rating": 3}, {"user_id": 3, "course_id": 103, "course_name": "JavaScript", "completion_date": "2024-03-18", "course_rating": 3}, {"user_id": 3, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-04-22", "course_rating": 2}, {"user_id": 3, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-05-28", "course_rating": 3}, {"user_id": 4, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-12", "course_rating": 5}, {"user_id": 4, "course_id": 108, "course_name": "Data Science", "completion_date": "2024-02-16", "course_rating": 5}, {"user_id": 4, "course_id": 109, "course_name": "Machine Learning", "completion_date": "2024-03-22", "course_rating": 5}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build the result in three relational stages

The query uses two common table expressions and one final aggregation:

1. `top_students` decides which users qualify.
2. `course_pairs` orders each qualifying user's history and attaches the next course to every current course.
3. The outer query removes rows with no next course, counts equal transitions, and applies the required output order.

Keeping these stages separate is useful because each one answers a different question: who is eligible, what each adjacency is, and how often each adjacency occurs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"course_completions": [{"user_id": 1, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-05", "course_rating": 5}, {"user_id": 1, "course_id": 102, "course_name": "SQL Fundamentals", "completion_date": "2024-02-10", "course_rating": 4}, {"user_id": 1, "course_id": 103, "course_name": "JavaScript", "completion_date": "2024-03-15", "course_rating": 5}, {"user_id": 1, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-04-20", "course_rating": 4}, {"user_id": 1, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-05-25", "course_rating": 5}, {"user_id": 1, "course_id": 106, "course_name": "Docker", "completion_date": "2024-06-30", "course_rating": 4}, {"user_id": 2, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-08", "course_rating": 4}, {"user_id": 2, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-02-14", "course_rating": 5}, {"user_id": 2, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-03-20", "course_rating": 4}, {"user_id": 2, "course_id": 106, "course_name": "Docker", "completion_date": "2024-04-25", "course_rating": 5}, {"user_id": 2, "course_id": 107, "course_name": "AWS Fundamentals", "completion_date": "2024-05-30", "course_rating": 4}, {"user_id": 3, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-10", "course_rating": 3}, {"user_id": 3, "course_id": 102, "course_name": "SQL Fundamentals", "completion_date": "2024-02-12", "course_rating": 3}, {"user_id": 3, "course_id": 103, "course_name": "JavaScript", "completion_date": "2024-03-18", "course_rating": 3}, {"user_id": 3, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-04-22", "course_rating": 2}, {"user_id": 3, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-05-28", "course_rating": 3}, {"user_id": 4, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-12", "course_rating": 5}, {"user_id": 4, "course_id": 108, "course_name": "Data Science", "completion_date": "2024-02-16", "course_rating": 5}, {"user_id": 4, "course_id": 109, "course_name": "Machine Learning", "completion_date": "2024-03-22", "course_rating": 5}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filter users using their complete histories

The first CTE groups `course_completions` by `user_id`. Each group contains all completion rows for one user. Its `HAVING` clause requires both

`COUNT(1) >= 5`

and

`AVG(course_rating) >= 4`.

`WHERE` cannot perform this group-level test because the decision depends on multiple rows. `HAVING` is evaluated after grouping and aggregation, which is exactly when the course count and average rating exist.

Both comparisons are inclusive. A user with exactly five completion rows qualifies, provided the average across all five is at least four. A user with more courses is tested across the entire history; the query does not select only the five best ratings. Likewise, a user with a 4.0 average qualifies, while a 3.999 average does not.

The CTE returns only `user_id`. This makes it a compact eligibility relation that can be joined back to the original rows.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Restrict the sequence construction to qualifying users

`top_students JOIN course_completions USING (user_id)` keeps all completion rows belonging to qualifying users and discards every row from other users.

The join happens before course pairs are counted. Therefore an ineligible user's transitions cannot accidentally contribute to the frequency and then be filtered afterward. Every row reaching the window function is already known to belong to a top performer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["first_course", "second_course", "transition_count"], "rows": [["Node.js", "Docker", 2], ["React Basics", "Node.js", 2], ["Docker", "AWS Fundamentals", 1], ["JavaScript", "React Basics", 1], ["Python Basics", "React Basics", 1], ["Python Basics", "SQL Fundamentals", 1], ["SQL Fundamentals", "JavaScript", 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"course_completions": [{"user_id": 1, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-05", "course_rating": 5}, {"user_id": 1, "course_id": 102, "course_name": "SQL Fundamentals", "completion_date": "2024-02-10", "course_rating": 4}, {"user_id": 1, "course_id": 103, "course_name": "JavaScript", "completion_date": "2024-03-15", "course_rating": 5}, {"user_id": 1, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-04-20", "course_rating": 4}, {"user_id": 1, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-05-25", "course_rating": 5}, {"user_id": 1, "course_id": 106, "course_name": "Docker", "completion_date": "2024-06-30", "course_rating": 4}, {"user_id": 2, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-08", "course_rating": 4}, {"user_id": 2, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-02-14", "course_rating": 5}, {"user_id": 2, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-03-20", "course_rating": 4}, {"user_id": 2, "course_id": 106, "course_name": "Docker", "completion_date": "2024-04-25", "course_rating": 5}, {"user_id": 2, "course_id": 107, "course_name": "AWS Fundamentals", "completion_date": "2024-05-30", "course_rating": 4}, {"user_id": 3, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-10", "course_rating": 3}, {"user_id": 3, "course_id": 102, "course_name": "SQL Fundamentals", "completion_date": "2024-02-12", "course_rating": 3}, {"user_id": 3, "course_id": 103, "course_name": "JavaScript", "completion_date": "2024-03-18", "course_rating": 3}, {"user_id": 3, "course_id": 104, "course_name": "React Basics", "completion_date": "2024-04-22", "course_rating": 2}, {"user_id": 3, "course_id": 105, "course_name": "Node.js", "completion_date": "2024-05-28", "course_rating": 3}, {"user_id": 4, "course_id": 101, "course_name": "Python Basics", "completion_date": "2024-01-12", "course_rating": 5}, {"user_id": 4, "course_id": 108, "course_name": "Data Science", "completion_date": "2024-02-16", "course_rating": 5}, {"user_id": 4, "course_id": 109, "course_name": "Machine Learning", "completion_date": "2024-03-22", "course_rating": 5}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["first_course", "second_course", "transition_count"], "rows": [["Node.js", "Docker", 2], ["React Basics", "Node.js", 2], ["Docker", "AWS Fundamentals", 1], ["JavaScript", "React Basics", 1], ["Python Basics", "React Basics", 1], ["Python Basics", "SQL Fundamentals", 1], ["SQL Fundamentals", "JavaScript", 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Self-join on the next date:** Joining each row to the minimum later date can express adjacency, but it is more cumbersome and may perform repeated searches. `LEAD` states the sequence relation directly.
- **Correlated subquery for the next course:** This can also find a successor but risks one lookup per row and complicated tie handling.
- **Filter ratings before grouping:** That would change both the course count and average. Qualification must use every completion row in the user's history.
- **Use `WHERE COUNT(...)`:** Aggregate conditions belong in `HAVING` because they are defined only after grouping.
- **Omit `PARTITION BY user_id`:** This could create false cross-user pairs at partition boundaries.
- **Use a later course instead of `LEAD`:** The contract counts adjacent transitions only; skipping an intervening completion invents a pair.
- **User with exactly five courses and average exactly four:** Both inclusive conditions pass.
- **Qualifying user with one final course row:** Its `LEAD` value is `NULL` and that incomplete pair is discarded.
- **Repeated named transition within one user:** Every occurrence is counted, as required by the row-level `COUNT(1)`.
- **Different IDs with the same course name:** The source groups by names, so those IDs contribute to the same displayed transition.
- **Tied completion dates:** The exact window order contains no secondary key. If one user has multiple courses on the same date, their relative order is not guaranteed by this query; the data needs an unambiguous chronology or the source would need an authorized tie-break rule.
- **No qualifying users:** `course_pairs` is empty and the query returns an empty result table.
- **A qualifying user's first course:** It can be `first_course` but never appears as a `second_course` unless another completion precedes it.
- **A qualifying user's last course:** It may be `second_course` for the prior row, while its own generated row is removed because there is no successor.
- **Final tie ordering:** Omitting either name key would leave equal-frequency rows without the full specified order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R + P log P)$. Let $R$ be the number of completion rows and $P$ the number of distinct output course-name pairs.
- **Auxiliary Space Complexity:** $O(R + P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
