## Description

You are given a **bitonic** array `nums` of length `n`.

Split the array into **two** parts:

- **Ascending part**: from index 0 to the peak element (inclusive).

- **Descending part**: from the peak element to index $n - 1$ (inclusive).

The peak element belongs to both parts.

Return:

- 0 if the sum of the **ascending** part is greater.

- 1 if the sum of the **descending** part is greater.

- -1 if both sums are **equal**.

**Notes**:

- A **bitonic** array is an array that is **strictly increasing** up to a **single peak** element and then **strictly decreasing**.

- An array is said to be **strictly increasing** if each element is **strictly greater** than its **previous** one (if exists).

- An array is said to be **strictly decreasing** if each element is **strictly smaller** than its **previous** one (if exists).
### Function Contract

**Inputs**

- `nums`: A bitonic integer array that is strictly increasing up to one peak and strictly decreasing after it.

Let $p$ be the unique peak index. Strict increase means `nums[i] < nums[i + 1]` for every $0\le i<p$, while strict decrease means `nums[i] > nums[i + 1]` for every $p\le i<n-1$. Define the two inclusive sums as

$$
A=\sum_{i=0}^{p}\texttt{nums[i]}
\qquad\text{and}\qquad
B=\sum_{i=p}^{n-1}\texttt{nums[i]}.
$$

The peak value `nums[p]` appears once in each sum.

**Return value**

Return `0` if $A>B$, return `1` if $B>A$, and return `-1` if $A=B$.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,3,2,1]

**Output:** 1

**Explanation:**

- Peak element is $\text{nums}[1] = 3$

- Ascending part = `[1, 3]`, sum is $1 + 3 = 4$

- Descending part = `[3, 2, 1]`, sum is $3 + 2 + 1 = 6$

- Since the descending part has a larger sum, return 1.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,4,5,2]

**Output:** 0

**Explanation:**

- Peak element is $\text{nums}[2] = 5$

- Ascending part = `[2, 4, 5]`, sum is $2 + 4 + 5 = 11$

- Descending part = `[5, 2]`, sum is $5 + 2 = 7$

- Since the ascending part has a larger sum, return 0.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,4,3]

**Output:** -1

**Explanation:**

- Peak element is $\text{nums}[2] = 4$

- Ascending part = `[1, 2, 4]`, sum is $1 + 2 + 4 = 7$

- Descending part = `[4, 3]`, sum is $4 + 3 = 7$

- Since both parts have equal sums, return -1.

</div>
### Constraints

- $3 \le n = \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- `nums` is a bitonic array.