## Description

You are given an integer array `nums` of length `n` and an integer array `queries`.

Let `gcdPairs` denote an array obtained by calculating the GCD of all possible pairs $(\text{nums}[i], \text{nums}[j])$, where $0 \le i < j < n$, and then sorting these values in **ascending** order.

For each query $\text{queries}[i]$, you need to find the element at index $\text{queries}[i]$ in `gcdPairs`.

Return an integer array `answer`, where $\text{answer}[i]$ is the value at $gcdPairs[\text{queries}[i]]$ for each query.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [2,3,4], queries = [0,2,2]

**Output:** [1,2,2]

**Explanation:**

$gcdPairs = [gcd(\text{nums}[0], \text{nums}[1]), gcd(\text{nums}[0], \text{nums}[2]), gcd(\text{nums}[1], \text{nums}[2])] = [1, 2, 1]$.

After sorting in ascending order, $gcdPairs = [1, 1, 2]$.

So, the answer is `[gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,4,2,1], queries = [5,3,1,0]

**Output:** [4,2,1,1]

**Explanation:**

`gcdPairs` sorted in ascending order is `[1, 1, 1, 2, 2, 4]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [2,2], queries = [0,0]

**Output:** [2,2]

**Explanation:**

$gcdPairs = [2]$.

</div>
### Constraints

- $2 \le n = \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 5 * 10^{4}$

- $1 \le \text{queries.length} \le 10^{5}$

- $0 \le \text{queries}[i] < n * (n - 1) / 2$