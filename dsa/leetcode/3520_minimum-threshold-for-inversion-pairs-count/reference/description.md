## Description

You are given an array of integers `nums` and an integer `k`.

An inversion pair with a **threshold** `x` is defined as a pair of indices `(i, j)` such that:

- `i < j`

- $\text{nums}[i] > \text{nums}[j]$

- The difference between the two numbers is **at most** `x` (i.e. $\text{nums}[i] - \text{nums}[j] \le x$).

Your task is to determine the **minimum** integer $\text{min}_{threshold}$ such that there are **at least** `k` inversion pairs with threshold $\text{min}_{threshold}$.

If no such integer exists, return `-1`.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3,4,3,2,1], k = 7

**Output:** 2

**Explanation:**

For threshold $x = 2$, the pairs are:

- `(3, 4)` where $\text{nums}[3] = 4$ and $\text{nums}[4] = 3$.

- `(2, 5)` where $\text{nums}[2] = 3$ and $\text{nums}[5] = 2$.

- `(3, 5)` where $\text{nums}[3] = 4$ and $\text{nums}[5] = 2$.

- `(4, 5)` where $\text{nums}[4] = 3$ and $\text{nums}[5] = 2$.

- `(1, 6)` where $\text{nums}[1] = 2$ and $\text{nums}[6] = 1$.

- `(2, 6)` where $\text{nums}[2] = 3$ and $\text{nums}[6] = 1$.

- `(4, 6)` where $\text{nums}[4] = 3$ and $\text{nums}[6] = 1$.

- `(5, 6)` where $\text{nums}[5] = 2$ and $\text{nums}[6] = 1$.

There are less than `k` inversion pairs if we choose any integer less than 2 as threshold.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [10,9,9,9,1], k = 4

**Output:** 8

**Explanation:**

For threshold $x = 8$, the pairs are:

- `(0, 1)` where $\text{nums}[0] = 10$ and $\text{nums}[1] = 9$.

- `(0, 2)` where $\text{nums}[0] = 10$ and $\text{nums}[2] = 9$.

- `(0, 3)` where $\text{nums}[0] = 10$ and $\text{nums}[3] = 9$.

- `(1, 4)` where $\text{nums}[1] = 9$ and $\text{nums}[4] = 1$.

- `(2, 4)` where $\text{nums}[2] = 9$ and $\text{nums}[4] = 1$.

- `(3, 4)` where $\text{nums}[3] = 9$ and $\text{nums}[4] = 1$.

There are less than `k` inversion pairs if we choose any integer less than 8 as threshold.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le k \le 10^{9}$