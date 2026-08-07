## Description

You are given an integer array `nums` and an integer `k`.

Find the absolute difference between:

- the **sum** of the `k` **largest** elements in the array; and

- the **sum** of the `k` **smallest** elements in the array.

Return an integer denoting this difference.
### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `k`: The number of smallest and largest occurrences included in the two sums.

Let $N=\lvert\texttt{nums}\rvert$ and let $V=100$ be the size of the permitted value domain. The two groups are chosen independently and may overlap when $2 * k > n$.

**Return value**

Return $abs(\text{largest}_{sum} - \text{smallest}_{sum})$. When $k = n$, both groups contain the whole array and the result is zero.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [5,2,2,4], k = 2

**Output:** 5

**Explanation:**

- The $k = 2$ largest elements are 4 and 5. Their sum is $4 + 5 = 9$.

- The $k = 2$ smallest elements are 2 and 2. Their sum is $2 + 2 = 4$.

- The absolute difference is $abs(9 - 4) = 5$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [100], k = 1

**Output:** 0

**Explanation:**

- The largest element is 100.

- The smallest element is 100.

- The absolute difference is $abs(100 - 100) = 0$.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$

- $1 \le k \le n$