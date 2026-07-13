# Best Time to Buy and Sell Stock with Cooldown

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 309 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) |

## Problem Description
### Goal
You are given one stock price for each day. You may complete any number of buy-then-sell transactions, but can hold at most one share at a time. After selling a share, the following day is a cooldown during which buying is forbidden.

Return the maximum total profit achievable by the end of the price history. A sale must occur after its purchase, transactions cannot overlap, and a new purchase may occur only after the full cooldown day has passed. You may skip any day or make no trades when gains are unavailable. Return only the best profit, not the schedule of actions.

### Function Contract
**Inputs**

- `prices`: a nonempty list where `prices[i]` is the stock price on day `i`

**Return value**

The maximum achievable profit after the final day.

### Examples
**Example 1**

- Input: `prices = [1,2,3,0,2]`
- Output: `3`

**Example 2**

- Input: `prices = [49,27,3]`
- Output: `0`

**Example 3**

- Input: `prices = [37,49]`
- Output: `12`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**End each day in one of three economic states**

Track the best profit for three mutually exclusive states:

- `hold`: one share is held after the day;
- `sold`: a share was sold today, so tomorrow is a cooldown day;
- `rest`: no share is held and buying is allowed after today.

Before any prices, resting profit is zero while holding and selling are impossible. For each price, compute all new states from the previous day's values rather than updating in place.

**The cooldown restriction is encoded in the buy transition**

A holding state either continues holding or buys today from yesterday's `rest` state:
`new_hold = max(hold, rest - price)`.
It must not buy from yesterday's `sold` state, which is exactly how the mandatory cooldown is enforced.

Selling today requires a share held yesterday:
`new_sold = hold + price`.
Resting today either continues resting or spends the cooldown day after a prior sale:
`new_rest = max(rest, sold)`.

For `[1,2,3,0,2]`, buy at one and sell the next day at two for profit one. Day two is the cooldown; buying at zero on day three and selling at two on day four adds two, for total profit three. The tempting sale at price three would make the zero-price day unavailable for buying.

**The three states retain every legal strategy**

After each day, classify every legal trading history by whether it ends holding, selling today, or resting. These classes are disjoint and exhaustive. The transitions enumerate every legal predecessor for each class: holding or a permitted buy, a sale from holding, and continued rest or cooldown after sale.

Taking the maximum over each complete predecessor set therefore preserves the best history in every class by induction. A final profit cannot use an unsold share, so `max(sold, rest)` is exactly the optimum.

#### Complexity detail

Each of the `n` prices performs a constant number of arithmetic operations and comparisons, giving $O(n)$ time. Three previous-state values and three new values use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Try every buy/sell pair after every prefix:** is correct with dynamic programming but takes $O(n^2)$ time.
- **Sum every positive adjacent increase:** ignores cooldown and may select incompatible transactions.
- One day or monotonically decreasing prices yield zero. Repeated equal prices preserve the current best states without profit.

</details>
