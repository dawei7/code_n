### 1. Description

You are given an integer array `nums` and two integers `k` and `numOperations`.

You must perform an **operation** `numOperations` times on `nums`, where in each operation you:

- Select an index `i` that was **not** selected in any previous operations.

- Add an integer in the range `[-k, k]` to $\text{nums}[i]$.

Return the **maximum** possible frequency of any element in `nums` after performing the **operations**.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).
- `numOperations`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,4,5], k = 1, numOperations = 2

- **Output:** 2

- **Explanation:** We can achieve a maximum frequency of two by:

- Adding 0 to $\text{nums}[1]$, after which `nums` becomes `[1, 4, 5]`.

- Adding -1 to $\text{nums}[2]$, after which `nums` becomes `[1, 4, 4]`.

#### Example 2

- **Input:** nums = [5,11,20,20], k = 5, numOperations = 1

- **Output:** 2

- **Explanation:** We can achieve a maximum frequency of two by:

- Adding 0 to $\text{nums}[1]$.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $0 \le k \le 10^{9}$

- $0 \le numOperations \le \text{nums.length}$
