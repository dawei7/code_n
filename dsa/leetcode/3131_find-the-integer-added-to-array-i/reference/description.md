### 1. Description

You are given two arrays of equal length, `nums1` and `nums2`.

Each element in `nums1` has been increased (or decreased in the case of negative) by an integer, represented by the variable `x`.

As a result, `nums1` becomes **equal** to `nums2`. Two arrays are considered **equal** when they contain the same integers with the same frequencies.

Return the integer `x`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums1 = [2,6,4], nums2 = [9,7,5]

**Output:** 3

**Explanation:**

The integer added to each element of `nums1` is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** nums1 = [10], nums2 = [5]

**Output:** -5

**Explanation:**

The integer added to each element of `nums1` is -5.

</div>
#### Example 3

<div class="example-block">
**Input:** nums1 = [1,1,1,1], nums2 = [1,1,1,1]

**Output:** 0

**Explanation:**

The integer added to each element of `nums1` is 0.

</div>

### 4. Constraints

- $1 \le \text{nums1.length} = \text{nums2.length} \le 100$

- $0 \le \text{nums1}[i], \text{nums2}[i] \le 1000$

- The test cases are generated in a way that there is an integer `x` such that `nums1` can become equal to `nums2` by adding `x` to each element of `nums1`.