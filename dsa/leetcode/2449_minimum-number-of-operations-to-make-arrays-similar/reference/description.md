## Description

You are given two positive integer arrays `nums` and `target`, of the same length.

In one operation, you can choose any two **distinct** indices `i` and `j` where $0 \le i, j < \text{nums.length}$ and:

- set $\text{nums}[i] = \text{nums}[i] + 2$ and

- set $\text{nums}[j] = \text{nums}[j] - 2$.

Two arrays are considered to be **similar** if the frequency of each element is the same.

Return *the minimum number of operations required to make *`nums`* similar to *`target`. The test cases are generated such that `nums` can always be similar to `target`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [8,12,6], target = [2,14,10]`
- **Output:** `2`
- **Explanation:** It is possible to make nums similar to target in two operations:
- Choose i = 0 and j = 2, nums = [10,12,4].
- Choose i = 1 and j = 2, nums = [10,14,2].
It can be shown that 2 is the minimum number of operations needed.
#### Example 2

- **Input:** `nums = [1,2,5], target = [4,1,3]`
- **Output:** `1`
- **Explanation:** We can make nums similar to target in one operation:
- Choose i = 1 and j = 2, nums = [1,4,3].
#### Example 3

- **Input:** `nums = [1,1,1,1,1], target = [1,1,1,1,1]`
- **Output:** `0`
- **Explanation:** The array nums is already similiar to target.
### Constraints

- $n = \text{nums.length} = \text{target.length}$

- $1 \le n \le 10^{5}$

- $1 \le \text{nums}[i], \text{target}[i] \le 10^{6}$

- It is possible to make `nums` similar to `target`.