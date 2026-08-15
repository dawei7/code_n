# Maximum Profit from Trading Stocks with Discounts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3562 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/) |

## Problem Description

### Goal

A company has `n` employees with IDs from `1` through `n`. Employee `1` is the CEO and is a direct or indirect boss of every other employee. For employee $u$, `present[u - 1]` is the price of buying that employee's stock today, and `future[u - 1]` is its expected selling price tomorrow. Each employee's stock may be bought at most once.

The directed pairs `[boss, employee]` in `hierarchy` form the company tree. A purchase by an employee's **direct** boss discounts that employee's current price to $\lfloor\text{price}/2\rfloor$. A more distant ancestor does not provide the discount unless the direct boss also buys. All purchases must be funded from the original `budget`; tomorrow's profits cannot finance additional stocks.

Choose which stocks to buy without exceeding the budget, accounting for discounts created by those same choices, and return the maximum total profit. Buying no stock is allowed, so the result is never negative.

### Function Contract

**Inputs**

- `n`: The number of employees, whose IDs are `1` through `n`.
- `present`: The current buying prices; employee $u$ has price `present[u - 1]`.
- `future`: The expected selling prices; employee $u$ has value `future[u - 1]` tomorrow.
- `hierarchy`: The `n - 1` directed pairs `[u, v]`, each meaning that `u` is the direct boss of `v`.
- `budget`: The maximum total amount available for today's purchases.

Let $B=\texttt{budget}$. The constraints are $1 \le n,B \le 160$ and $1 \le \texttt{present}[i],\texttt{future}[i] \le 50$. The hierarchy has no duplicate edge or cycle, and every employee is reachable from employee `1`.

**Return value**

Return the maximum sum of `future price - actual buying price` over the selected stocks, where each actual price reflects whether that employee's direct boss was also selected and total buying cost is at most `budget`.

### Examples

#### Example 1

- **Input:** `n = 2, present = [1,2], future = [4,3], hierarchy = [[1,2]], budget = 3`
- **Output:** `5`
- **Explanation:** Buying the CEO for `1` discounts employee 2's stock from `2` to `1`. Their profits are `3` and `2`, for total profit `5` at cost `2`.

#### Example 2

- **Input:** `n = 2, present = [3,4], future = [5,8], hierarchy = [[1,2]], budget = 4`
- **Output:** `4`
- **Explanation:** Buying only employee 2 costs `4` and yields profit `4`; the budget cannot fund the better-looking combined purchase.

#### Example 3

- **Input:** `n = 3, present = [4,6,8], future = [7,9,11], hierarchy = [[1,2],[1,3]], budget = 10`
- **Output:** `10`
- **Explanation:** Buy employee 1 for `4` and employee 3 at the discounted price `4`. Their profits are `3` and `7`.

#### Example 4

- **Input:** `n = 3, present = [5,2,3], future = [8,5,6], hierarchy = [[1,2],[2,3]], budget = 7`
- **Output:** `12`
- **Explanation:** Buying all three stocks costs `5 + 1 + 1 = 7`; consecutive direct-boss purchases propagate the discounts down the chain.

---
