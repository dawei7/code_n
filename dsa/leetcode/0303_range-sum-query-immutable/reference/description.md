### 1. Description

Given an integer array `nums`, handle multiple queries of the following type:

- Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where $left \le right$.

Implement the `NumArray` class:

- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.

- `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. $\text{nums}[left] + nums[left + 1] + ... + \text{nums}[right]$).

### 2. Function Contract

**Inputs**

- `nums`: The immutable integer array used to construct native `NumArray`.
- `queries`: The app adapter's ordered `[left, right]` inclusive ranges.

**Return value**

Return one range sum per entry in `queries`, in the same order. The native interface returns each value from a separate `sumRange` call.

### 3. Examples

#### Example 1

```
**Input**
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
**Output**
[null, 1, -1, -3]

**Explanation**
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$

- $0 \le left \le right < \text{nums.length}$

- At most $10^{4}$ calls will be made to `sumRange`.