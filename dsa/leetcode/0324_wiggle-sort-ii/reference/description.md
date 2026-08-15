### 1. Description

Given an integer array `nums`, reorder it such that $\text{nums}[0] < \text{nums}[1] > \text{nums}[2] < \text{nums}[3]...$.

You may assume the input array always has a valid answer.

### 2. Function Contract

**Inputs**

- `nums`: The mutable integer array to rearrange.

**Return value**

Return `None`. Mutate `nums` in place into any permutation satisfying the strict wiggle inequalities.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,5,1,1,6,4]`
- **Output:** `[1,6,1,5,1,4]`
- **Explanation:** [1,4,1,5,1,6] is also accepted.

#### Example 2

- **Input:** `nums = [1,3,2,2,3,1]`
- **Output:** `[2,3,1,3,1,2]`

### 4. Constraints

- $1 \le \text{nums.length} \le 5 * 10^{4}$

- $0 \le \text{nums}[i] \le 5000$

- It is guaranteed that there will be an answer for the given input `nums`.

**Follow Up:** Can you do it in `O(n)` time and/or **in-place** with `O(1)` extra space?
