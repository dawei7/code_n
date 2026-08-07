### 1. Description

Given an integer array `nums`, return *the maximum difference between two successive elements in its sorted form*. If the array contains less than two elements, return `0`.

You must write an algorithm that runs in linear time and uses linear extra space.

### 2. Function Contract

**Inputs**

- `nums`: A non-empty array of nonnegative integers.

**Return value**

Return the largest difference between successive values in sorted order, or `0` when fewer than two values exist.

### 3. Examples

#### Example 1

- **Input:** `nums = [3,6,9,1]`
- **Output:** `3`
- **Explanation:** The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
#### Example 2

- **Input:** `nums = [10]`
- **Output:** `0`
- **Explanation:** The array contains less than 2 elements, therefore return 0.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{9}$