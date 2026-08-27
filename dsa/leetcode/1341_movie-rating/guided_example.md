# Guided Example: Movie Rating

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Movies": [{"movie_id": 1, "title": "Avengers"}, {"movie_id": 2, "title": "Frozen 2"}, {"movie_id": 3, "title": "Joker"}], "Users": [{"user_id": 1, "name": "Daniel"}, {"user_id": 2, "name": "Monica"}, {"user_id": 3, "name": "Maria"}, {"user_id": 4, "name": "James"}], "MovieRating": [{"movie_id": 1, "user_id": 1, "rating": 3, "created_at": "2020-01-12"}, {"movie_id": 1, "user_id": 2, "rating": 4, "created_at": "2020-02-11"}, {"movie_id": 1, "user_id": 3, "rating": 2, "created_at": "2020-02-12"}, {"movie_id": 1, "user_id": 4, "rating": 1, "created_at": "2020-01-01"}, {"movie_id": 2, "user_id": 1, "rating": 5, "created_at": "2020-02-17"}, {"movie_id": 2, "user_id": 2, "rating": 2, "created_at": "2020-02-01"}, {"movie_id": 2, "user_id": 3, "rating": 2, "created_at": "2020-03-01"}, {"movie_id": 3, "user_id": 1, "rating": 3, "created_at": "2020-02-22"}, {"movie_id": 3, "user_id": 2, "rating": 4, "created_at": "2020-02-25"}]}}`
- **Required output:** `{"columns": ["results"], "rows": [["Daniel"], ["Frozen 2"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Movies`

The objective is to compute `{"columns": ["results"], "rows": [["Daniel"], ["Frozen 2"]]}` from `{"tables": {"Movies": [{"movie_id": 1, "title": "Avengers"}, {"movie_id": 2, "title": "Frozen 2"}, {"movie_id": 3, "title": "Joker"}], "Users": [{"user_id": 1, "name": "Daniel"}, {"user_id": 2, "name": "Monica"}, {"user_id": 3, "name": "Maria"}, {"user_id": 4, "name": "James"}], "MovieRating": [{"movie_id": 1, "user_id": 1, "rating": 3, "created_at": "2020-01-12"}, {"movie_id": 1, "user_id": 2, "rating": 4, "created_at": "2020-02-11"}, {"movie_id": 1, "user_id": 3, "rating": 2, "created_at": "2020-02-12"}, {"movie_id": 1, "user_id": 4, "rating": 1, "created_at": "2020-01-01"}, {"movie_id": 2, "user_id": 1, "rating": 5, "created_at": "2020-02-17"}, {"movie_id": 2, "user_id": 2, "rating": 2, "created_at": "2020-02-01"}, {"movie_id": 2, "user_id": 3, "rating": 2, "created_at": "2020-03-01"}, {"movie_id": 3, "user_id": 1, "rating": 3, "created_at": "2020-02-22"}, {"movie_id": 3, "user_id": 2, "rating": 4, "created_at": "2020-02-25"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rank users by how many ratings they submitted

The first branch joins `Users` to `MovieRating` with `USING (user_id)`. Every rating row acquires the unique name belonging to its user. It then groups by `user_id`.

Because `(movie_id, user_id)` is the primary key of `MovieRating`, one user cannot have two rating rows for the same movie. Thus `COUNT(1)` within a user group is exactly the number of movies that user rated, not merely an arbitrary row count with duplicates.

`ORDER BY COUNT(1) DESC, name` applies the two ranking rules in priority order:

- More rating rows come first because the count is descending.
- If counts tie, the lexicographically smaller `name` comes first because ascending order is the default.

`LIMIT 1` retains only the winner. Names are unique, so after the count and name ordering there is no unresolved tie. Grouping by the primary-key `user_id` while selecting `name` is meaningful because each identifier determines exactly one user name.

The join is an inner join. A user with no ratings produces no group. Such a user cannot beat any user who has rated at least one movie, so excluding zero-rating users is harmless when the rating table contains the data required by the task.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Movies": [{"movie_id": 1, "title": "Avengers"}, {"movie_id": 2, "title": "Frozen 2"}, {"movie_id": 3, "title": "Joker"}], "Users": [{"user_id": 1, "name": "Daniel"}, {"user_id": 2, "name": "Monica"}, {"user_id": 3, "name": "Maria"}, {"user_id": 4, "name": "James"}], "MovieRating": [{"movie_id": 1, "user_id": 1, "rating": 3, "created_at": "2020-01-12"}, {"movie_id": 1, "user_id": 2, "rating": 4, "created_at": "2020-02-11"}, {"movie_id": 1, "user_id": 3, "rating": 2, "created_at": "2020-02-12"}, {"movie_id": 1, "user_id": 4, "rating": 1, "created_at": "2020-01-01"}, {"movie_id": 2, "user_id": 1, "rating": 5, "created_at": "2020-02-17"}, {"movie_id": 2, "user_id": 2, "rating": 2, "created_at": "2020-02-01"}, {"movie_id": 2, "user_id": 3, "rating": 2, "created_at": "2020-03-01"}, {"movie_id": 3, "user_id": 1, "rating": 3, "created_at": "2020-02-22"}, {"movie_id": 3, "user_id": 2, "rating": 4, "created_at": "2020-02-25"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Restrict movie averages to the requested month

The second branch joins `MovieRating` to `Movies` with `USING (movie_id)`, attaching the unique title to each rating. The filter
`DATE_FORMAT(created_at, '%Y-%m') = '2020-02'` keeps dates whose year and month are February 2020. Ratings from January, March, or another year make no contribution to the averages.

The surviving rows are grouped by `movie_id`. `AVG(rating)` computes the arithmetic mean of all February ratings in each movie group. The ordering `AVG(rating) DESC, title` puts the greatest average first and breaks an equal-average tie with the lexicographically smaller title. `LIMIT 1` keeps the required movie.

The order of aggregation and filtering is crucial. Filtering before `AVG` means the denominator includes only February reviews. Averaging all-time ratings and filtering movies merely because they had some February activity would answer a different question.

Movie titles are unique, so the title tie-breaker is deterministic. The primary key also guarantees at most one February rating per user and movie, but different users can contribute separate ratings to the same movie’s mean.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The second branch joins `MovieRating` to `Movies` with `USIN... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Combine the two winners without deduplication

