# Online Stock Span

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 901 |
| Difficulty | Medium |
| Topics | Stack, Design, Monotonic Stack, Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/online-stock-span/) |

## Problem Description
### Goal
Design an online algorithm that receives one stock price per day and reports the current day's price span.

For a given day, the span is the maximum number of consecutive days ending today for which every price is less than or equal to today's price. The interval always includes today and extends backward until the beginning of the stream or the first earlier price that is strictly greater.

Implement `StockSpanner` so each new quote is incorporated before its span is returned.

### Function Contract
Let $q$ be the number of calls made to `next`.

**Operations**

- `StockSpanner()`: initialize an empty price stream.
- `next(price)`: record today's price and return its span, where $1 \leq \texttt{price} \leq 10^5$.
- At most $10^4$ calls are made.

**App-local input**

- `operations`: calls encoded as `["next", price]`.

**Return value**

Return the span produced by every `next` call in order.

### Examples
**Example 1**

- Input: `operations = [["next",100],["next",80],["next",60],["next",70],["next",60],["next",75],["next",85]]`
- Output: `[1,1,1,2,1,4,6]`

**Example 2**

- Input: `operations = [["next",7],["next",2],["next",1],["next",2]]`
- Output: `[1,1,1,3]`

The final price `2` covers today and the preceding prices `1` and `2`, but stops before `7`.

**Example 3**

- Input: `operations = [["next",5],["next",5],["next",5]]`
- Output: `[1,2,3]`
