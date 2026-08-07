## Description

You are given a positive integer array `sides` of length 3.

Determine if there exists a triangle with **positive** area whose three side lengths are given by the elements of `sides`.

If such a triangle exists, return an array of three floating-point numbers representing its internal angles (in **degrees**), **sorted** in **non-decreasing** order. Otherwise, return an empty array.

Answers within $10^{-5}$ of the actual answer will be accepted.
### Function Contract

**Inputs**

- `sides`: An integer array containing exactly three positive side lengths.

The order of the three values carries no geometric meaning. A triangle has positive area precisely when its longest side is strictly shorter than the sum of the other two sides.

**Return value**

Return the three internal angles in degrees, sorted in non-decreasing order, when the side lengths form a positive-area triangle. Otherwise return `[]`.

### Examples
#### Example 1

<div class="example-block">
**Input:** sides = [3,4,5]

**Output:** [36.86990,53.13010,90.00000]

**Explanation:**

You can form a right-angled triangle with side lengths 3, 4, and 5. The internal angles of this triangle are approximately 36.869897646, 53.130102354, and 90 degrees respectively.

</div>
#### Example 2

<div class="example-block">
**Input:** sides = [2,4,2]

**Output:** []

**Explanation:**

You cannot form a triangle with positive area using side lengths 2, 4, and 2.

</div>
### Constraints

- $\text{sides.length} = 3$

- $1 \le \text{sides}[i] \le 1000$