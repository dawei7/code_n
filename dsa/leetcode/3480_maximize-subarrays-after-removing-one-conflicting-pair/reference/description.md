### 1. Description

You are given an integer `n` which represents an array `nums` containing the numbers from 1 to `n` in order. Additionally, you are given a 2D array `conflictingPairs`, where $\text{conflictingPairs}[i] = [a, b]$ indicates that `a` and `b` form a conflicting pair.

Remove **exactly** one element from `conflictingPairs`. Afterward, count the number of non-empty subarrays of `nums` which do not contain both `a` and `b` for any remaining conflicting pair `[a, b]`.

Return the **maximum** number of subarrays possible after removing **exactly** one conflicting pair.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 4, conflictingPairs = [[2,3],[1,4]]

**Output:** 9

**Explanation:**

- Remove `[2, 3]` from `conflictingPairs`. Now, $conflictingPairs = [[1, 4]]$.

- There are 9 subarrays in `nums` where `[1, 4]` do not appear together. They are `[1]`, `[2]`, `[3]`, `[4]`, `[1, 2]`, `[2, 3]`, `[3, 4]`, `[1, 2, 3]` and `[2, 3, 4]`.

- The maximum number of subarrays we can achieve after removing one element from `conflictingPairs` is 9.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]

**Output:** 12

**Explanation:**

- Remove `[1, 2]` from `conflictingPairs`. Now, $conflictingPairs = [[2, 5], [3, 5]]$.

- There are 12 subarrays in `nums` where `[2, 5]` and `[3, 5]` do not appear together.

- The maximum number of subarrays we can achieve after removing one element from `conflictingPairs` is 12.

</div>

### 4. Constraints

- $2 \le n \le 10^{5}$

- $1 \le \text{conflictingPairs.length} \le 2 * n$

- $\text{conflictingPairs}[i].length = 2$

- $1 \le \text{conflictingPairs}[i][j] \le n$

- $\text{conflictingPairs}[i][0] \neq \text{conflictingPairs}[i][1]$