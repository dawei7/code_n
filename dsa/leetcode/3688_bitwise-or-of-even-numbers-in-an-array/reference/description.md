### 1. Description

You are given an integer array `nums`.

Return the bitwise **OR** of all **even** numbers in the array.

If there are no even numbers in `nums`, return 0.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,3,4,5,6]

- **Output:** 6

- **Explanation:** The even numbers are 2, 4, and 6. Their bitwise OR equals 6.

#### Example 2

- **Input:** nums = [7,9,11]

- **Output:** 0

- **Explanation:** There are no even numbers, so the result is 0.

#### Example 3

- **Input:** nums = [1,8,16]

- **Output:** 24

- **Explanation:** The even numbers are 8 and 16. Their bitwise OR equals 24.

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$
