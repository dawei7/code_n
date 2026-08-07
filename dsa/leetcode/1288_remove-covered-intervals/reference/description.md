## Description

Given an array `intervals` where $\text{intervals}[i] = [l_{i}, r_{i}]$ represent the interval $[l_{i}, r_{i})$, remove all intervals that are covered by another interval in the list.

The interval `[a, b)` is covered by the interval `[c, d)` if and only if $c \le a$ and $b \le d$.

Return *the number of remaining intervals*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $intervals = [[1,4],[3,6],[2,8]]$
- **Output:** `2`
- **Explanation:** Interval [3,6] is covered by [2,8], therefore it is removed.
#### Example 2

- **Input:** $intervals = [[1,4],[2,3]]$
- **Output:** `1`
### Constraints

- $1 \le \text{intervals.length} \le 1000$

- $\text{intervals}[i].length = 2$

- $0 \le l_{i} < r_{i} \le 10^{5}$

- All the given intervals are **unique**.