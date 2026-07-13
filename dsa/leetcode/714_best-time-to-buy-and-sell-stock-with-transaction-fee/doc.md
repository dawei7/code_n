# Best Time to Buy and Sell Stock with Transaction Fee

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 714 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) |

## Problem Description
### Goal
Given daily stock prices and a transaction fee, find the maximum profit you can achieve. You may complete as many buy-sell transactions as you like, but you may hold at most one share at a time and therefore must sell before buying again.

The fee is charged exactly once for each completed purchase-and-sale transaction. Return the greatest final profit after any valid sequence of actions, allowing days with no action and allowing no transactions when trading would lose money. A share must be bought before it is sold.

### Function Contract
**Inputs**

- `prices`: the stock price on each consecutive day
- `fee`: the cost charged once for every completed buy-sell transaction

**Return value**

- The greatest achievable final profit

### Examples
**Example 1**

- Input: `prices = [1,3,2,8,4,9], fee = 2`
- Output: `8`

**Example 2**

- Input: `prices = [1,3,7,5,10,3], fee = 3`
- Output: `6`

**Example 3**

- Input: `prices = [1,2,3], fee = 1`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Keep one state for each legal end-of-day position**

Let `cash` be the best profit after the processed days while holding no share. Let `hold` be the best profit while holding one share, with the purchase cost already subtracted. Initially cash is zero and holding means buying at the first price.

**Update the no-stock state**

On a new price, either remain out of the market with the old `cash` or sell the held share for `hold + price - fee`. Take the better result.

**Update the holding state**

Either keep the old share or buy today using the previous no-stock profit, producing `previous_cash - price`. Using the saved previous cash makes the two transitions describe decisions from the same prior day.

**Why two values contain the complete history**

Every valid strategy ends each day in exactly one of these two states. For each state, the recurrence considers every legal final action—do nothing, buy, or sell—and combines it with the best compatible prior state. Induction therefore preserves the best profit for both positions. A completed strategy cannot finish with more usable profit by holding a share, so final `cash` is the answer.

#### Complexity detail

The state machine performs constant work for each of the `n` prices, taking $O(n)$ time. It stores only the two state values and one saved previous value, using $O(1)$ extra space.

#### Alternatives and edge cases

- **Greedy effective purchase price:** track the cheapest fee-adjusted entry and realize profit when price rises beyond it; it is also linear but its state reinterpretation is less direct.
- **Full DP table:** store cash and hold for every day; it exposes the recurrence visually but uses $O(n)$ space.
- **Try every earlier buy for each sell day:** combine each transaction with prior optimal profit; it is correct but takes $O(n^2)$ time.
- A single day or monotonically decreasing prices produce zero profit.
- A fee larger than every possible rise makes every transaction unprofitable.
- Multiple transactions may outperform one long transaction when prices fall enough between profitable rises.
- The fee is charged once per completed transaction, not on both buying and selling.

</details>
