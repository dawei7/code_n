# Capital Gain/Loss

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1393 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/capital-gainloss/) |

## Problem Description

### Goal

The `Stocks` table records buy and sell operations for named stocks. Each operation has its own day and price, and the same stock can be bought and sold multiple times.

For every stock, calculate the total capital gain or loss across all its operations. Buying spends the recorded price, so it contributes a negative amount; selling receives the recorded price, so it contributes a positive amount. Return one row per stock with its name and final signed total.

### Function Contract

**Inputs**

- `Stocks(stock_name, operation, operation_day, price)`: $N$ stock-operation rows. `operation` is either `"Buy"` or `"Sell"`, and `(stock_name, operation_day)` uniquely identifies a row.

Let $K$ be the number of distinct stock names.

**Return value**

- A relation with columns `stock_name` and `capital_gain_loss`, containing one signed aggregate for each of the $K$ stocks. Row order is not constrained.

### Examples

**Example 1**

- Input: `Stocks = [["Leetcode","Buy",1,1000],["Leetcode","Sell",5,9000],["Leetcode","Buy",8,1230],["Leetcode","Sell",10,1900]]`
- Output: `[["Leetcode",8670]]`

**Example 2**

- Input: `Stocks = [["Handbags","Buy",17,30000],["Handbags","Sell",29,7000],["Handbags","Buy",37,17000],["Handbags","Sell",47,20000]]`
- Output: `[["Handbags",-20000]]`

**Example 3**

- Input: one stock bought for `40` and sold for `40`.
- Output: that stock with `capital_gain_loss = 0`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(K)$

<details>
<summary>Approach</summary>

#### General

**Convert every operation to a signed cash flow.** Use a `CASE` expression that maps a `Buy` price to its negation and leaves a `Sell` price positive. Group rows by `stock_name` and sum those signed values.

For any stock, the aggregate contains every purchase exactly once with a minus sign and every sale exactly once with a plus sign. It therefore equals total sale proceeds minus total purchase cost, which is precisely the requested capital gain or loss. Grouping isolates the operations of different stock names.

The result does not depend on operation order: `operation_day` distinguishes rows and describes their chronology, but addition of the signed amounts is commutative.

#### Complexity detail

A hash aggregation reads all $N$ rows once and maintains one accumulator per distinct stock, taking $O(N)$ expected time and $O(K)$ grouping space. A database may instead sort by `stock_name`, giving $O(N\log N)$ execution under a sort-based physical plan; the authored query expresses the linear grouping algorithm.

#### Alternatives and edge cases

- **Separate buy and sell subqueries:** Aggregate each operation type and join the results. It is correct but scans and combines more intermediate data than one conditional sum.
- **Correlated aggregate per stock:** Select distinct names and rescan `Stocks` for every name. Without an index-assisted plan this costs $O(KN)$ time.
- **Net zero:** Equal total purchases and sales must produce `0`, not omit the stock.
- **Capital loss:** The signed result can be negative when purchase costs exceed sale proceeds.
- **Multiple trading cycles:** Sum every row rather than assuming one buy and one sell per stock.
- **Independent names:** Operations for one stock must never affect another stock's accumulator.

</details>
