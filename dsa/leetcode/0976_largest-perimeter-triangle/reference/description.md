### 1. Description

Given an integer array `nums`, return *the largest perimeter of a triangle with a non-zero area, formed from three of these lengths*. If it is impossible to form any triangle of a non-zero area, return `0`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [2,1,2]`
- **Output:** `5`
- **Explanation:** You can form a triangle with three side lengths: 1, 2, and 2.
#### Example 2

- **Input:** `nums = [1,2,1,10]`
- **Output:** `0`
- **Explanation:**
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

### 4. Constraints

- $3 \le \text{nums.length} \le 10^{4}$

- $1 \le \text{nums}[i] \le 10^{6}$