### 1. Description

Given an array of positive integers `nums`, return *the number of **distinct prime factors** in the product of the elements of* `nums`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Note

that:

- A number greater than `1` is called **prime** if it is divisible by only `1` and itself.

- An integer `val1` is a factor of another integer `val2` if $val2 / val1$ is an integer.

### 4. Examples

#### Example 1

- **Input:** `nums = [2,4,3,7,10,6]`
- **Output:** `4`
- **Explanation:** The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = $2^{5}$ * $3^{2}$ * 5 * 7.
There are 4 distinct prime factors so we return 4.

#### Example 2

- **Input:** `nums = [2,4,8,16]`
- **Output:** `1`
- **Explanation:** The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = $2^{10}$.
There is 1 distinct prime factor so we return 1.

### 5. Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $2 \le \text{nums}[i] \le 1000$
