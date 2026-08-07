### 1. Description

You are given an integer array `nums`.

Consider all pairs of **distinct** values `x` and `y` from `nums` such that:

- `x < y`

- `x` and `y` have different frequencies in `nums`.

Among all such pairs:

- Choose the pair with the smallest possible value of `x`.

- If multiple pairs have the same `x`, choose the one with the smallest possible value of `y`.

Return an integer array `[x, y]`. If no valid pair exists, return `[-1, -1]`.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

For every value $v$ that occurs in `nums`, let $f(v)$ denote its frequency. A candidate pair must consist of two distinct present values and satisfy

$x < y \quad\text{and}\quad f(x) \ne f(y).$

Pairs are ordered lexicographically: a smaller `x` takes priority, and `y` breaks ties only when `x` is equal.

**Return value**

Return `[x, y]` for the lexicographically smallest valid pair. Return `[-1, -1]` when no valid pair exists.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,1,2,2,3,4]

**Output:** [1,3]

**Explanation:**

The smallest value is 1 with a frequency of 2, and the smallest value greater than 1 that has a different frequency from 1 is 3 with a frequency of 1. Thus, the answer is `[1, 3]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,5]

**Output:** [-1,-1]

**Explanation:**

Both values have the same frequency, so no valid pair exists. Return `[-1, -1]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [7]

**Output:** [-1,-1]

**Explanation:**

There is only one value in the array, so no valid pair exists. Return `[-1, -1]`.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$