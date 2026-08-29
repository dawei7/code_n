# Guided Example: Count Artist Occurrences On Spotify Ranking List

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Spotify": [{"id": 303651, "track_name": "Heart Won't Forget", "artist": "Sia"}, {"id": 1046089, "track_name": "Shape of You", "artist": "Ed Sheeran"}, {"id": 33445, "track_name": "I'm the One", "artist": "DJ Khalid"}, {"id": 811266, "track_name": "Young Dumb & Broke", "artist": "DJ Khalid"}, {"id": 505727, "track_name": "Happier", "artist": "Ed Sheeran"}]}}`
- **Required output:** `{"columns": ["artist", "occurrences"], "rows": [["DJ Khalid", 2], ["Ed Sheeran", 2], ["Sia", 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Spotify`

The objective is to compute `{"columns": ["artist", "occurrences"], "rows": [["DJ Khalid", 2], ["Ed Sheeran", 2], ["Sia", 1]]}` from `{"tables": {"Spotify": [{"id": 303651, "track_name": "Heart Won't Forget", "artist": "Sia"}, {"id": 1046089, "track_name": "Shape of You", "artist": "Ed Sheeran"}, {"id": 33445, "track_name": "I'm the One", "artist": "DJ Khalid"}, {"id": 811266, "track_name": "Young Dumb & Broke", "artist": "DJ Khalid"}, {"id": 505727, "track_name": "Happier", "artist": "Ed Sheeran"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One table row is one ranking occurrence

Every row in `Spotify` represents one listed track and its artist. To count appearances by artist, rows must be partitioned by the `artist` column.

The query uses:

`GROUP BY artist`.

Each distinct artist name becomes one result group.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Spotify": [{"id": 303651, "track_name": "Heart Won't Forget", "artist": "Sia"}, {"id": 1046089, "track_name": "Shape of You", "artist": "Ed Sheeran"}, {"id": 33445, "track_name": "I'm the One", "artist": "DJ Khalid"}, {"id": 811266, "track_name": "Young Dumb & Broke", "artist": "DJ Khalid"}, {"id": 505727, "track_name": "Happier", "artist": "Ed Sheeran"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count rows inside each group

`COUNT(1)` evaluates the non-null constant one for every row and counts those evaluations.

Therefore, within artist group $a$:

$$
\texttt{COUNT(1)}
=
\#\{\text{Spotify rows whose artist is }a\}.
$$

The result is aliased:

`AS occurrences`.

This supplies the exact requested output column name and makes it available to the ordering clause.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why tracks, not distinct track names, are counted

The question asks how many times the artist appears on the ranking list. Every table row is an appearance.

The query does not use `COUNT(DISTINCT track_name)`. If the same track title appeared in multiple separate rows, each row would count, consistent with row occurrence semantics.

Primary key `id` guarantees rows themselves are distinct.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["artist", "occurrences"], "rows": [["DJ Khalid", 2], ["Ed Sheeran", 2], ["Sia", 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Spotify": [{"id": 303651, "track_name": "Heart Won't Forget", "artist": "Sia"}, {"id": 1046089, "track_name": "Shape of You", "artist": "Ed Sheeran"}, {"id": 33445, "track_name": "I'm the One", "artist": "DJ Khalid"}, {"id": 811266, "track_name": "Young Dumb & Broke", "artist": "DJ Khalid"}, {"id": 505727, "track_name": "Happier", "artist": "Ed Sheeran"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["artist", "occurrences"], "rows": [["DJ Khalid", 2], ["Ed Sheeran", 2], ["Sia", 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`COUNT(*)`:** Equivalent row-count expression and often the clearest spelling.
- **`COUNT(artist)`:** Would ignore rows with null artist and is not identical if nulls are possible.
- **Window count:** Could annotate every original row but would then require deduplication; grouping is simpler.
- **One artist only:** Produces one row with the total table row count.
- **Every artist tied:** Final order is ascending artist name.
- **Repeated track title:** Each table row still counts as one occurrence.
- **Null artist:** `COUNT(1)` counts it and grouping forms one null group.
- **Primary key:** Unique `id` prevents duplicate physical ranking rows by identifier.
- **Alias use:** `occurrences` can be referenced in result ordering.
- **Default second direction:** Omitted direction on `artist` means ascending.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R)$. Let $R$ be the number of ranking rows and $A$ the number of distinct artists.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
