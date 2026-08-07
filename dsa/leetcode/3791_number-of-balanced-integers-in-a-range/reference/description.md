## Description

You are given two integers `low` and `high`.

An integer is called **balanced** if it satisfies **both** of the following conditions:

- It contains **at least** two digits.

- The **sum of digits at even positions** is equal to the **sum of digits at odd positions** (the leftmost digit has position 1).

Return an integer representing the number of balanced integers in the range `[low, high]` (both inclusive).
### Function Contract

**Inputs**

- `low`: The inclusive lower endpoint of the range.
- `high`: The inclusive upper endpoint, with `high >= low`.

Position parity is determined from the actual leftmost digit of each integer; leading zeros are not part of its representation. One-digit values never qualify.

**Return value**

Return the count of integers `x` satisfying `low <= x <= high`, having at least two digits, and having equal odd-position and even-position digit sums.

### Examples
#### Example 1

<div class="example-block">
**Input:** low = 1, high = 100

**Output:** 9

**Explanation:**

The 9 balanced numbers between 1 and 100 are 11, 22, 33, 44, 55, 66, 77, 88, and 99.

</div>
#### Example 2

<div class="example-block">
**Input:** low = 120, high = 129

**Output:** 1

**Explanation:**

Only 121 is balanced because the sum of digits at even and odd positions are both 2.

</div>
#### Example 3

<div class="example-block">
**Input:** low = 1234, high = 1234

**Output:** 0

**Explanation:**

1234 is not balanced because the sum of digits at odd positions $(1 + 3 = 4)$ does not equal the sum at even positions $(2 + 4 = 6)$.

</div>
### Constraints

- $1 \le low \le high \le 10^{15}$