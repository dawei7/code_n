### 1. Description

Given an array of integers `nums` and an integer `k`, an element $\text{nums}[i]$ is considered **good** if it is **strictly** greater than the elements at indices $i - k$ and $i + k$ (if those indices exist). If neither of these indices *exists*, $\text{nums}[i]$ is still considered **good**.

Return the **sum** of all the **good** elements in the array.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,3,2,1,5,4], k = 2

- **Output:** 12

- **Explanation:** The good numbers are $\text{nums}[1] = 3$, $\text{nums}[4] = 5$, and $\text{nums}[5] = 4$ because they are strictly greater than the numbers at indices $i - k$ and $i + k$.

#### Example 2

- **Input:** nums = [2,1], k = 1

- **Output:** 2

- **Explanation:** The only good number is $\text{nums}[0] = 2$ because it is strictly greater than $\text{nums}[1]$.

### 4. Constraints

- $2 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 1000$

- $1 \le k \le floor(\text{nums.length} / 2)$
