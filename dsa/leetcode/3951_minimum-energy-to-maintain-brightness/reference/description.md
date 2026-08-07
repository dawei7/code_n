## Description

You are given an integer `n`, representing `n` light bulbs arranged in a line and indexed from 0 to $n - 1$.

You are also given an integer `brightness` and a 2D integer array `intervals`, where $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$ represents an **inclusive** time interval during which the lighting requirement **must** be satisfied.

At each time unit, every bulb can independently be either on or off. A bulb that is on **illuminates** its own position and its **adjacent** positions, if they exist.

The **total illumination** at a time unit is the number of **illuminated** positions. Each position is counted **at most once**.

For every integer time unit covered by **at least** one interval in `intervals`, the **total illumination** must be **at least** `brightness`. At time units not covered by any interval, all bulbs may remain off. Each bulb that is on consumes 1 unit of energy for that time unit.

Return an integer denoting the **minimum** total energy required.
### Function Contract

**Inputs**

- `n`: The number of bulb positions in the line.
- `brightness`: The minimum number of distinct positions that must be illuminated at every active time.
- `intervals`: Inclusive integer-time intervals `[start, end]` during which the requirement applies.

Let $m$ be the number of intervals.

**Return value**

Return the minimum sum of on-bulb time units needed over the union of all intervals.

### Examples

#### Example 1

<div class="example-block">
**Input:** n = 5, brightness = 5, intervals = [[6,12]]

**Output:** 14

**Explanation:**

- Turn on the light bulbs at positions 1 and 4.

- Current state of line: `0 1 0 0 1`.

- All 5 positions are illuminated, so the required brightness is reached.

- The active interval has length $12 - 6 + 1 = 7$, so the total energy is $2 * 7 = 14$.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 2, brightness = 1, intervals = [[0,0],[2,2]]

**Output:** 2

**Explanation:**

- Turn on one light bulb during each active interval.

- Each interval has length 1, so the total active time is $1 + 1 = 2$.

- The total energy is $1 * 2 = 2$.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 4, brightness = 2, intervals = [[1,3],[2,4]]

**Output:** 4

**Explanation:**

- Turn on one light bulb. It can illuminate at least 2 positions.

- The active intervals overlap, so the total active time is the length of `[1,4]`, which is 4.

- The total energy is $1 * 4 = 4$.

</div>
### Constraints

- $1 \le n \le 10^{6}$

- $1 \le brightness \le n$

- $1 \le \text{intervals.length} \le 10^{5}$

- $\text{intervals}[i] = [\text{start}_{i}, \text{end}_{i}]$

- $0 \le \text{start}_{i} \le \text{end}_{i} \le 10^{9}$