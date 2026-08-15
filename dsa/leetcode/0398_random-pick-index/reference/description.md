### 1. Description

Given an integer array `nums` with possible **duplicates**, randomly output the index of a given `target` number. You can assume that the given target number must exist in the array.

Implement the `Solution` class:

- `Solution(int[] nums)` Initializes the object with the array `nums`.

- `int pick(int target)` Picks a random index `i` from `nums` where $\text{nums}[i] = target$. If there are multiple valid i's, then each index should have an equal probability of returning.

### 2. Function Contract

**Inputs**

- `nums`: The stored integer array, including possible duplicate values.
- `targets`: In cOde(n), the target supplied to each successive `pick` call.

**Return value**

The app adapter returns one selected index per target. On LeetCode, construct `Solution(nums)` and call `pick(target)` directly; every matching index must have equal probability.

### 3. Examples

#### Example 1

```
**Input**
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
**Output**
[null, 4, 0, 2]

**Explanation**
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
```

### 4. Constraints

- $1 \le \text{nums.length} \le 2 * 10^{4}$

- $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$

- `target` is an integer from `nums`.

- At most $10^{4}$ calls will be made to `pick`.
