## Description

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that $i \neq j$, $i \neq k$, and $j \neq k$, and $\text{nums}[i] + \text{nums}[j] + \text{nums}[k] = 0$.

Notice that the solution set must not contain duplicate triplets.
### Function Contract

**Inputs**

- `nums`: The integer array to search.

**Return value**

Return all distinct zero-sum value triplets, in any order.

### Examples

#### Example 1

- **Input:** `nums = [-1,0,1,2,-1,-4]`
- **Output:** `[[-1,-1,2],[-1,0,1]]`
- **Explanation:**
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
#### Example 2

- **Input:** `nums = [0,1,1]`
- **Output:** `[]`
- **Explanation:** The only possible triplet does not sum up to 0.
#### Example 3

- **Input:** `nums = [0,0,0]`
- **Output:** `[[0,0,0]]`
- **Explanation:** The only possible triplet sums up to 0.
### Constraints

- $3 \le \text{nums.length} \le 3000$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$