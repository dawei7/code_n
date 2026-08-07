## Description

You are given an integer array `nums` of length `n`.

Construct a new array `ans` of length $2 * n$ such that the first `n` elements are the same as `nums`, and the next `n` elements are the elements of `nums` in reverse order.

Formally, for $0 \le i \le n - 1$:

- $\text{ans}[i] = \text{nums}[i]$

- $ans[i + n] = nums[n - i - 1]$

Return an integer array `ans`.
### Function Contract

**Inputs**

- `nums`: The integer array whose forward and reversed orders must be concatenated.

Let $n$ be `nums.length`.

**Return value**

Return a new array `ans` of length $2n$ satisfying

$$
\texttt{ans}[i] = \texttt{nums}[i]
\quad\text{and}\quad
\texttt{ans}[i+n] = \texttt{nums}[n-i-1]
$$

for every $0 \le i < n$.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3]

**Output:** [1,2,3,3,2,1]

**Explanation:**

The first `n` elements of `ans` are the same as `nums`.

For the next $n = 3$ elements, each element is taken from `nums` in reverse order:

- $\text{ans}[3] = \text{nums}[2] = 3$

- $\text{ans}[4] = \text{nums}[1] = 2$

- $\text{ans}[5] = \text{nums}[0] = 1$

Thus, $ans = [1, 2, 3, 3, 2, 1]$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1]

**Output:** [1,1]

**Explanation:**

The array remains the same when reversed. Thus, $ans = [1, 1]$.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$