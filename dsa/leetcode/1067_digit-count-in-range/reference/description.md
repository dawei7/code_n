### 1. Description

Given a single-digit integer `d` and two integers `low` and `high`, return *the number of times that *`d`* occurs as a digit in all integers in the inclusive range *`[low, high]`.

### 2. Function Contract

**Inputs**

- `d`: the single decimal digit whose occurrences are counted.
- `low`: the inclusive lower bound of the positive-integer range.
- `high`: the inclusive upper bound of the positive-integer range.

Every integer in the closed interval from `low` through `high` is interpreted using its ordinary base-ten representation. Both endpoints contribute, repeated appearances within one representation contribute separately, and omitted leading zeros do not contribute.

**Return value**

- The total number of written occurrences of `d` across all integers in the inclusive range.

### 3. Examples

#### Example 1

- **Input:** $d = 1, low = 1, high = 13$
- **Output:** `6`
- **Explanation:** The digit d = 1 occurs 6 times in 1, 10, 11, 12, 13.
Note that the digit d = 1 occurs twice in the number 11.
#### Example 2

- **Input:** $d = 3, low = 100, high = 250$
- **Output:** `35`
- **Explanation:** The digit d = 3 occurs 35 times in 103,113,123,130,131,...,238,239,243.

### 4. Constraints

- $0 \le d \le 9$

- $1 \le low \le high \le 2 * 10^{8}$