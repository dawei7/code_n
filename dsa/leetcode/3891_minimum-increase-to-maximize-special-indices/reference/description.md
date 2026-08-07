## Description

You are given an integer array `nums` of length `n`.

An index `i` ($0 < i < n - 1$) is **special** if $\text{nums}[i] > nums[i - 1]$ and $\text{nums}[i] > nums[i + 1]$.

You may perform operations where you choose **any** index `i` and **increase** $\text{nums}[i]$ by 1.

Your goal is to:

- **Maximize** the number of **special** indices.

- **Minimize** the total number of **operations** required to achieve that **maximum**.

Return an integer denoting the **minimum** total number of operations required.
### Function Contract

**Inputs**

- `nums`: An integer array of length $n$.

An operation may increase any one element by exactly $1$. Elements cannot be decreased. The two endpoints can never be special, although their values affect whether the adjacent interior indices are special.

**Return value**

Return the minimum total number of unit increases needed to attain the greatest possible number of special indices.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,2]

**Output:** 1

**Explanation:**​​​​​​​

- Start with `nums = [1, 2, 2]`.

- Increase $\text{nums}[1]$ by 1, array becomes `[1, 3, 2]`.

- The final array is `[1, 3, 2]` has 1 special index, which is the maximum achievable.

- It is impossible to achieve this number of special indices with fewer operations. Thus, the answer is 1.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,1,1,3]

**Output:** 2

**Explanation:**​​​​​​​

- Start with `nums = [2, 1, 1, 3]`.

- Perform 2 operations at index 1, array becomes `[2, 3, 1, 3]`.

- The final array is `[2, 3, 1, 3]` has 1 special index, which is the maximum achievable. Thus, the answer is 2.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [5,2,1,4,3]

**Output:** 4

**Explanation:**​​​​​​​​​​​​​​​​​​​​​

- Start with `nums = [5, 2, 1, 4, 3]`.

- Perform 4 operations at index 1, array becomes `[5, 6, 1, 4, 3]`.

- The final array is `[5, 6, 1, 4, 3]` has 2 special indices, which is the maximum achievable. Thus, the answer is 4.​​​​​​​

</div>
### Constraints

- $3 \le n \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$