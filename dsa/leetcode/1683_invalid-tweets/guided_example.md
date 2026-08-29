# Guided Example: Invalid Tweets

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Tweets": [{"tweet_id": 1, "content": "Let us Code"}, {"tweet_id": 2, "content": "More than fifteen chars are here!"}]}}`
- **Required output:** `{"columns": ["tweet_id"], "rows": [[2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Tweets`

The objective is to compute `{"columns": ["tweet_id"], "rows": [[2]]}` from `{"tables": {"Tweets": [{"tweet_id": 1, "content": "Let us Code"}, {"tweet_id": 2, "content": "More than fifteen chars are here!"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate “invalid” into one row predicate

A tweet is invalid exactly when its content contains strictly more than 15 characters. The query therefore needs no join, grouping, or aggregation. Each `Tweets` row can be tested independently.

The source selects only `tweet_id` and filters with

`CHAR_LENGTH(content) > 15`.

Rows satisfying the predicate enter the result; all others are excluded.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Tweets": [{"tweet_id": 1, "content": "Let us Code"}, {"tweet_id": 2, "content": "More than fifteen chars are here!"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why `CHAR_LENGTH` is the right function

MySQL distinguishes character count from byte count. `CHAR_LENGTH(content)` returns the number of characters in the string. `LENGTH(content)` returns the number of encoded bytes.

The contract is expressed in characters, so `CHAR_LENGTH` matches it directly. The local schema limits content to alphanumeric characters, exclamation marks, and spaces, for which byte length commonly equals character length in the expected encoding, but using the character-aware function remains semantically correct and robust.

Spaces and `!` characters count because they are characters in the content. The function does not count words or only letters.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the comparison is strictly greater

The predicate uses `> 15`, not `>= 15`. A tweet containing exactly 15 characters is valid and must not appear. A tweet containing 16 is the smallest invalid case and must appear.

This boundary follows the wording “strictly greater than 15” exactly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["tweet_id"], "rows": [[2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Tweets": [{"tweet_id": 1, "content": "Let us Code"}, {"tweet_id": 2, "content": "More than fifteen chars are here!"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["tweet_id"], "rows": [[2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`LENGTH(content)`:** It counts bytes rather than characters. It happens to work for the restricted simple character set in common encodings, but `CHAR_LENGTH` states the requirement correctly.
- **Computed length column:** A stored or indexed generated column can accelerate repeated length filters, but it changes schema design and is unnecessary for this query.
- **Return content too:** That would add an unrequested output column; only `tweet_id` belongs in the result.
- **Use `>= 15`:** This is an off-by-one error because exactly 15 characters is valid.
- **Exactly 16 characters:** This is the smallest invalid length and passes the predicate.
- **Spaces:** Every space contributes one character, including repeated or leading spaces if the data contains them.
- **Exclamation mark:** It contributes one character just like a letter or digit.
- **Empty content outside the stated model:** Its length is zero and it would be valid.
- **`NULL` content outside the stated model:** `CHAR_LENGTH(NULL)` is null and the predicate is unknown, so SQL would exclude it; a different null policy would need explicit handling.
- **No invalid tweets:** The query correctly returns an empty table with the `tweet_id` column.
- **All tweets invalid:** Every row passes and every unique ID appears once.
- **Any-order requirement:** Omitting `ORDER BY` avoids an unnecessary sort and remains fully correct.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let `R` be the number of tweet rows and `C` the total number of characters across all `content` values. Evaluating character lengths can require examining the content, so a precise logical bound is $O(C)$ time. If content length is treated as bounded by the schema or problem environment, this is commonly summarized as $O(R)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
