### 1. Description

You are given an array of integers `nums` of size 3.

Return the **maximum** possible number whose *binary representation* can be formed by **concatenating** the *binary representation* of **all** elements in `nums` in some order.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Note

that the binary representation of any number *does not* contain leading zeros.

### 4. Examples

#### Example 1

- **Input:** nums = [1,2,3]

- **Output:** 30

- **Explanation:** Concatenate the numbers in the order `[3, 1, 2]` to get the result `"11110"`, which is the binary representation of 30.

#### Example 2

- **Input:** nums = [2,8,16]

- **Output:** 1296

- **Explanation:** Concatenate the numbers in the order `[2, 8, 16]` to get the result `"10100010000"`, which is the binary representation of 1296.

### 5. Constraints

- $\text{nums.length} = 3$

- $1 \le \text{nums}[i] \le 127$
