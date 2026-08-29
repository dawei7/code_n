# Guided Example: Capital Gain/Loss

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Stocks": [{"stock_name": "Leetcode", "operation": "Buy", "operation_day": 1, "price": 1000}, {"stock_name": "Leetcode", "operation": "Sell", "operation_day": 5, "price": 9000}, {"stock_name": "Leetcode", "operation": "Buy", "operation_day": 8, "price": 1230}, {"stock_name": "Leetcode", "operation": "Sell", "operation_day": 10, "price": 1900}]}}`
- **Required output:** `{"columns": ["stock_name", "capital_gain_loss"], "rows": [["Leetcode", 8670]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Stocks`

The objective is to compute `{"columns": ["stock_name", "capital_gain_loss"], "rows": [["Leetcode", 8670]]}` from `{"tables": {"Stocks": [{"stock_name": "Leetcode", "operation": "Buy", "operation_day": 1, "price": 1000}, {"stock_name": "Leetcode", "operation": "Sell", "operation_day": 5, "price": 9000}, {"stock_name": "Leetcode", "operation": "Buy", "operation_day": 8, "price": 1230}, {"stock_name": "Leetcode", "operation": "Sell", "operation_day": 10, "price": 1900}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat every transaction as signed cash flow

Buying a stock sends money out, so a buy price contributes a negative amount. Selling brings money in, so a sell price contributes a positive amount. Once each row has the correct sign, a stock's total capital gain or loss is simply the sum of all its signed transactions.

The exact expression

`IF(operation = 'Buy', -price, price)`

returns negative `price` for a buy and positive `price` otherwise. The table's enum guarantees the only other operation is `'Sell'`, so the else branch represents sales exactly.

This avoids pairing each buy row with a particular later sell row. Pairing is unnecessary for total net result because addition is associative:

$$
\sum(\text{sell prices}-\text{buy prices})
=
\sum\text{sell prices}-\sum\text{buy prices}.
$$

The guarantees about earlier buys and later sells ensure the data describes valid trading sequences, but chronological order does not affect the final net cash flow.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Stocks": [{"stock_name": "Leetcode", "operation": "Buy", "operation_day": 1, "price": 1000}, {"stock_name": "Leetcode", "operation": "Sell", "operation_day": 5, "price": 9000}, {"stock_name": "Leetcode", "operation": "Buy", "operation_day": 8, "price": 1230}, {"stock_name": "Leetcode", "operation": "Sell", "operation_day": 10, "price": 1900}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group independently by stock

`GROUP BY 1` groups by the first expression in the `SELECT` list, which is `stock_name`. Each stock receives its own aggregation group, so transactions belonging to different names never mix.

Within one group, `SUM(...)` adds all signed prices and names the result `capital_gain_loss`. A positive value is a net gain, a negative value a net loss, and zero means buys and sells balance exactly.

Using the column position is legal MySQL syntax, although `GROUP BY stock_name` would be more explicit and less fragile if the select-list order later changed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Following the sample

Leetcode has a buy at 1000 and a sell at 9000. Their signed contributions are $-1000$ and $+9000$, totaling 8000.

Handbags contributes $-30000+7000=-23000$, so the negative output correctly represents a capital loss.

Corona Masks contributes

$$
-10+1010-1000+500-1000+10000=9500.
$$

This equals the sum of the three separately described trade gains, but the query never needs to discover or materialize those pairs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["stock_name", "capital_gain_loss"], "rows": [["Leetcode", 8670]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Stocks": [{"stock_name": "Leetcode", "operation": "Buy", "operation_day": 1, "price": 1000}, {"stock_name": "Leetcode", "operation": "Sell", "operation_day": 5, "price": 9000}, {"stock_name": "Leetcode", "operation": "Buy", "operation_day": 8, "price": 1230}, {"stock_name": "Leetcode", "operation": "Sell", "operation_day": 10, "price": 1900}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["stock_name", "capital_gain_loss"], "rows": [["Leetcode", 8670]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`CASE` expression:** Use `CASE WHEN operation = 'Buy' THEN -price ELSE price END`. It is standard and often more portable than MySQL `IF`.
- **Separate buy and sell aggregates:** Sum buys and sells in separate expressions and subtract. It is correct but repeats conditions and is longer.
- **Pair transactions with window functions:** This is unnecessary for net gain and adds assumptions about matching individual trades.
- **Self-join buys to sells:** It risks multiplicative matches when a stock trades several times and is much harder to make correct.
- **One buy-sell pair:** The aggregate reduces directly to sell price minus buy price.
- **Several trading cycles:** All signed flows combine correctly regardless of conceptual pairing.
- **Net loss:** A negative sum is returned as-is; no absolute value should be applied.
- **Zero net result:** Equal total buys and sells produce zero.
- **Operation domain:** The else branch assumes every non-buy row is `Sell`, guaranteed by the enum. Unexpected values would be incorrectly treated as sales.
- **Transaction order:** `operation_day` is unnecessary for the total, though it establishes valid chronological semantics.
- **Positional grouping:** `GROUP BY 1` means the first selected expression, `stock_name`; explicit naming is more maintainable.
- **Any result order:** The lack of `ORDER BY` is intentional.
- **Null prices outside the contract:** `SUM` would ignore null contributions, so valid data must provide the stated integer price.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of transaction rows and $K$ the number of distinct stock names. A hash-aggregation plan reads each row once, computes one signed value, and updates one group total, giving expected $O(N)$ time. The hash table stores one accumulator per stock, using $O(K)$ space. These bounds match the manifest.
- **Auxiliary Space Complexity:** $O(K)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
