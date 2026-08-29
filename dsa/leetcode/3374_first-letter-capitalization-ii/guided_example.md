# Guided Example: First Letter Capitalization II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"user_content": [{"content_id": 1, "content_text": "hello world of SQL"}, {"content_id": 2, "content_text": "the QUICK-brown fox"}, {"content_id": 3, "content_text": "modern-day DATA science"}, {"content_id": 4, "content_text": "web-based FRONT-end development"}]}}`
- **Required output:** `{"columns": ["content_id", "original_text", "converted_text"], "rows": [[1, "hello world of SQL", "Hello World Of Sql"], [2, "the QUICK-brown fox", "The Quick-Brown Fox"], [3, "modern-day DATA science", "Modern-Day Data Science"], [4, "web-based FRONT-end development", "Web-Based Front-End Development"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: $\text{user}_{content}$

The objective is to compute `{"columns": ["content_id", "original_text", "converted_text"], "rows": [[1, "hello world of SQL", "Hello World Of Sql"], [2, "the QUICK-brown fox", "The Quick-Brown Fox"], [3, "modern-day DATA science", "Modern-Day Data Science"], [4, "web-based FRONT-end development", "Web-Based Front-End Development"]]}` from `{"tables": {"user_content": [{"content_id": 1, "content_text": "hello world of SQL"}, {"content_id": 2, "content_text": "the QUICK-brown fox"}, {"content_id": 3, "content_text": "modern-day DATA science"}, {"content_id": 4, "content_text": "web-based FRONT-end development"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Apply one pure text conversion to every DataFrame row.** Inner helper `convert_text` receives one `content_text` string and returns its converted version. Pandas `apply(convert_text)` invokes it independently for each row, and the resulting series becomes new column `converted_text`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"user_content": [{"content_id": 1, "content_text": "hello world of SQL"}, {"content_id": 2, "content_text": "the QUICK-brown fox"}, {"content_id": 3, "content_text": "modern-day DATA science"}, {"content_id": 4, "content_text": "web-based FRONT-end development"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Split on the literal space delimiter.** `text.split(" ")` differs importantly from `text.split()`. Supplying an explicit delimiter preserves empty fields produced by leading, trailing, or repeated spaces. For example:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `" a"` becomes `["", "a"]`;
- `"a  b"` becomes `["a", "", "b"]`;
- `"a "` becomes `["a", ""]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["content_id", "original_text", "converted_text"], "rows": [[1, "hello world of SQL", "Hello World Of Sql"], [2, "the QUICK-brown fox", "The Quick-Brown Fox"], [3, "modern-day DATA science", "Modern-Day Data Science"], [4, "web-based FRONT-end development", "Web-Based Front-End Development"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"user_content": [{"content_id": 1, "content_text": "hello world of SQL"}, {"content_id": 2, "content_text": "the QUICK-brown fox"}, {"content_id": 3, "content_text": "modern-day DATA science"}, {"content_id": 4, "content_text": "web-based FRONT-end development"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["content_id", "original_text", "converted_text"], "rows": [[1, "hello world of SQL", "Hello World Of Sql"], [2, "the QUICK-brown fox", "The Quick-Brown Fox"], [3, "modern-day DATA science", "Modern-Day Data Science"], [4, "web-based FRONT-end development", "Web-Based Front-End Development"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Regular-expression replacement:** It can capitalize word and post-hyphen letters in one pass but must carefully preserve spacing and lowercase all other letters.
- **Character-state machine:** It avoids temporary split lists and offers exact control over punctuation boundaries.
- **`split()` without a delimiter:** It would collapse repeated spaces and strip leading/trailing spaces, violating the formatting rule.
- **Multiple spaces:** Empty fields preserve them.
- **Leading and trailing spaces:** Explicit split plus join retains them.
- **Multiple hyphens:** Every nonempty component is capitalized and delimiters survive.
- **Leading or trailing hyphen:** Empty components preserve the boundary hyphen.
- **One-character part:** It becomes uppercase.
- **Already normalized text:** Conversion is idempotent.
- **Other allowed punctuation:** It remains present, but `capitalize` does not necessarily uppercase the first letter after it.
- **Empty string:** It splits to one empty field and reconstructs as empty.
- **Input DataFrame mutation:** `converted_text` is added to the supplied object.
- **Output column order:** The final bracket projection enforces it explicitly.
- **Pandas dependency:** The solution requires a compatible `pd.DataFrame` environment.
- **Manifest discrepancy:** No sort, boundary automaton, or hyphen validation exists in the exact source.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(SL + n log n)$. Let $S$ be the total number of characters across all text rows. Each character participates in a constant number of split, capitalization, and join operations, so the core conversion is $O(S)$ time. Pandas `apply` adds per-row Python-call overhead, and column assignment/rename/projection add $O(n)$ object-management work.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
