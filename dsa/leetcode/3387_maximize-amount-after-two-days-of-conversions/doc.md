# Maximize Amount After Two Days of Conversions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3387 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/) |

## Problem Description

### Goal

You begin with `1.0` unit of `initialCurrency`. Two independent sets of currency conversions are available on two consecutive days. On day 1, `pairs1[i] = [start, target]` allows an amount of `start` to be multiplied by `rates1[i]` and converted into `target`. Day 2 uses `pairs2` and `rates2` in the same way.

Every listed conversion is reversible: the corresponding conversion from `target` to `start` has multiplier `1 / rate`. During each day you may make any number of that day's conversions, including none. All day-1 conversions must occur before any day-2 conversion.

Each day's rates are internally valid and contain no contradictory conversion paths or profitable cycles; the two days need not agree with each other. Choose a currency to hold between the days and any valid path on each day so that the final amount of `initialCurrency` is as large as possible.

### Function Contract

**Inputs**

- `initialCurrency`: An uppercase currency code of length 1 to 3.
- `pairs1`: The $n$ directed currency pairs listed for day 1.
- `rates1`: The $n$ forward multipliers corresponding to `pairs1`.
- `pairs2`: The $m$ directed currency pairs listed for day 2.
- `rates2`: The $m$ forward multipliers corresponding to `pairs2`.

The bounds are $1 \le n,m \le 10$ and $1.0 \le \texttt{rates1[i]}, \texttt{rates2[i]} \le 10.0$. Every currency code contains only uppercase English letters and has length at most 3. The result is at most $5 \times 10^{10}$.

**Return value**

Return the maximum amount of `initialCurrency` obtainable after the two days, in order.

### Examples

**Example 1**

- Input: `initialCurrency = "EUR", pairs1 = [["EUR", "USD"], ["USD", "JPY"]], rates1 = [2.0, 3.0], pairs2 = [["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]], rates2 = [4.0, 5.0, 6.0]`
- Output: `720.0`

**Example 2**

- Input: `initialCurrency = "NGN", pairs1 = [["NGN", "EUR"]], rates1 = [9.0], pairs2 = [["NGN", "EUR"]], rates2 = [6.0]`
- Output: `1.5`

**Example 3**

- Input: `initialCurrency = "USD", pairs1 = [["USD", "EUR"]], rates1 = [1.0], pairs2 = [["EUR", "JPY"]], rates2 = [10.0]`
- Output: `1.0`
