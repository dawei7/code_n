### 1. Description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

### 2. Function Contract

**Inputs**

- `nums`: The integer array to inspect for repeated values.

**Return value**

Return `true` if any two positions contain the same value; otherwise return `false`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,3,1]

- **Output:** true

- **Explanation:** The element 1 occurs at the indices 0 and 3.

#### Example 2

- **Input:** nums = [1,2,3,4]

- **Output:** false

- **Explanation:** All elements are distinct.

#### Example 3

- **Input:** nums = [1,1,1,3,3,4,3,2,4,2]

- **Output:** true

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$
