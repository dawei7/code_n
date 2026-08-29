# Guided Example: Find All Unique Email Domains

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Emails": [{"id": 336, "email": "hwkiy@test.edu"}, {"id": 489, "email": "adcmaf@outlook.com"}, {"id": 449, "email": "vrzmwyum@yahoo.com"}, {"id": 95, "email": "tof@test.edu"}, {"id": 320, "email": "jxhbagkpm@example.org"}, {"id": 411, "email": "zxcf@outlook.com"}]}}`
- **Required output:** `{"columns": ["email_domain", "count"], "rows": [["outlook.com", 2], ["yahoo.com", 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Emails`

The objective is to compute `{"columns": ["email_domain", "count"], "rows": [["outlook.com", 2], ["yahoo.com", 1]]}` from `{"tables": {"Emails": [{"id": 336, "email": "hwkiy@test.edu"}, {"id": 489, "email": "adcmaf@outlook.com"}, {"id": 449, "email": "vrzmwyum@yahoo.com"}, {"id": 95, "email": "tof@test.edu"}, {"id": 320, "email": "jxhbagkpm@example.org"}, {"id": 411, "email": "zxcf@outlook.com"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Filter to addresses ending in the required suffix.** `WHERE email LIKE '%.com'` keeps strings whose final characters are `.com`. The leading percent wildcard can match any preceding text, including the local part and domain prefix.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Emails": [{"id": 336, "email": "hwkiy@test.edu"}, {"id": 489, "email": "adcmaf@outlook.com"}, {"id": 449, "email": "vrzmwyum@yahoo.com"}, {"id": 95, "email": "tof@test.edu"}, {"id": 320, "email": "jxhbagkpm@example.org"}, {"id": 411, "email": "zxcf@outlook.com"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Because the address itself ends where its domain ends, filtering the complete email suffix is equivalent to filtering extracted domains for valid email input.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Extract everything after the final at-sign.** MySQL's

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["email_domain", "count"], "rows": [["outlook.com", 2], ["yahoo.com", 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Emails": [{"id": 336, "email": "hwkiy@test.edu"}, {"id": 489, "email": "adcmaf@outlook.com"}, {"id": 449, "email": "vrzmwyum@yahoo.com"}, {"id": 95, "email": "tof@test.edu"}, {"id": 320, "email": "jxhbagkpm@example.org"}, {"id": 411, "email": "zxcf@outlook.com"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["email_domain", "count"], "rows": [["outlook.com", 2], ["yahoo.com", 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **CTE for extracted domains:** Compute `email_domain` once, filter it, then group. This can make the operation order clearer but is not required.
- **`RIGHT(email,4)='.com'`:** It expresses the suffix test directly; `LIKE` is concise and equivalent for this literal suffix.
- **Filter after extraction:** It may be clearer semantically, especially if malformed email input is possible.
- **Multiple users on one domain:** They form one row with count equal to their number.
- **Same email under different IDs:** Both rows count because the task asks for individuals.
- **Subdomain ending in .com:** It remains a distinct full domain group, such as `mail.example.com`.
- **Uppercase domain:** The reference excludes uppercase addresses, so no normalization is needed.
- **Missing at-sign:** `SUBSTRING_INDEX` would return the whole string; valid-email assumptions prevent this.
- **No qualifying domains:** The result is empty.
- **Ordering:** `ORDER BY 1` sorts by the selected domain expression ascending.
- **Why the local part is discarded completely:** Individuals are grouped by the organization/provider portion after `@`. Different usernames such as `a@example.com` and `b@example.com` correctly enter the same domain group.
- **Exact suffix, not substring containment:** `example.com.au` contains `.com` but does not end with it and is excluded, while `service.example.com` is included.
- **Primary key role:** Unique `id` values identify source individuals. The query does not need to select or group by IDs because each row contributes exactly one unit to its domain count.
- **Alias `count`:** Although `COUNT` is a function name, using lowercase `count` as a select alias is accepted in this context and matches the requested output column.
- **Collation and uniqueness:** Domains differing only by case could group together under a case-insensitive collation, but the source guarantee that emails contain no uppercase letters removes that ambiguity.
- **Filter-before-group benefit:** Non-.com rows are discarded before aggregation, so they consume no domain-group state and cannot affect counts for qualifying domains.
- **Negative substring index:** The `-1` argument selects the text after the final at-sign, which is the domain portion under the valid-email guarantee.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S + g log g)$. Let $R$ be the number of email rows, $S$ the total number of characters scanned, and $G$ the number of qualifying domains. Suffix matching and extraction cost $O(S)$ logically. Grouping costs expected $O(R)$ with hashing, and ordering $G$ groups costs $O(G\log G)$.
- **Auxiliary Space Complexity:** $O(g)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
