# Guided Example: Richest Customer Wealth

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"accounts": [[1, 2, 3], [3, 2, 1]]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` integer grid `accounts` where $\text{accounts}[i][j]$ is the amount of money the $i​​​​​^​​​​​​th​​​​$ customer has in the $j​​​​​^​​​​​​th$​​​​ bank. Return* the **wealth** that the richest customer has.*

The objective is to compute `6` from `{"accounts": [[1, 2, 3], [3, 2, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the table into one total per customer

Each inner list in `accounts` belongs to one customer. Its entries are the amounts that customer holds in different banks. The problem defines wealth as the sum across all those entries, so for a row `v` the exact wealth is `sum(v)`.

Once every customer has one row sum, the richest wealth is simply the largest of those sums. The source expresses both levels directly:

`max(sum(v) for v in accounts)`.

The generator visits the customer rows one at a time. For the current row, `sum` visits all bank balances and produces that customer’s total. `max` compares each produced total with the largest one seen so far and ultimately returns the greatest.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"accounts": [[1, 2, 3], [3, 2, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a generator is enough

There is no need to remember every customer’s total after comparing it. If the first processed customer has wealth six, the running maximum is six. If the next has wealth ten, the running maximum becomes ten. A later total of eight cannot change it. At every point, only the greatest wealth among the rows processed so far matters.

The generator expression supplies totals lazily to `max` instead of constructing a separate list such as `[sum(v) for v in accounts]`. That avoids storing one additional number per customer. Each row already exists in the input; only its scalar sum is temporarily produced.

The constraints guarantee at least one customer, so `max` always receives at least one value. No default value or empty-input branch is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | There is no need to remember every customer’s total after co... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A trace

For `accounts = [[1, 5], [7, 3], [3, 5]]`:

- the first row yields `1 + 5 = 6`, so the current maximum is six;
- the second yields `7 + 3 = 10`, replacing the current maximum;
- the third yields `3 + 5 = 8`, which is smaller than ten.

The returned answer is ten. The index or identity of the customer does not need to be returned, so the implementation stores only the wealth value.

For `[[1, 2, 3], [3, 2, 1]]`, both row sums are six. `max` returns six regardless of which tied customer is considered first. This matches the contract: it asks for the wealth of a richest customer, not for a unique customer ID.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"accounts": [[1, 2, 3], [3, 2, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit nested loops:** Maintain `current_wea:** - **Explicit nested loops:** Maintain `current_wealth` for each row and `best` globally. This is longer but exposes the same $O(S)$ time and $O(1)$ space mechanics.
- **List comprehension of row sums:** `max([sum(v) for v in accounts])` is correct but allocates an $O(m)$ temporary list that the generator avoids.
- **Sort customer totals:** Sorting can identify the largest value but costs $O(m\log m)$ after the sums and stores all totals, neither of which is needed for one maximum.
- **Tied richest customers:** Only the wealth is returned, so equal maximum totals need no tie-breaking rule.
- **One customer:** The only row sum is necessarily the maximum and is returned.
- **One bank per customer:** Every row sum equals its single entry, so the operation reduces naturally to finding the largest balance.
- **All balances equal:** Row lengths are equal in the rectangular input, so all wealth totals tie and that common total is returned.
- **Positive-input guarantee:** It permits an explicit-loop version to initialize a maximum to zero, but the exact built-in expression does not rely on that detail.
- **Nonempty-grid guarantee:** Without at least one row, `max` would raise an exception; the stated `m >= 1` makes the call safe.
- **No customer index returned:** Tracking which row produced the maximum would be extra state for information the contract does not request.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let `m` be the number of customers, let customer `i` have `n_i` accounts, and define
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
