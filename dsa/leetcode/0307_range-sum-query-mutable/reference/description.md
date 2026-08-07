## Description

Given an integer array `nums`, handle multiple queries of the following types:

- **Update** the value of an element in `nums`.

- Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where $left \le right$.

Implement the `NumArray` class:

- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.

- `void update(int index, int val)` **Updates** the value of $\text{nums}[index]$ to be `val`.

- `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. $\text{nums}[left] + nums[left + 1] + ... + \text{nums}[right]$).
### Function Contract

**Inputs**

- `arr`: The app adapter's source array.
- `n`: The number of leading values from `arr` used to construct native `NumArray`.
- `queries`: Ordered app operations of the form `["update", index, val]` or `["sum", left, right]`.
- `q`: The number of leading operations from `queries` to execute.

**Return value**

Return the results of the executed `sum` operations in order. Updates change subsequent query results and produce no output.

### Examples
#### Example 1

```
**Input**
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
**Output**
[null, 9, null, 8]

**Explanation**
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
```
### Constraints

- $1 \le \text{nums.length} \le 3 * 10^{4}$

- $-100 \le \text{nums}[i] \le 100$

- $0 \le index < \text{nums.length}$

- $-100 \le val \le 100$

- $0 \le left \le right < \text{nums.length}$

- At most $3 * 10^{4}$ calls will be made to `update` and `sumRange`.