# Best Time to Buy and Sell Stock III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 123 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) |

## Problem Description
### Goal
You are given the price of a stock for each day in chronological order. Choose a trading schedule containing at most two completed transactions, where each transaction buys one share and sells it on a later day. You cannot hold more than one share, so a second purchase can occur only after the first holding has been sold.

Return the maximum combined profit attainable with zero, one, or two transactions. The two transactions may use different profitable intervals and do not both have to be present. If every possible sale loses money, return `0`; never count an unfinished purchase or allow the same held share to be sold twice.

### Function Contract
**Inputs**

- `prices`: stock prices in chronological order

**Return value**

The maximum profit attainable with zero, one, or two completed transactions.

### Examples
**Example 1**

- Input: `prices = [3, 3, 5, 0, 0, 3, 1, 4]`
- Output: `6`

**Example 2**

- Input: `prices = [1, 2, 3, 4, 5]`
- Output: `4`

**Example 3**

- Input: `prices = [7, 6, 4, 3, 1]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Four balances represent the only legal action stages**

Maintain the best balance after the first buy, first sale, second buy, and second sale. A balance is cash after executing that stage, with a buy state also representing one currently held stock.

Initialize buy states to negative infinity because no buy has occurred before any day, and sale states to zero because doing no transaction is allowed. A first buy transitions from zero cash; a second buy transitions only from a completed first sale, enforcing nonoverlap.

**Each price offers one transition or the choice to keep an earlier state**

For price `p`, apply:

```text
buy1  = max(buy1, -p)
sell1 = max(sell1, buy1 + p)
buy2  = max(buy2, sell1 - p)
sell2 = max(sell2, buy2 + p)
```

Keeping the prior value models taking no action. In-place left-to-right updates may allow a sale and following buy at the same price on one day, but that zero-profit boundary is equivalent to holding stages across adjacent days and cannot create illegal positive profit.

**Every state retains only the dominant history for its stage**

After each day, every state is the maximum balance achievable at its transaction/holding stage using only processed prices. A lower balance at the same stage can never outperform a higher one under identical future prices, so retaining only the maximum loses no optimal schedule.

**Trace two profitable nonoverlapping intervals**

In `[3,3,5,0,0,3,1,4]`, the first completed transaction can earn `2`, and after buying again at `0` or `1`, the second can raise total profit to `6`.

**Four stages enumerate every legal two-transaction schedule**

Any valid history moves in order through first buy, first sell, second buy, and second sell, possibly skipping arbitrarily many days between actions. Each state update either retains the best earlier history for that stage or performs today's action from the immediately preceding stage.

Those are the only legal ways to end a day in each stage. Keeping only the maximum balance discards histories that can never outperform it under identical future actions. After all prices, the second-sell state is therefore the best profit using at most two completed transactions.

#### Complexity detail

Each of `n` prices performs four constant-time updates, giving $O(n)$ time. Four scalar balances give $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Try every split day with separate scans:** takes $O(n^2)$ without prefix/suffix preprocessing.
- **General `k`-transaction DP:** is flexible but stores more state than needed for fixed $k=2$.
- **Sum every positive rise:** allows unlimited transactions and can overstate the answer.
- Fewer than two profitable opportunities naturally leave `sell2` equal to the best zero- or one-transaction result.
- Empty or decreasing inputs return zero through the sale-state initialization.

</details>
