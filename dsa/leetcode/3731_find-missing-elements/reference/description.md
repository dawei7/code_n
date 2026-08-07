## Description

You are given an integer array `nums` consisting of **unique** integers.

Originally, `nums` contained **every integer** within a certain range. However, some integers might have gone **missing** from the array.

The **smallest** and **largest** integers of the original range are still present in `nums`.

Return a **sorted** list of all the missing integers in this range. If no integers are missing, return an **empty** list.
### Function Contract

**Inputs**

- `nums`: An array of distinct integers containing both endpoints of the original consecutive range.

The input order is arbitrary. Let $L=\min(\texttt{nums})$ and $H=\max(\texttt{nums})$; only absent integers in the inclusive range $[L,H]$ belong in the result.

**Return value**

Return a list containing each integer in $[L,H]$ that does not occur in `nums`, ordered from smallest to largest.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,4,2,5]

**Output:** [3]

**Explanation:**

The smallest integer is 1 and the largest is 5, so the full range should be `[1,2,3,4,5]`. Among these, only 3 is missing.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [7,8,6,9]

**Output:** []

**Explanation:**

The smallest integer is 6 and the largest is 9, so the full range is `[6,7,8,9]`. All integers are already present, so no integer is missing.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [5,1]

**Output:** [2,3,4]

**Explanation:**

The smallest integer is 1 and the largest is 5, so the full range should be `[1,2,3,4,5]`. The missing integers are 2, 3, and 4.

</div>
### Constraints

- $2 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$