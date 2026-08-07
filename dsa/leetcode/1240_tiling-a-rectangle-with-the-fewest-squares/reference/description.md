## Description

Given a rectangle of size `n` x `m`, return *the minimum number of integer-sided squares that tile the rectangle*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

![](images/sample_11_1592.png)

- **Input:** $n = 2, m = 3$
- **Output:** `3`
- **Explanation:** 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)
#### Example 2

![](images/sample_22_1592.png)

- **Input:** $n = 5, m = 8$
- **Output:** `5`
#### Example 3

![](images/sample_33_1592.png)

- **Input:** $n = 11, m = 13$
- **Output:** `6`
### Constraints

- $1 \le n, m \le 13$