## Description

There are an infinite amount of bags on a number line, one bag for each coordinate. Some of these bags contain coins.

You are given a 2D array `coins`, where $\text{coins}[i] = [l_{i}, r_{i}, c_{i}]$ denotes that every bag from $l_{i}$ to $r_{i}$ contains $c_{i}$ coins.

The segments that `coins` contain are non-overlapping.

You are also given an integer `k`.

Return the **maximum** amount of coins you can obtain by collecting `k` consecutive bags.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4

**Output:** 10

**Explanation:**

Selecting bags at positions `[3, 4, 5, 6]` gives the maximum number of coins: $2 + 0 + 4 + 4 = 10$.

</div>
#### Example 2

<div class="example-block">
**Input:** coins = [[1,10,3]], k = 2

**Output:** 6

**Explanation:**

Selecting bags at positions `[1, 2]` gives the maximum number of coins: $3 + 3 = 6$.

</div>
### Constraints

- $1 \le \text{coins.length} \le 10^{5}$

- $1 \le k \le 10^{9}$

- $\text{coins}[i] = [l_{i}, r_{i}, c_{i}]$

- $1 \le l_{i} \le r_{i} \le 10^{9}$

- $1 \le c_{i} \le 1000$

- The given segments are non-overlapping.