## Description

You are given an integer array `nums`.

You want to maximize the **alternating sum** of `nums`, which is defined as the value obtained by **adding** elements at even indices and **subtracting** elements at odd indices. That is, $\text{nums}[0] - \text{nums}[1] + \text{nums}[2] - \text{nums}[3]...$

You are also given a 2D integer array `swaps` where $\text{swaps}[i] = [p_{i}, q_{i}]$. For each pair $[p_{i}, q_{i}]$ in `swaps`, you are allowed to swap the elements at indices $p_{i}$ and $q_{i}$. These swaps can be performed any number of times and in any order.

Return the maximum possible **alternating sum** of `nums`.
### Function Contract

**Inputs**

- `nums`: The positive integer values whose positions determine their plus or minus signs.
- `swaps`: Distinct index pairs $[p_{i}, q_{i}]$ that may be applied any number of times and in any order.

An index is positive in the alternating sum exactly when it is even. Values can move through a sequence of allowed pairs; they are not restricted to one direct listed swap.

**Return value**

Return the greatest alternating sum obtainable after any valid sequence of swaps, including the empty sequence.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3], swaps = [[0,2],[1,2]]

**Output:** 4

**Explanation:**

The maximum alternating sum is achieved when `nums` is `[2, 1, 3]` or `[3, 1, 2]`. As an example, you can obtain `nums = [2, 1, 3]` as follows.

- Swap $\text{nums}[0]$ and $\text{nums}[2]$. `nums` is now `[3, 2, 1]`.

- Swap $\text{nums}[1]$ and $\text{nums}[2]$. `nums` is now `[3, 1, 2]`.

- Swap $\text{nums}[0]$ and $\text{nums}[2]$. `nums` is now `[2, 1, 3]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3], swaps = [[1,2]]

**Output:** 2

**Explanation:**

The maximum alternating sum is achieved by not performing any swaps.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,1000000000,1,1000000000,1,1000000000], swaps = []

**Output:** -2999999997

**Explanation:**

Since we cannot perform any swaps, the maximum alternating sum is achieved by not performing any swaps.

</div>
### Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $0 \le \text{swaps.length} \le 10^{5}$

- $\text{swaps}[i] = [p_{i}, q_{i}]$

- $0 \le p_{i} < q_{i} \le \text{nums.length} - 1$

- $[p_{i}, q_{i}] \neq [p_{j}, q_{j}]$