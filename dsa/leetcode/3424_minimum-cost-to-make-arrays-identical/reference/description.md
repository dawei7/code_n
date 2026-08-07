## Description

You are given two integer arrays `arr` and `brr` of length `n`, and an integer `k`. You can perform the following operations on `arr` *any* number of times:

- Split `arr` into *any* number of **contiguous** subarrays and rearrange these subarrays in *any order*. This operation has a fixed cost of `k`.

- Choose any element in `arr` and add or subtract a positive integer `x` to it. The cost of this operation is `x`.

Return the **minimum **total cost to make `arr` **equal** to `brr`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** arr = [-7,9,5], brr = [7,-2,-5], k = 2

**Output:** 13

**Explanation:**

- Split `arr` into two contiguous subarrays: `[-7]` and `[9, 5]` and rearrange them as `[9, 5, -7]`, with a cost of 2.

- Subtract 2 from element $\text{arr}[0]$. The array becomes `[7, 5, -7]`. The cost of this operation is 2.

- Subtract 7 from element $\text{arr}[1]$. The array becomes `[7, -2, -7]`. The cost of this operation is 7.

- Add 2 to element $\text{arr}[2]$. The array becomes `[7, -2, -5]`. The cost of this operation is 2.

The total cost to make the arrays equal is $2 + 2 + 7 + 2 = 13$.

</div>
#### Example 2

<div class="example-block">
**Input:** arr = [2,1], brr = [2,1], k = 0

**Output:** 0

**Explanation:**

Since the arrays are already equal, no operations are needed, and the total cost is 0.

</div>
### Constraints

- $1 \le \text{arr.length} = \text{brr.length} \le 10^{5}$

- $0 \le k \le 2 * 10^{10}$

- $-10^{5} \le \text{arr}[i] \le 10^{5}$

- $-10^{5} \le \text{brr}[i] \le 10^{5}$