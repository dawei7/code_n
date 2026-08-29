# Maximize Total Tastiness of Purchased Fruits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2431 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximize Total Tastiness of Purchased Fruits](https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/) |

## Problem Description

### Goal

Two non-negative arrays, `price` and `tastiness`, describe the same $n$ fruits: `price[i]` is the cost of fruit $i$, and `tastiness[i]` is the value gained by purchasing it. Select any subset whose total paid cost does not exceed `maxAmount`, maximizing the sum of its tastiness values.

You may apply at most `maxCoupons` coupons. A coupon can be used on a purchased fruit at most once and changes its cost to `price[i] // 2`, including the downward rounding for odd prices. Every fruit can be purchased at most once. Return the greatest total tastiness achievable under these rules.

### Function Contract

**Inputs**

- `price`: The non-negative prices of the fruits.
- `tastiness`: The corresponding non-negative tastiness values.
- `maxAmount`: The maximum total amount that may be paid.
- `maxCoupons`: The maximum number of coupons that may be used.

The arrays have the same length $n$, where $1 \le n \le 100$. Each array value and `maxAmount` lies in `[0,1000]`, and $0 \le \texttt{maxCoupons} \le 5$.

**Return value**

- The maximum total tastiness of a valid purchase.

### Examples

#### Example 1

- **Input:** `price = [10, 20, 20], tastiness = [5, 8, 8], maxAmount = 20, maxCoupons = 1`
- **Output:** `13`

Buy the first fruit for 10 and one of the other fruits with a coupon for 10.

#### Example 2

- **Input:** `price = [10, 15, 7], tastiness = [5, 8, 20], maxAmount = 10, maxCoupons = 2`
- **Output:** `28`

Coupons reduce the second and third prices to 7 and 3, so both fit exactly.

#### Example 3

- **Input:** `price = [0, 5], tastiness = [4, 9], maxAmount = 0, maxCoupons = 1`
- **Output:** `4`

The zero-price fruit can be purchased without spending the coupon, but the other fruit still costs 2 after discounting.
