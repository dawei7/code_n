## Description

You have an array `arr` of length `n` where $\text{arr}[i] = (2 * i) + 1$ for all valid values of `i` (i.e., $0 \le i < n$).

In one operation, you can select two indices `x` and `y` where $0 \le x, y < n$ and subtract `1` from $\text{arr}[x]$ and add `1` to $\text{arr}[y]$ (i.e., perform $\text{arr}[x] -=1$and $\text{arr}[y] += 1$). The goal is to make all the elements of the array **equal**. It is **guaranteed** that all the elements of the array can be made equal using some operations.

Given an integer `n`, the length of the array, return *the minimum number of operations* needed to make all the elements of arr equal.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $n = 3$
- **Output:** `2`
- **Explanation:** arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
#### Example 2

- **Input:** $n = 6$
- **Output:** `9`
### Constraints

- $1 \le n \le 10^{4}$