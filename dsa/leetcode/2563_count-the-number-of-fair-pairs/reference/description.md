## Description

Given a **0-indexed** integer array `nums` of size `n` and two integers `lower` and `upper`, return *the number of fair pairs*.

A pair `(i, j)` is **fair **if:

- $0 \le i < j < n$, and

- $lower \le \text{nums}[i] + \text{nums}[j] \le upper$
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [0,1,7,4,4,5], lower = 3, upper = 6`
- **Output:** `6`
- **Explanation:** There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
#### Example 2

- **Input:** `nums = [1,7,9,2,5], lower = 11, upper = 11`
- **Output:** `1`
- **Explanation:** There is a single fair pair: (2,3).
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $\text{nums.length} = n$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$

- $-10^{9} \le lower \le upper \le 10^{9}$