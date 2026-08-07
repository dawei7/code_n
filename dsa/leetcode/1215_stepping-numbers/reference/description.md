## Description

A **stepping number** is an integer such that all of its adjacent digits have an absolute difference of exactly `1`.

- For example, `321` is a **stepping number** while `421` is not.

Given two integers `low` and `high`, return *a sorted list of all the **stepping numbers** in the inclusive range* `[low, high]`.
### Function Contract

**Inputs**

- `low`: The inclusive lower bound.
- `high`: The inclusive upper bound.

The bounds are nonnegative and satisfy $low \le high$. Let $S$ be the number of stepping numbers from $0$ through `high`, inclusive.

**Return value**

Return all stepping numbers from `low` through `high`, including qualifying endpoints, in increasing order.

### Examples

#### Example 1

- **Input:** $low = 0, high = 21$
- **Output:** `[0,1,2,3,4,5,6,7,8,9,10,12,21]`
#### Example 2

- **Input:** $low = 10, high = 15$
- **Output:** `[10,12]`
### Constraints

- $0 \le low \le high \le 2 * 10^{9}$