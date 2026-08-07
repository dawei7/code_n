## Description

Given an array of integers `arr`, and three integers `a`, `b` and `c`. You need to find the number of good triplets.

A triplet $(\text{arr}[i], \text{arr}[j], \text{arr}[k])$ is **good** if the following conditions are true:

- $0 \le i < j < k < \text{arr.length}$

- $|\text{arr}[i] - \text{arr}[j]| \le a$

- $|\text{arr}[j] - \text{arr}[k]| \le b$

- $|\text{arr}[i] - \text{arr}[k]| \le c$

Where `|x|` denotes the absolute value of `x`.

Return* the number of good triplets*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3`
- **Output:** `4`
- **Explanation:** There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
#### Example 2

- **Input:** `arr = [1,1,2,2,3], a = 0, b = 0, c = 1`
- **Output:** `0`
- **Explanation:** No triplet satisfies all conditions.
### Constraints

- $3 \le \text{arr.length} \le 100$

- $0 \le \text{arr}[i] \le 1000$

- $0 \le a, b, c \le 1000$