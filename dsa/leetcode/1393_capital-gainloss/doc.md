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
