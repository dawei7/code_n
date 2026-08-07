### 1. Description

You are given an integer array `nums` consisting only of 0, 1, and 2.

A pair of indices `(i, j)` is called **valid** if $\text{nums}[i] = 1$ and $\text{nums}[j] = 2$.

Return the **minimum** absolute difference between `i` and `j` among all valid pairs. If no valid pair exists, return -1.

The absolute difference between indices `i` and `j` is defined as $abs(i - j)$.

### 2. Function Contract

**Inputs**

- `nums`: An array containing only the integers `0`, `1`, and `2`.

Let $n=\lvert\texttt{nums}\rvert$. Indices are zero-based. A valid pair is ordered by value—its first component indexes a `1` and its second indexes a `2`—but its distance is symmetric.

**Return value**

Return $\min \lvert i-j\rvert$ over all indices satisfying $\text{nums}[i] = 1$ and $\text{nums}[j] = 2$. Return `-1` when that set of pairs is empty.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,0,0,2,0,1]

**Output:** 2

**Explanation:**

The valid pairs are:

- (0, 3) which has absolute difference of $abs(0 - 3) = 3$.

- (5, 3) which has absolute difference of $abs(5 - 3) = 2$.

Thus, the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,0,1,0]

**Output:** -1

**Explanation:**

There are no valid pairs in the array, thus the answer is -1.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $0 \le \text{nums}[i] \le 2$