Each parenthesized branch contains its own `ORDER BY` and `LIMIT 1`, so each produces at most one row. `UNION ALL` concatenates them and intentionally does not remove duplicate text. If a user name happens to equal the winning movie title, the result must still contain two logical answers; plain `UNION` could collapse them into one row.

In MySQL’s execution for this accepted pattern, the first branch is emitted before the second, yielding the user followed by the movie. Formally, SQL does not guarantee final row order without an outer `ORDER BY`. A portability-focused version would add an ordinal to each branch, union them, and order by that ordinal before projecting `results`.

The first branch is complete because every rating belongs to exactly one user group and the ordering implements both winner criteria. The second is complete because every relevant February rating belongs to exactly one movie group and the ordering implements both movie criteria. Combining their top rows produces precisely the requested two values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["results"], "rows": [["Daniel"], ["Frozen 2"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Movies": [{"movie_id": 1, "title": "Avengers"}, {"movie_id": 2, "title": "Frozen 2"}, {"movie_id": 3, "title": "Joker"}], "Users": [{"user_id": 1, "name": "Daniel"}, {"user_id": 2, "name": "Monica"}, {"user_id": 3, "name": "Maria"}, {"user_id": 4, "name": "James"}], "MovieRating": [{"movie_id": 1, "user_id": 1, "rating": 3, "created_at": "2020-01-12"}, {"movie_id": 1, "user_id": 2, "rating": 4, "created_at": "2020-02-11"}, {"movie_id": 1, "user_id": 3, "rating": 2, "created_at": "2020-02-12"}, {"movie_id": 1, "user_id": 4, "rating": 1, "created_at": "2020-01-01"}, {"movie_id": 2, "user_id": 1, "rating": 5, "created_at": "2020-02-17"}, {"movie_id": 2, "user_id": 2, "rating": 2, "created_at": "2020-02-01"}, {"movie_id": 2, "user_id": 3, "rating": 2, "created_at": "2020-03-01"}, {"movie_id": 3, "user_id": 1, "rating": 3, "created_at": "2020-02-22"}, {"movie_id": 3, "user_id": 2, "rating": 4, "created_at": "2020-02-25"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["results"], "rows": [["Daniel"], ["Frozen 2"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Conditional aggregation:** Separate common tab:** - **Conditional aggregation:** Separate common table expressions can compute user counts and February movie averages before ranking. This is more verbose but makes the two logical reports explicit.
- **Window functions:** `ROW_NUMBER` over count-descending and average-descending rankings can identify each winner. It is useful when more than one ranked row is needed.
- **Sargable month filter:** Use `created_at >= '2020-02-01' AND created_at < '2020-03-01'`. It expresses the same month and can use a normal date index more effectively.
- **Plain `UNION`:** This is unsafe because identical user and movie text would be deduplicated. `UNION ALL` preserves both answers.
- **Final row order:** SQL only guarantees presentation order with an outer `ORDER BY`. Add branch ordinals for portable user-first ordering.
- **User count tie:** Ascending `name` after descending count selects the lexicographically smaller unique name.
- **Movie average tie:** Ascending `title` after descending average selects the lexicographically smaller unique title.
- **Ratings outside February:** They count toward the user’s all-time number of rated movies but do not enter the movie-average branch.
- **No February ratings:** The second branch returns no row. The normal problem data is expected to provide a winner; a generalized report may need explicit missing-data behavior.
- **Users with zero ratings:** The inner join omits them. They cannot win against a positive rating count, but an entirely empty rating table would leave the first branch empty too.
- **Primary key guarantee:** One user rates a given movie at most once, so `COUNT(1)` is also a count of distinct rated movies without needing `COUNT(DISTINCT movie_id)`.
- **Average versus total:** Ordering by `SUM(rating)` would favor movies with more reviews and is not equivalent to ordering by `AVG(rating)`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $U$ be the number of users, $M$ the number of movies, and $R$ the number of rating rows. Let $N = U + M + R$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
