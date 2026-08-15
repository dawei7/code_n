### 1. Description

Given a **circular** array `nums`, find the **maximum** absolute difference between adjacent elements.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Note

: In a circular array, the first and last elements are adjacent.

### 4. Examples

#### Example 1

- **Input:** nums = [1,2,4]

- **Output:** 3

- **Explanation:** Because `nums` is circular, $\text{nums}[0]$ and $\text{nums}[2]$ are adjacent. They have the maximum absolute difference of $|4 - 1| = 3$.

#### Example 2

- **Input:** nums = [-5,-10,-5]

- **Output:** 5

- **Explanation:** The adjacent elements $\text{nums}[0]$ and $\text{nums}[1]$ have the maximum absolute difference of $|-5 - (-10)| = 5$.

### 5. Constraints

- $2 \le \text{nums.length} \le 100$

- $-100 \le \text{nums}[i] \le 100$
