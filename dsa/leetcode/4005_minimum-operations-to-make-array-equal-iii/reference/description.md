### 1. Description

You are given an integer array `nums`.

In one operation, you may choose **any** element $\text{nums}[i]$ and perform one of the following:

- **Multiply** $\text{nums}[i]$ by an integer `k`, where $k \ge 2$.

- **Divide** $\text{nums}[i]$ by an integer `k`, where $2 \le k < \text{nums}[i]$, provided that $\text{nums}[i]$ is divisible by `k`.

Return the **minimum** number of operations required to make all elements of `nums` **equal**.

### 2. Function Contract

**Inputs**

- `nums`: An array of $n$ positive integers.

Each operation changes exactly one array entry. Multiplication must use an integer factor of at least $2$. Division must be exact, and its factor must be at least $2$ but strictly smaller than the entry's current value.

For the Required Complexity bound, let $U$ be the number of distinct entries, let $V=\max(\texttt{nums})$, let $D$ be the total number of divisors generated across those distinct values, and let $P=\sqrt V\log\log V$ denote the prime-sieve work.

**Return value**

Return the minimum number of permitted multiplication and division operations required to make all entries equal.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [6,12,8]

**Output:** 3

**Explanation:**

We can perform following operates to make all numbers to 6:

- Divide $\text{nums}[1] = 12$ by 2 to get 6.

- Divide $\text{nums}[2] = 8$ by 4 to get 2.

- Multiply $\text{nums}[2] = 2$ by 3 to get 6.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,15,20]

**Output:** 2

**Explanation:**

We can perform following operates to make all numbers to 5:

- Divide $\text{nums}[1] = 15$ by 3 to get 5.

- Divide $\text{nums}[2] = 20$ by 4 to get 5.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [7,7,7]

**Output:** 0

**Explanation:**

All elements are already equal, so no operations are needed.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^​​​​​​​9$