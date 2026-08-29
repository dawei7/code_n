# Guided Example: Find Users With Valid E-Mails

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Users": [{"user_id": 1, "name": "Winston", "mail": "winston@leetcode.com"}, {"user_id": 2, "name": "Jonathan", "mail": "jonathanisgreat"}, {"user_id": 3, "name": "Annabelle", "mail": "bella-@leetcode.com"}, {"user_id": 4, "name": "Sally", "mail": "sally.come@leetcode.com"}, {"user_id": 5, "name": "Marwan", "mail": "quarz#2020@leetcode.com"}, {"user_id": 6, "name": "David", "mail": "david69@gmail.com"}, {"user_id": 7, "name": "Shapiro", "mail": ".shapo@leetcode.com"}]}}`
- **Required output:** `{"columns": ["user_id", "name", "mail"], "rows": [[1, "Winston", "winston@leetcode.com"], [3, "Annabelle", "bella-@leetcode.com"], [4, "Sally", "sally.come@leetcode.com"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Users`

The objective is to compute `{"columns": ["user_id", "name", "mail"], "rows": [[1, "Winston", "winston@leetcode.com"], [3, "Annabelle", "bella-@leetcode.com"], [4, "Sally", "sally.come@leetcode.com"]]}` from `{"tables": {"Users": [{"user_id": 1, "name": "Winston", "mail": "winston@leetcode.com"}, {"user_id": 2, "name": "Jonathan", "mail": "jonathanisgreat"}, {"user_id": 3, "name": "Annabelle", "mail": "bella-@leetcode.com"}, {"user_id": 4, "name": "Sally", "mail": "sally.come@leetcode.com"}, {"user_id": 5, "name": "Marwan", "mail": "quarz#2020@leetcode.com"}, {"user_id": 6, "name": "David", "mail": "david69@gmail.com"}, {"user_id": 7, "name": "Shapiro", "mail": ".shapo@leetcode.com"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Breaking the validity rule into a full-string pattern

The query uses a regular expression to enforce the prefix grammar and domain shape:

`^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$`

Each part has a distinct job.

The caret anchors matching at the beginning of the mail string. `[a-zA-Z]` requires the first character to be an uppercase or lowercase English letter. This prevents a prefix beginning with a digit, underscore, period, or dash.

`[a-zA-Z0-9_.-]*` permits zero or more remaining prefix characters. The character class allows letters, digits, underscore, literal period, and dash. Zero repetitions are allowed, so a one-letter prefix is valid.

`@leetcode\\.com` represents the required domain. The period must be escaped for the regular-expression engine because an unescaped dot means any single character. The dollar sign anchors the match at the end, preventing extra text after `.com`.

Together, the two anchors ensure the entire mail value follows the grammar rather than merely containing a valid-looking fragment.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Users": [{"user_id": 1, "name": "Winston", "mail": "winston@leetcode.com"}, {"user_id": 2, "name": "Jonathan", "mail": "jonathanisgreat"}, {"user_id": 3, "name": "Annabelle", "mail": "bella-@leetcode.com"}, {"user_id": 4, "name": "Sally", "mail": "sally.come@leetcode.com"}, {"user_id": 5, "name": "Marwan", "mail": "quarz#2020@leetcode.com"}, {"user_id": 6, "name": "David", "mail": "david69@gmail.com"}, {"user_id": 7, "name": "Shapiro", "mail": ".shapo@leetcode.com"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the BINARY LIKE condition is also present

MySQL regular-expression matching can be case-insensitive depending on the string collation. The contract requires the domain to be exactly lowercase.

`BINARY mail LIKE '%@leetcode.com'` converts the left operand to a binary string for a case-sensitive comparison. The percent wildcard permits any prefix, while the fixed suffix requires the exact lowercase domain at the end.

The regular expression already controls which prefix characters are legal and where the domain begins. The binary `LIKE` adds a separate case-sensitive suffix guard. A value ending in `@LeetCode.com` may pass a case-insensitive regex, but it fails the binary suffix test.

In a `LIKE` pattern, the period is an ordinary literal rather than the regex any-character operator, so it does not need backslash escaping there.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why both predicates together are sound

If a row passes the regex, its prefix begins with a letter, every later prefix character belongs to the allowed set, and the remaining shape is the LeetCode domain. If it also passes binary `LIKE`, the actual ending characters have the exact required lowercase spelling.

Conversely, any mail satisfying the stated grammar matches every regex component and ends with the exact lowercase domain, so it passes both predicates.

The query returns `SELECT *`, which produces `user_id`, `name`, and `mail` from `Users`. No `ORDER BY` is required because output order is unrestricted.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "name", "mail"], "rows": [[1, "Winston", "winston@leetcode.com"], [3, "Annabelle", "bella-@leetcode.com"], [4, "Sally", "sally.come@leetcode.com"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Users": [{"user_id": 1, "name": "Winston", "mail": "winston@leetcode.com"}, {"user_id": 2, "name": "Jonathan", "mail": "jonathanisgreat"}, {"user_id": 3, "name": "Annabelle", "mail": "bella-@leetcode.com"}, {"user_id": 4, "name": "Sally", "mail": "sally.come@leetcode.com"}, {"user_id": 5, "name": "Marwan", "mail": "quarz#2020@leetcode.com"}, {"user_id": 6, "name": "David", "mail": "david69@gmail.com"}, {"user_id": 7, "name": "Shapiro", "mail": ".shapo@leetcode.com"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "name", "mail"], "rows": [[1, "Winston", "winston@leetcode.com"], [3, "Annabelle", "bella-@leetcode.com"], [4, "Sally", "sally.come@leetcode.com"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Case-sensitive regex collation:** Apply a binary or case-sensitive collation to the entire regex and omit the extra `LIKE`. Syntax varies by MySQL version.
- **REGEXP_LIKE with match flags:** Newer MySQL versions can request case-sensitive matching explicitly, making intent clearer.
- **String functions without regex:** Prefix and suffix tests plus illegal-character detection are possible but more verbose and easier to get wrong.
- **One-letter prefix:** It is valid because the remainder class uses zero-or-more repetition.
- **Uppercase prefix:** It is permitted by `a-zA-Z`.
- **Uppercase domain letter:** The binary suffix predicate rejects it.
- **Period first:** The required initial letter rejects it.
- **Hash in prefix:** The allowed character class rejects it.
- **Extra suffix text:** The regex end anchor and suffix comparison reject it.
- **Null mail:** SQL predicates evaluate to unknown, so the row is not returned.
- **Unrestricted order:** No sorting clause is necessary.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S + n\log n)$. Let $N$ be the number of users and $S$ the total number of characters across their mail strings. With no usable index for this anchored regex-plus-suffix predicate, the engine typically scans each row and examines its mail value, giving roughly $O(S)$ matching work.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
