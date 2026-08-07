## Description

Given an array of `prices` `[p_1,p_2...,p_n]` and a `target`, round each price `p_i` to `Round_i(p_i)` so that the rounded array `[Round_1(p_1),Round_2(p_2)...,Round_n(p_n)]` sums to the given `target`. Each operation `Round_i(p_i)` could be either `Floor(p_i)` or `Ceil(p_i)`.

Return the string `"-1"` if the rounded array is impossible to sum to `target`. Otherwise, return the smallest rounding error, which is defined as `Σ |Round_i(p_i) - (p_i)|` for <italic>`i`</italic> from `1` to <italic>`n`</italic>, as a string with three places after the decimal.

**Example 1:**

```
**Input:** prices = ["0.700","2.800","4.900"], target = 8
**Output:** "1.000"
**Explanation:**
Use Floor, Ceil and Ceil operations to get (0.7 - 0) + (3 - 2.8) + (5 - 4.9) = 0.7 + 0.2 + 0.1 = 1.0 .
```

**Example 2:**

```
**Input:** prices = ["1.500","2.500","3.500"], target = 10
**Output:** "-1"
**Explanation:** It is impossible to meet the target.
```

**Example 3:**

```
**Input:** prices = ["1.500","2.500","3.500"], target = 9
**Output:** "1.500"
```

**Constraints:**

	- `1 <= prices.length <= 500`

	- Each string `prices[i]` represents a real number in the range `[0.0, 1000.0]` and has exactly 3 decimal places.

	- `0 <= target <= 10^6`
