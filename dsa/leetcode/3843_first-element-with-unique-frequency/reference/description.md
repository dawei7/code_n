## Description

You are given an integer array `nums`.

Return an integer denoting the **first** element (scanning from left to right) in `nums` whose **frequency** is **unique**. That is, no other integer appears the same number of times in `nums`. If there is no such element, return -1.
### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers, kept in its original order.

For each distinct value $x$ in `nums`, define its frequency as

$F(x)=\left\lvert\left\{i\mid\texttt{nums}[i]=x\right\}\right\rvert.$

Also let $M(f)$ be the number of distinct values whose frequency equals $f$. Thus, the frequency of $x$ is unique exactly when $M(F(x))=1$.

**Return value**

Return $\text{nums}[i]$ for the smallest index $i$ satisfying $M(F(\texttt{nums}[i]))=1$. Return `-1` if no index satisfies that condition.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [20,10,30,30]

**Output:** 30

**Explanation:**

- 20 appears once.

- 10 appears once.

- 30 appears twice.

- The frequency of 30 is unique because no other integer appears exactly twice.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [20,20,10,30,30,30]

**Output:** 20

**Explanation:**

- 20 appears twice.

- 10 appears once.

- 30 appears 3 times.

- The frequency of 20, 10, and 30 are unique. The first element that has unique frequency is 20.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [10,10,20,20]

**Output:** -1

**Explanation:**

- 10 appears twice.

- 20 appears twice.

- No element has a unique frequency.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$