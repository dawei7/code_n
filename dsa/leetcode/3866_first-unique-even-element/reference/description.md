### 1. Description

You are given an integer array `nums`.

Return an integer denoting the first **even** integer (earliest by array index) that appears **exactly** once in `nums`. If no such integer exists, return -1.

An integer `x` is considered **even** if it is divisible by 2.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

Let $N=\lvert\texttt{nums}\rvert$. Uniqueness is determined from each value's frequency in the entire array, while priority is determined by the original index. The requested result is therefore the first array element `x` for which $x \bmod 2 = 0$ and the total count of `x` is one.

**Return value**

Return the earliest-by-index even integer that appears exactly once. Return `-1` when no such integer exists.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [3,4,2,5,4,6]

**Output:** 2

**Explanation:**

Both 2 and 6 are even and they appear exactly once. Since 2 occurs first in the array, the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,4]

**Output:** -1

**Explanation:**

No even integer appears exactly once, so return -1.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$