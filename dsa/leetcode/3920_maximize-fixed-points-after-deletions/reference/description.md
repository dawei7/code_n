## Description

You are given an integer array `nums`.

A position `i` is called a **fixed point** if $\text{nums}[i] = i$.

You are allowed to delete **any** number of elements (including zero) from the array. After each deletion, the remaining elements **shift left**, and indices are reassigned starting from 0.

Return an integer denoting the **maximum** number of fixed points that can be achieved after performing any number of deletions.
### Function Contract

**Inputs**

- `nums`: A list of non-negative integers. Deletions preserve the relative order of every retained element.

Let $n=\lvert\texttt{nums}\rvert$. An element originally at index $i$ can become a fixed point only if enough earlier elements can be deleted to move it to index `nums[i]`.

**Return value**

Return the largest possible number of indices `i` satisfying `nums[i] == i` in the array remaining after any number of deletions. Return `0` if no retained element can be made a fixed point.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [0,2,1]

**Output:** 2

**Explanation:**

- Delete $\text{nums}[1] = 2$. The array becomes `[0, 1]`.

- Now, $\text{nums}[0] = 0$ and $\text{nums}[1] = 1$, so both indices are fixed points.

- Thus, the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,1,2]

**Output:** 2

**Explanation:**

- Do not delete any elements. The array remains `[3, 1, 2]`.

- Here, $\text{nums}[1] = 1$ and $\text{nums}[2] = 2$, so these indices are fixed points.

- Thus, the answer is 2.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,0,1,2]

**Output:** 3

**Explanation:**

- Delete $\text{nums}[0] = 1$. The array becomes `[0, 1, 2]`.

- Now, $\text{nums}[0] = 0$, $\text{nums}[1] = 1$, and $\text{nums}[2] = 2$, so all indices are fixed points.

- Thus, the answer is 3.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{5}$