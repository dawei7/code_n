## Description

You are given an integer array `nums`.

An element $\text{nums}[i]$ is considered **valid** if it satisfies **at least** one of the following conditions:

- It is **strictly greater** than every element to its left.

- It is **strictly greater** than every element to its right.

The first and last elements are always valid.

Return an array of all valid elements in the same order as they appear in `nums`.
### Function Contract

**Inputs**

- `nums`: The non-empty integer array whose elements are tested against all values on either side.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

Return all values whose positions satisfy at least one strict side-maximum condition, in their original order. If $n=1$, return the single input value once.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,4,2,3,2]

**Output:** [1,2,4,3,2]

**Explanation:**

- $\text{nums}[0]$ and $\text{nums}[5]$ are always valid.

- $\text{nums}[1]$ and $\text{nums}[2]$ are strictly greater than every element to their left.

- $\text{nums}[4]$ is strictly greater than every element to its right.

- Thus, the answer is `[1, 2, 4, 3, 2]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,5,5,5]

**Output:** [5,5]

**Explanation:**

- The first and last elements are always valid.

- No other elements are strictly greater than all elements to their left or to their right.

- Thus, the answer is `[5, 5]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1]

**Output:** [1]

**Explanation:**

Since there is only one element, it is always valid. Thus, the answer is `[1]`.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$