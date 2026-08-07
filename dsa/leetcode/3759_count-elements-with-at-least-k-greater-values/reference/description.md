## Description

You are given an integer array `nums` of length `n` and an integer `k`.

An element in `nums` is said to be **qualified** if there exist **at least** `k` elements in the array that are **strictly greater** than it.

Return an integer denoting the total number of qualified elements in `nums`.
### Function Contract

**Inputs**

- `nums`: A nonempty integer array whose occurrences are tested independently.
- `k`: The minimum number of strictly greater array elements required for qualification.

Let $n=\lvert\texttt{nums}\rvert$. Comparisons are against every element of the same array; equality never contributes to the strictly-greater count.

**Return value**

Return the number of occurrences in `nums` for which at least `k` other array values are strictly greater.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [3,1,2], k = 1

**Output:** 2

**Explanation:**

The elements 1 and 2 each have at least $k = 1$ element greater than themselves.

​​​​​​​No element is greater than 3. Therefore, the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,5,5], k = 2

**Output:** 0

**Explanation:**

Since all elements are equal to 5, no element is greater than the other. Therefore, the answer is 0.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $0 \le k < n$