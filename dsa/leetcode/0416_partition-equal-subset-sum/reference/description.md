### 1. Description

Given an integer array `nums`, return `true` *if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or *`false`* otherwise*.

### 2. Function Contract

**Inputs**

- `nums`: The non-empty array of positive integers to divide between two subsets.

**Return value**

Return `true` when `nums` can be partitioned into two subsets with equal sums; otherwise, return `false`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,5,11,5]`
- **Output:** `true`
- **Explanation:** The array can be partitioned as [1, 5, 5] and [11].

#### Example 2

- **Input:** `nums = [1,2,3,5]`
- **Output:** `false`
- **Explanation:** The array cannot be partitioned into equal sum subsets.

### 4. Constraints

- $1 \le \text{nums.length} \le 200$

- $1 \le \text{nums}[i] \le 100$
