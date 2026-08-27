# Guided Example: First Letter Capitalization

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"user_content": [{"content_id": 1, "content_text": "hello world of SQL"}, {"content_id": 2, "content_text": "the QUICK brown fox"}, {"content_id": 3, "content_text": "data science AND machine learning"}, {"content_id": 4, "content_text": "TOP rated programming BOOKS"}]}}`
- **Required output:** `{"columns": ["content_id", "original_text", "converted_text"], "rows": [[1, "hello world of SQL", "Hello World Of Sql"], [2, "the QUICK brown fox", "The Quick Brown Fox"], [3, "data science AND machine learning", "Data Science And Machine Learning"], [4, "TOP rated programming BOOKS", "Top Rated Programming Books"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: $\text{user}_{content}$

The objective is to compute `{"columns": ["content_id", "original_text", "converted_text"], "rows": [[1, "hello world of SQL", "Hello World Of Sql"], [2, "the QUICK brown fox", "The Quick Brown Fox"], [3, "data science AND machine learning", "Data Science And Machine Learning"], [4, "TOP rated programming BOOKS", "Top Rated Programming Books"]]}` from `{"tables": {"user_content": [{"content_id": 1, "content_text": "hello world of SQL"}, {"content_id": 2, "content_text": "the QUICK brown fox"}, {"content_id": 3, "content_text": "data science AND machine learning"}, {"content_id": 4, "content_text": "TOP rated programming BOOKS"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Process one space-delimited token per recursive row.** The recursive common table expression `capitalized_words` creates several intermediate rows for each source row in `user_content`. Each intermediate row retains `content_id` and the complete `content_text`, while also storing:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"user_content": [{"content_id": 1, "content_text": "hello world of SQL"}, {"content_id": 2, "content_text": "the QUICK brown fox"}, {"content_id": 3, "content_text": "data science AND machine learning"}, {"content_id": 4, "content_text": "TOP rated programming BOOKS"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- `word`: the next token to process;
- `remaining_text`: everything after that token and its following separator;
- `processed_word`: the converted prefix built so far.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - `word`: the next token to process;
- `remaining_text`: eve... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The non-recursive part creates the first intermediate row. `SUBSTRING_INDEX(content_text, ' ', 1)` returns the characters before the first space. That value becomes the first `word`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["content_id", "original_text", "converted_text"], "rows": [[1, "hello world of SQL", "Hello World Of Sql"], [2, "the QUICK brown fox", "The Quick Brown Fox"], [3, "data science AND machine learning", "Data Science And Machine Learning"], [4, "TOP rated programming BOOKS", "Top Rated Programming Books"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"user_content": [{"content_id": 1, "content_text": "hello world of SQL"}, {"content_id": 2, "content_text": "the QUICK brown fox"}, {"content_id": 3, "content_text": "data science AND machine learning"}, {"content_id": 4, "content_text": "TOP rated programming BOOKS"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["content_id", "original_text", "converted_text"], "rows": [[1, "hello world of SQL", "Hello World Of Sql"], [2, "the QUICK brown fox", "The Quick Brown Fox"], [3, "data science AND machine learning", "Data Science And Machine Learning"], [4, "TOP rated programming BOOKS", "Top Rated Programming Books"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Position-based recursive CTE:** Process one ch:** - **Position-based recursive CTE:** Process one character at a time with an “at word start” flag; it can preserve leading, repeated, and trailing spaces exactly.
- **Built-in title-case function:** MySQL has no universally equivalent built-in that also guarantees the required spacing behavior.
- **Split-and-reassemble:** It is conceptually simple but must retain empty tokens and trailing separators to meet the contract.
- **One-character word:** The first character is uppercased and the empty remainder is harmless.
- **All-uppercase word:** Every character after the first becomes lowercase.
- **Already converted word:** Applying the transformation again leaves it unchanged.
- **Repeated internal spaces:** Empty recursive tokens commonly reconstruct their multiplicity.
- **Leading spaces:** Empty initial tokens can carry them forward, though collation and substring behavior deserve explicit testing.
- **Trailing spaces:** The exact source drops them when `remaining_text` becomes empty.
- **Empty content:** The local description gives no explicit nonempty guarantee; behavior would depend on the anchor and aggregate collation.
- **No special characters:** Tokenization needs to distinguish only literal spaces and letters.
- **`MAX` as last-row selection:** It relies on each completed prefix comparing no smaller than its proper prefix under the active collation.
- **Ordinal grouping:** `GROUP BY 1,2` refers to `content_id` and `original_text`.
- **Unique key:** Grouping cannot merge two different source rows with the same text because IDs differ.
- **Manifest discrepancy:** Exact space preservation and linear character processing are not fully supported by the SQL.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S+n)$. Let $S$ be the total number of characters and $w$ the number of extracted tokens across all rows. A high-level manifest estimate may treat the recursive scan as $O(S)$ plus grouping work. The exact SQL repeatedly scans suffixes with `SUBSTRING_INDEX` and copies growing prefixes with `CONCAT`. For a single long row, the cumulative character work can reach $O(Lw)$ and $O(L^2)$ in the worst case.
- **Auxiliary Space Complexity:** $O(S + n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
