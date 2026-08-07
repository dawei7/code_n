## Description

You are given an integer array `nums` and two integers `k` and `mul`.

Select **exactly** `k` elements from `nums`. Process these elements one by one in any order you choose.

For each selected element, **independently** choose one of the following:

- **Add** the element's value to the total sum, or

- **Multiply** the element by the **current** value of `mul` and **add** the result to the total sum.

After processing each selected element, `mul` **decreases** by 1, regardless of which option was chosen. The current value of `mul` may become 0 or negative.

Return an integer denoting the **maximum** possible total sum.
### Function Contract

`solve(nums, k, mul) -> int`

**Inputs**

- `nums`: A nonempty array of positive integers. Equal values at different indices are separate selectable elements.
- `k`: The exact number of array elements that must be selected and processed.
- `mul`: The multiplier available before the first selected element is processed; it decreases by one after every step.

**Output**

Return the maximum possible integer total after exactly `k` selected elements have been processed in a freely chosen order.

At each step, adding the original value and adding its product with the current multiplier are both permitted. No modulus is applied to the result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [6,1,2,9], k = 3, mul = 2

**Output:** 26

**Explanation:**

One optimal way:

- One optimal selection is $\text{nums}[3] = 9$, $\text{nums}[0] = 6$, and $\text{nums}[2] = 2$.

- Process $\text{nums}[3] = 9$ first: choose multiplication, so it contributes $9 * 2 = 18$. Now, `mul` becomes 1.

- Process $\text{nums}[0] = 6$ next: choose multiplication, so it contributes $6 * 1 = 6$. Now, `mul` becomes 0.

- Process $\text{nums}[2] = 2$ last: choose addition, so it contributes 2.

- The total sum is $18 + 6 + 2 = 26$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,7,5,2], k = 2, mul = 4

**Output:** 43

**Explanation:**

One optimal way:

- One optimal selection is $\text{nums}[1] = 7$ and $\text{nums}[2] = 5$.

- Process $\text{nums}[1] = 7$ first: choose multiplication, so it contributes $7 * 4 = 28$. Now, `mul` becomes 3.

- Process $\text{nums}[2] = 5$ next: choose multiplication, so it contributes $5 * 3 = 15$.

- The total sum is $28 + 15 = 43$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [4,4], k = 1, mul = 1

**Output:** 4

**Explanation:**

One optimal way:

- One optimal selection is $\text{nums}[0] = 4$.

- Process $\text{nums}[0] = 4$: choose multiplication, so it contributes $4 * 1 = 4$.

- The total sum is 4.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $1 \le k \le \text{nums.length}$

- $1 \le mul \le 10^{5}$