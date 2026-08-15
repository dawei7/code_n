### 1. Description

You are given an array `nums` of **non-negative** integers and an integer `k`.

An array is called **special** if the bitwise `OR` of all of its elements is **at least** `k`.

Return *the length of the **shortest** **special** **non-empty** subarray of* `nums`, *or return* `-1` *if no special subarray exists*.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,3], k = 2

- **Output:** 1

- **Explanation:** The subarray `[3]` has `OR` value of `3`. Hence, we return `1`.

#### Example 2

- **Input:** nums = [2,1,8], k = 10

- **Output:** 3

- **Explanation:** The subarray `[2,1,8]` has `OR` value of `11`. Hence, we return `3`.

#### Example 3

- **Input:** nums = [1,2], k = 0

- **Output:** 1

- **Explanation:** The subarray `[1]` has `OR` value of `1`. Hence, we return `1`.

### 4. Constraints

- $1 \le \text{nums.length} \le 2 * 10^{5}$

- $0 \le \text{nums}[i] \le 10^{9}$

- $0 \le k \le 10^{9}$
