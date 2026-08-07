## Description

You are given an integer array `nums`.

In one move, you may **increase** the value of any single element $\text{nums}[i]$ by 1.

Return the **minimum total** number of **moves** required so that all elements in `nums` become **equal**.
### Function Contract

**Inputs**

- `nums`: An array of `n` positive integers.

Only increases are allowed: a move changes one selected value from `nums[i]` to `nums[i] + 1`. Different elements may receive different numbers of moves.

**Return value**

Return the minimum total number of single-element increments after which all array values are equal.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [2,1,3]

**Output:** 3

**Explanation:**

To make all elements equal:

- Increase $\text{nums}[0] = 2$ by 1 to make it 3.

- Increase $\text{nums}[1] = 1$ by 1 to make it 2.

- Increase $\text{nums}[1] = 2$ by 1 to make it 3.

Now, all elements of `nums` are equal to 3. The minimum total moves is `3`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,4,5]

**Output:** 2

**Explanation:**

To make all elements equal:

- Increase $\text{nums}[0] = 4$ by 1 to make it 5.

- Increase $\text{nums}[1] = 4$ by 1 to make it 5.

Now, all elements of `nums` are equal to 5. The minimum total moves is `2`.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$